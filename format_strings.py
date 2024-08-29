# using f-strings
price = 23490877.769
quantity = 12
fruit = "pomogranates"
def cost_of_items(a = 1):
    return (price * quantity * 1)
txt = f'The price is {price:,} dollars and quantity is {quantity} thus the cost is {(price * quantity):.2f}'
print(txt)
# using if ... else statements inside the placeholders
conclusion = f'It is very {'Expensive' if price > 235 else 'Cheap'}'
print(conclusion)
# Using functions in f-strings
my_deal = f"I bought {fruit.upper()} at $ {round(cost_of_items())}"
print(my_deal)
