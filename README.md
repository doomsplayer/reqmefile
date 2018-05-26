# ReqMeFile

It's laborious to open a webpage and click somewhere if you want to create dropbox file request and shorten the URL.

# Requirement

python3

# Usage

Download the file and put it into your `$PATH`. 

# Detail usage

```
Usage:
  reqmefile.py [-g <google_api_key>] [-d <dropbox_api_key>] [-p <path>] -t <title>

Options:
  -g <google_api_key>   google api key, if none, it will read from env `REQMEFILE_DROPBOX_API`
  -d <dropbox_api_key>  dropbox api key, if none, it will read from env `REQMEFILE_GOOGLE_API`
  -t <title>            title of this request
  -p <path>             the location that request files should reside in [default: /files]
```

# API keys

## Dropbox 

I'm too lazy to create an OAuth server. If you want to use this script, just go to [Here](https://www.dropbox.com/developers/apps) create yourself a dropbox App, then click the button under `Generated access token`.

## Google

Go to [Here](https://developers.google.com/url-shortener/v1/getting_started#APIKey) to get a key or just use mime: `AIzaSyBv4geoZKn9pZDQJFEZehv4AkDaL2bC6G4`