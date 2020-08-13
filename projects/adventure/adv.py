from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class ExploreRooms:
    def __init__(self, world: World):
        self.world = world
        self.start = self.world.starting_room
        self.path = []

# group utility function to class
# staticMethod()
    @ staticmethod
    def get_neighbors(room: Room):
        neighbors = []
        if room.n_to is not None:
            neighbors.append((room.n_to, 'n'))
        if room.w_to is not None:
            neighbors.append((room.w_to, 'w'))
        if room.e_to is not None:
            neighbors.append((room.e_to, 'e'))
        if room.s_to is not None:
            neighbors.append((room.s_to, 's'))
        return neighbors

    def DFT(self, room: Room):
        # Depth first transversal return room with no unexplored pathways
        path = [room]
        stack = [path]
        visited = set()

        while stack:
            # get path way and last room
            path = stack.pop()
            rm = path[-1][0]

            # checks if it has been explored
            if rm.id not in visited:
                visited.add(rm.id)

                # If all of the neighboring rooms are on this path
                # this is a dead end
                # return the path to this room

                neighbors = self.get_neighbors(rm)
                if all([neighbor_room.id in [path_room.id for path_room, _ in path]
                        for neighbor_room, _ in neighbors]):
                    # The start of this path is already a part of the main path.
                    return path[1:]

                # Otherwise, keep exploring this path.
                for neighbor in neighbors:
                    # Only add neighbors that aren't yet on the main path.
                    if neighbor[0].id not in [room.id for room, _ in self.path]:
                        new_path = [*path, neighbor]
                        stack.append(new_path)
        return path

    def BFT(self, room: Room):
        path = [room]
        visited = set()
        queue = deque()
        queue.append(path)

        while queue:
            # Get a candidate path and the last room user was in.
            path = queue.popleft()
            rm = path[-1][0]

            # Check that this room hasn't been seen.
            if rm.id not in visited:
                visited.add(rm.id)

                # If any neighbor of this room is not yet on the main path, return the path to this room.
                neighbors = self.get_neighbors(rm)
                if any([neighbor_room.id not in [path_room.id for path_room, _ in self.path]
                        for neighbor_room, _ in neighbors]):
                    # The start of this path is already a part of the main path.
                    return path[1:]

                # Otherwise, continue looking for a room with an unexplored neighbors.
                for neighbor in neighbors:
                    new_path = [*path, neighbor]
                    queue.append(new_path)

    def explore_paths(self):

        print('Finding path...')
        # Initialize path with a tuple (starting room, empty string)
        self.path = [(self.start, '')]

        # loop
        while True:
            # Create a new reference for this loop
            main_path = self.path.copy()
            # use DFT to a room with no more neighors available
            dft_path = self.DFT(main_path[-1])
            # append path to path list
            main_path = [*main_path, *dft_path]
            # Update for BFT
            self.path = main_path
            # use BFT to go back to closest room with unexplored neighbor
            bft_path = self.BFT(main_path[-1])

            # If BFT finds no unexplored rooms, the graph has been traversed.
            if not bft_path:
                # return path
                return [direction for _, direction in self.path[1:]]
            # append path to main path
            main_path = [*main_path, *bft_path]
            # Update for next loop.
            self.path = main_path


mapper = ExploreRooms(world=world)
traversal_path = mapper.explore_paths()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
