import random

greetings = ["Good day", "How are you?", "What's up?", "Hail and Well Met!"]
goodbyes = ["Adieu", "See ya!", "Goodbye", "Have a great day", "Bye!"]
keywords = ["Futurism", "Shakespeare", "Variety", "Surrealism", "Avant-garde"]
responses = ["Futurism sees the future as liberation from tradition, but futurism can trend to fascism if we take out the humanity",
             "Shakespeare is a traditionalist, but at least we can remix and remediate how we want - love public domain",
             "Variety is where futurism and burlesque overlap - this is a foundational concept",
             "Surrealism is the way we feel when we look at generated 'art' sometimes",
             "Avant-garde work will help us move into the future thoughtfully"]

print(random.choice(greetings))
user = input("What theatre word do you want to know about? (or type bye to quit): ")
user = user.lower()

# The loop continues until the user types "bye"
while user != "bye":
    keyword_found = False
    # Check if any keyword is found in the user's input
    for index in range(len(keywords)):
        if keywords[index].lower() in user:
            print("Bot: " + responses[index])
            keyword_found = True
            break  # If a keyword is found, stop the loop early

    # If no keyword is found, prompt for new keyword and response
    if not keyword_found:
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to? ").capitalize()
        keywords.append(new_keyword)
        new_response = input(f"How should I respond to {new_keyword}? ")
        responses.append(new_response)


    # Get input again for the next loop iteration
    user = input("Talk to me about theatre (or type bye to quit): ")
    user = user.lower()

# After the user types "bye", say a goodbye message
print(random.choice(goodbyes))
