import configparser
import os

class ConfigReader:
    # Reads configuration from the properties file

    @staticmethod
    def get_property(property_name):
        # Fetch a property from config.properties
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), "../config.properties")
        
        # Read the config file
        config.read(config_path)

        # Ensure the key exists before returning
        if property_name in config["DEFAULT"]:
            return config["DEFAULT"][property_name]
        else:
            raise KeyError(f"Property '{property_name}' not found in config.properties")
