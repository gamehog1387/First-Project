from datetime import datetime
import json


def login():    
    print("Welcome to Williams Workout Tracker!")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        Username = input("What is your username?  ")
        password = input("what is your password")
        
        if Username == "USER1" and password == '768768':
            print("Login successful!!!! Welcome William! ")
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Login was incorrect, please try again")
            else:
                print("Ran out of attempts buddy. check your source code for app")
                #Change print for this before establish of Gui Interface
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
 
# Login before accessing the app
if not login():
    exit()

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
        print("goodybe!")
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
    