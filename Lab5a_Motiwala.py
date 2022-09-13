#Name: Muhammed Motiwala
#Program: Complete
# Finds average grade from 5 grades, then outputs letter grade.


def main():
    numavg = 0.0
    grades = 0.0
    counter= 0
    #This loop will run 5 times and a counter is built in so we know how many times it has gone through.
    for i in range(5):
        counter += 1
        print ("enter score #", counter, "'s grade")
 #It will ask for a number and validate it       
        nums = float(input("from 1 - 100: "))
        if nums > 100 or nums < 1:
            nums = float(input("Try again, enter 5 grades, each between 1-100 "))
            #add all the numbers together
        grades = grades + nums
        #Average
    numavg = (grades / 5)
    print ("your average is :", format(numavg, '.2f'))
    #call bottom function.
    determine_grade(numavg)


def determine_grade(gradeavg):
    if gradeavg > 90:
        print("you earned an A")
    elif gradeavg > 80:
        print(" you earned a B")
    elif gradeavg > 70:
        print("you earned a C")
    elif gradeavg >60:
        print("you earned a D")
    else:
        print("you earned a F")
    

        
main()
