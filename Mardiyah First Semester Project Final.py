#!/usr/bin/env python
# coding: utf-8


#function to calculate total sales made in the day
def total_sales():
    morning_sales = [] #List to store sales data for morning shift
    evening_sales = [] #List to store sales data for evening shift
    shifts = ["morning", "evening"] #List representing the shifts in the day

    for shift in shifts:
        print(f"Entering sales data for {shift} shift:") 
        entry_index = 1 #keeps track of the number of sales made for a particular shift
        while True:
            try:
                #prompts user to enter the sales data for morning and evening shifts
                total_sales = float(input(f"Enter sales {entry_index} made for {shift} shift (or enter 0 to terminate): "))
                if total_sales < 0:
                    raise ValueError("Sales cannot be negative.") #raises an error when inputted sales is negative
                if total_sales == 0: #prompts program to end the loop when total sales is zero
                    break
                elif shift == "morning":
                    morning_sales.append(total_sales)           
                elif shift == "evening":
                    evening_sales.append(total_sales)
                else:
                    print("Invalid input")
                entry_index += 1  # Increment the entry index
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    total_sales = sum(morning_sales) + sum(evening_sales) #calculates the total sales for the day
    print(f"\nThe total sales for the day is: {total_sales}") #displays the total sales for the day



#function to calculate the daily salary for workers based on their hourly rate and hours worked
def workers_salary():
    while True:
        try:
            #prompts user to enter worker's ID which is either 1 or 2 
            ID_option = input("Enter worker's ID (1/2), or enter 'q' to quit: ")
            if ID_option.lower() == 'q':
                break
            elif ID_option == "1" :
                while True:
                    try:
                        hourly_rate = float(input(f"Enter worker {ID_option} hourly rate: ")) #prompts user to input hourly rate for worker 1
                        if hourly_rate < 0:
                            raise ValueError("Hourly rate cannot be negative.") #raises an error when inputted rate is negative
                        hours_worked1 = int(input("Enter number of hours worked: ")) #prompts user to input number of hours worked for worker 1
                        if hours_worked1 < 0:
                            raise ValueError("Hours worked cannot be negative.") #raises an error when inputted hours is negative
                        worker1_salary = hours_worked1 * hourly_rate
                        print(f"Total daily salary for worker {ID_option} is: {worker1_salary}\n") #displays salary for worker 1
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric value.")
                        
            elif ID_option == "2":
                while True:
                    try:
                        hourly_rate = float(input(f"Enter worker {ID_option} hourly rate: ")) #prompts user to input hourly rate for worker 2
                        if hourly_rate < 0:
                            raise ValueError("Hourly rate cannot be negative.") #raises an error when inputted rate is negative
                        hours_worked2 = int(input("Enter number of hours worked: ")) #prompts user to input number of hours worked for worker 2
                        if hours_worked2 < 0:
                            raise ValueError("Hours worked cannot be negative.") #raises an error when inputted hours is negative
                        worker2_salary = hours_worked2 * hourly_rate
                        print(f"Total daily salary for worker {ID_option} is: {worker2_salary}\n") #displays salary for worker 2
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric value.")
            else:
                print("ID does not exist. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")



#function to calculate profit or loss made based on total sales and total costs
def profit_made():
    total_sales_costs = [0,0] #List to store total sales and total costs, initializiing at zero

    while True:
        try:
            sales = float(input("Enter total sales: ")) #prompts user to input total sales
            if sales < 0:
                raise ValueError("Sales cannot be negative.") #raises an error when inputted sales is negative
            costs = float(input("Enter total costs: ")) #prompts user to input total costs
            if costs < 0:
                raise ValueError("Costs cannot be negative.") #raises an error when inputted costs is negative
            total_sales_costs[0] += sales #tells program to add total sales to sales index of our list
            total_sales_costs[1] += costs #tells program to add total sales to cost of product index of our list
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    total_profit = total_sales_costs[0] - total_sales_costs[1] #calculates total profit by subtracting total costs from total sales
    if total_profit < 0:
        print(f"\nBusiness made a loss of {total_profit}") #displays when the business made a loss
    else:
        print(f"\nBusiness made a profit of {total_profit}") #displays when the business made a profit



