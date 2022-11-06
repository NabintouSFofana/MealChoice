from tabulate import tabulate

ingredients = ['chicken', 'egg', 'beef', 'fish', 'onion', 'tomato', 'garlic', 'bell_pepper', 'rice', 'pasta', 'bread']
recipes = ['chicken & rice', 'fried beef & rice with vegetables', 'tomato pasta & meat(fish or chicken) ball',
           'fried eggs & bread',
           'fried fish with potatoes']

chicken, beef, any_meat, egg, fish = recipes

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

                        if 'chicken' in all_ingredients:
                            print("\nHere are some meals you can cook:")
                            print(f"\n{chicken}, and {any_meat}")

                            f = open("meal.txt", "w")
                            f = open("meal.txt", "a")

                            mydata = [
                                [f"{all_ingredients}", f"{chicken}, and {any_meat}"]
                            ]
                            head = ["Ingredients", "Meal ideas"]
                            f.write(
                                tabulate(mydata, headers=head, tablefmt="grid"))
                            print("\ncheck the file 'meal' and 'cooking_instructions' and follow the instruction ")
                            break

                        elif 'fish' in all_ingredients:
                            print("\nHere are some meals you can cook:")
                            print(f"\n{fish}, and {any_meat}")

                            f = open("meal.txt", "w")
                            f = open("meal.txt", "a")

                            mydata = [
                                [f"{all_ingredients}", f"{fish}, and {any_meat}"]
                            ]
                            head = ["Ingredients", "Meal ideas"]
                            f.write(
                                tabulate(mydata, headers=head, tablefmt="grid"))
                            print("\ncheck the file 'meal' and 'cooking_instructions' and follow the instruction ")
                            break

                        elif 'beef' in all_ingredients:
                            print("\nHere are some meals you can cook:")
                            print(f"\n{beef}, and {any_meat}")

                            f = open("meal.txt", "w")
                            f = open("meal.txt", "a")

                            mydata = [
                                [f"{all_ingredients}", f"{beef}, and {any_meat}"]
                            ]
                            head = ["Ingredients", "Meal ideas"]
                            f.write(
                                tabulate(mydata, headers=head, tablefmt="grid"))
                            print("\ncheck the file 'meal' and 'cooking_instructions' and follow the instruction ")
                            break

                        elif 'egg' in all_ingredients:
                            print("\nHere are some meals you can cook:")
                            print(egg)

                            f = open("meal.txt", "w")
                            f = open("meal.txt", "a")

                            mydata = [
                                [f"{all_ingredients}", f"{egg}"]
                            ]
                            head = ["Ingredients", "Meal ideas"]
                            f.write(
                                tabulate(mydata, headers=head, tablefmt="grid"))
                            print("\ncheck the file 'meal' and 'cooking_instructions' and follow the instruction ")
                            break

                        else:
                            print('try again please')

                    else:
                        print("Try again please")
                        return meal.ingredient()
                break

        return 'ENJOY YOUR MEAL'

    def fish_meal(self):
        for x in range(4):
            print("enter a protein")
            console = input('>')
            for item in recipes:
                if console == 'fish':
                    return fish, any_meat
                break
            print('try again please')

    def beef_meal(self):
        for x in range(4):
            print("enter a protein")
            console = input('>')
            for item in recipes:
                if console == 'beef':
                    return beef, any_meat
                break
            print('try again please')

    def chicken_meal(self):
        for x in range(4):
            print("enter a protein")
            console = input('>')
            for item in recipes:
                if console == 'chicken':
                    return chicken, any_meat
                break
            print('try again please')

    '''

    def chicken2(self):
        print("\nHere are some meals you can cook")
        print(f"{chicken}, and {any_meat}")

        f = open("meal.txt", "w")
        f = open("meal.txt", "a")

        mydata = [
            [f"{ingredients}", f"{chicken}, and {any_meat}"]
        ]
        head = ["Ingredients", "Meal ideas"]
        f.write(
            tabulate(mydata, headers=head, tablefmt="grid"))
        print("check the file 'meal' and 'cooking_instructions' and follow the instruction ")
   '''


'''
 with open('cooking_instructions.txt') as f:
                contents = f.read()
                print(contents)
                return 'Good! See you soon'
'''


def egg_meal(self):
    for x in range(4):
        print("enter a protein")
        console = input('>')
        for item in recipes:
            if console == 'egg':
                return egg
            break
        print('try again please')


'''
    def recipes(self):

        for item in recipes:
            i = 0
            for i in range(1):
                print(item)
                i += 1
                break
'''


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

# print(meal.fish_meal())

'''
for item in recipes:
    print("enter a protein")
    console = input('>')
    if console == 'chicken':
        print(f"{chicken}, and {any_meat}")
        break
    elif console == 'fish':
        print(f"{fish}, and {any_meat}")
        break
    elif console == 'beef':
        print(f"{beef}, and {any_meat}")
        break
    elif console == 'egg':
        print(egg)
        break
    else:
        print('try again please')
'''
