------------------------------------------------------------------------------------------
-- Sanity check 1: Check if invoice unit price always corresponds to the track unit price
--
------------------------------------------------------------------------------------------
SELECT il.InvoiceId , il.UnitPrice , t.Name , t.UnitPrice AS true_unit_price
FROM InvoiceLine il 
INNER JOIN Track t ON il.TrackId = t.TrackId
WHERE il.UnitPrice <> t.UnitPrice;
-- If a result is returned, fix the corresponding UnitPrice on the table InvoiceLine