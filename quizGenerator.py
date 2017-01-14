#! /usr/bin/env python3

import random
import os

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

# shuffle the order of the states.
states = list(capitals.keys())
random.shuffle(states)

# Set quiz directory.
os.chdir(
    os.path.join(
        "/home", "peksi", "Documents", "python3", "projects",
        "repositories", "python-automation", "quizzes"))
quizDirectory = os.getcwd()
print("Quiz and answer files generated to {}".format(quizDirectory))


# Generate 35 quiz and answer key files
def quizGenerator():
    # Create quiz and aswer key files.
    for num in range(35):
        # Create quiz files
        with open("quiz{}.txt".format(num + 1), "w") as quiz:
            quiz.write("Name:\n\nDate:\n\nPeriod:\n\n")
            quiz.write(
                (" " * 20) + "State Capital Quiz (Form {})\n\n".format(
                    num + 1))

            # write the question and answer options to the quiz file.
            for questions in range(50):
                correctAnswer = capitals[states[questions]]
                wrongAnswers = list(capitals.values())
                del wrongAnswers[wrongAnswers.index(correctAnswer)]
                wrongAnswers = random.sample(wrongAnswers, 3)
                answerOptions = wrongAnswers + [correctAnswer]
                random.shuffle(answerOptions)

                quiz.write(
                    "{}. What is the capital of {}?\n".format(
                        questions + 1, states[questions]))
                for i in range(4):
                    quiz.write(
                        " {}. {}\n".format("ABCD"[i], answerOptions[i]))
                quiz.write("\n")

        # create answer key files.
        with open("quizAnswer{}.txt".format(num + 1), "w") as answers:

            # write the answer key to a file.
            for questions in range(50):
                correctAnswer = capitals[states[questions]]
                wrongAnswers = list(capitals.values())
                del wrongAnswers[wrongAnswers.index(correctAnswer)]
                wrongAnswers = random.sample(wrongAnswers, 3)
                answerOptions = wrongAnswers + [correctAnswer]
                random.shuffle(answerOptions)

                answers.write(
                    "{}. {}\n".format(
                        questions + 1, "ABCD"[answerOptions.index(
                            correctAnswer)]))


quizGenerator()
