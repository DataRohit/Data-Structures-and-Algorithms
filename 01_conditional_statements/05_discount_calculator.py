# Function to calculate the discount
def calculate_discount(price, quantity):
    # Calculate the total price
    total_price = price * quantity

    # Total price >= 1000
    if total_price >= 1000 and price > 0 and quantity > 0:
        return int(total_price * 0.1)
    else:
        return -1


# Take user input for price and quantity
price, quantity = map(float, input().split())

# Get and print the discount
print(calculate_discount(price, quantity))
