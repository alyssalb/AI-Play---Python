import random
import json
import os

# Lists of greetings and goodbyes
greetings = ["Good day", "How are you?", "What's up?", "Hail and Well Met!"]
goodbyes = ["Adieu", "See ya!", "Goodbye", "Have a great day", "Bye!"]

# File to store definitions and synonyms
definitions_file = 'definitions.json'

# Load definitions from a JSON file if it exists
if os.path.exists(definitions_file):
    with open(definitions_file, 'r') as file:
        definitions = json.load(file)
else:
    # Initialize the definitions dictionary
    definitions = {
        "Futurism": {
            "definitions": [
                "Futurism sees the future as liberation from tradition, but futurism can trend to fascism if we take out the humanity"
            ],
            "synonyms": ["Future Movement"]
        },
        "Shakespeare": {
            "definitions": [
                "Shakespeare is a traditionalist, but at least we can remix and remediate how we want - love public domain"
            ],
            "synonyms": ["Bard", "William Shakespeare"]
        },
        "Variety": {
            "definitions": [
                "Variety is where futurism and burlesque overlap - this is a foundational concept"
            ],
            "synonyms": ["Diversity"]
        },
        "Surrealism": {
            "definitions": [
                "Surrealism is the way we feel when we look at generated 'art' sometimes"
            ],
            "synonyms": []
        },
        "Avant-garde": {
            "definitions": [
                "Avant-garde work will help us move into the future thoughtfully"
            ],
            "synonyms": ["Cutting Edge", "Vanguard"]
        }
    }

# Start the conversation with a random greeting
print(random.choice(greetings))

# Function to find a word by name or synonym
def find_word(input_word):
    for word, data in definitions.items():
        if word.lower() == input_word.lower() or input_word.lower() in [syn.lower() for syn in data.get('synonyms', [])]:
            return word
    return None

# Main interaction loop
while True:
    print("\nWhat would you like to do?")
    print("1. Get definitions of a word")
    print("2. Add a definition to a word")
    print("3. Add a new word")
    print("4. Add synonyms to a word")
    print("5. Search for words")
    print("6. Quit")
    choice = input("Please enter the number of your choice: ").strip()

    if choice == "6":
        print(random.choice(goodbyes))
        break

    elif choice == "1":
        user_input = input("Enter the word you want definitions for: ").strip()
        word = find_word(user_input)
        if word:
            # Display existing definitions
            print(f"\nDefinitions of {word}:")
            for idx, definition in enumerate(definitions[word]['definitions'], start=1):
                print(f"{idx}. {definition}")
            # Display synonyms
            if definitions[word].get('synonyms'):
                print(f"Synonyms: {', '.join(definitions[word]['synonyms'])}")
        else:
            print(f"'{user_input}' is not in the dictionary.")

    elif choice == "2":
        user_input = input("Enter the word you want to add a definition to: ").strip()
        word = find_word(user_input)
        if word:
            new_definition = input(f"Please provide a new definition for '{word}': ").strip()
            definitions[word]['definitions'].append(new_definition)
            print(f"New definition added for '{word}'.")
        else:
            print(f"'{user_input}' is not in the dictionary.")

    elif choice == "3":
        new_word = input("Enter the new word you want to add: ").strip().title()
        if new_word in definitions:
            print(f"'{new_word}' already exists in the dictionary.")
        else:
            new_definition = input(f"Please provide a definition for '{new_word}': ").strip()
            definitions[new_word] = {
                "definitions": [new_definition],
                "synonyms": []
            }
            print(f"Word '{new_word}' added to the dictionary with its definition.")

    elif choice == "4":
        user_input = input("Enter the word you want to add synonyms to: ").strip()
        word = find_word(user_input)
        if word:
            new_synonyms = input(f"Enter synonyms for '{word}' separated by commas: ").strip()
            synonyms_list = [syn.strip().title() for syn in new_synonyms.split(',')]
            definitions[word]['synonyms'].extend(synonyms_list)
            # Remove duplicates
            definitions[word]['synonyms'] = list(set(definitions[word]['synonyms']))
            print(f"Synonyms added for '{word}'.")
        else:
            print(f"'{user_input}' is not in the dictionary.")

    elif choice == "5":
        search_term = input("Enter the term to search for: ").strip().lower()
        results = []
        for word in definitions.keys():
            if search_term in word.lower():
                results.append(word)
            else:
                # Search in synonyms
                synonyms = definitions[word].get('synonyms', [])
                if any(search_term in syn.lower() for syn in synonyms):
                    results.append(word)
        if results:
            print("Words found:")
            for word in results:
                print(f"- {word}")
        else:
            print("No words found matching your search.")

    else:
        print("Invalid choice. Please select a number from 1 to 6.")

# After the loop ends, save the definitions back to the JSON file
with open(definitions_file, 'w') as file:
    json.dump(definitions, file, indent=4)
