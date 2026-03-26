def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

def display_inventory(inventory):
    print("Inventory:")
    for item, count in inventory.items():
        print(f"{count} {item}")
    print(f"Total number of items: {sum(inventory.values())}")

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)