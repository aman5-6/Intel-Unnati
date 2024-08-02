import simpy
from shapely.geometry import Point

def vehicle_movement(env, vehicle, road_network, toll_zones):
    print(f"Vehicle {vehicle['vehicle_id']} starting at {vehicle['start']}")
    current_position = vehicle['start']
    
    while current_position != vehicle['end']:
        next_position = Point(current_position.x + 1, current_position.y + 1)
        
        for _, toll_zone in toll_zones.iterrows():
            if toll_zone['geometry'].contains(next_position):
                print(f"Vehicle {vehicle['vehicle_id']} entered toll zone {toll_zone['zone']}")
        
        current_position = next_position
        yield env.timeout(1)

def simulate_vehicles(env, vehicles, road_network, toll_zones):
    for _, vehicle in vehicles.iterrows():
        env.process(vehicle_movement(env, vehicle, road_network, toll_zones))

