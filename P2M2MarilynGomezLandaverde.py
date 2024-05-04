def list_o_matic(word, options):
    if word == "":
        return options.pop() + " popped from list"
    elif word in options:
        options.remove(word)
        return "1 instance of " + word + " removed from list"
    else:
        options.append(word)
        return "1 instance of " + word + " appended to list"
animals = ['cat', 'goat', 'cat']
name = input("YOUR NAME GOES HERE: ")
print("Welcome,", name + ". Look at all the animals", animals)
while True:
    answer = input("enter the name of an animal (enter 'quit' to quit): ")
    if answer.lower() == "quit":
        print("Goodbye!")
        break
    print(list_o_matic(answer, animals))
    print("Welcome,", name + ". Look at all the animals", animals)
