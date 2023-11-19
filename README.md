# Python Practices
 A collection of concise and straightforward Python code snippets created by me solving everyday problems. Perfect for beginners and those looking for simple, practical coding solutions.

## Python Security Checker

A Python program to verify if a customer is present in the database. This program employs only if-elif-else loops to handle the various cases, ensuring accuracy and reliability.

### Overview

This Python script is designed to meticulously check whether a customer is listed in a database. It follows a step-by-step process to ensure accuracy and reliability in the verification process. The program relies exclusively on if-elif-else loops to handle different scenarios efficiently.

## Bishop Knight

A simple Python program to determine if a bishop or knight in a game of chess can attack each other. This program exclusively uses if-else-elif statements for educational purposes.

### Overview

This Python script allows you to assess whether a bishop and a knight in a game of chess can attack each other based on their positions on the board. It engages the user by prompting input for the horizontal and vertical positions of both the knight and the bishop. Subsequently, it calculates whether the two pieces can attack each other or not.


## Bingo_Score_Check
Tombala Game Simulation

This is a Python program that simulates a simplified version of the Tombala game for two players. The game is typically known as a bingo-like game, and this implementation provides an overview of the basic rules and gameplay.

### Introduction

In this Tombala game simulation, two players, Grandma and you, each receive a card at the beginning of the game. Each card contains 12 unique numbers, ranging from 1 to 30. It's important to note that, in the traditional game, cards usually contain 15 numbers ranging from 1 to 90. However, for simplicity, we have chosen to use a smaller range of numbers in this version of the game.

The game is played using a sack containing 30 stones, each with a unique number ranging from 1 to 30. The objective of the game is for the players to mark off all the numbers on their cards as the stones are drawn from the sack.

### Game Rules

The Tombala game is played in rounds, and in each round, one stone is randomly drawn from the sack. If the number on the drawn stone matches any of the numbers on a player's card, that number is marked as achieved. The winner of the game is the player who successfully achieves all the numbers on their card first.

There are three possible outcomes for this two-player version of the game:

You Win: If you manage to achieve all the numbers on your card before Grandma does.
Grandma Wins: If Grandma achieves all the numbers on her card before you do.
Tie: A tie can occur if both you and Grandma have only one number remaining on your cards, and that number is drawn from the sack.

## Rock, Paper, Scissors Game

This Python program lets you play the classic "Rock, Paper, Scissors" game against the computer. The game continues until one of the players (you or the computer) wins three times in total. Your program will keep track of the scores for both the user and the computer.

### How to Play

1. Enter your weapon choice (rock, paper, or scissors) as input. Make sure to use all lowercase letters.

2. The computer will randomly select its weapon choice.

3. If you enter an incorrect input, the program will prompt you to provide a valid weapon choice until you do so.

4. The game ends when one side reaches a total of 3 wins.

Enjoy the game and may the best player win!


## Election_Simulation
A Python program simulating a local election system with 3 political parties, user input validation, and data management for city-based election results. Includes menu options for entering, changing, and displaying election results in a user-friendly manner.

### Features

- User-friendly input validation for political party names and city names.
- Ensure the uniqueness of political party names (case-insensitive).
- Menu options for:
  - Entering results for a new city.
  - Changing election results for a specific city.
  - Displaying the current election results, including leading parties.
  - Exiting the program.
- Data management for storing election results in a compact format.
- Provides clear and informative error messages for user guidance.

### Usage

1. Run the program.
2. Enter the names of three political parties.
3. Choose from the menu options to manage and analyze election results.

## Dictionary_IO

This Python program is designed to help you make informed choices when buying a product. It uses file operations and dictionaries to manage information about products and their ratings from different companies. The program keeps prompting the user for input until the special command 'exit' is entered.

### Problem Description

The objective is to create a Python program that advises users on which product to buy based on ratings from different companies. The program uses two input files, "products.txt" and "ratings.txt," to create dictionaries containing information about products and their ratings from various companies.

### Program Workflow

Read the input files, "products.txt" and "ratings.txt." </br>
Create dictionaries for products and ratings, mapping each product to the company selling it and its rating. </br>
Take a string input from the user, referring to the item they want to buy. </br>
Find the company that sells the requested product with the highest rating. </br>
Print the name of the selected company. </br>


## Facebook Friend Recommender

This project simulates a simple friend suggestion algorithm for Facebook, based on a given dataset of friend pairs. The dataset, named friendship.txt, contains anonymized user IDs representing friendships. The goal is to suggest friends for a specific user using a basic algorithm.

### Dataset Format

The dataset is in a tab-separated format, with each line containing two integer values representing the user IDs of a friend pair:
*user1\tuser2
Facebook's undirected relationship format ensures that if user1 is friends with user2, then user2 is also friends with user1.

## Usage

To run the program, provide an integer input corresponding to the ID of the user for whom friend suggestions will be made. The program will then suggest the most frequent user(s) among the friends of the friends of the input user (2nd degree connections). If the input user ID does not exist in the dataset, the program will display "There is no such user."

##Algorithm

Verify if the input user ID exists in the dataset. </br>
If the user exists: </br>
Identify 1st degree connections (friends) of the input user. </br>
Find friends of these 1st degree connections. </br>
Determine the most frequent user ID among these 2nd degree connections. </br>
Display the suggested friend(s). </br>
If the user does not exist, display "There is no such user." </br>
