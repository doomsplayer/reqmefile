#! /usr/bin/env python3
"""reqmefile
Usage:
  reqmefile.py [-g <google_api_key>] [-d <dropbox_api_key>] [-p <path>] -t <title>

Options:
  -g <google_api_key>   google api key, if none, it will read from env `REQMEFILE_DROPBOX_API`
  -d <dropbox_api_key>  dropbox api key, if none, it will read from env `REQMEFILE_GOOGLE_API`
  -t <title>            title of this request
  -p <path>             the location that request files should reside in [default: /files]
"""

from os import environ

import requests
from docopt import docopt
from dropbox.dropbox import Dropbox

GOOGLE_URL = "https://www.googleapis.com/urlshortener/v1/url"


def imp(dapi, gapi, path, title):
    client = Dropbox(dapi)
    resp = client.file_requests_create(title, path)

    req = requests.post("{}?key={}".format(GOOGLE_URL, gapi), json={"longUrl": resp.url})
    print("File request URL is:", req.json()["id"])


if __name__ == "__main__":
    args = docopt(__doc__)
    DROPBOX_API_KEY = args["-d"] or environ.get("REQMEFILE_DROPBOX_API")
    GOOGLE_API_KEY = args["-g"] or environ.get("REQMEFILE_GOOGLE_API")
    PATH = args["-p"]
    TITLE = args["-t"]

    if DROPBOX_API_KEY is None:
        raise RuntimeError("Dropbox API is not set")
    if GOOGLE_API_KEY is None:
        raise RuntimeError("Google API is not set")

    imp(DROPBOX_API_KEY, GOOGLE_API_KEY, PATH, TITLE)
