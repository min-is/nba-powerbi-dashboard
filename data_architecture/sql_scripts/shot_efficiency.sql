WITH shot_zones AS (
    SELECT 
        player_key,
        CASE 
            WHEN shot_distance < 5 THEN 'Restricted Area'
            WHEN shot_distance BETWEEN 5 AND 15 THEN 'Paint'
            WHEN shot_distance > 23 THEN 'Three-Pointer'
            ELSE 'Mid-Range'
        END AS zone,
        COUNT(*) FILTER (WHERE made) AS made_shots,
        COUNT(*) AS attempted_shots
    FROM fact_shot_data
    GROUP BY 1,2
)
SELECT 
    p.full_name,
    z.zone,
    ROUND(z.made_shots::NUMERIC / z.attempted_shots, 3) AS efficiency,
    RANK() OVER (PARTITION BY z.zone ORDER BY efficiency DESC) AS zone_rank
FROM shot_zones z
JOIN dim_player p USING (player_key)
WHERE attempted_shots > 100;