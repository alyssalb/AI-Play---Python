I'm here to play with AI. :) 

import random
greetings = ["Good day", "How are you?", "What's up?", "Hail and Well Met!"]
goodbyes = ["Adieu", "See ya!", "Goodbye", "Have a great day", "Bye!"]
keywords = ["Futurism", "Shakespeare", "Burlesque", "Surrealism", "Avant-garde"]
responses = ["Futurism sees the future as liberation from tradition, but futurism can trend to fascism if we take out the humanity", "Shakespeare is a traditionalist, but at least we can remix and remediate how we want - love public domain", "Variety is where futurism and burlesque overlap - this is a foundational concept - how is variety available in both fascist leaning and liberatory queerness", "Surrealism is the way we feel when we look at generated 'art' sometimes", "Avant-garde work will help us move into the future thoughtfully"]
print(random.choice(greetings))
user = input("Talk to me about theatre (or type bye to quit): ")
user = user.lower()
while (user != "bye"):
  keyword_found = False
  for index in range(len(keywords)):
    if (keywords[index] in user):
      print("Bot: " + responses[index])
      keyword_found = True

if (keyword_found == False):
  new_keyword = input("I'm not sure how to respond. What keyword should I respond to?")
  keywords.append(new_keyword)
  new_response = input("How should I respond to " + new_keyword + "? ")
  responses.append(new_response)

user = input("Talk to me about theatre (or type bye to quit): ")
user = user.lower()
print(random.choice(goodbyes))
