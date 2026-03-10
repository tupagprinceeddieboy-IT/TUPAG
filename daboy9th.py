class ShoppingCart:
    def __init__(self):
        self.items = {}

    def AddItem(self, name, price):
        self.items[name] = price

    def RemoveItem(self, name):
        if name in self.items:
            self.items.pop(name)
            print("Item removed...")
        else:
            print("Item not found...")

    def ViewCart(self):
        if len(self.items) == 0:
            print("\nCart is empty.")
        else:
            print("\nItems in cart:")
            for name in self.items:
                print(f"{name} - ₱ {self.items[name]}")

    def Checkout(self):
        if len(self.items) == 0:
            print("\nNo items to checkout.")
        else:
            total = 0
            print("\nYour items:")
            for name in self.items:
                price = self.items[name]
                print(f"{name} - ₱ {price}")
                total += price  
            print(f"Total: ₱ {total}")


cart = ShoppingCart()

while True:
    print("\n=== Shopping Cart ===")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Checkout/Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cart.ViewCart()

    elif choice == "2":
        MaxItems = int(input("\nHow many items to add in the cart: "))
        for i in range(MaxItems):
            name = input(f"Add Item No.{i + 1}: ")
            price = float(input("Add Price: "))
            cart.AddItem(name, price)
        print("Item added to cart.")

    elif choice == "3":
        name = input("\nEnter item to remove: ")
        cart.RemoveItem(name)

    elif choice == "4":
        cart.Checkout()
        print("\nThank you for Shopping!!")
        break

    else:
        print("\nInvalid choice. Choose only (1-4).")