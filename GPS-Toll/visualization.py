import matplotlib.pyplot as plt
import folium

def plot_map(road_network, toll_zones):
    fig, ax = plt.subplots()
    road_network.plot(ax=ax, color='blue', label='Roads')
    toll_zones.plot(ax=ax, color='red', alpha=0.5, label='Toll Zones')
    plt.legend()
    plt.show()

def create_folium_map(road_network, toll_zones):
    m = folium.Map(location=[0, 0], zoom_start=13)

    for _, toll_zone in toll_zones.iterrows():
        folium.GeoJson(toll_zone['geometry']).add_to(m)

    for _, road in road_network.iterrows():
        folium.PolyLine(list(road['geometry'].coords), color='blue').add_to(m)

    m.save('map.html')

