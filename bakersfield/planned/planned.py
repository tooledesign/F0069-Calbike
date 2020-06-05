import pybna

# import network
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/BakoPlannedRoutesFinal.osm",keep_holding_tables=True)

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.segment_stress()
s.crossing_stress()

# at this point we need to parse the lts=low tags in the OSM
# and override stress scores before proceeding

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

# scores
bna.score("automated.bna_scores",with_geoms=True)

# travel sheds
bna.travel_sheds(["060290006002009"],"automated.bakersfield_hsr_travel_shed")