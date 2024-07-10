----------------------------------------------------------------
-- Test if in TableB we have the same Ids as we have in TableA
----------------------------------------------------------------
SELECT ta.TrackId as missing_id
FROM TableA ta
LEFT JOIN TableB tb ON ta.TrackId =tb.TrackId 
WHERE tb.TrackId IS NULL;
-- If any Ids are returned, some SQL like this might fix the problem:
--WITH missing AS (
--SELECT ta.TrackId, ta.Name, ta.AlbumId, ta.MediaTypeId, ta.GenreId, ta.Composer, ta.Milliseconds, ta.Bytes, ta.UnitPrice
--FROM TableA ta
--LEFT JOIN TableB tb ON ta.TrackId =tb.TrackId 
--WHERE tb.TrackId IS NULL
--)
--INSERT INTO TableB (TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
--SELECT m.TrackId, m.Name, m.AlbumId, m.MediaTypeId, m.GenreId, m.Composer, m.Milliseconds, m.Bytes, m.UnitPrice
--FROM missing m;

-- Delete a few rows again, to have the test returning an error
-- DELETE FROM TableB WHERE TrackId < 10;
