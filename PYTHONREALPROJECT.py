from datetime import datetime
import json

print("FOR real passwords they have to be stored securely. these ones are meant to be viewd in the python file for me to see easier. May add secure method later")
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
            return "user_1"
        elif user_choice == '2' and password == '3299393':
            print("Welcome to the site!")
            return "first_project"
        else:
            print("Invalid password or user choice!")
        
        attempts += 1
        if attempts < attempts_remaining:
            print(f"Invalid input: {attempts_remaining - attempts} attempts remain!")
        else:
            print("GOODBYE!")
            return None
    return None

    
def double_verification():
    print("Before entering")
    attempts = 0
    attempts_remaining = 3
    while attempts < attempts_remaining:
        color = input("what is your favorite color? ")
        if color.lower() == 'blue':
            return True
        else:
            attempts += 1
            print(f"NOPE! attempts remaining = {attempts_remaining - attempts}")
        print("Goodbye")
        return'False'
    
    



def save_data(username):
    filename = f"workouts_{username}.json"
    with open(filename, "w") as f:
        json.dump(workouts, f, indent=4)

def load_data(username):
    filename = f"workouts_{username}.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


# Login before accessing the app
current_user = login()
if not current_user:
    exit()
if not double_verification():
    exit()
workouts = load_data(current_user)

def add_workout():
    while True:
        try:
            Excercise = input("Excercise Name? ")
            Weight = int(input("Weight moved "))
        except ValueError:
            print("Invalid input for weight, please enter a number.")
            continue
        Reps = int(input("How many Reps? "))
        current_date = datetime.now().strftime("%Y-%m-%d")
        workout = {
        "Date": current_date, 
        "Excercise": Excercise,
        "Weight": Weight,
        "Reps": Reps,
        }

        workouts.append(workout)
        save_data(current_user)
        print("Workout Added!")
        
        another = input("Add another workout? (yes/no): ").lower()
        if another != "yes" and another != "y":
            break
        

def exit_menu():
    leave_now = input("Would you like to leave, Yes or No? ").lower()
    if leave_now.lower() == 'yes':
        print("Okay<3 Goodybye!")
        return True
    elif leave_now.lower() == 'no':
        print("okaaa!")
        return False
    else:
        print("e9i4iei error::::: please repeat")
        return False

def view_personal_records():
    if not workouts:
        print("No workouts recorded so far!")
        return
    pr_data = {}

    for workout in workouts:
        excercise = workout['Excercise']
        weight = workout['Weight']
        reps = workout['Reps']
        volume = weight * reps

        if excercise not in pr_data:
            pr_data[excercise] = {
                'max_weight': weight,
                'max_reps': reps,
                'max_volume': volume,
                'date': workout['Date']
            }
        else:
            if weight > pr_data[excercise]['max_weight']:
                pr_data[excercise]['max_weight'] = weight
                pr_data[excercise]['date'] = workout['Date']
            if volume > pr_data[excercise]['max_volume']:
                pr_data[excercise]['max_volume'] = volume

    print("\n============== Personal Records ============")
    for exercise, data in pr_data.items():
        print(f"\n{exercise}")
        print(f" Max weight: {data['max_weight']} lbs")
        print(f" Max Reps: {data['max_reps']}")
        print(f" Max volume (weight x reps): {data['max_volume']}")
        print(f" Date: {data['date']}")
        print("==========\n")
while True:
   
    print("\n William's Workout Tracker")
    print("1. Add Workout")
    print("2. View Workout")
    print("3. Exit Workout")
    print("4. Delete Workout")
    print("5. View Personal Records")

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
    elif choice == '5':
        view_personal_records()

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
                    save_data(current_user)
                    print (f"Deleted: {removed_workout['Excercise']}")
                    
                    more = input("Delete another workout? (yes/no): ").lower()
                    if more != "yes" and more != "y":
                        break
                    if not workouts:
                        print("No more workouts to delete!")
                        break
                except (ValueError, IndexError):
                    print("Invalid number please try again")
