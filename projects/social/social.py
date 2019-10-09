import random
from itertools import combinations

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(numUsers):
            self.addUser(user)
        # Create friendships
        friends_comb = []
        combo = combinations(range(1, numUsers + 1), 2)
        for relationship in list(combo):
            friends_comb.append(relationship)

        random.shuffle(friends_comb)
        total_friends = int((avgFriendships * numUsers)/2)
        new_friend = friends_comb[:total_friends]
        
        for friendship in new_friend:
            first_friend = friendship[0]
            second_friend = friendship[1]
            self.addFriendship(first_friend, second_friend)
        # for userID in self.users:
        #     for friendID in range(userID +1, self.lastID):
        #         friends_comb.append((userID, friendID))
        #     random.shuffle(friends_comb)
        
        # for i in range(0, (numUsers * avgFriendships // 2)):
        #     friendship = friends_comb[i]
        #     first_friend = friendship[0]
        #     second_friend = friendship[1]
        #     self.addFriendship(first_friend, second_friend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        qq = Queue()
        qq.enqueue([userID])

        while qq.size() > 0:
            path  = qq.dequeue()
            node = path[-1]

            if node not in visited:
                visited[node] = path
                for next_node in self.friendships[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    qq.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Connections for 1:")
    print(connections)
    connections = sg.getAllSocialPaths(2)
    print("Connections for 2:")
    print(connections)
    connections = sg.getAllSocialPaths(10)
    print("Connections for 10:")
    print(connections)
