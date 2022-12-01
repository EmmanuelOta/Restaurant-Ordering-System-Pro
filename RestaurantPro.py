import re
import json
global count 
count = 0
global user_data
user_data = {}
dine_in ={}
pickup = {}
deliveries = {}


class MainApp():
    def __init__(self):
        print("Please Enter 1 for Sign Up")
        print("Please Enter 2 for Sign In")
        print("Please enter 3 for Quit")
        self.input = input(":")


class SignUP():
    def __init__(self):
        self.user_data = {}
        self.name = input("Please enter your full name:")
        self.user_data["name"] = self.name
        self.number = input("Please enter your contact number:")
        self.user_data["number"] = self.number
        while True:
            if len(self.number) == 10 and self.number.startswith("0"):
                break
            else:
                print("You have entered an incorrect number!!\n")
                self.number = input("Please enter your contact number:")
                self.user_data["number"] = self.number

        self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
        self.confirm_pass = input("Password confirmation:")
        self.patterns = "[A-Z][a-z][a-z][@|&][0-9]*$"
        while True:
            if  self.password == self.confirm_pass and re.match(self.patterns, self.password):
                self.user_data["password"] = self.confirm_pass
                break
            else:
                print("Your password doesn't follow the required pattern please enter a valid password!!")
                self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                self.confirm_pass = input("Password confirmation:")
                self.user_data["password"] = self.password  


        self.address = input("Please enter your address or press enter to Skip:")  
        self.user_data["address"] = self.address


        self.date_of_birth = input("Please enter your date of birth in the format DD/MM/YYYY (NO SPACE):")
        match = "(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/]\d{4}"
        while True:
            if re.match(match, self.date_of_birth):
                self.split_D0B = self.date_of_birth.split("/")
                self.birth_year = self.split_D0B[2]
                age = 2021 - int(self.birth_year)
                if age >= 21:
                    print("You have successfully Signed up!!")
                    break
                else:
                    print("You are too young to Sign up!")
                    break

            else:
                print("You have the entered the Date of Birth in invalid format.\nPlease start again\n:")
                self.date_of_birth = input("Please enter your date of birth in the format DD/MM/YYYY (No Space):")

        with open(f"{self.number}.json", "w") as file:
                    json.dump(self.user_data, file)


class SignIn():
    def __init__(self):
        global user_data
        global pickup
        global deliveries
        self.username = input("Please enter your username (Mobile Number):")
        try:
            with open(f"{self.username}.json", "r") as file:
                self.loaded_data = json.load(file)
                user_data = self.loaded_data
                self.password = input("Please enter your password:")
                self.count = 0
                while self.count < 3:
                    if self.loaded_data["password"] != self.password:
                        print(f"You have entered the wrong Password\nPlease try again!")
                        self.password = input("Please enter your password:")
                        self.count += 1
                        if self.count == 3:
                            print("You have used the maximum attempts of login:")
                            print("Please reset the password by entering the below details:")
                            try:
                                self.username_confirmation = input("Please enter your Username (Mobile Number) to confirm:")
                                with open(f"{self.username_confirmation}.json", "r") as file:
                                    self.userConfirmData = json.load(file)
                            except:
                                print("You have not signed in with this username!!\n")
                                app = MainApp()
                            self.dob_confirmation = input("Please enter your Date of Birth in DD/MM/YYYY format, to confirm:")
                            self.match = "[A-Z][a-z][a-z][@|&][0-9]*$"
                            self.new_password = input("Please enter your new password in format Sam@20 or Sam&20:")
                            self.new_password_confirm = input("Please re-enter your new password:")
                            while True:
                                if re.match(self.match, self.password) and self.password == self.new_password_confirm:
                                    self.userConfirmData["password"] = self.new_password_confirm
                                    with open(f"{self.username_confirmation}.json", "w") as file:
                                        json.dump(self.userConfirmData, file)
                                    print("Your password has been reset successfully!!")
                                    break

                                if self.userConfirmData["password"] == self.new_password_confirm:
                                    print("You cannot use the password used earlier.")
                                    self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                                    self.new_password_confirm = input("Please re-enter your new password:")

                                else:
                                    print("Your password doesn't follow the required pattern or they don't match, Please enter a valid password!!")
                                    self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                                    self.new_password_confirm = input("Please re-enter your new password:")

                    else:
                        print(f"You have successfully Signed in {self.loaded_data['name']}")
                        self.menu()
                        break   
            
        except:
            print("You have not Signed up with this Contact Number, Please Sign up first.")   

    def menu(self):
        while True:
                print("Please enter 2.1 to start ordering.")
                print("Please enter 2.2 to Print Statistics.")
                print("Please enter 2.3 for Logout.")
                self.input = input(":")
                if self.input == "2.1":
                    order = StartOrdering()
                    break
                elif self.input == "2.2":
                    stats = PrintStats()
                elif self.input == "2.3":
                    app = MainApp()
                    break
                else:
                    print("Please enter a valid input.")
                    self.input = input(":")


