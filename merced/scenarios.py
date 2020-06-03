import pybna
bna = pybna.pyBNA(config="/home/spencer/dev/calbike/merced/config.yaml")
bna.calculate_scenario_connectivity("scenario",scenario_ids=["upgrades"])

# scores
bna.score("automated.bna_scores_improved",scenario_id="upgrades",with_geoms=True)

# travel travel_sheds
bna.travel_sheds(
    ["060290006002009"],
    "automated.merced_hsr_travel_shed_improved",
    scenario_id="upgrades"
)
