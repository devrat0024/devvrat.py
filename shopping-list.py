# Create an empty list to store the shopping items
shopping_list = []

def add_item():
    """
    Function to add an item to the shopping list
    """
    item = input("Enter the item you want to add to the shopping list: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def view_list():
    """
    Function to view the current shopping list
    """
    if not shopping_list:
        print("The shopping list is currently empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

# Main program loop
while True:
    choice = input("Enter 'add' to add an item, 'view' to view the list, or 'quit' to exit: ")
    
    if choice.lower() == 'add':
        add_item()
    elif choice.lower() == 'view':
        view_list()
    elif choice.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")# Create an empty list to store the shopping items
shopping_list = []

def add_item():
    """
    Function to add an item to the shopping list
    """
    item = input("Enter the item you want to add to the shopping list: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def view_list():
    """
    Function to view the current shopping list
    """
    if not shopping_list:
        print("The shopping list is currently empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

# Main program loop
while True:
    choice = input("Enter 'add' to add an item, 'view' to view the list, or 'quit' to exit: ")
    
    if choice.lower() == 'add':
        add_item()
    elif choice.lower() == 'view':
        view_list()
    elif choice.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")