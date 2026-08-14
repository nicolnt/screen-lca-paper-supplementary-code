import bw2data as bd
import bw2calc as bc

def get_ecoinvent_databases(bw_db_names: str, project_name: str):
    # NOTE: Select the right method
    # Optional additional condition to take the method from a specific Ecoinvent database version: `m[0] == "ecoinvent-3.12"`
    bd.projects.set_current(name=project_name)

    gwp_keys = [m for m in bd.methods if "climate change: total (excl. biogenic CO2)" == m[2] and "IPCC 2021" == m[1] and "global warming potential (GWP100)" == m[3]]

    ECOINVENT_DATABASES = {}

    # NOTE: Prepare LCA object
    for ecoinvent_database_name in bw_db_names:
        ecoinvent_database_dict = {}

        # NOTE: Produces a string which looks something like "ecoinvent-x.x.x" out of "ecoinvent-x.x.x-model"
        method_key_db_name = "-".join(ecoinvent_database_name.split("-")[0:2])

        # NOTE: Select the relevant key, based on Ecoinvent version (no matter the system model)
        gwp_key = [key for key in gwp_keys if method_key_db_name in key[0]][0]
        ecoinvent_database_dict['gwp_key'] = gwp_key

        db = bd.Database(ecoinvent_database_name)
        ecoinvent_database_dict['db'] = db

        # NOTE: The selected activity here do not matter much. AN activity is required to run an LCA (`demand` parameter)
        random_activity = db.random()

        # NOTE: Create the LCA object and run the calculation
        lca = bc.LCA(demand={random_activity.id: 1}, method=gwp_key)
        lca.lci(factorize=True)
        lca.lcia()

        ecoinvent_database_dict['lca'] = lca

        # NOTE: Used by calculate_LCA_optimized function
        # Source : 13-08-2026 - https://claude.ai/share/37e61aa6-5b64-449a-b015-6ec4caf7c36e
        ecoinvent_database_dict['h'] = lca.characterization_matrix.diagonal()

        ECOINVENT_DATABASES[ecoinvent_database_name] = ecoinvent_database_dict

    return ECOINVENT_DATABASES