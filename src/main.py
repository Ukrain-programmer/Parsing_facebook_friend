from constants import MAIN
from service.file.json import JsonFileService
from service.parser.parser import FriendsParser
import argparse
import subprocess
import logging
import logging.config
import time

LOGGER = logging.getLogger(MAIN)


class Launcher:
    @classmethod
    def launch(cls):
        cls._initialize()
        cls._execute()

    @classmethod
    def _initialize(cls):
        file_separator = "/" if "/" in subprocess.check_output("pwd", universal_newlines=True) else "\\"
        logging.config.dictConfig(JsonFileService.read(f"config{file_separator}logger.json"))

    @classmethod
    def _execute(cls):
        parser = argparse.ArgumentParser(description='The program gets a list of friends on Facebook with their links.')
        parser.add_argument("login", type=str, help="Login from Facebook account")
        parser.add_argument("password", type=str, help="Facebook account password")
        args = parser.parse_args()

        with FriendsParser() as parser:
            parser.go("https://www.facebook.com")
            parser.sing_in(args.login, args.password)
            time.sleep(2)
            parser.find_friends_page()
            parser.calculate_friends()

    def _report(self):
        pass


if __name__ == '__main__':
    Launcher.launch()