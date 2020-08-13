import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.last_id += 1  # automatically increment the ID to assign the new user

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        
        Creates that number of users and a randomly distributed friendships
        between those users.
        
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        if num_users <= avg_friendships:
            print("Warning! num_users must be greater than avg_friendships.")
            return
        # Add users.
        for i in range(num_users):
            self.add_user(i)
        # Friendships come in pairs.
        friendships = (num_users * avg_friendships) // 2
        for _ in range(friendships):
        # Create unique, random friendships.
            while True:
                user = random.randint(0, self.last_id - 1)
                friend = random.randint(0, self.last_id - 1)
                # Be sure friendships aren't repeating.
                if (friend != user
                        and friend not in self.friendships[user]
                        and user not in self.friendships[friend]):
                    break
            self.add_friendship(user, friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        
        Returns a dictionary containing every user in that user's
        extended visited with the shortest friendship path between them.
        
        The key is the friend's ID and the value is the path.
        """
  
        visited = {}  # Note that this is a dictionary, not a set
 
        # !!!! IMPLEMENT ME
        # Start the path at the given id.
        path = [user_id]
        # Populate a queue with the starting path.
        queue = deque([path])
        while queue:
            # Get a path from the queue.
            path = queue.popleft()
            # Get the last friend from the queue.
            id_ = path[-1]
            # Make sure they're not already in the visited.
            if id_ not in visited:
                # Add the friend and the path to the visited.
                visited[id_] = path
                # Find new friends to add.
                for friend in self.friendships[id_]:
                    # Add the new friend to the current path and add it to the queue.
                    new_path = [*path, friend]
                    queue.append(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
