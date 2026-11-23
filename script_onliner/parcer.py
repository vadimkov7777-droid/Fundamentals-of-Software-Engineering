import requests

URL = "https://catalog.onliner.by/sdapi/catalog.api/search/dram"
PARAMS = {"group": 0, "group_limit": 0, "limit": 30, "dramkit[0]": "ddr4dimm", "dramkit[1]": "ddr4sodimm", "dramkit[operation]": "union"}

data = requests.get(URL, params=PARAMS).json()