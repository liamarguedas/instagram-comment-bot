from pathlib import Path
import json
from getpass import getpass
from datetime import datetime

ROOT_PATH = Path(__file__).parents[1]

class Utils:
    """todo"""

    def __init__(self) -> None:

        self.cfgs = ROOT_PATH / "cfg" / "config.json"
        self.logs = ROOT_PATH / "logs" / "log.txt"

    @staticmethod
    def get_current_time():
        """todo"""
        return datetime.now().strftime('%H:%M:%S - %d/%m/%Y')


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

    def write_to_logs(self, line_to_write: str):

        with open(self.logs, "a", encoding="utf-8") as file:
            file.write(line_to_write)

    def log(self, log_string: str):
        now = self.get_current_time()

        log_text = f"[{now}]: {log_string}"

        self.write_to_logs(log_text)
        print(log_text)














