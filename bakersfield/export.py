import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/existing/config.yaml")
bna.export("/home/spencer/gis/calbike/bakersfield_existing.gpkg")

bna.export_table(
    "generated.bakersfield_existing_edges",
    "/home/spencer/gis/calbike/bakersfield_existing.gpkg",
    layer="bna_edges_existing"
)

bna.export_table(
    "automated.bakersfield_bna_scores",
    "/home/spencer/gis/calbike/bakersfield_existing.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.bakersfield_hsr_travel_shed",
    "/home/spencer/gis/calbike/bakersfield_existing.gpkg",
    layer="travel_shed_existing"
)

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/planned/config.yaml")
bna.export("/home/spencer/gis/calbike/bakersfield_planned.gpkg")

bna.export_table(
    "generated.bakersfield_planned_edges",
    "/home/spencer/gis/calbike/bakersfield_planned.gpkg",
    layer="bna_edges_planned"
)

bna.export_table(
    "automated.bakersfield_planned_bna_scores",
    "/home/spencer/gis/calbike/bakersfield_planned.gpkg",
    layer="bna_scores_planned"
)

bna.export_table(
    "automated.bakersfield_planned_hsr_travel_shed",
    "/home/spencer/gis/calbike/bakersfield_planned.gpkg",
    layer="travel_shed_planned"
)

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/bakersfield/proposed/config.yaml")

conn = bna.get_db_connection()
cur = conn.cursor()
cur.execute("select distinct project from generated.bakersfield_proposed_streets where project is not null")
projects = [p[0] for p in cur.fetchall()]
for project in projects:
    print(project)
    edge_table = "automated.bakersfield_proposed_edges_{}".format(project.replace(" ","_").lower())
    edge_layer = "bna_edges_{}".format(project.replace(" ","_").lower())
    bna_table = "automated.bakersfield_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
    bna_layer = "bna_scores_{}".format(project.replace(" ","_").lower())
    shed_table = "automated.bakersfield_proposed_hsr_travel_shed_{}".format(project.replace(" ","_").lower())
    shed_layer = "travel_shed_{}".format(project.replace(" ","_").lower())

    bna.export_table(
        edge_table,
        "/home/spencer/gis/calbike/bakersfield_proposed.gpkg",
        layer=edge_layer
    )

    bna.export_table(
        bna_table,
        "/home/spencer/gis/calbike/bakersfield_proposed.gpkg",
        layer=bna_layer
    )

    bna.export_table(
        shed_table,
        "/home/spencer/gis/calbike/bakersfield_proposed.gpkg",
        layer=shed_layer
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
