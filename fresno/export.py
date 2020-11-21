import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/existing/config.yaml")
bna.export("/home/spencer/gis/calbike/fresno_existing.gpkg")

bna.export_table(
    "generated.fresno_existing_edges",
    "/home/spencer/gis/calbike/fresno_existing.gpkg",
    layer="bna_edges_existing"
)

bna.export_table(
    "automated.fresno_bna_scores",
    "/home/spencer/gis/calbike/fresno_existing.gpkg",
    layer="bna_scores_existing"
)

bna.export_table(
    "automated.fresno_hsr_travel_shed",
    "/home/spencer/gis/calbike/fresno_existing.gpkg",
    layer="travel_shed_existing"
)

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/planned/config.yaml")
bna.export("/home/spencer/gis/calbike/fresno_planned.gpkg")

bna.export_table(
    "generated.fresno_planned_edges",
    "/home/spencer/gis/calbike/fresno_planned.gpkg",
    layer="bna_edges_planned"
)

bna.export_table(
    "automated.fresno_planned_bna_scores",
    "/home/spencer/gis/calbike/fresno_planned.gpkg",
    layer="bna_scores_planned"
)

bna.export_table(
    "automated.fresno_planned_hsr_travel_shed",
    "/home/spencer/gis/calbike/fresno_planned.gpkg",
    layer="travel_shed_planned"
)

bna = pybna.pyBNA(config="/home/spencer/dev/calbike/fresno/proposed/config.yaml")

conn = bna.get_db_connection()
cur = conn.cursor()
cur.execute("select distinct project from generated.fresno_proposed_streets where project is not null")
projects = [p[0] for p in cur.fetchall()]
for project in projects:
    print(project)
    edge_table = "automated.fresno_proposed_edges_{}".format(project.replace(" ","_").lower())
    edge_layer = "bna_edges_{}".format(project.replace(" ","_").lower())
    bna_table = "automated.fresno_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
    bna_layer = "bna_scores_{}".format(project.replace(" ","_").lower())
    shed_table = "automated.fresno_proposed_hsr_travel_shed_{}".format(project.replace(" ","_").lower())
    shed_layer = "travel_shed_{}".format(project.replace(" ","_").lower())
    bna.export_table(
        edge_table,
        "/home/spencer/gis/calbike/fresno_proposed.gpkg",
        layer=edge_layer
    )
    bna.export_table(
        bna_table,
        "/home/spencer/gis/calbike/fresno_proposed.gpkg",
        layer=bna_layer
    )
    bna.export_table(
        shed_table,
        "/home/spencer/gis/calbike/fresno_proposed.gpkg",
        layer=shed_layer
    )
bna.export_table(
    "automated.fresno_proposed_aggregate_scores",
    "/home/spencer/gis/calbike/fresno_proposed.gpkg",
    layer="aggregate_scores",
    nonspatial=True
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
