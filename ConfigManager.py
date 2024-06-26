import yaml


class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file, "r") as file:
            config_data = yaml.safe_load(file)
        return config_data

    def get_config_file(self):
        return self.config_file

    def get_n(self):
        return self.config_data["simulation_parameters"]["n"]

    def get_sample(self):
        return self.config_data["simulation_parameters"]["sample"]

    def get_Y1(self):
        return self.config_data["simulation_parameters"]["Y1"]

    def get_Y2(self):
        return self.config_data["simulation_parameters"]["Y2"]

    def get_lc(self):
        return self.config_data["simulation_parameters"]["lc_parameter"]

    def get_E1(self):
        # returns the load matrix E1 with load parameter = 1
        return [[1, 0], [0, 0]]

    def get_E2(self):
        # returns the load matrix E2 with load parameter = 1
        return [[0, 0], [0, 1]]

    def get_E3(self):
        # returns the load matrix E3 with load parameter = 1
        return [[0, 1], [1, 0]]

    def get_absolute_path_to_dir_with_data(self):
        return self.config_data["directories"]["absolute_path_to_dir_with_data"]

    def get_dir_where_yamls_are_created(self):
        return self.get_absolute_path_to_dir_with_data() + self.config_data["directories"]["dir_where_yamls_are_created"]

    def get_path_to_yaml_template(self):
        return self.get_absolute_path_to_dir_with_data() + self.config_data["directories"]["path_to_yaml_template"]

    def get_directory_where_vtus_are_created(self):
        return self.get_absolute_path_to_dir_with_data() + self.config_data["directories"]["directory_where_vtus_are_created"]

    def dir_where_mesh_and_geo_are_created(self):
        return self.get_absolute_path_to_dir_with_data() + self.config_data["directories"]["dir_where_mesh_and_geo_are_created"]

    def get_name_of_file_with_tensor(self):
        return self.config_data["results_file_settings"]["name_of_file_with_tensor"]

    def get_output_dir_of_file_with_tensor(self):
        return self.get_absolute_path_to_dir_with_data() + self.config_data["results_file_settings"]["output_dir_of_file_with_tensor"]

    def get_delete_yaml_dir_after_simulation(self):
        return self.config_data["additional_settings"]["delete_yaml_dir_after_simulation"]

    def get_delete_vtu_dir_after_simulation(self):
        return self.config_data["additional_settings"]["delete_vtu_dir_after_simulation"]

    def get_change_names_of_computed_yamls(self):
        return self.config_data["additional_settings"]["change_names_of_computed_yamls"]

    def get_new_names_of_yamls(self):
        return self.config_data["additional_settings"]["new_names_of_yamls"]

    def get_change_names_of_computed_output_dirs(self):
        return self.config_data["additional_settings"]["change_names_of_computed_output_dirs"]

    def get_new_names_of_output_dirs(self):
        return self.config_data["additional_settings"]["new_names_of_output_dirs"]

    def get_change_names_of_computed_vtu_files(self):
        return self.config_data["additional_settings"]["change_names_of_computed_vtu_files"]

    def get_new_names_of_vtu_files(self):
        return self.config_data["additional_settings"]["new_names_of_vtu_files"]

    def get_change_name_of_msh_file(self):
        return self.config_data["additional_settings"]["change_name_of_msh_file"]

    def get_create_geo_file(self):
        return self.config_data["additional_settings"]["create_geo_file"]

    def get_change_name_of_geo_file(self):
        return self.config_data["additional_settings"]["change_name_of_geo_file"]

    def get_new_name_of_geo(self):
        return self.config_data["additional_settings"]["new_name_of_geo"]

    def get_new_name_of_mesh(self):
        return self.config_data["additional_settings"]["new_name_of_mesh"]

    def get_measure_time_of_computation(self):
        return self.config_data["additional_settings"]["measure_time_of_computation"]