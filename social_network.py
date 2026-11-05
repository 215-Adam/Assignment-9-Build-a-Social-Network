class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Avoid storing the same friend twice
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        missing = [n for n in (person1_name, person2_name) if n not in self.people]
        if missing:
            verb = "doesn't" if len(missing) == 1 else "don't"
            print(f"Friendship not created. {' and '.join(missing)} {verb} exist!")
            return
        if person1_name == person2_name:
            print(f"Friendship not created. {person1_name} can't befriend themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = ", ".join(friend.name for friend in person.friends)
            print(f"{person.name} is friends with: {friend_names}")


# Test your code here
if __name__ == "__main__":
    # Person class basics
    alex = Person("Alex")
    jordan = Person("Jordan")
    print(alex.friends)  # []
    alex.add_friend(jordan)
    print(alex.friends[0].name)  # Jordan

    print("\n--- Building the network ---")
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    print(network.people)
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Edge case: duplicate person
    network.add_person("Alex")  # Alex already exists in the network!

    # Create friendships (8+ valid friendships)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # Friendship not created. Johnny doesn't exist!
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Edge cases: neither person exists, duplicate friendship, self-friendship
    network.add_friendship("Sam", "Pat")       # Friendship not created. Sam and Pat don't exist!
    network.add_friendship("Alex", "Jordan")   # duplicate: no repeated entry
    network.add_friendship("Casey", "Casey")   # can't befriend themselves

    print("\n--- Network ---")
    network.print_network()

    # Print again after more additions
    print("\n--- Network after adding Drew ---")
    network.add_person("Drew")
    network.add_friendship("Drew", "Casey")
    network.add_friendship("Drew", "Alex")
    network.print_network()
