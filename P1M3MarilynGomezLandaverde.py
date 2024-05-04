minweight = 1
maxweight = 100
price = 7.99

name = input("Enter your full name: ")

def cheese_order():
    order_amount = float(input(name + ", enter cheese order weight (numeric value): " ))

    if order_amount < minweight:
        return(order_amount, "is below the minimum order amount")
    elif order_amount > maxweight:
        return(order_amount, "is more than currently available stock")
    else:
        total = order_amount * price
        cost = str(order_amount)+" costs $"+ str(total) 
        return cost

print(cheese_order())