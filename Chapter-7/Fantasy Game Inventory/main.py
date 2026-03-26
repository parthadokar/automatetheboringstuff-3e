def display_inventory(inventory):
    print('Inventory:')
    for item, count in inventory.items():
        print(f"{count} {item}")
    print(f"Total number of items: {sum(inventory.values())}")

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)