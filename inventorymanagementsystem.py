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

def 