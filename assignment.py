drink = "tea"
sales = {"tea": 3, "coffee": 5}
sold = sales[drink]
sold = sold + 1
print(drink) # tea will be printed
print(sold) # 4 will be printed because sold refers to the sales of the drink and the drink is tea and tea is 3.
