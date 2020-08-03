import pybna
from psycopg2 import sql

# import network
# use the calbike branch on the pdx server so that LTS tags are preserved
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/Merced PG 7 30 20.osm",keep_holding_tables=True)

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

# scores
bna.score("automated.merced_planned_bna_scores",with_geoms=True)

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.merced_planned_connected_blocks_3mi"
bna.db_connectivity_table = "automated.merced_planned_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("merced_planned_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
bna.calculate_connectivity(blocks=["060290006002009"])
bna.travel_sheds(["060290006002009"],"automated.merced_planned_hsr_travel_shed")
