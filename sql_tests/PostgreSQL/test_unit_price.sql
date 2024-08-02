-- For demo purposes: Create an error
UPDATE invoice_line SET unit_price = 1.99
WHERE invoice_line_id = 10;
------------------------------------------------------------------------------------------
-- Sanity check 1: Check if invoice unit price always corresponds to the track unit price
------------------------------------------------------------------------------------------
SELECT il.invoice_id , il.unit_price , t.Name , t.unit_price AS true_unit_price
FROM invoice_line il
INNER JOIN track t ON il.track_id = t.track_id
WHERE il.unit_price <> t.unit_price;
-- If a result is returned, fix the corresponding unit_price on the table invoice_line

--------------------------------------------------------------------------------------------------------
-- If this returns an error, we should assume that the correct unit_price is the one in the table track
--------------------------------------------------------------------------------------------------------
--UPDATE invoice_line SET unit_price =
--(
-- SELECT unit_price FROM track
-- WHERE track.track_id = invoice_line.track_id
--);


