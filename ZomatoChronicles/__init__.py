import random
import datetime

class Dish:
    def __init__(self,dish_id,name,price,availability):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"id : {self.dish_id}, Name : {self.name}, Price : {self.price}, Avail : {self.availability}"


class Menu:
    def __init__(self):
        self.dishes = []


class Order:
    def __init__(self,order_id,customer_id,dish_name,order_value,date,status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.dish_name = dish_name
        self.order_value = order_value
        self.date = date
        self.status = status

    def __str__(self):
        return f"id : {self.order_id}, cus_id = {self.customer_id}, dish = {self.dish_name}, price = {self.order_value}, date = {self.date}, status = {self.status}"


class Customer:
    def __init__(self,cus_id,name):
        self.cus_id = cus_id
        self.name = name


class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
        self.customers = []

    def add_customer(self,customer):
        for cus in self.customers:
            if cus.cus_id == customer.cus_id:
                print("customer with this id is already registered")
                return
        self.customers.append(customer)


    def see_menu(self):
        if len(self.menu.dishes) == 0:
            print("menu is empty")
            return
        for dish in self.menu.dishes:
            print(dish)

    def make_order(self,order):
        for ord in self.orders:
            if ord.order_id == order.order_id:
                print("Order with id is already Exist")
                return

        flag = 0
        for cus in self.customers:
            if cus.cus_id == order.customer_id:
                flag =1
                break

        if flag == 0:
            print("first register yourself... then only you can make orders")
        else:
            self.orders.append(order)
            print("Order placed successfully...")

    def cancel_order(self,orderId):
        for order in self.orders:
            if order.order_id == orderId:
                order.status = "Cancelled"
                print("order is cancelled successfully")
                return
        print("order id is not available")

    def order_updates(self,orderId):
        for order in self.orders:
            if order.order_id == orderId:
                order.status = "Delivered"
                print("order is Delivered successfully")
                return
        print("order id is not available")

    def check_order_status(self,orderId):
        for order in self.orders:
            if order.order_id == orderId:
                print(order)
                return
        print("order id is not available")

    def see_orders(self):
        for order in self.orders:
            print(order)


def main():

    restaurant = Restaurant()

    while True:
        print("\n Welcome to Zomato Chronicles")
        print("1. Admin")
        print("2. Customer")
        print("0. exit")

        choice_one = int(input("Input Your Choice : "))
        if choice_one == 1:
            while True:
                print("1. Add Dishes in Menu")
                print("2 update status of Pending order")
                print("3 see all orders")
                print("0. ToExit")
                choice_two = int(input("Input Your Choice : "))
                if choice_two == 1:
                    dish_id = input("Enter dish Id")
                    dish_name = input("Enter dish name")
                    dish_price = float(input("Enter dish price"))
                    restaurant.menu.dishes.append(Dish(dish_id,dish_name,dish_price,"yes"))

                elif choice_two == 2:
                    order_id = input("Enter dish id")
                    restaurant.order_updates(order_id)

                elif choice_two == 3:
                    restaurant.see_orders()

                elif choice_two == 0:
                    print("Exited...")
                    break
                else:
                    print("Please enter valid input")

        elif choice_one == 0:
            print("Exited.....")
            break
        elif choice_one == 2:
            print("Register first....")
            cusid = input("Enter your id")
            name = input("Enter your name")

            restaurant.add_customer(Customer(cusid,name))
            while True:
                print("1. See Menu")
                print("2. Place an Order")
                print("3. Cancel the Order")
                print("4. Check your Order status")
                print("0. exit")

                choice_three = int(input("Please enter your input"))

                if choice_three == 1:
                    restaurant.see_menu()
                elif choice_three == 2:

                    count = 1
                    print("choose your dish")
                    for dish in restaurant.menu.dishes:
                        print(f"{count}. Dish- {dish}")
                        count = count+1
                    order_id = random.randint(1, 10000)
                    cus_id = input("enter your id")
                    dish_number = input("enter dish number from the list")

                    dish_name = restaurant.menu.dishes[int(dish_number)-1].name

                    order_date = datetime.datetime.now()
                    date = f"{order_date.day}-{order_date.month}-{order_date.year}"
                    order_value = restaurant.menu.dishes[int(dish_number)-1].price
                    print(order_id)
                    print(dish_name)
                    print(order_value)
                    print(date)

                    if order_value == -1:
                        print("This dish is not available")
                        return

                    restaurant.make_order(Order(order_id,cus_id,dish_name,order_value,date,"Pending"))
                elif choice_three == 3:
                    order_id = input("INput order id")
                    restaurant.cancel_order(order_id)

                elif choice_three == 4:
                    order_id = input("Enter order id")
                    restaurant.check_order_status(order_id)
                elif choice_three == 0:
                    print("Exited....")
                    break
                else:
                    print("please enter valid input")


if __name__ == '__main__':
    main()
