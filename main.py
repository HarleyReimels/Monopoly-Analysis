# This program analyzes the chance of landing on each property in the game of Monopoly
# Import function to roll a die 1-6

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from monopolyVariables import *


    d = pd.DataFrame(np.zeros((10,10)))
    
    # Current position sets the player on the Go spot on the board
    current_position = 0

    # Keeps tracks of how many times the player passes go
    passed_go = 0

    # Keep track of doubles
    doubles = 0
    jail_by_doubles = 0
    
    # Game will run a total of 1000 times, we can change this value
    chance_deck = []
    community_deck = []
    games_to_play = 1000
    
    for total_games in range(games_to_play):
        # Game runs is set to 0, this helps control how many games we play
        game_runs = 0
        # Game ends is how many times we throw the die
        # Each game is set to 100 dice rolls
        game_ends = 100
        while game_runs < game_ends:
            # Assign a die roll to each die each time the loop starts over
            die_one = roll_die()
            die_two = roll_die()

            # If we roll a double we increase double variable, else we set it to 0
            if die_one == die_two:
                doubles += 1
            else:
                doubles = 0

            # Increments how many times each die landed on a number
            die_one_rolled_amount[die_one] += 1
            die_two_rolled_amount[die_two] += 1

            # The players current position is equal to both die rolls
            current_position += die_one + die_two

            # If doubles equals 3 then we send player to jail
            if doubles == 3:
                current_position = 10
                jail_by_doubles += 1

            # If the players current position is greater than 39, this means they have passed GO
            # 39 is Boardwalk, if they hit 40, they will be on Go, we need to subtract 40 to simulate all the spaces
            if current_position > 39:
                current_position -= 40
                # Increment Passed Go variable
                passed_go += 1

            # This line accesses the properties list, and gets the name of the property based off the current position
            # Then it finds that property name in the dictionary and increments the value by 1
            properties_dictionary[properties_list[current_position]] += 1

            # Creates the chance deck
            if len(chance_deck) == 0:
                chance_deck = create_chance_list()
            if len(community_deck) == 0:
                community_deck = create_community_list()

            # If player lands on any chance space they draw a card
            if current_position == 7 or current_position == 22 or current_position == 36:
                # Draw Card
                chance_card = draw_card(chance_deck)
                # Get movement
                my_move = card_movement(chance_card, current_position)
                # If not a movement card, we do nothing
                if isinstance(my_move, int):
                    # If movement card, update the properties list with new location
                    current_position = my_move
                    properties_dictionary[properties_list[current_position]] += 1

            # If player lands on community space, they draw a card
            if current_position == 2 or current_position == 17 or current_position == 33:
                # Draw a card from community deck and removes it
                community_card = draw_card(community_deck)
                # Assign my_move with he cards value
                my_move = card_movement(community_card, current_position)
                # If the card has value then we update the property list and move the positIon to it
                if isinstance(my_move, int):
                    current_position = my_move
                    properties_dictionary[properties_list[current_position]] += 1

            # Position 30 is Jail, we will reset the players position to Jail
            if current_position == 30:
                current_position = 10

            # Controls the games loop
            game_runs += 1

    # Create our Board DataFrame
    board_data = {
        'Property': properties_dictionary.keys(),
        'Landed': properties_dictionary.values(),
        "Color": properties_color.values(),
    }
    board_df = pd.DataFrame(board_data)

    # Create Die DataFrame
    die_one_data = {
        "Number": die_one_rolled_amount.keys(),
        "Die One": die_one_rolled_amount.values(),
        "Die Two": die_two_rolled_amount.values()
    }
    die_one_df = pd.DataFrame(die_one_data)

    print(board_df.sort_values(by="Landed", ascending=False))
    print(die_one_df)
    
    # Create heatmap
    my_heatmap = create_heat_map(properties_dictionary, game_ends, games_to_play)
    print(my_heatmap)
    
    # Replace 0 with nan for better representation
    my_heatmap[my_heatmap == 0] = np.nan
    
    # Adjust display size and color
    fig, ax = plt.subplots(figsize=(8,6))
    my_cmap = sns.color_palette(palette='Oranges')
    
    # Put labels on map
    x_labels = properties_list[0:11]
    x_labels.reverse()
    y_labels = properties_list[10:21]
    y_labels.reverse()
    
    
    # Display heatmap
    res = sns.heatmap(my_heatmap, linewidths=1, linecolor="black", fmt=".2f", cmap=my_cmap, annot=True, annot_kws={"size":10},
                xticklabels = x_labels, yticklabels=y_labels)
    # Stops text from getting cut off
    plt.tight_layout()
    # Stops top from getting cut off
    plt.subplots_adjust(top=0.95)
    res.set_title(f"{games_to_play} games of monopoly lasting {game_ends} turns per game.")
    
    plt.show()
    

    # board_df.to_csv('game1.csv')
