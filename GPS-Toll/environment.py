import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString, Polygon

def setup_environment():
    # Define toll zones as polygons
    toll_zones = gpd.GeoDataFrame({
        'zone': ['A', 'B'],
        'geometry': [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]), Polygon([(3, 3), (5, 3), (5, 5), (3, 5)])]
    })

    # Define road network as lines
    road_network = gpd.GeoDataFrame({
        'road': ['R1', 'R2'],
        'geometry': [LineString([(0, 0), (3, 3), (6, 6)]), LineString([(2, 0), (2, 5)])]
    })

    # Initialize vehicles with starting locations and destinations
    vehicles = pd.DataFrame({
        'vehicle_id': [1, 2],
        'start': [Point(0, 0), Point(2, 0)],
        'end': [Point(6, 6), Point(2, 5)]
    })

    return road_network, toll_zones, vehicles

