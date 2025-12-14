import requests
from urllib.parse import urlparse

API = "https://pbx1botapi.vercel.app/api/hubcloud?url="

def match(url: str):
    domain = urlparse(url).netloc.lower()
    return "hubcloud" in domain

def bypass(url: str):
    r = requests.get(API + url, timeout=20)
    return r.text
