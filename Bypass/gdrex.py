import requests
API="https://pbx1botapi.vercel.app/api/gdrex?url="
def match(url): return "gdrex" in url
def bypass(url): return requests.get(API+url,timeout=20).text
