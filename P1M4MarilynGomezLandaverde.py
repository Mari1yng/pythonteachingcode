name = input("enter your full name:")

def str_analysis (response):
    if response.isalpha():
        return '"' + response + '"' + " is all alphabetical characters"
    elif response.isdigit():
        if int(response) > 99:
            return response + " is a pretty big number"
        elif int(response) < 99:
            return response + " is a smaller number than expected"

response = ''

while response == '':
    response = input(name + ", enter word or integer: ")
    
print(str_analysis(response))
