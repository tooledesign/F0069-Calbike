import pybna
from psycopg2 import sql

# import network
# (Not needed for Bksfld because they did edits directly on the network.
# Instead see bakersfield_proposed_streets.sql)
# i = pybna.Importer(config="/home/sgardner/config.yaml")
# i.import_osm_network(osm_file="/home/sgardner/BakoproposedRoutesFinal.osm",keep_holding_tables=True)

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.drop_table("generated.bna_stress_seg_forward")
s.drop_table("generated.bna_stress_seg_backward")
s.drop_table("generated.bna_stress_cross_forward")
s.drop_table("generated.bna_stress_cross_backward")
s.segment_stress()
s.crossing_stress()

# at this point we need to parse the lts=low tags in the OSM
# and override stress scores before proceeding
# see process_lts.sql

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

#### left off here

bna.calculate_scenario_connectivity("project")

# get scores for each scenario
conn = bna.get_db_connection()
cur = conn.cursor()
cur.execute("select distinct project from generated.bakersfield_proposed_streets where project is not null")
projects = [p[0] for p in cur.fetchall()]
for project in projects:
    table = "automated.bakersfield_proposed_bna_scores_{}".format(project)
    bna.score(table,scenario_id=project,with_geoms=True,overwrite=True)

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.bakersfield_proposed_connected_blocks_3mi"
bna.db_connectivity_table = "automated.bakersfield_proposed_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("bakersfield_proposed_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
bna.calculate_connectivity(blocks=["060290006002009"])
bna.calculate_scenario_connectivity(blocks=["060290006002009"])
for project in projects:
    table = "automated.bakersfield_proposed_hsr_travel_shed_{}".format(project)
    bna.travel_sheds(["060290006002009"],table)