class StartOrdering():
    def __init__(self) :
        super(StartOrdering, self).__init__()
        while True:
            print("2.1")
            print("Please Enter 1 for Dine in.")
            print("Please Enter 2 for Order Online.")
            print("Please Enter 3 to go to Login Page.")
            self.input = input(":")
            if self.input == "1":
                dine_in = DineIn()
                break
            elif self.input == "2":
                order_online = OrderOnline()
                break
            elif self.input == "3":
                sign_up = SignUP()
                break
            else:
                print("Please enter a valid input.")
                self.input = input(":")


class OrderOnline():
    def __init__(self):
        super(OrderOnline, self).__init__()
        global user_data
        global count
        self.pickUp = {}                
        self.deliveries = {}

        self.food_orders = {"1": "2",
                            "2": "4",
                            "3": "6",
                            "4": "8",
                            "5": "10",
                            "6": "20"}

        self.drink_orders = {"1": "2",
                             "2": "2",
                             "3": "6"}

        self.restaurant_radius = {"0": "5",
                                  "1": "5",
                                  "2": "5",
                                  "3": "5",
                                  "4": "5",
                                  "5": "5",
                                  "6": "10",
                                  "7": "10",
                                  "8": "10",
                                  "9": "10",
                                  "10": "10",
                                  "11": "18",
                                  "12": "18",
                                  "13": "18",
                                  "14": "18",
                                  "15": "18",}

        while True:
            print("Enter 1 for Self Pickup.")
            print("Enter 2 for Home Delivery.")
            print("Enter 3 to go to Previous Menu.")
            self.input = input(":")
            if self.input == "3":
                start_order = StartOrdering()
                break

            # DELIVERY MODE
            if self.input == "1" or self.input == "2":
                print("Enter 1 for Noodles \tPrice AUD 2.")
                print("Enter 2 for Sandwich \tPrice AUD 4.")
                print("Enter 3 for Dumpling \tPrice AUD 6.")
                print("Enter 4 for Muffins \tPrice AUD 8.")
                print("Enter 5 for Pasta \tPrice AUD 10.")
                print("Enter 6 for Pizza \tPrice AUD 20.")
                print("Enter 7 for Drinks Menu:")
            
                self.food_order = input(":")
                self.food_listed_order = list(self.food_order)
                self.prices = ""
                try:
                    for each_ordered_item in self.food_listed_order:
                        self.food_prices =self.food_orders[each_ordered_item]
                        self.prices += self.food_prices
                except:
                    pass

                print("Please enter 7 to exit Food menu.")
                self.food_order = input(":")

                if self.food_order == "7":
                    print("Enter 1 for Coffee \tPrice AUD 2.")
                    print("Enter 2 for ColdDrink \tPrice AUD 4.")
                    print("Enter 3 for Shake \tPrice AUD 6.")
                    print("Enter 4 for CheckOut:")
                    self.drink_order = input(":")
                    self.drink_listed_order = list(self.drink_order)
                    try:
                        for each_item in self.drink_listed_order:
                            self.drink_prices =self.drink_orders[each_item]
                            self.prices += self.drink_prices
                    except:
                        pass
                    self.int_price = 0
                    for each_price in self.prices:
                        self.int_price += int(each_price)
                    print("Please enter 4 to check out.")
                    self.drink_order = input(":")
                    if self.drink_order == "4" and self.input == "2":
                        while True:
                            self.proceed_to_checkout = input("Please Enter y to proceed to CheckOut or enter n to cancel the order: ")
                            if self.proceed_to_checkout == "y" and user_data["address"] != "":
                                print(f"Your total payable amount is: {self.int_price} AUD and there will be additional charges for Delivery.")
                                self.delivery_date = input("Please enter the Date of Delivery (format: DD/MM/YYYY): ")
                                self.delivery_time = input("Please enter the Time of Delivery (format: HH:MM): ")
                                self.distance = input("Please enter the Distance from the restaurant:")
                                self.int_distance = int(self.distance)
                                self.num = user_data["number"]
                                if self.int_distance <=  15:
                                    print("Thank you for your Order, Your Order has been confirmed.")

                                    # GENERATING THE USER ID IN FORMAT S001
                                    self.delivery_id = "S"
                                    count += 1
                                    self.deliveryID = f"{count:03d}"
                                    self.delivery_id += self.deliveryID
                                    self.deliveries["OrderID"] = self.delivery_id
                                    self.deliveries["Date"] = self.delivery_date
                                    self.deliveries["Total_Amount"] = self.int_price
                                    self.deliveries["OrderType"] = "Delivery"
                                    deliveries[self.num] = self.deliveries
                                
                                    SignIn.menu(self)
                                    break
                                else:
                                    print("Distance from restaurant is more than the applicable limits")
                                    order = OrderOnline()
                            elif self.proceed_to_checkout == "n":
                                order = StartOrdering()
                                break
                            elif self.proceed_to_checkout == "y" and user_data["address"] == "":
                                print("You have not mentioned your address, while signing up.")
                                self.to_checkout = input("Please Enter y if you would like to enter your address or\nEnter n if you would like to select other mode of order: ")
                                if self.to_checkout == "y":
                                    self.new_addr = input("Enter new addr:")
                                    user_data["address"] = self.new_addr
                                    self.num = user_data["number"]
                                    with open(f"{self.num}.json", "w") as file:
                                        json.dump(user_data, file)
                                    print(f"Your total payable amount is: {self.int_price} AUD and there will be additional charges for Delivery.")
                                    self.delivery_date = input("Please enter the Date of Delivery (format: DD/MM/YYYY): ")
                                    self.delivery_time = input("Please enter the Time of Delivery (format: HH:MM): ")
                                    self.distance = input("Please enter the Distance from the restaurant:")
                                    self.int_distance = int(self.distance)
                                    if self.int_distance <=  15:
                                        print("Thank you for your Order, Your Order has been confirmed.")

                                        # GENERATING THE USER ID IN FORMAT S001
                                        self.delivery_id = "S"
                                        count += 1
                                        self.deliveryID = f"{count:03d}"
                                        self.delivery_id += self.deliveryID
                                        self.deliveries["OrderID"] = self.delivery_id
                                        self.deliveries["Date"] = self.delivery_date
                                        self.deliveries["Total_Amount"] = self.int_price
                                        self.deliveries["OrderType"] = "Delivery"
                                        deliveries[self.num] = self.deliveries
                                    
                                        SignIn.menu(self)
                                        break
                                    else:
                                        print("Distance from restaurant is more than the applicable limits")
                                        order = OrderOnline()
                                    
                                elif self.to_checkout == "n":
                                    order = StartOrdering()
                                    break
                                else:
                                    print("Invalid Input")
                                    self.to_checkout = input(":")
                            else:
                                print("Invalid Input")
                                self.proceed_to_checkout = input(":")


                # Pick Up MODE
                if self.drink_order == "4" and self.input == "1":
                    while True:
                            self.proceed_to_checkout = input("Please Enter y to proceed to CheckOut or enter n to cancel the order: ")
                            if self.proceed_to_checkout == "y":
                                print(f"Your total payable amount is: {self.int_price} AUD and no additional Charges for click and collect .")
                                self.pickup_date = input("Please enter the Date of Pick up (format: DD/MM/YYYY): ")
                                self.pickup_time = input("Please enter the Time of Pick up (format: HH:MM): ")
                                self.persons = input("Please enter the number of Persons:")
                                print("Thank You for entering the details, Your Booking is confirmed")
                                self.num = user_data["number"]
                                
                                # GENERATING THE USER ID IN FORMAT S001
                                self.pickup_id = "S"
                                count += 1
                                self.pickupID = f"{count:03d}"
                                self.pickup_id += self.pickupID
                                self.pickUp["OrderID"] = self.pickup_id
                                self.pickUp["Date"] = self.pickup_date
                                self.pickUp["Total_Amount"] = self.int_price
                                self.pickUp["OrderType"] = "Pick Up"
                                pickup[self.num] = self.pickUp
                                SignIn.menu(self)
                                break
                            elif self.proceed_to_checkout == "n":
                                order = StartOrdering()
                                break


