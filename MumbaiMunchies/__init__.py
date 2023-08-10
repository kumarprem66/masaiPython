class Snack:
    def __init__(self, snack_id, name, price, available):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"Id : {self.snack_id}, Name : {self.name}, Price : {self.price}, Available : {self.available}"


def load_inventory(filename):
    inventory = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                snack_data = line.strip().split(",")
                if len(snack_data) == 4:
                    snack_id, name, price, available = snack_data
                    inventory.append(Snack(snack_id, name, float(price), available))
    except FileNotFoundError:
        pass
    return inventory


def load_sales_record(filename):
    sales_record = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                sold_data = line.strip().split(",")
                if len(sold_data) == 4:
                    snack_id, name, price, available = sold_data
                    sales_record.append(Snack(snack_id, name, float(price), available))
    except FileNotFoundError:
        pass
    return sales_record


class Canteen:
    def __init__(self):
        self.inventory = load_inventory("inventory.csv")
        self.sales_record = load_sales_record("sales_record.csv")

    def add_snack(self, snack ):
        for sna in self.inventory:
            if sna.snack_id == snack.snack_id:
                print("Snack with this id already exist..")
                return
            
        self.inventory.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id and snack.available == True:
                snack.available = False

                print(f"Snack '{snack.name}' removed from inventory")
                return

        print("Snack not found in inventory.")

    def update_availability(self, snack_id, available):
        for snack in self.inventory:
            if snack.snack_id == snack_id and snack.available == True:
                snack.available = available
                print(f"Availability of snack '{snack.name}' updated to {available}")
                return
        print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.available:
                    snack.available = False
                    self.sales_record.append(snack)
                    print(f"Snack '{snack.name}' sold")
                    return
                else:
                    print("Snack is not available for sale.")

        print("Snack not found in inventory.")

    def show_snack(self):
        if len(self.inventory) == 0:
            print("Empty Inventory..")
            return

        for snack in self.inventory:
            print(snack.__str__())


def main():
    canteen = Canteen()

    while True:
        print("\nCanteen Management System")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. Show all Snack")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                snack_id = input("Enter snack ID")
                name = input("Enter snack name: ")
                price = float(input("Enter snack price: "))
                avail = input("Is the snack available? (yes/no): ").lower() == "yes"
            except ValueError:
                print("Invalid input for price. Please enter a valid numeric value.")
                continue
            else:
                snack = Snack(snack_id, name, price, avail)
                canteen.add_snack(snack)
                print("snack added successfully..")

        elif choice == "2":
            try:
                snack_id = input("Enter snack ID to remove: ")
            except TypeError:
                print("Invalid input...")
                continue
            canteen.remove_snack(snack_id)

        elif choice == "3":
            snack_id = input("Enter snack ID to update availability: ")
            available = input("Is the snack available? (yes/no): ").lower() == "yes"
            canteen.update_availability(snack_id, available)

        elif choice == "4":
            snack_id = input("Enter snack ID to sell: ")
            canteen.sell_snack(snack_id)

        elif choice == "5":
            print("================  All snacks  ==================")
            canteen.show_snack()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    with open("inventory.csv", "w") as file:
        for snack in canteen.inventory:
            # print(snack)
            file.write(f"{snack.snack_id},{snack.name},{snack.price},{snack.available}\n")

    with open("sales_record.csv", "w") as file:
        for snack in canteen.sales_record:
            # print(snack)
            file.write(f"{snack.snack_id},{snack.name},{snack.price},{snack.available}\n")


if __name__ == '__main__':
    main()
