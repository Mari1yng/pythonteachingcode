# [ ] create, call and test fishstore() function 
def fishstore(name, fish, price):
    return("Report for " + name + ". Fish Type: " + fish.capitalize() + " costs $" + price)
name_entry = input("Enter your full name: ")
fish_entry = input("Enter fish type: ")
price_entry = input("Enter fish type price: ")
print(fishstore(name_entry, fish_entry, price_entry))
