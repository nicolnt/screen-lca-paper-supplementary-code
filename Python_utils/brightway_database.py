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


class BrightwayDatabase:

    def __init__(self, bw_database_name, bw_project_name: str, method_key):
        # NOTE: Select the right method
        # Optional additional condition to take the method from a specific Ecoinvent database version: `m[0] == "ecoinvent-3.12"`
        bd.projects.set_current(name=bw_project_name)
    
        # NOTE: Select the relevant key, based on Ecoinvent version (no matter the system model)
        self.method = method_key

        db = bd.Database(bw_database_name)
        self.db = db

        # NOTE: The selected activity here do not matter much. AN activity is required to run an LCA (`demand` parameter)
        random_activity = db.random()

        # NOTE: Create the LCA object and run the calculation
        lca = bc.LCA(demand={random_activity.id: 1}, method=method_key)
        lca.lci(factorize=True)
        lca.lcia()

        self.lca = lca

        # NOTE: Used by calculate_LCA_optimized function
        # Source : 13-08-2026 - https://claude.ai/share/37e61aa6-5b64-449a-b015-6ec4caf7c36e
        self.h = lca.characterization_matrix.diagonal()


    # NOTE: calculate LCA score for a product by reusing a pre-calculated Brightway LCA object
    def calculate_LCA(self, activity_code=None, activity_id=None, amount=1):

        if activity_id is None:
            activity_id = self.db.get(activity_code).id
        
        # NOTE: Reuse the LCA object created before.
        # Source: https://github.com/brightway-lca/brightway2/blob/master/notebooks/Using%20redo_lci%20and%20redo_lcia.ipynb
        self.lca.lcia(demand={activity_id: amount})
        return self.lca.score


    # NOTE: calculate LCA score for a product by reusing a pre-calculated Brightway LCA object
    # Source : 13-08-2026 - https://claude.ai/share/37e61aa6-5b64-449a-b015-6ec4caf7c36e
    def calculate_LCA_optimized(self, activity_code=None, activity_id=None, amount=1):

        if activity_id is None:
            activity_id = self.db.get(activity_code).id

        self.lca.build_demand_array({activity_id: amount})
        supply = self.lca.solve_linear_system() 
        score = self.h @ (self.lca.biosphere_matrix @ supply)
        return score

    
    def get_activity_by_name_location_priority(self, name, location_priority = ['RER', 'GLO', 'RoW']):
        activities = [a for a in self.db.search(name) if a['name'] == name]
        
        if len(activities) > 0:
            for location in location_priority:
                activities_location = [a for a in activities if a['location'] == location]
                if len(activities_location):
                    return activities_location[0]

            # NOTE: Select any location (region)
            # Situation not encountered with this case study, dataset always existed for either of 'RER', 'GLO' or 'RoW'    
            return activities.random() 

        else:
            return None


    def get_activity_by_name_specific_location(self, name, location):
        activities = [a for a in self.db.search(name) if a['name'] == name]
        
        if len(activities) > 0:
            activities_location = [a for a in activities if a['location'] == location]
            if len(activities_location):
                return activities_location[0]
            else:
                return "Location not found"

        else:
            return "Activity not found"

    def get_activity_locations(self, name):
        activities = [a for a in self.db.search(name) if a['name'] == name]
        
        if len(activities) > 0:
            return [a['location'] for a in activities]
        else:
            return "Activity not found"