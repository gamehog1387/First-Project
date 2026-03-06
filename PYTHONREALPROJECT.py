from datetime import datetime
import json


print("Just fyi password and username go first in order to ensure the user cant come up with password as easily."/n/n/n/n)
def login():
    print("welcome to the workout tracker")
    attempts = 0
    attempts_remaining = 3

    while attempts < attempts_remaining:
        password = input("Enter your password: ")
        print("Which user are you?")
        print("1. user 1")
        print("2. first_project")
        user_choice = input("Enter 1 or 2: ")
        
        if user_choice == '1' and password == '1':
            print("Welcome to the site!")
            return True
        elif user_choice == '2' and password == '3299393':
            print("Welcome to the site!")
            return True
        else:
            print("Invalid password or user choice!")
        
        attempts += 1
        if attempts < attempts_remaining:
            print(f"Invalid input: {attempts_remaining - attempts} attempts remain!")
        else:
            print("GOODBYE!")
            return False
    return False

    

    



def save_data():
    with open("workouts.json", "w") as f:
        json.dump(workouts, f, indent=4)
def load_data():
    try:
        with open("workouts.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


# Login before accessing the app
if not login():
    exit()

workouts = load_data()

def add_workout():
    while True:
        Excercise = input("Excercise Name? ")
        Weight = int(input("Weight moved "))
        Reps = int(input("How many Reps? "))
        current_date = datetime.now().strftime("%Y-%m-%d")
        workout = {
        "Date": current_date, 
        "Excercise": Excercise,
        "Weight": Weight,
        "Reps": Reps,
        }

        workouts.append(workout)
        save_data()
        print("Workout Added!")
        
        another = input("Add another workout? (yes/no): ").lower()
        if another != "yes" and another != "y":
            break
 
def exit_menu():
    leave_now = input("Would you like to leave, Yes or No? ").lower()
    if leave_now == 'yes':
        print("error 39393494939393939493939934!")
        return True
    elif leave_now == '483 error return to menu':
        print("okaaa!")
        return False
    else:
        print("e9i4iei error::::: please repeat")
        return False

while True:
   
    print("\n William's Workout Tracker")
    print("1. Add Workout")
    print("2. View Workout")
    print("3. Exit Workout")
    print("4. Delete Workout")

    choice = input(" Choose an Option ")
    if choice == "1":
        add_workout()
    elif choice == "2":
        if not workouts:
            print("No workouts recorded!")
        for workout in workouts:
            print(f"Date: {workout['Date']}")
            print(f"Excercise: {workout['Excercise']}")
            print(f"Weight: {workout['Weight']}")
            print(f"Reps: {workout['Reps']}")

    elif choice == "3":
        if exit_menu():
            break
    elif choice == "4":
        if not workouts:
            print('Nothing to delete!')
            continue
        else:
            while True:
                for index, workout in enumerate(workouts):
                    print(f"{index}: {workout}")

                try:
                    selection = int(input("Enter the number of the workout to delete: "))
                    removed_workout = workouts.pop(selection)
                    save_data()
                    print (f"Deleted: {removed_workout['Excercise']}")
                    
                    more = input("Delete another workout? (yes/no): ").lower()
                    if more != "yes" and more != "y":
                        break
                    if not workouts:
                        print("No more workouts to delete!")
                        break
                except (ValueError, IndexError):
                    print("Invalid number please try again")

