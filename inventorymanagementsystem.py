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

