import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/config.yaml")

bna.export("/home/spencer/gis/calbike/bakersfield.gpkg")

bna.export_table(
    "automated.bna_scores",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.bakersfield_hsr_travel_shed",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="travel_shed_existing"
)

bna.export_table(
    "automated.bna_scores_improved",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_scores_improved"
)

bna.export_table(
    "automated.bakersfield_hsr_travel_shed_improved",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="travel_shed_improved"
)
