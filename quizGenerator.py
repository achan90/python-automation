#! /usr/bin/env python3

import shelve
import os
import pyperclip
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {"Alabama": "Montgomery",
            "Alaska": "Juneau",
            "Arizona": "Phoenix",
            "Arkansas": "Little Rock",
            "California": "Sacramento",
            "Colorado": "Denver",
            "Connecticut": "Hartford",
            "Delaware": "Dover",
            "Florida": "Tallahassee",
            "Georgia": "Atlanta",
            "Hawaii": "Honolulu",
            "Idaho": "Boise",
            "Illinois": "Springfield",
            "Indiana": "Indianapolis",
            "Iowa": "Des Moines",
            "Kansas": "Topeka",
            "Kentucky": "Frankfort",
            "Louisiana": "Baton Rouge",
            "Maine": "Augusta",
            "Maryland": "Annapolis",
            "Massachusetts": "Boston",
            "Michigan": "Lansing",
            "Minnesota": "Saint Paul",
            "Mississippi": "Jackson",
            "Missouri": "Jefferson City",
            "Montana": "Helena",
            "Nebraska": "Lincoln",
            "Nevada": "Carson City",
            "New Hampshire": "Concord",
            "New Jersey": "Trenton",
            "New Mexico": "Santa Fe",
            "New York": "Albany",
            "North Carolina": "Raleigh",
            "North Dakota": "Bismarck",
            "Ohio": "Columbus",
            "Oklahoma": "Oklahoma City",
            "Oregon": "Salem",
            "Pennsylvania": "Harrisburg",
            "Rhode Island": "Providence",
            "South Carolina": "Columbia",
            "South Dakota": "Pierre",
            "Tennessee": "Nashville",
            "Texas": "Austin",
            "Utah": "Salt Lake City",
            "Vermont": "Montpelier",
            "Virginia": "Richmond",
            "Washington": "Olympia",
            "West Virginia": "Charleston",
            "Wisconsin": "Madison",
            "Wyoming": "Cheyenne"}

# Generate 35 quiz files
for num in range(35):
    # Create the quiz and answer key files
    with open("quiz{}.txt".format(num + 1), "w+") as quiz:
        pass

    with open("quiz{}Answer.txt".format(num + 1), "w+") as answer:
        pass

        # Write out header for the quiz
        # Shuffle the order of the states
        # Loop through all 50 states, making questions for each
