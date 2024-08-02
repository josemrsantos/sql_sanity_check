------------------------------------------------------------------------------------------
-- Sanity check 2: Check if all Tracks have an UnitPrice
--
------------------------------------------------------------------------------------------
SELECT Name , unit_price, track_id 
FROM Track
WHERE unit_price is NULL or track_id <=0;
-- If a result is returned, add a unit price to that Track