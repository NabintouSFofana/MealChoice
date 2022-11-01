from tabulate import tabulate

ingredients = ['chicken', 'egg', 'beef', 'fish', 'onion', 'tomato', 'garlic', 'bell_pepper', 'rice', 'pasta', 'bread']
recipes = ['chicken & rice', 'fried beef & rice with vegetables', 'tomato pasta & meat ball', 'fried eggs & bread',
           'fried fish with potatoes']
chicken = rice = [recipes[0]]
beef = rice = garlic = [recipes[1]]
tomato = onion = pasta = bread = garlic = [recipes[2]]
egg = bread = [recipes[3]]
fish = [recipes[4]]
selected_ingredient = []
selected_meal = []


class Meals:
    # initialize construct an object
    def __init__(self):
        pass

    def user_register(self):
        print("Welcome! \nHere a some choices. Tell me what you have in your fridge/pantry and I will tell you what "
              "to cook.")
        print('can I have your name please')
        name = input('>')
        print(f"Hello {name}, hope you are doing well. Enter your email here")
        email = input('>')
        file_register = open("User.txt", "w")
        file_register = open("User.txt", "a")
        mydata = [
            [f"{name}", f"{email}"]
        ]
        head = ["User Name", "User Email"]
        file_register.write(tabulate(mydata, headers=head, tablefmt="grid"))
        file_register.close()
        print("Enter 'S' to start choosing and 'Q' to leave")
        console2 = input('>')
        if console2.upper() == 'Q':
            meal.stop()
        elif console2.upper() == 'S':
            meal.groceries()
        else:
            meal.error()

    def groceries(self):
        print("Do you have some groceries? Enter 'Y' for yes and 'N' for no")
        console2 = input('>')
        if console2.upper() == 'Y':
            print(meal.ingredient())
        elif console2.upper() == 'N':
            meal.shop()
        else:
            meal.error()
            # print('Bye, see you soon!')

    def ingredient(self):
        i = 0

        for i in range(5):
            print(f"\nChoose at least '1' ingredient from the first row, "
                  f"\n'2' ingredients from the second row, and "
                  f"\n'1' ingredient from the third row."
                  f"\nto start. Add coma between them. Enter:")
            with open('ingredient.txt') as f:
                contents = f.read()
                print(contents)
                print("")
                ingredient1 = input('>')
                ingredient2 = input('>')
                ingredient3 = input('>')
                ingredient4 = input('>')

                for items in ingredients:
                    if ingredient1 in ingredients:
                        selected_ingredient.append(ingredient1)
                        selected_ingredient.append(ingredient2)
                        selected_ingredient.append(ingredient3)
                        selected_ingredient.append(ingredient4)

                        all_ingredients = ingredient1 + ", " + ingredient2 + ", " + ingredient3 + " and " + ingredient4

                        print(f"\nOk,you have {all_ingredients}.")
                        print("\nHere are some meals you can cook")
                        f = open("meal.txt", "w")
                        f = open("meal.txt", "a")
                        mydata = [
                            [f"{ingredient1}", f"{recipes}"]
                        ]
                        head = ["Ingredients", "Meal ideas"]
                        f.write(
                            tabulate(mydata, headers=head, tablefmt="grid"))
                        f = open("meal.txt", "r")
                        print(f.read())
                        f.close()
                        with open('cooking_instructions.txt') as f:
                            contents = f.read()
                            print(contents)
                            return 'Good! See you soon'
                    else:
                        print("Try again please")
                        return meal.ingredient()
                break

    def recipes(self):

        for item in recipes:
            i = 0
            for i in range(5):
                print(item)
                i += 1
                break


def shop(self):
    print('Go do some shopping on INSTACART, you will enjoy fast delivery')
    exit(0)


def stop(self):
    print('Bye, see you soon')
    exit(0)


def error(self):
    print('Wrong choice, try again please!')


meal = Meals()
# print(meal.i)
print(meal.ingredient())

# print(meal.recipe())
