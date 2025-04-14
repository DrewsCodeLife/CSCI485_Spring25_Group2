*note, these are from a brief overview of the slides and websites, I haven't done a deep dive into any of them ~Drew*
---
# Primary:
## PeMS (Caltrans)
- Dense temporal resolution
- Road segment identifiers
- Speed, occupancy, volume
- Covers a major U.S. region (California)
- Model volume over time and integrate spatial adjacency
- Probably the highest quality and most easily accessible

[PeMS](https://pems.dot.ca.gov/)

# Graph Feature Engineering:
## OpenStreetMap (OSM)
- Build a road network graph
- Extract adjacent intersections, road hierarchy
- Enables the desired dynamic map

[OSM](https://www.openstreetmap.org/)

## Secondary (if we want to do within a city):
### City of Los Angeles Open Data – Traffic Flow
- Should pair well with OpenStreetMap for road networks
- Similar to PeMS data I think?
- Could abstract the data to build a model of some portion of the city and simulate it!

[LA Traffic counted at intersections](https://data.lacity.org/Transportation/LADOT-Traffic-Counts-Summary/94wu-3ps3/about_data)
[Pedestrian and bike data?](https://data.lacity.org/Transportation/2023-Walk-Bike-Count-Data/6ux4-qj74/about_data)
[More ped and bike data, different area](https://data.lacity.org/Transportation/Arts-District-Pedestrian-and-Bike-Counts-LA-CoMoti/mbz9-j2zk/about_data)

There are also a number of datasets on meter occupancy, though I doubt we want to use that.


