import rebrickable_api
from typing import List
import time

release_years: List[int] = []
num_parts: List[int] = []
perc_unique: List[float] = []
mocs: List[bool] = []

themes: List[int] = rebrickable_api.show_themes("star wars")

for theme in themes:
    sets = rebrickable_api.show_sets(theme)
    for set in sets:
        time.sleep(1)
        if set['num_parts']>0:
            release_years.append(set['year'])
            num_parts.append(set['num_parts'])
            time.sleep(1)
            unique_parts = rebrickable_api.unique_parts(set['set_num'])
            perc_unique.append(unique_parts/set['num_parts'])
            time.sleep(1)
            moc_flag = rebrickable_api.moc_count(set['set_num'])>0
            mocs.append(moc_flag)
print(release_years)
print(num_parts)
print(perc_unique)
print(mocs)