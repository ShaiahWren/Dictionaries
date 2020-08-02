meal = {
    "drink" : "orange juice",
    "appetizer" : "crab stuffed mushrooms",
    "entree" : "lobster roll",
    "dessert" : "churros"
   
}

# print("This Thursday I will have a %s and a %s for dinner!" % (meal["drink"], meal["entree"]))

if "dessert" in meal:
    meal["dessert"] = "ice cream"
    del meal["dessert"]
    print(meal)
    # print("Of course, Shaiah had dessert! They ate %" % (meal["dessert"]))
else:
    meal["dessert"] = "churros"
    print(meal)