class DineIn():
    def __init__(self) :
        super(DineIn, self).__init__()
        global count
        global dine_in
        self.user_dineIn = {}
        self.food_orders = {"1": "2",
                            "2": "4",
                            "3": "6",
                            "4": "8",
                            "5": "10",
                            "6": "20",
                            "7": "2",
                            "8": "4",
                            "9": "6"}

        print("Enter 1 for Noodles \tPrice AUD 2.")
        print("Enter 2 for Sandwich \tPrice AUD 4.")
        print("Enter 3 for Dumpling \tPrice AUD 6.")
        print("Enter 4 for Muffins \tPrice AUD 8.")
        print("Enter 5 for Pasta \tPrice AUD 10.")
        print("Enter 6 for Pizza \tPrice AUD 20.")
        print("Enter 7 for Coffee \tPrice AUD 2.")
        print("Enter 8 for ColdDrink \tPrice AUD 4.")
        print("Enter 9 for Shake \tPrice AUD 6.")
        self.orders = input(":")
        self.listed_order = list(self.orders)
        self.prices = ""
        try:
            for each_ordered_item in self.listed_order:
                self.temp_food =self.food_orders[each_ordered_item]
                self.prices += self.temp_food
        except:
                pass
        self.int_price = 0
        for each_price in self.prices:
            self.int_price += int(each_price)
        self.service_charges = 0.15 * self.int_price
        self.total_price = self.int_price + self.service_charges
        while True:
            self.proceed_to_checkout = input("Please Enter y to proceed to  CheckOut or\nEnter n to cancel the order: ")
            if self.proceed_to_checkout == "y":
                print(f"Your total payable amount is {self.total_price} including {self.service_charges} for Service Charges")
                self.dine_date = input("Please enter the Date of Booking for Dine in (format: DD/MM/YYYY): ")
                self.dine_time = input("Please enter the Time of Booking for Dine in (format: HH:MM): ")
                self.persons = input("Please enter the Number of Persons:")
                print("Thank You for entering the details, Your Booking is confirmed.")
                # GENERATING THE USER ID IN FORMAT S001
                self.dineIn_id = "S"
                count += 1
                self.dineInID = f"{count:03d}"
                self.dineIn_id += self.dineInID
                self.user_dineIn["OrderId"] = self.dineIn_id
                self.user_dineIn["Date"] = self.dine_date
                self.user_dineIn["Total_Amount"] = self.total_price
                self.user_dineIn["OrderType"] = "Dine In"
                self.num = user_data["number"]
                dine_in[self.num] = self.user_dineIn
                SignIn.menu(self)
                break

            elif self.proceed_to_checkout == "n":
                order = StartOrdering()
                break
            else:
                print("Invalid Input ")
                self.proceed_to_checkout = input(":")


