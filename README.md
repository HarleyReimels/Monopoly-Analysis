# Monopoly-Analysis

#### This program runs through N amount of games, with each game being N amount of throws, and shows how often each space was landed on, and how often each number on a die was thrown.
<hr/>


## How it's made
##### Tech Used: Python, Pandas, Matplotlib, Seaborn
This project uses Pandas to log information into a dataframe that will be later used to determine probabilities of landing on a space in the game of Monopoly.
I then use Matplotlib and Seaborn to create a heatmap showcasing percentages in a Monopoly-style heat map.
This project was inspired by the YouTube channel Numberphile, specifically the Monopoly episode. 

###### Keeping track of Variables
At the time of creation, Dictionaries were unordered, this means for me to track the index of the player's position, I needed to create a duplicate list of all the property names.

There is a dictionary where the key is the property name and the value is initially 0 and is incremented by 1 when a player lands on the space. 

There are also dictionaries to track the die rolls, and to record how many times we rolled a number. 

I also have the Chance and Community Chest decks, these cards have movement cards and are necessary for accurate data. If a person lands on Chance or Community Chest
and gets a movement card, Chance, and the movement space are incremented by 1, and that movement card is removed from the Deck. Once a deck is empty, a new deck is created and reshuffled. 

We also created our initial Dataframe, an 11 x 11 filled with 0's. The purpose of this is to assign the outside elements with the properties of Monopoly. Once the Properties have been assigned, we perform
some basic math to get the percentage of each space. Now that all properties have a number, we set the 0's to nan, to not affect the heatmap we will be creating.

###### The game
The main loop is run with a for statement, controlled by how many games you want to play. Next, we set how many rolls we want each game to last, this is where the main heart of the code exists.
It begins by rolling two dice, if the dice are doubles, we keep track, three doubles means straight to Jail. Next, we increment our dictionary to record how many times we rolled each die. Next, we
check to see if their movement roll is going to be higher than 40, this means they have completed a full lap. If this happens we take their current position ex: 43 and subtract it from 40, placing them
on the third property. This property is now incremented.

If they land on a Chance or Community Deck, a card is drawn from the deck, if it is a movement card, then they will move. The card is then discarded from the deck, when a deck is empty it will be
refilled and reshuffled. 

Once all the games are complete, we load our dictionaries full of values into a dataframe. Once this is complete we use Matplotlib and Seaborn to showcase the results.


Author: Harley Reimels

Contact: Reimels.Harley@gmail.com
