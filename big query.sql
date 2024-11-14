-- Comprehensive Join Query for Dashboard Creation
CREATE OR REPLACE TABLE psyched-scene-436623-m0.sales_project.Analytics_dim AS(
SELECT 
    -- Customer Information
    c.Customer_ID,
    c.Age,
    c.Gender,
    c.Loyalty_Member,
    
    -- Order Information
    o.Order_Status,
    o.Payment_Method,
    o.Shipping_Type,
    o.order_id,
    
    -- Date Information
    pd.Purchase_Date,
    pd.date_year,
    pd.date_month,
    pd.date_weekday,
    
    -- Product and Transaction Details
    f.Product_Type,
    f.SKU,
    f.Unit_Price,
    f.Quantity,
    f.Total_Price,
    f.Rating,
    f.`Add-ons_Purchased`,
    f.`Add-on_Total`,
    
    -- Calculated Fields
    (f.Total_Price + COALESCE(f.`Add-on_Total`, 0)) as grand_total,
    CASE 
        WHEN f.`Add-on_Total` > 0 THEN 'Yes'
        ELSE 'No'
    END as has_addons
FROM psyched-scene-436623-m0.sales_project.fact_table f
JOIN psyched-scene-436623-m0.sales_project.customer_dim c ON f.customer_id = c.customer_id
JOIN psyched-scene-436623-m0.sales_project.order_dim o ON f.order_id = o.order_id
JOIN psyched-scene-436623-m0.sales_project.purchase_date_dim pd ON f.purchase_date_id = pd.purchase_date_id);
