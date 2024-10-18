-- Lists all bands with Glam rock as their main style, ranked by their lifespan (in years until 2022)
SELECT band_name, (2022 - split) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC; 
