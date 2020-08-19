import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/merced/existing/config.yaml")
bna.export("/home/spencer/gis/calbike/merced.gpkg")

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/merced/planned/config.yaml")
bna.export("/home/spencer/gis/calbike/merced.gpkg")

bna.export_table(
    "generated.merced_existing_edges",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_edges_existing"
)

bna.export_table(
    "generated.merced_planned_edges",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_edges_planned"
)

bna.export_table(
    "automated.merced_bna_scores",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.merced_planned_bna_scores",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="bna_scores_planned"
)

bna.export_table(
    "automated.merced_hsr_travel_shed",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="travel_shed_existing"
)

bna.export_table(
    "automated.merced_planned_hsr_travel_shed",
    "/home/spencer/gis/calbike/merced.gpkg",
    layer="travel_shed_planned"
)


# improved
#
# bna.export_table(
#     "automated.merced_bna_scores_improved",
#     "/home/spencer/gis/calbike/merced.gpkg",
#     layer="bna_scores_improved"
# )
#
# bna.export_table(
#     "automated.merced_hsr_travel_shed_improved",
#     "/home/spencer/gis/calbike/merced.gpkg",
#     layer="travel_shed_improved"
# )
