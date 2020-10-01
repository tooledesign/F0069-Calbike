--
-- Creates intersection points for the Bkrsfld proposed network
-- It's possible there are manual edits to this table, although the script
-- has been set up to run automatically. Proceed with caution.
--
BEGIN;
    DROP TABLE IF EXISTS generated.bakersfield_proposed_ints;
    CREATE TABLE generated.bakersfield_proposed_ints (
    	id SERIAL PRIMARY KEY,
    	geom geometry(POINT, 26911)
    );

    INSERT INTO generated.bakersfield_proposed_ints (geom)
    SELECT geom FROM tdg_MakeIntersections('generated.bakersfield_proposed_streets', 1) geom
    ;

    UPDATE generated.bakersfield_proposed_streets i
    SET
        source = NULL,
        target = NULL
    ;

    UPDATE generated.bakersfield_proposed_streets i
    SET
        source = ints.source,
        target = ints.target
    FROM tdg_AssignIntersections('generated.bakersfield_proposed_streets','generated.bakersfield_proposed_ints',1) ints
    WHERE
        i.id = ints.id
    ;

    CREATE INDEX sidx_bakersfield_proposed_ints ON generated.bakersfield_proposed_ints USING gist (geom);
COMMIT;
