import simpy
from environment import setup_environment
from vehicle import simulate_vehicles
from toll import calculate_toll
from payment import deduct_toll, user_accounts
from analytics import generate_report
from visualization import plot_map, create_folium_map

def main():
    # Setup environment
    road_network, toll_zones, vehicles = setup_environment()

    # Create simulation environment
    env = simpy.Environment()

    # Simulate vehicles
    simulate_vehicles(env, vehicles, road_network, toll_zones)
    
    # Run simulation
    env.run(until=10)

    # Calculate and deduct tolls (example)
    distance_traveled = 5  # Example distance
    for _, vehicle in vehicles.iterrows():
        toll = calculate_toll(vehicle, distance_traveled)
        deduct_toll(vehicle['vehicle_id'], toll)

    # Generate report
    generate_report(vehicles, user_accounts)

    # Visualization
    plot_map(road_network, toll_zones)
    create_folium_map(road_network, toll_zones)

if __name__ == "__main__":
    main()
