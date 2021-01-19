import pybna
from psycopg2 import sql

# import network
# use the calbike branch on the pdx server so that LTS tags are preserved
i = pybna.Importer(config="/home/sgardner/config.yaml")
i.import_osm_network(osm_file="/home/sgardner/Merced_12_17.osm",keep_holding_tables=True)

# stress
s = pybna.Stress(config="/home/sgardner/config.yaml")
s.drop_table("generated.bna_stress_seg_forward")
s.drop_table("generated.bna_stress_seg_backward")
s.drop_table("generated.bna_stress_cross_forward")
s.drop_table("generated.bna_stress_cross_backward")
s.segment_stress()
s.crossing_stress()

# at this point we need to parse the lts=low tags in the OSM
# and override stress scores before proceeding. Also need to process
# the project designations.
# see process_lts.sql

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()
bna.calculate_connectivity()

# get scores for each scenario
conn = bna.get_db_connection()
cur = conn.cursor()
cur.execute("select distinct project from generated.merced_proposed_streets where project is not null")
projects = [p[0] for p in cur.fetchall()]
for project in projects:
    print(project)
    edge_table = "automated.merced_proposed_edges_{}".format(project.replace(" ","_").lower())
    bna_table = "automated.merced_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
    bna.save_scenario_edges("project",scenario_id=project,table=edge_table,overwrite=True)
    bna.calculate_scenario_connectivity("project",scenario_ids=[project])
    bna.score(bna_table,scenario_id=project,with_geoms=True,overwrite=True)

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.merced_proposed_connected_blocks_3mi"
bna.db_connectivity_table = "automated.merced_proposed_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("merced_proposed_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
bna.calculate_connectivity(blocks=["060470013023031","060470013023032"])
for project in projects:
    table = "automated.merced_proposed_hsr_travel_shed_{}".format(project.replace(" ","_").lower())
    bna.calculate_scenario_connectivity("project",scenario_ids=[project],origin_blocks=["060470013023031","060470013023032"])
    bna.travel_sheds(["060470013023031","060470013023032"],table,scenario_id=project,overwrite=True)

# aggregate scores
bna.aggregate("automated.merced_proposed_aggregate_scores","automated.merced_planned_bna_scores",overwrite=True,scenario_name="Planned network")
q_id = "alter table {} drop column id;"
q_insert = """
    insert into automated.merced_proposed_aggregate_scores
    select * from {};
"""
bna._run_sql(q_id.format("automated.merced_proposed_aggregate_scores"))
for project in projects:
    bna_table = "automated.merced_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
    agg_table = "scratch.merced_agg_{}".format(project.replace(" ","_").lower())
    bna.aggregate(agg_table,bna_table,scenario_name=project,overwrite=True)
    bna._run_sql(q_id.format(agg_table))
    bna._run_sql(q_insert.format(agg_table))
    bna.drop_table(agg_table)
bna._run_sql("alter table automated.merced_proposed_aggregate_scores add column id serial primary key;")
