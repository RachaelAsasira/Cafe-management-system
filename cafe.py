# Create a menu for a cafe
menu_list = {'coffee', 'pie', 'tea', 'cake'}

# Create a stock dictionary.
stock = {
    'coffee' : 40,
    'pie' : 100,
    'tea' : 50,
    'cake' : 20
}

# Create a price dictionary.
price = {
    'coffee' : 2.0,
    'pie' : 3.5,
    'tea' : 1.5,
    'cake' : 3
}

# Calculate total stock worth in the cafe
total_stock_worth = sum(stock[item] * price[item] for item in menu_list)

# Print the result
print(f'Total Stock Worth: ${total_stock_worth:.2f}')

