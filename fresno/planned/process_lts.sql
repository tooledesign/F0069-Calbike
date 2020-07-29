-- parse LTS tags to apply low stress on network
UPDATE generated.fresno_planned_streets s
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE EXISTS (
    SELECT 1
    FROM generated.fresno_planned_osm_ways w
    WHERE
        w.osmid && s.osmid
        AND trim(lower(w.lts)) = 'low stress'
);

-- handle new trails
DROP TABLE IF EXISTS tmp_trails;
CREATE TEMP TABLE tmp_trails AS (
    SELECT UNNEST(osmid) AS osmid
    FROM generated.fresno_planned_streets
    WHERE functional_class = 'path'
);
DELETE FROM tmp_trails WHERE osmid > 0;

UPDATE generated.fresno_planned_streets s
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE EXISTS (
    SELECT 1
    FROM tmp_trails w
    WHERE
        w.osmid = ANY(s.osmid)
);

-- handle bike lanes that weren't part of existing condition
UPDATE generated.fresno_planned_streets
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE
	ft_bike_infra = 'lane'
	AND osmid NOT IN (SELECT osmid FROM generated.fresno_streets bs WHERE ft_bike_infra = 'lane')
;