#function to calculate tips for morning or evening / morning and evening shifts based on total sales
def shift_tips():
    morning_sales = [] #List to store total sales for the morning shift
    evening_sales = [] #List to store total sales for the evening shift
    total_tips = 0 #variable to store the total tips for both shifts

    while True:
        
        try:
            #prompts user to select the option of the shifts they want to calculate tips for
            get_tip = input("Enter '1' to get tip for morning shift, '2' for evening shift, '3' for both, or 'q' to quit: ")
            
            if get_tip.lower() == 'q': #tells program to exit the loop when the user enters q
                break 
                
            elif get_tip == "1":
                morning_sales_input = float(input("Enter total sales made for morning shift: ")) #prompts user to enter total sales for morning shift
                if mornin_sales_input < 0:
                    raise ValueError("Morning sales cannot be negative.") #raises an error when inputted sales is negative
                morning_sales.append(morning_sales_input)
                morning_tip = morning_sales_input * 0.02 #calculates 2% of morning sales as tip 
                print(f"\nMorning tip is: {morning_tip}\n") #displays amount of tip gotten from morning shift
                total_tips += morning_tip

            elif get_tip == "2":
                evening_sales_input = float(input("Enter total sales made for evening shift: ")) #prompts user to enter total sales for evening shift
                if evening_sales_input < 0:
                    raise ValueError("Evening sales cannot be negative.") #raises an error when inputted sales is negative
                evening_sales.append(evening_sales_input)
                evening_tip = evening_sales_input * 0.02 #calculates 2% of evening sales as tip
                print(f"\nEvening tip is: {evening_tip}\n") #displays amount of tip gotten from evening shift
                total_tips += evening_tip

            elif get_tip == "3":
                morning_sales_input = float(input("Enter total sales made for morning shift: "))
                if morning_sales_input < 0:
                    raise ValueError("Morning sales cannot be negative.") #raises an error when inputted sales is negative
                morning_sales.append(morning_sales_input)
                evening_sales_input = float(input("Enter total sales made for evening shift: "))
                if evening_sales_input < 0:
                    raise ValueError("Evening sales cannot be negative.") #raises an error when inputted sales is negative
                evening_sales.append(evening_sales_input)
                morning_tip = morning_sales_input * 0.02
                evening_tip = evening_sales_input * 0.02
                total_tips += morning_tip + evening_tip #sums up tips made in the morning and tips made in the evening
                print(f"\nTotal tips for the day: {total_tips}") #displays total tips made for the day

            else:
                print("Option does not exist, enter 1, 2, 3, or 'q'")

        except ValueError:
            print("Invalid input, try again") 
#The try and except function as seen in all the functions is used to handle errors that might come from users intentionally or 
#unintentionally entering non-numeric values so as not to crash the program.



#function to provide a menu-driven interface to execute essential accounting tasks based on user input
def run_accounting_task():
    while True:
        #displays a list of option users can choose from to perform
        print("\nEssential Accounting tasks")
        print("1. Get total sales")
        print("2. Get worker's salary")
        print("3. Get Profit")
        print("4. Get shift tips")
        print("5. Exit")
        
        Option = input("Enter any of option(1-5):\n") #prompts user to enter the option they want by selecting any number between 1 to 5
        if Option == '1':
            total_sales() #retieves total sales function
        elif Option == '2':
            workers_salary() #retrieves workers salary function
        elif Option == '3':
            profit_made() #retrieves profit made function
        elif Option == '4':
            shift_tips() #retrieves shift tips function
        elif Option == '5':
            print("You have successfully exit the program") #allows user to end the program
            break
        else:
            print("Invalid choice. please enter a number between 1 and 5.") #prompts the user to enter a valid choice (1 - 5) in case of mistake


run_accounting_task()

