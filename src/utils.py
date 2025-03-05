from pathlib import Path
import json
from getpass import getpass
ROOT_PATH = Path(__file__).parents[1]

class Utils:
    """todo"""

    def __init__(self) -> None:

        self.cfgs = ROOT_PATH / "cfg" / "config.json"

    def read_configuration(self):
        """todo"""
        if self.cfgs.is_file():

            with open(self.cfgs, encoding="utf-8") as file:
                return json.load(file)

        self.generate_json_cfg()
        return self.read_configuration()



    def generate_json_cfg(self):
        """todo"""
        username = input("Instagram username: ")
        pws = getpass("Password: ")

        cfgs = {
            "username": username,
            "password": pws
        }

        with open(self.cfgs, "w", encoding="utf-8") as file:
            json.dump(cfgs, file)
