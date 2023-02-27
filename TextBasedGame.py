# Trick or Treat or Die written by Ty Simpson
def main():
    """Main Program Function"""
    rooms_dict = {  # Dictionary of rooms and items
        'Entry Hall': {'East': 'Living Dead Room'},
        'Living Dead Room': {'West': 'Entry Hall', 'North': 'Den of 1000 Screams', 'East': 'Die-ning Room',
                             'South': 'Bloodied Hallway', 'item': 'Candy Bar of Courage'},
        'Den of 1000 Screams': {'South': 'Living Dead Room', 'East': 'Library', 'item': 'Candy Bar of Peace'},
        'Library': {'West': 'Den of 1000 Screams', 'item': 'Candy Bar of Truth'},
        'Die-ning Room': {'West': 'Living Dead Room', 'North': 'Hell\'s Kitchen', 'item': 'Candy Bar of Strength'},
        'Hell\'s Kitchen': {'South': 'Die-ning Room', 'item': 'Candy Bar of Destiny'},
        'Bloodied Hallway': {'North': 'Living Dead Room', 'East': 'Cursed Bedroom', 'item': 'Candy Bar of Wisdom'},
        'Cursed Bedroom': {'boss': 'Evil Spirit'}  # Boss room
    }

    game_status = 'Inactive'  # Assigns game status to determine gameplay loop
    valid_directions = ('North', 'South', 'East', 'West')  # Tuple of valid direction input
    valid_commands = ('Move', 'Look Around', 'Search', 'Collect', 'Quit')  # Tuple of valid commands
    current_room = 'Entry Hall'  # Sets default room
    inventory = []  # Sets inventory list to empty

    def start_game(name):
        """Start game messaging"""
        print("It's Halloween. While trick or treating with friends, you get separated from your friends and come\n"
              "across a creepy old house. You see a sign posted in the overgrown front lawn, written in what appears\n"
              "to be red paint:\n")
        print('Trick Or Treat Or Die:\n 6 Full Size Candy bars Await You Inside\n But Beware the Dangerous Spirit\n '
              'Or You '
              'Shall Surely Die\n')
        print('Welcome', name, 'enter if you dare!')

    def status_action(room, items, commands):
        """Displays player status and gets user input on action"""
        print('Room: ', room)
        print('Inventory: ', items)
        print(
            'Actions:\n{} - Move to another room\n{} - Find valid directions\n{} - Search for candy\n{} - Collect Candy\n{} - Quit Game\n'.format(
                *commands))
        action = input('What will you do?')
        return action

    def move(directions, rooms, player_room):
        """"Function that allows player movement."""
        end_loop = 'No'
        while end_loop == 'No':
            print('Please choose a direction from the list (case sensitive): ')
            print('{}\n{}\n{}\n{}\n'.format(*directions))
            user_direction = input('Which way will you go?\n')
            if user_direction in directions:
                if user_direction in rooms[player_room]:
                    player_room = rooms[player_room][user_direction]
                    return player_room
                else:
                    print('You moved {} but there is no way out. Try again.'.format(user_direction))
            else:
                print('{} is an invalid direction. Try again.'.format(user_direction))

    def boss_check(rooms, room, items):
        """Checks if player is in boss room (Cursed Bedroom). Then checks inventory to determine win or lose."""
        if 'boss' in rooms[room]:
            print('Room: {}'.format(room))
            print('Inventory: ', items)
            if len(items) < 6:
                print('The Evil Spirit appears before you. You are powerless before it and feel your life force leave '
                      'your body. Game Over.')
                game = 'Inactive'
                return game
            else:
                print('The Evil Spirit appears before you. The candy bars in your possession begin to glow.\nThe light '
                      'pierces through the Evil Spirit. The Evil Spirit then takes the form of a kind old man.\nThe '
                      'old man smiles at you and vanishes. It seems you have broken a curse.\nCongratulations, '
                      'you have beat the game. Happy Halloween!')
                game = 'Inactive'
                return game
        else:
            game = 'Active'
            return game

    def look_around(directions, rooms, room):
        """Function to allow user to find valid paths to take"""
        for d in directions:
            if d in rooms[room]:
                print('You can go {}'.format(d))
        print()

    def candy_search(rooms, room):
        """Function to allow user to search for candy in room"""
        if 'item' in rooms[room]:
            print('You see a: {}'.format(rooms[room]['item']))
        else:
            print('You could not find any candy here.')

    def candy_collect(rooms, room, items):
        """Function to add candy to inventory"""
        if 'item' in rooms[room]:
            print('You picked up the {} and added it to your bucket'.format(rooms[room]['item']))
            items.append(rooms[room]['item'])
            rooms[room].pop('item')
        else:
            print('You could not find any candy here.')

    if game_status == 'Inactive':  # Sets whether user wants to play game and then choose player name. Ends game if player says no.
        play_message = input('Would you like to play?\nYes\nNo\n')
        if play_message == 'Yes':
            game_status = 'Active'
            player_name = input('What is your name?')
            start_game(player_name)
        elif play_message == 'No':
            print('Good Bye.')
            game_status = 'Quit'  # Ends Program
        else:
            print('Invalid selection. Try again.')

        while game_status == 'Active':
            command = status_action(current_room, inventory, valid_commands)
            if command in valid_commands:
                if command == 'Move':
                    current_room = move(valid_directions, rooms_dict, current_room)
                    game_status = boss_check(rooms_dict, current_room, inventory)
                elif command == 'Look Around':
                    look_around(valid_directions, rooms_dict, current_room)
                elif command == 'Search':
                    candy_search(rooms_dict, current_room)
                elif command == 'Collect':
                    candy_collect(rooms_dict, current_room, inventory)
                else:
                    print('You have quit the game.')
                    game_status = 'Quit'  # Ends program
            else:
                print('You have entered an invalid command, try again.')


if __name__ == '__main__':
    main()
