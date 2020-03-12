import requests
import json
import logging
import time
import sys
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class weerLive:

    def __init__(self, api: str = None):
        try:
            if api is None:
                raise Exception("Sorry, no API key provided!")
            self.url = f"https://weerlive.nl/api/json-10min.php?key={api}&locatie="
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) +
                            " | " + str(fname) + " | " + str(exc_tb.tb_lineno))

    def get_url(self, url=None):
        try:
            if url is None:
                raise Exception("No Url!")

            r = requests.get(url, timeout=10, verify=False)
            if r.status_code == 200:
                content = r.content.decode("utf8")
                return content
            else:
                raise Exception("Error getting URL : " + str(r.status_code))

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) +
                            " | " + str(fname) + " | " + str(exc_tb.tb_lineno))
            return False

    def get_json(self, url=None):
        try:
            if url is None:
                raise Exception("No Url!")

            content = self.get_url(url)

            if content is None or content == "" or content is False:
                raise Exception("No content!")

            js = json.loads(content)
            return js

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) +
                            " | " + str(fname) + " | " + str(exc_tb.tb_lineno))

    def getData(self, plaats: str = None):
        try:
            if plaats is None:
                raise Exception("Geen plaats!")

            url = f"{self.url}{plaats}"
            data = self.get_json(url)
            return data
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(str(e) + " | " + str(exc_type) +
                            " | " + str(fname) + " | " + str(exc_tb.tb_lineno))
