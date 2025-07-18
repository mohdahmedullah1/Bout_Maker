import random

class Fighter:
    def __init__(self, name, weight, months_trained, age, fights_fought):
        self.name = name
        self.weight = weight
        self.weight_class = self.get_weight_class()
        self.months_trained = months_trained
        self.age = age
        self.age_group = self.get_age_group()
        self.fights_fought = fights_fought
        self.wins = 0  # Track the number of wins
        self.event_fights = 0  # Track the number of matches in the event
        self.losses = 0  # Track the number of losses in the event

    def get_weight_class(self):
        if self.weight < 56.7:
            return "Flyweight"
        elif self.weight < 61.2:
            return "Bantamweight"
        elif self.weight < 65.8:
            return "Featherweight"
        elif self.weight < 70.3:
            return "Lightweight"
        elif self.weight < 77.1:
            return "Welterweight"
        elif self.weight < 83.9:
            return "Middleweight"
        elif self.weight < 93.0:
            return "Light Heavyweight"
        else:
            return "Heavyweight"

    def get_age_group(self):
        if self.age < 16:
            return "Under 16"
        elif self.age < 18:
            return "Under 18"
        else:
            return "18 or Above"

def input_fighter():
    name = input("Enter fighter's name: ")
    weight = float(input("Enter weight in kg: "))
    months_trained = int(input("Enter number of months trained: "))
    age = int(input("Enter age: "))
    fights_fought = int(input("Enter number of fights fought: "))
    return Fighter(name, weight, months_trained, age, fights_fought)

def create_groups(fighters, group_size=5):
    groups = []
    for i in range(0, len(fighters), group_size):
        groups.append(fighters[i:i + group_size])
    return groups

def match_fighters(group):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if group[i].event_fights < 4 and group[j].event_fights < 4:
                print(f"Match: {group[i].name} vs {group[j].name}")
                winner_name = input(f"Enter the winner of {group[i].name} vs {group[j].name}: ").strip()
                if winner_name == group[i].name:
                    group[i].wins += 1
                    group[j].losses += 1
                elif winner_name == group[j].name:
                    group[j].wins += 1
                    group[i].losses += 1
                group[i].event_fights += 1
                group[j].event_fights += 1

def display_results(groups):
    for group in groups:
        group.sort(key=lambda x: (x.wins, -x.losses), reverse=True)
        medals = ["Gold", "Silver", "Bronze"]
        for i, fighter in enumerate(group[:3]):
            print(f"{medals[i]} Medal: {fighter.name} with {fighter.wins} wins and {fighter.losses} losses")
        for fighter in group[3:]:
            print(f"{fighter.name} with {fighter.wins} wins and {fighter.losses} losses")

def main():
    num_fighters = int(input("Enter the number of fighters: "))
    fighters = []
    for _ in range(num_fighters):
        fighters.append(input_fighter())

    # Group fighters by age division
    age_groups = {"Under 16": [], "Under 18": [], "18 or Above": []}
    for fighter in fighters:
        age_groups[fighter.age_group].append(fighter)

    # Create optimal groups within each age division
    all_groups = []
    for group_name, group_fighters in age_groups.items():
        groups = create_groups(group_fighters)
        all_groups.extend(groups)

    # Matchmaking and user input for winners
    for group in all_groups:
        match_fighters(group)

    # Display results and award medals
    display_results(all_groups)

    print("\nRanked Fighters:")
    all_fighters = sorted(fighters, key=lambda x: (x.wins, -x.losses), reverse=True)
    for rank, fighter in enumerate(all_fighters, start=1):
        print(f"{rank}. {fighter.name}: {fighter.wins} wins, {fighter.losses} losses, {fighter.event_fights} matches fought")

if __name__ == "__main__":
    main()
