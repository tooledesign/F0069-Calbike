import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/existing/config.yaml")
bna.export("/home/spencer/gis/calbike/fresno.gpkg")

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/planned/config.yaml")
bna.export("/home/spencer/gis/calbike/fresno.gpkg")

bna.export_table(
    "generated.fresno_existing_edges",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="bna_edges_existing"
)

bna.export_table(
    "generated.fresno_planned_edges",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="bna_edges_planned"
)

bna.export_table(
    "automated.fresno_bna_scores",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.fresno_planned_bna_scores",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="bna_scores_planned"
)

bna.export_table(
    "automated.fresno_hsr_travel_shed",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="travel_shed_existing"
)

bna.export_table(
    "automated.fresno_planned_hsr_travel_shed",
    "/home/spencer/gis/calbike/fresno.gpkg",
    layer="travel_shed_planned"
)


# improved
#
# bna.export_table(
#     "automated.fresno_bna_scores_improved",
#     "/home/spencer/gis/calbike/fresno.gpkg",
#     layer="bna_scores_improved"
# )
#
# bna.export_table(
#     "automated.fresno_hsr_travel_shed_improved",
#     "/home/spencer/gis/calbike/fresno.gpkg",
#     layer="travel_shed_improved"
# )
