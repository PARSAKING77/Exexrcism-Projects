from collections import Counter

def create_inventory(input_list):
    """
    Creates an inventory from a list of items.

    Args:
        input_list (list): A list of item names.

    Returns:
        dict: A dictionary containing each item name paired with their respective quantity.
    """
    return dict(Counter(input_list))

def add_items(inventory, item_list):
    """
    Adds a list of items to the existing inventory.

    Args:
        inventory (dict): The current inventory dictionary.
        item_list (list): A list of items to add.

    Returns:
        dict: Updated inventory dictionary.
    """
    for item in item_list:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def decrement_items(inventory, item_list):
    """
    Decrements the quantity of items in the inventory.

    Args:
        inventory (dict): The current inventory dictionary.
        item_list (list): A list of items to decrement.

    Returns:
        dict: Updated inventory dictionary.
    """
    for item in item_list:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    """
    Removes an item from the inventory.

    Args:
        inventory (dict): The current inventory dictionary.
        item (str): The item to remove.

    Returns:
        dict: Updated inventory dictionary.
    """
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    """
    Returns the content of the inventory as a list of (item, quantity) tuples.

    Args:
        inventory (dict): The current inventory dictionary.

    Returns:
        list: A list of tuples containing items with quantities greater than zero.
    """
    return [(item, quantity) for item, quantity in inventory.items() if quantity > 0]

# Example usage:
# 1. Create inventory
inv = create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
print(inv)  # Output: {"coal": 1, "wood": 2, "diamond": 3}

# 2. Add items
inv = add_items(inv, ["wood", "iron", "coal", "wood"])
print(inv)  # Output: {"coal": 2, "wood": 4, "diamond": 3, "iron": 1}

# 3. Decrement items
inv = decrement_items(inv, ["diamond", "coal", "iron", "iron"])
print(inv)  # Output: {"coal": 1, "diamond": 2, "iron": 0, "wood": 4}

# 4. Remove an item
inv = remove_item(inv, "coal")
print(inv)  # Output: {"wood": 4, "diamond": 2, "iron": 0}

# 5. List inventory
items = list_inventory(inv)
print(items)  # Output: [('wood', 4), ('diamond', 2)]