--
-- Creates the bakersfield_proposed_streets table from the network edits submitted
-- by Calbike. The table is intended for manual updates. This script should not
-- be run again and is provided merely for reference.
--

BEGIN;
    CREATE TABLE generated.bakersfield_proposed_streets (
    	id SERIAL PRIMARY KEY,
    	geom geometry(LINESTRING, 26911),
    	osmid BIGINT[],
    	functional_class TEXT,
    	path_id INTEGER,
    	oneway TEXT,
    	"source" INTEGER,
        target INTEGER,
    	width FLOAT,
    	speed_limit INTEGER,
    	ft_bike_infra TEXT,
    	ft_bike_infra_width FLOAT,
    	tf_bike_infra TEXT,
    	tf_bike_infra_width FLOAT,
    	ft_lanes INTEGER,
    	tf_lanes INTEGER,
    	ft_cross_lanes INTEGER,
    	tf_cross_lanes INTEGER,
    	twltl_cross_lanes INTEGER,
    	ft_park bool,
    	tf_park bool,
    	fwd_seg_stress INTEGER,
    	fwd_int_stress INTEGER,
    	bwd_seg_stress INTEGER,
    	bwd_int_stress INTEGER,
    	xwalk INTEGER
    );
    CREATE INDEX sidx_bakersfield_proposed_streets ON generated.bakersfield_proposed_streets USING gist (geom);

    INSERT INTO generated.bakersfield_proposed_streets
    SELECT * FROM generated.bakersfield_planned_streets
    ;

    ALTER SEQUENCE bakersfield_proposed_streets_id_seq RESTART WITH 41789;

    ALTER TABLE generated.bakersfield_proposed_streets ADD COLUMN project TEXT;
    UPDATE generated.bakersfield_proposed_streets s
    SET project = calbike.project
    FROM scratch.bk_proposed_streets calbike
    WHERE s.id = calbike.id
    ;
COMMIT;
