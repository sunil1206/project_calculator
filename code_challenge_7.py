# Assume you want to build two functions for discounting products on a
# website.
# Function number 1 is for student discount which discounts the current price
# to 10%.
# Function number 2 is for additional discount for regular buyers which
# discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts
# on the products.
# Design the above two mentioned functions and apply them both
# simultaneously on the price.

def std_dis(x):
    return lambda x:x*(0.90)*0.95

print(std_dis(100))