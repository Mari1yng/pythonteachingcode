name = input("ENTER YOUR NAME: ")
print("Welcome " + name + " list any 5 of the first 20 elements in the Period table ")
def get_names():
    answer = []
    cnt = 1
    while True:
        if cnt <= 5:
            element = input("Enter the name of an element: ").strip().lower()
        else:
            break

        if element == '':
            print("Empty enter is not allowed ")
        elif element not in answer:
            answer.append(element)
            cnt += 1
        else:
            print(element, "was already entered ")    
    return answer

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
file = open('elements1_20.txt', 'r')
elements = []
while file:
    line = file.readline()
    if line == '':
        break
    else:
        elements.append(line.strip().lower())
        

answer = get_names()
correct = []
incorrect = []
for response in answer:
    if response in elements:
        correct.append(response)
    else:
        incorrect.append(response)

print()
print(str(len(correct)*20), "% correct")
print("Found: ", end='')
for element_id in range(len(correct)):
    print(correct[element_id].title(), end=' ')
print("\nNot Found: ", end='')
for element_id in range(len(incorrect)):
    print(incorrect[element_id].title(), end=' ')
print()

file.close()