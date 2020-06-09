import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/existing/config.yaml")

bna.export("/home/spencer/gis/calbike/fresno.gpkg")

bna.export_table(
    "automated.fresno_bna_scores",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="bna_scores_existing"
)
