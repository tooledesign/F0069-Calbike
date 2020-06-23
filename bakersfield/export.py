import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/existing/config.yaml")
bna.export("/home/spencer/gis/calbike/bakersfield.gpkg")

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/planned/config.yaml")
bna.export("/home/spencer/gis/calbike/bakersfield.gpkg")

bna.export_table(
    "generated.bakersfield_existing_edges",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_edges_existing"
)

bna.export_table(
    "generated.bakersfield_planned_edges",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_edges_planned"
)

bna.export_table(
    "automated.bakersfield_bna_scores",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.bakersfield_planned_bna_scores",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="bna_scores_planned"
)

bna.export_table(
    "automated.bakersfield_hsr_travel_shed",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="travel_shed_existing"
)

bna.export_table(
    "automated.bakersfield_planned_hsr_travel_shed",
    "/home/spencer/gis/calbike/bakersfield.gpkg",
    layer="travel_shed_planned"
)


# improved
#
# bna.export_table(
#     "automated.bakersfield_bna_scores_improved",
#     "/home/spencer/gis/calbike/bakersfield.gpkg",
#     layer="bna_scores_improved"
# )
#
# bna.export_table(
#     "automated.bakersfield_hsr_travel_shed_improved",
#     "/home/spencer/gis/calbike/bakersfield.gpkg",
#     layer="travel_shed_improved"
# )
