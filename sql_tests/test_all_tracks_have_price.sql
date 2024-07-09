------------------------------------------------------------------------------------------
-- Sanity check 2: Check if all Tracks have an UnitPrice
--
------------------------------------------------------------------------------------------
SELECT Name , UnitPrice, TrackId 
FROM Track
WHERE UnitPrice is NULL or UnitPrice <=0;
-- If a result is returned, add a unit price to that Track