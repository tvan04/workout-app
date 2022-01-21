import tkinter 
import pickle 

def main():
    userchoice = input("""This is a workout buddy to help keep track of your fitness goals! 
    1) See the workout!
    2) Set/change workout routine
    3) Change/calculate maxes
    Please enter a number: """)

    if int(userchoice) == 1:
        userchoice1(1)
    #set/changing workout routines 
    elif int(userchoice) == 2:
        userchoice2(2)
    #Calculating and changing the maxes
    
    elif int(userchoice) == 3:
        userchoice3(3)


def userchoice1(userchoice):
    savefile = pickle.load(open("exercises.pickle", "rb"))
    print(savefile)

def userchoice2(userchoice):
    exercises = {}
    while True: 
        choice2 = int(input("Press '1' if you want to add an exercise along with the sets and reps in __x__ format (ex. 5x5). Type '2' when finished or '3' to wipe your workout.\n"))    
        if choice2 == 1:
            exer = input("Please enter your exercise: ")
            setsandreps = input("Please enter set and reps: ")
            exercises[exer] = setsandreps
        elif choice2 == 2:
            savefile = pickle.dump(exercises, open("exercises.pickle", "wb"))
            break
        elif choice2 == 3:
            empty_list = []
            clearfile = open('exercises.pickle', 'wb')
            pickle.dump(empty_list, clearfile)
            clearfile.close()
            break

def userchoice3(userchoice):
    choice3 = input("Do you want to (1) view/edit your current maxes or (2) calculate a new 1RM?\nPlease enter 1 or 2: ")
    if int(choice3) == 1:
        choice3_1 = input ("Do you want to (1) see current maxes or (2) change them?\nPlease enter 1 or 2:")
        maxes = {"Bench" : "", "Squat" : "", "Deadlift" : "", "Row" : "", "OHP" : ""}
        if int(choice3_1) == 1:
            maxes = pickle.load(open("maxes.pickle", "rb"))
            for key, value in maxes.items():
                print(key, ':', value)
        if int(choice3_1) == 2:
            maxes["Bench"] = int(input("What is your max bench: "))
            maxes["Squat"] = int(input("What is your max squat: "))
            maxes["Deadlift"] = int(input("What is your max deadlift: "))
            maxes["Row"] = int(input("What is your max row: "))
            maxes["OHP"] = int(input("What is your max ohp: "))
            pickle.dump(maxes, open("maxes.pickle", "wb"))

    if int(choice3) == 2:

        print("This 1RM Calculator uses the Brzycki formula. Please enter your weight, and reps that you can perform")
        weight = input("Enter weight: ")   
        reps = input("Enter reps: ")
        oneRM = (int(weight) / ( 1.0278 - 0.0278 * int(reps)))
        print("Your 1RM is",round(oneRM,2),"lbs")
    else:
        print("This is an invalid option.")

if __name__ == "__main__":
    main()