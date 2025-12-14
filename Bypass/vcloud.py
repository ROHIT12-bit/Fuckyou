import requests
API="https://pbx1botapi.vercel.app/api/vcloud?url="
def match(url): return "vcloud" in url
def bypass(url): return requests.get(API+url,timeout=20).text
