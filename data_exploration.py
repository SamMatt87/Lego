import rebrickable_api
from typing import Dict
import numpy as np
import time
from matplotlib import pyplot as plt

themes = rebrickable_api.show_themes('star wars')
print(themes)

year_count: Dict[int, int] = {}
for year in range(1999,2025):
    year_count[year] = 0
part_count: Dict[int,int] = {}
unique_parts: Dict[float, int] = {}
moc_counts: Dict[int,int]={}
for hundred in range(0,1100,100):
    part_count[hundred] = 0
for thousand in range(2000,11000,1000):
    part_count[thousand] = 0
for percentage in range(0,11,1):
    unique_parts[percentage/10] = 0
for count in range(0,41):
    moc_counts[count] = 0
for theme in themes:
    print(len(rebrickable_api.show_sets(theme)))
    for set in rebrickable_api.show_sets(theme):
        time.sleep(1)
        year_count[set['year']] +=1
        if set['num_parts']<1000:
            part_count[int(np.floor(set['num_parts']/100))*100] += 1
        else:
            part_count[int(np.floor(set['num_parts']/1000))*1000] += 1
        if set['num_parts']>0:
            unique_parts[np.round((rebrickable_api.unique_parts(set['set_num'])/set['num_parts']),1)]+=1
        else:
            print(set)
        time.sleep(1)
        mocs = rebrickable_api.moc_count(set['set_num'])
        moc_counts[mocs] += 1
print(year_count)
print(part_count)
print(unique_parts)
print(moc_counts)
print(sum(year_count.values()))
print(sum(part_count.values()))
print(sum(unique_parts.values()))
print(sum(moc_counts.values()))
def plot(data: Dict[int,int]) -> None:
    plt.bar(range(len(data)), list(data.values()), align="center")
    plt.xticks(range(len(data)), list(data.keys()))
    plt.show()

plot(year_count)
plot(part_count)
plot(unique_parts)
plot(moc_counts)
