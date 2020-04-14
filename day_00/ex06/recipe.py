import sys

cook_book = {}
sandwich = {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time':'10'}
cake = {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time':'60'}
salad = {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time':'15'}

cook_book["sandwich"] = sandwich
cook_book["cake"] = cake
cook_book["salad"] = salad

def print_dico(dico, option):
    for key in dico:
        if option == 1 or option == 3:
            print(key)
        elif option == 2 or option == 3:
            print(dico[key])

def print_recipe(name):
    if name in cook_book:
        print(f"Recipe for {name}:\nIngredients list: {cook_book[name]['ingredients']}")
        print(f"To be eaten for {cook_book[name]['meal']}\
        \nTakes {cook_book[name]['prep_time']} minutes of cooking\n")
    else: print("no recipies for this name !\n")

def del_recipe(name):
    if name in cook_book:
        del cook_book[name]
        print(f"recipe for {name} deleted\n")
    else: print("no recipies for this name !\n")

def new_recipe(name, ingredients, meal, time):
    if name in cook_book:
        print("recipe already in cook_book")
        sys.exit(0)
    new = {'ingredients': ingredients, 'meal': meal, 'prep_time': time}
    cook_book[name] = new

def cookbook_loop():
    end = 0
    while end != 1:
        choice = input("Select an option with the corresponding number:\n" 
        "1:Add recipe\n2:Delete a recipe\n3:Print a recipe\n"
        "4:Print the cook_book\n5:Quit\n>>")
        if choice == '5':
            print("\nCook_book closed!") 
            end = 1
        elif choice == '4':
            for name in cook_book: 
                print('\n')
                print_recipe(name)
        elif choice == '3': print_recipe(input("\nEnter recipe name:\n>>"))
        elif choice == '2': del_recipe(input("\nEnter recipe name:\n>>"))
        elif choice == '1':
            new_name = input("\nplease write a name for the new recipe!\n>>")
            new_ingr = input("\nplease write the ingredients separated by spaces\n>>")
            new_meal = input("\nplease write the type of meal\n>>")
            new_time = input("\nplease write the preparation time in minutes (ex: 120)\n>>")
            new_ingr = new_ingr.split(' ')
            new_recipe(new_name, new_ingr, new_meal, new_time)
            print(f"\nnew recipe for {new_name} added!\n")
        else:
            print("wrong options please choose from the menu below\n")
cookbook_loop()

