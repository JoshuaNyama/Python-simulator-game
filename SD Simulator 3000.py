import random


class Player:
    def __init__(self, name):
        # initialise the code with default attributes.
        self.name = name    # player's name
        self.inventory = []  # Bag to store maximum of 4 items
        self.player_health = 100  # Player's health. Starting at full.
        self.player_position = "Home"  # Starting location
        self.balance = 0  # Amount of money player has. Currency --> SD

    def move(self, direction, location):
        """
        If the direction is correct, player moves to a new location
        direction: where the player wants to go
        location: The dictionary showing the possible directions
        """
        if direction in location[self.player_position]:
            self.player_position = location[self.player_position][direction]
            self.player_health -= 10  # Reduce health after every move
            print(f"You moved {direction} to {self.player_position}.")
            print(f"health - 10 --> {self.player_health}")
        else:
            print("Please enter an appropriate direction.")

    def collect_item(self, item):
        """
        Items are added to the inventory. With a max of 4 items.
        item: items to be collected
        """
        if len(self.inventory) < 4:
            self.inventory.append(item)
            print(f"You collected: {item}.")
        else:
            print("Max items collected. Empty bag to collect more items")

    def check_health(self):
        """
        Check player's health
        """
        print(f"Your health is --> {self.player_health}.")

    def check_balance(self):
        """
        Check player's balance
        """
        print(f"Your current balance is --> {self.balance} SD")

    def add_coins(self, amount):
        """
        Add money to player's balance
        """
        self.balance += amount
        print(f"You have been credited with {amount} SD! You now have {self.balance} SD.")

    def check_inventory(self):
        if self.inventory:
            print("__Your inventory__")
            for item in self.inventory:
                print(f"--> {item}")    # Check player's inventory
        else:
            print("Inventory is empty.")

    def drop_item(self, player):
        """
        Allows player to drop items if items are available in inventory
        """
        if player.inventory:
            print("__Your inventory__")
            for idx, item in enumerate(player.inventory):
                print(f"{idx + 1}. {item}")  # Display numbered list of items

            choice = input("Enter the number of the item you want to drop: ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(player.inventory):
                    dropped_item = player.inventory.pop(choice - 1)
                    print(f"You dropped {dropped_item}.")
                else:
                    print("Invalid selection. Please choose a valid item number.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("Your inventory is empty. Nothing to drop.")


locations = {
    "Home": {"south": "Gate", "west": "Market", "east": "Rock site"},
    "Gate": {"north": "Home", "south": "Forest"},
    "Forest": {"west": "Mountain", "north": "Gate", "east": "River", "south": "Cave"},
    "Market": {"north": "Stage", "east": "Home"},
    "Mountain": {"south": "Cliff", "east": "Forest", "north": "Rock site"},
    "Cave": {"north": "Forest"},
    "Rock site": {"west": "Home"},
    "River": {"west": "Forest", "north": "Market"},
    "Cliff": {"north": "Mountain"},
    "Stage": {"south": "Market"},
}

items_by_location = {
    "Forest": ["Fruits"],
    "Mountain": ["Crystals"],
    "Cliff": ["Herbs"],
    "Cave": ["Bat wings"],
    "River": ["Fish", "Drinking water"],
    "Rock site": ["Gold"]
}

challenges_by_location = {
    "Cave": "Cave might collapse. Chance of winning 5/10."
            "\n Collect valuable bat wings or flee.",
    "Mountain": "Battle mythical Eagle to acquire Crystals "
                "\nat the cost of 50 health or flee. Chance of winning 3/10",
    "Rock site": "Site is poisonous, "
                 "\ncollect gold at the cost of 90 health or flee. "
                 "\nChance of winning 1/10"
}

item_prices = {
    "Fruits": 2,
    "Crystals": 60,
    "Herbs": 12,
    "Bat wings": 20,
    "Fish": 4, "Drinking water": 1,
    "Gold": 90
}

items_by_health = {
    "Fruits": 10,
    "Herbs": 20,
    "Fish": 5,
    "Drinking water": 2,
}


# Main Game
def start_game():
    print("Welcome to SD simulator 3000!"
          "\nCurrency --> SD")
    name = input("Enter your character's name: ")
    player = Player(name)
    print(f"Hello, {player.name}. You're currently at {player.player_position}.")

    while True:
        """
        Loops through the game until certain conditions are met. For example, player exists, wins or, runs out of 
        health.
        """
        if player.player_health <= 0:
            print("You have run out of health. Game over!")
            break

        print(f"\nYou are currently at {player.player_position}.")
        print("__Available options__")
        print("1. Move to a new location")
        print("2. Check health")
        print("3. Check inventory")
        print("4. Check balance")
        print("5. Use item")
        print("6. Drop items")
        print("7. Exit the game")

        choice = input("What would you like to do? (1-7): ")

        if choice == "1":
            print("__Available directions__")
            for direction, location in locations[player.player_position].items():
                print(f"--> {direction} to {location}")

            move = input("Which direction would you like to go?: ").lower()
            player.move(move, locations)

            if player.player_position == "Forest":
                option = input("1. Look around for items (yes/no): ")
                if option == "no":
                    print("You can still come back to collect items.")
                    continue
                if option == "yes":
                    print("Items available:"
                          "\n1. Fruits")
                    item_option = input("Choose item to collect: ")
                    if item_option == "1":
                        player.collect_item("Fruits")
                    else:
                        print("Option not available")
                else:
                    print("Option not available!")
            elif player.player_position == "Market":
                print("What would you like to do?"
                      "\n1. Purchase an item"
                      "\n2. Sell items")
                user_option = input("Select option (1/2): ")
                if user_option == "1":
                    print("__Available option__"
                          "\n1. Fruits --> 2 SD"
                          "\n2. Herbs --> 7 SD"
                          "\n3. Fish --> 4 SD"
                          "\n4. Drink water --> 1"
                          "\nNOTE: available items can restore health..")
                    if player.balance < 7:
                        print("You currently don't have enough money to purchase items")
                        continue
                    user_select = input("Select an item (1-4) or 0 to cancel: ")
                    if user_select == "1":
                        player.collect_item("Fruits")
                        player.balance -= 2
                        print("2 SD was deducted from Balance"
                              f"\nCurrent balance --> {player.balance}")
                    elif user_select == "2":
                        player.collect_item("Herbs")
                        player.balance -= 7
                        print("7 SD was deducted from Balance"
                              f"\nCurrent balance --> {player.balance}")
                    elif user_select == "3":
                        player.collect_item("Fish")
                        player.balance -= 5
                        print("5 SD was deducted from Balance"
                              f"\nCurrent balance --> {player.balance}")
                    elif user_select == "4":
                        player.player_health += 2
                        player.balance -= 1
                        print("Health increases by 2")
                    elif user_select == "0":
                        print("Canceled")
                        continue
                    else:
                        print("option not available..")
                elif user_option == "2":
                    if not player.inventory:
                        print("Your inventory is empty. There's nothing to sell.")
                        continue

                    print("__Your inventory__")
                    for index, item in enumerate(player.inventory, start=1):
                        print(f"{index}. {item} (Value: {item_prices.get(item, 0)} SD)")

                    try:
                        choice = int(input("Enter the number of the item you want to sell (or 0 to cancel): "))
                        if choice == 0:
                            print("You decided not to sell anything.")
                            continue

                        if 1 <= choice <= len(player.inventory):
                            item_to_sell = player.inventory.pop(choice - 1)
                            value = item_prices.get(item_to_sell, 0)
                            player.add_coins(value)
                            print(f"You sold {item_to_sell} for {value} SD.")
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            elif player.player_position == "Gate":
                NCP = input("NCP: Do you want to proceed? (yes/no):  ").lower()
                if NCP == "yes":
                    print("Gate opened.. Proceed moving out.")
                    continue
                if NCP == "no":
                    print("Take your time!")
                    continue
                else:
                    print("Invalid option!")

            elif player.player_position == "Stage":
                print(f"NCP: Welcome {player.name}"
                      f"\nReady to travel away?")
                player_opt = input("You (yes/no): ").lower()
                if player_opt == "yes":
                    if player.balance >= 100:
                        print("You payed 100 SD."
                              f"\nCongratulations {player.name} you won!")
                        player.balance -= 100
                        break
                if player_opt == "no":
                    print("You can come back any time!")
                    continue
                else:
                    print("Balance not enough. Come back when you have 100 SD")

            elif player.player_position == "Cliff":
                print("1. Look around for items or 0 to cancel")
                ask_player = input("Enter option (1/0): ")
                if ask_player == "1":
                    print("__Items available__"
                          "\nHerbs")
                    player_collect = input("1. Collect item or 0 to cancel")
                    if player_collect == "1":
                        player.collect_item("Herbs")
                    else:
                        print("Canceled")
                        continue
                else:
                    print("Canceled")
                    continue

            elif player.player_position == "River":
                print("__Available items__"
                      "\n1. Drink water"
                      "\n2. Fish")
                player_choice = input("What would you like collect or 0 to cancel: ")
                if player_choice == "1":
                    player.player_health += 2
                    print("Health increases by 2")
                elif player_choice == "2":
                    player.collect_item("Fish")
                elif player_choice == "0":
                    print("Canceled")
                    continue
                else:
                    print("Invalid option!")
                    continue

            if player.player_position in challenges_by_location:
                print(challenges_by_location[player.player_position])
                if player.player_position == "Cave":
                    action = input("Enter option (yes/flee): ").lower()
                    if action == "yes":
                        rand_bat = random.randint(1, 10)
                        if rand_bat <= 5:
                            player.collect_item("Bat wings")
                        else:
                            player.player_health -= 20
                            print("You lost to Bats. Health -20. Better luck next time!")
                    else:
                        print("canceled")
                        continue

                elif player.player_position == "Mountain":
                    player_option = input("select option (yes/flee): ").lower()
                    if player_option == "yes":
                        rand = random.randint(1, 10)
                        if rand <= 3:
                            player.collect_item("Crystals")
                        else:
                            player.player_health -= 50
                            print("You lost to Mythical Eagle. Health -50")
                    else:
                        print("You fled to safety..")

                elif player.player_position == "Rock site":
                    player_decision = input("Select option (yes/flee): ").lower()
                    if player_decision == "yes":
                        rand = random.randint(1, 10)
                        if rand == 1:
                            player.collect_item("Gold")
                        else:
                            player.player_health -= 90
                    else:
                        print("You fled to safety")

        elif choice == "2":
            player.check_health()

        elif choice == "3":
            player.check_inventory()

        elif choice == "4":
            player.check_balance()

        elif choice == "5":
            if "Fruits" in player.inventory or "Herbs" in player.inventory or "Fish" in player.inventory:
                print("__usable items__"
                      "\n1. Fruits"
                      "\n2. Herbs"
                      "\n3. Fish")
                try:
                    option1 = int(input("Enter option (1/2): "))
                    if option1 == 1:
                        player.inventory.remove("Fruits")
                        player.player_health += 10
                        print("You consumed Fruits"
                              "\nHealth increases by 10")
                    elif option1 == 2:
                        player.inventory.remove("Herbs")
                        player.player_health += 50
                        print("You consumed herbs"
                              "\nHealth increases by 50")
                    elif option1 == 3:
                        player.inventory.remove("Fish")
                        player.player_health += 5
                        print("You consumed fish. Health increases by 5")
                    else:
                        print("Option not available")

                except ValueError:
                    print("Not available")
            else:
                print("Inventory must contain at least one of the following: Fruits, Herbs, or Fish")

        elif choice == "6":
            player.drop_item(player)

        elif choice == "7":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Option not available! Please select from (1-7)")


if __name__ == '__main__':
    start_game()
