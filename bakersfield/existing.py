import pybna

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
