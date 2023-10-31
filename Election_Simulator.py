#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Initialize empty lists to store city names and their corresponding party names
cities = []
loc_city = []

def getPartyName(promptData, partyNames):
    while True:
        # Get the name of the party from the user
        party_name = input(f"Please enter the name of the {promptData} party: ").capitalize()
        
        # Check if the party name is valid
        if not party_name[0].isalpha() or ' ' in party_name:
            print("Invalid party name. Please enter again.")
            continue

        if party_name in partyNames:
            print(f"{party_name} already exists. Please enter again.")
        else:
            partyNames.append(party_name)
            break

def getMenuOption():
    print("\nMenu:")
    print("1. Enter results for a new city.")
    print("2. Change results of a specific city.")
    print("3. Show current results.")
    print("4. Exit\n")

    while True:
        option = input("Select one of the options (1-4): ")
        if option in ["1", "2", "3", "4"]:
            return option
        else:
            print("You have entered an invalid input for menu selection. Please enter again.")

def getNewResults(citiesAndResults):
    while True:
        city = input("Please enter the name of the city: ").capitalize()

        while True:
            if not city.isalpha():
                city = input("Invalid city name. Please enter again: ").capitalize()
                continue

            if city in citiesAndResults:
                print(f"You cannot enter {city} since this city has already been entered. If you want, you can update the results of this city by using the 2nd menu option.")
                break
            else:
                global cities
                cities.append(city)
                citiesAndResults.append(city)
                results = input(f"Please enter results for {city}: ").split("-")
                for result in results:
                    citiesAndResults.append(result)
        break

def changeResults(citiesAndResults):
    city = input("Please enter the name of the city: ").capitalize()

    while True:
        if not city.isalpha():
            city = input("Invalid city name. Please enter again: ").capitalize()
            continue

        if city not in citiesAndResults:
            print(f"You cannot change the result of {city} since no result has been entered for this city yet.")
            break
        else:
            new_results = input(f"Please enter results for {city}: ").split("-")
            loc = citiesAndResults.index(city)
            for k in range(0, 3):
                citiesAndResults[loc + k + 1] = new_results[k]
            break

def showResults(citiesAndResults, partyNames):
    if len(citiesAndResults) == 0:
        print("No information available yet...")
    else:
        for city in cities:
            loc_city = citiesAndResults.index(city)
            scores = [float(score) for score in citiesAndResults[loc_city + 1 : loc_city + 4]]
            leading_parties = [partyNames[i - 1] for i, score in enumerate(scores, start=1) if score == max(scores)]

            if len(leading_parties) == 1:
                print(f"{city} {' '.join(map(str, scores))} --> {' '.join(leading_parties)} is leading")
            else:
                print(f"{city} {' '.join(map(str, scores))} --> {' '.join(leading_parties)} are leading")

# Main program
print("Welcome to this virtual local elections Python program.\n")

# Get the names of the parties
partyNames = []  # stores the valid party names
promptData = ["first", "second", "third"]
for i in range(3):
    getPartyName(promptData[i], partyNames)

# Initialize dataset
citiesAndResults = []  # stores the city-results information

# Display the menu, get user's option, and process accordingly
option = getMenuOption()
while option != "4":
    if option == "1":
        getNewResults(citiesAndResults)  # function call to update citiesAndResults with a new city
    elif option == "2":
        changeResults(citiesAndResults)  # function call to update citiesAndResults for an existing city
    elif option == "3":
        showResults(citiesAndResults, partyNames)  # function call to display current election results
    option = getMenuOption()

print("**********\nTerminating, goodbye dear citizen!!! Do not forget to vote in elections :)")

