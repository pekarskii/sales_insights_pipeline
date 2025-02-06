CREATE TABLE sales (
    transaction_id BIGINT PRIMARY KEY,
    store_id INTEGER,
    product_id INTEGER,
    category VARCHAR(50),
    price DECIMAL(10,2),
    quantity INTEGER,
    sale_date DATE,
    total_price DECIMAL(10,2)
);



select * from sales
limit 20;