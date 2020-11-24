import pybna
from psycopg2 import sql

# connectivity
bna = pybna.pyBNA(config="/home/sgardner/config.yaml")
bna.build_network()

# combine all projects
q = """
alter table {t} add column if not exists all_projects text;
update {t}
set all_projects = 'all_projects'
where project is not null
;
"""
bna._run_sql(q.format(t="generated.bakersfield_proposed_streets"))

# get scores
# conn = bna.get_db_connection()
# cur = conn.cursor()
# cur.execute("select distinct project from generated.bakersfield_proposed_streets where project is not null")
project = "all_projects"
edge_table = "automated.bakersfield_proposed_edges_{}".format(project.replace(" ","_").lower())
bna_table = "automated.bakersfield_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
bna.save_scenario_edges("all_projects",scenario_id=project,table=edge_table,overwrite=True)
bna.calculate_scenario_connectivity("all_projects",scenario_ids=[project])
bna.score(bna_table,scenario_id=project,with_geoms=True,overwrite=True)

# aggregate scores
q_id = "alter table {} drop column id;"
q_insert = """
    insert into automated.bakersfield_proposed_aggregate_scores
    select * from {};
"""
bna._run_sql(q_id.format("automated.bakersfield_proposed_aggregate_scores"))
bna_table = "automated.bakersfield_proposed_bna_scores_{}".format(project.replace(" ","_").lower())
agg_table = "scratch.bakersfield_agg_{}".format(project.replace(" ","_").lower())
bna.aggregate(agg_table,bna_table,scenario_name=project,overwrite=True)
bna._run_sql(q_id.format(agg_table))
bna._run_sql(q_insert.format(agg_table))
bna.drop_table(agg_table)
bna._run_sql("alter table automated.bakersfield_proposed_aggregate_scores add column id serial primary key;")

# 3 mi travel shed around station
bna.config.bna.connectivity.table = "automated.bakersfield_proposed_connected_blocks_3mi"
bna.db_connectivity_table = "automated.bakersfield_proposed_connected_blocks_3mi"
bna.sql_subs["connectivity_table"] = sql.Identifier("bakersfield_proposed_connected_blocks_3mi")
bna.sql_subs["connectivity_max_distance"] = sql.Literal(4830)
# bna.calculate_connectivity(blocks=["060290006002009"])
table = "automated.bakersfield_proposed_hsr_travel_shed_{}".format(project.replace(" ","_").lower())
bna.calculate_scenario_connectivity("all_projects",scenario_ids=[project],origin_blocks=["060290006002009"])
bna.travel_sheds(["060290006002009"],table,scenario_id=project,overwrite=True)
