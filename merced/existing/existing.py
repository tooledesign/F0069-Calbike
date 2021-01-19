import pybna

# import network
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/merced.osm",keep_holding_tables=True)
i.import_osm_destinations(osm_file="/home/sgardner/merced.osm")

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.segment_stress()
s.crossing_stress()

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

# scores
bna.score("automated.merced_bna_scores",with_geoms=True)

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.merced_connected_blocks_3mi"
bna.db_connectivity_table = "automated.merced_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("merced_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
bna.calculate_connectivity(blocks=["060470013023031","060470013023032"])
bna.travel_sheds(["060470013023031","060470013023032"],"automated.merced_hsr_travel_shed",overwrite=True)
