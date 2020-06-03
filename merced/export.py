import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/merced/config.yaml")

bna.export("/home/spencer/gis/calbike/merced.gpkg")

bna.export_table(
    "automated.bna_scores",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.merced_hsr_travel_shed",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="travel_shed_existing"
)

bna.export_table(
    "automated.bna_scores_improved",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_scores_improved"
)

bna.export_table(
    "automated.merced_hsr_travel_shed_improved",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="travel_shed_improved"
)
