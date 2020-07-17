import pybna
from psycopg2 import sql

# import network
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/bakersfield.osm",keep_holding_tables=True)
i.import_osm_destinations(osm_file="/home/sgardner/bakersfield.osm")

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.segment_stress()
s.crossing_stress()

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

# scores
bna.score("automated.bakersfield_bna_scores",with_geoms=True)

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.bakersfield_connected_blocks_3mi"
bna.db_connectivity_table = "automated.bakersfield_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("bakersfield_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
bna.calculate_connectivity(blocks=["060290006002009"])
bna.travel_sheds(["060290006002009"],"automated.bakersfield_hsr_travel_shed")
