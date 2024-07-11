def display_menu():
    print("Inventory Management System")
    print("1. Add New Item")
    print("2. View Inventory")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Exit")

def add_item(inventory):
    item_name = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity: "))
    if item_name in inventory:
        print("Item already exists. Use the update option to change the quantity.")
    else:
        inventory[item_name] = item_quantity
        print(f"{item_name} added to inventory.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        for item_name, item_quantity in inventory.items():
            print(f"Item: {item_name}, Quantity: {item_quantity}")

def update_item_quantity(inventory):
    item_name = input("Enter the name of the item to update: ")
    if item_name in inventory:
        item_quantity = int(input("Enter the new quantity: "))
        inventory[item_name] = item_quantity
        print(f"Quantity of {item_name} updated to {item_quantity}.")
    else:
        print(f"{item_name} does not exist in inventory.")

def remove_item(inventory):
    item_name = input("Enter the name of the item to remove: ")
    if item_name in  inventory:
        del inventory[item_name]
        print(f"{item_name} remove from the inventory.")
    else:
        print(f"{item_name} does not exist in inventory.")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Choose an Option: ")
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            update_item_quantity(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()