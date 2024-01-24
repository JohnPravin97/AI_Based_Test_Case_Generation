import carla
import random
import time

def spectate(world, vehicle):
    spectator = world.get_spectator()

    transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4,z=2.5)),vehicle.get_transform().rotation)
    # print("Vehicle at", ego_vehicle.get_transform())

    spectator.set_transform(transform)

def get_waypoint_of_spawn_points(world, user_road_id):
    maps = world.get_map()
    list_of_spawn_points = maps.get_spawn_points()
    possible_spawn_points =[]

    for spawn_points in list_of_spawn_points:
        # To get the nearest waypoint of the driving ego vehicle
        ego_spawn_way_point = maps.get_waypoint(spawn_points.location)
        if ego_spawn_way_point.road_id == user_road_id :
            possible_spawn_points.append(spawn_points)
    
    return possible_spawn_points

