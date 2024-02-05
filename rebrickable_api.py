import requests
from typing import Dict, List
from authorisation import Authorisation

url = "https://rebrickable.com"

header = {'Authorization': f"key {Authorisation}"}

def show_themes(name: str =None) -> Dict[int,str]:
    operation = "/api/v3/lego/themes"
    full_url = f"{url}{operation}"
    response = requests.get(full_url, headers= header)
    themes: Dict[int,str] = {}
    for entry in response.json()["results"]:
        if not name or name in entry['name'].lower() or entry['parent_id'] in themes.keys():
            themes[int(entry["id"])] =entry["name"]
    return themes

def show_sets(theme: int, min_year: int = None, min_parts: int = None, ordering: str =None, search: str =None) -> List[Dict]:
    operation = "/api/v3/lego/sets"
    theme_id = f"theme_id={theme}"
    extras = ""
    if min_year:
        extras+=f"&min_year={min_year}"
    if min_parts:
        extras+=f"&min_parts={min_parts}"
    if ordering:
        extras+=f"&ordering={ordering}"
    if search:
        extras+=f"&search={search}"
    full_url = f"{url}{operation}/?{theme_id}{extras}"
    response = requests.get(full_url, headers=header)
    return response.json()["results"]

def unique_parts(set: str) -> int:
    operation = f"/api/v3/lego/sets/{set}/parts/?page_size=1000"
    full_url = f"{url}{operation}"
    response = requests.get(full_url,headers=header)
    return len(response.json()['results'])

def moc_count(set: str) -> int:
    operation = f"/api/v3/lego/sets/{set}/alternates/?page_size=100"
    full_url = f"{url}{operation}"
    response = requests.get(full_url, headers=header)
    return len(response.json()['results'])


if __name__ == "__main__":
    print(show_themes("star wars"))
    print(show_sets(158))
    print(unique_parts("75252-1"))
    print(moc_count("912055-1"))