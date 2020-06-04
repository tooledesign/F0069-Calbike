import pybna

# import network
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/fresno.osm",keep_holding_tables=True)
i.import_osm_destinations(osm_file="/home/sgardner/fresno.osm")

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.drop_table("generated.bna_stress_seg_forward")
s.drop_table("generated.bna_stress_seg_backward")
s.drop_table("generated.bna_stress_cross_forward")
s.drop_table("generated.bna_stress_cross_backward")
s.segment_stress()
s.crossing_stress()

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

# scores
bna.score("automated.fresno_bna_scores",with_geoms=True)

# travel sheds
# bna.travel_sheds(["060290006002009"],"automated.fresno_hsr_travel_shed")
