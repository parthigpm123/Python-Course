The RIGHT JOIN keyword selects ALL records from the "right" table, and the matching records from the "left" table. The result is 0 records from the left side if there is no match.

SELECT testproduct_id, product_name, category_name
FROM testproducts
RIGHT JOIN categories ON testproducts.category_id = categories.category_id;
