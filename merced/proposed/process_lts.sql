-- parse LTS tags to apply low stress on network
UPDATE generated.merced_proposed_streets s
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE EXISTS (
    SELECT 1
    FROM generated.merced_proposed_osm_ways w
    WHERE
        w.osmid && s.osmid
        AND trim(lower(w.lts)) = 'low stress'
);


-- handle new trails
DROP TABLE IF EXISTS tmp_trails;
CREATE TEMP TABLE tmp_trails AS (
    SELECT UNNEST(osmid) AS osmid
    FROM generated.merced_proposed_streets
    WHERE functional_class = 'path'
);
DELETE FROM tmp_trails WHERE osmid > 0;

UPDATE generated.merced_proposed_streets s
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
UPDATE generated.merced_proposed_streets
SET
    fwd_seg_stress = 1,
    bwd_seg_stress = 1,
    fwd_int_stress = 1,
    bwd_int_stress = 1
WHERE
	ft_bike_infra = 'lane'
	AND osmid NOT IN (SELECT osmid FROM generated.merced_streets bs WHERE ft_bike_infra = 'lane')
;


-- process projects
ALTER TABLE generated.merced_proposed_streets ADD COLUMN IF NOT EXISTS project TEXT;
DROP TABLE IF EXISTS tmp_prjs;
CREATE TEMP TABLE tmp_prjs AS (
    SELECT
        s.id,
        w.project
    FROM
        generated.merced_proposed_streets s,
        generated.merced_proposed_osm_ways w
    WHERE
        w.osmid && s.osmid
        AND COALESCE(w.project,'NaN') != 'NaN'
);
UPDATE generated.merced_proposed_streets s
SET
    fwd_seg_stress = -1,
    bwd_seg_stress = -1,
    fwd_int_stress = -1,
    bwd_int_stress = -1,
    project = tmp_prjs.project
FROM tmp_prjs
WHERE s.id = tmp_prjs.id
;
