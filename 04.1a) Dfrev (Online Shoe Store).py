### Analysing orders for an online shoe store ###
import pandas as pd

#Part 1: reading the csv
orders = pd.read_csv('shoe_store.csv')     # name assigned here to the df is orders

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email
#emails = orders['email']     # Or the other way
print(emails)

#Part 4: the Frances Palmer incident
# Frances Palmer claims that her order was delivered wrong. What did Frances Palmer order?
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
#frances_palmer = orders[(orders.first_name == 'Frances')]
#frances_palmer = orders[orders.first_name == 'Frances']
print(frances_palmer)

#Part 5: Comfy feet means more time on the street
#Select all orders for shoe_type: clogs, boots, and ballet flats
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
print(comfy_shoes)
####################################################################################################






