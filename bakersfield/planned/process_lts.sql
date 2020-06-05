-- parse LTS tags to apply low stress on network
UPDATE generated.bakersfield_planned_streets s
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE EXISTS (
    SELECT 1
    FROM generated.bakersfield_planned_osm_ways w
    WHERE
        w.osmid && s.osmid
        AND w.lts IN ('low','Low')
);
