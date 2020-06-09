import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/merced/existing/config.yaml")

bna.export("/home/spencer/gis/calbike/merced.gpkg")

bna.export_table(
    "automated.merced_bna_scores",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_scores_existing"
)