class PrintStats():
    def __init__(self):
        global dine_in
        global pickup
        global deliveries
        global user_data
        self.num = user_data["number"]
        self.total_expenditure = ()
        print("Please enter the Option to Print the Statistics.")
        print("1 - All Dine in Orders.")
        print("2 - All Pick up Orders.")
        print("3 - All Deliveries.")
        print("4 - All Orders (Ascending Order).")
        print("5 - Total Amount Spent on All Orders.")
        print("6 - To go to Previous Menu.")
        self.input = input(":")
        if self.input == "1":
            print(dine_in)
        elif self.input == "2":
            print(pickup)
        elif self.input == "3":
            print(deliveries)
        elif self.input == "5":
            self.total_expenditure = 0
            for each_key, each_value in dine_in.items():
                for key_value in each_value:
                    if key_value == "Total_Amount":
                        self.expenditure = (int(each_value[key_value]))
                        self.total_expenditure += self.expenditure
            for each_key, each_value in pickup.items():
                for key_value in each_value:
                    if key_value == "Total_Amount":
                        self.expenditure = (int(each_value[key_value]))
                        self.total_expenditure += self.expenditure
            for each_key, each_value in deliveries.items():
                for key_value in each_value:
                    if key_value == "Total_Amount":
                        self.expenditure = (int(each_value[key_value]))
                        self.total_expenditure += self.expenditure
            
            print(f"Total Amount spent on all orders AUD {self.total_expenditure}")
        elif self.input == "6":
            SignIn.menu(self)
        elif self.input == "4":
            print(dine_in, pickup, deliveries)
        


while True:
    app = MainApp()
    if app.input == "3":
        print("Thank You for using the application.")
        break
    if app.input == "1":
        sign_up = SignUP()
    if app.input == "2":
        login = SignIn()