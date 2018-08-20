import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

observations = pd.read_csv('observations.csv')

sheep_observations = observations.merge(sheep_species)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
#print obs_by_park

parks = ['Bryce National Park', 'Great Smoky Mountains National Park',  'Yellowstone National Park', 'Yosemite National Park' ]

x = range(len(parks))
y = [250, 149, 507, 282]

plt.figure(figsize = (16,4))
ax = plt.subplot()
plt.bar(x, y)
ax.set_xticks(x)
ax.set_xticklabels(parks)
plt.ylabel('Number of Observatios')
plt.title('Observations of Sheep per week')
plt.show()