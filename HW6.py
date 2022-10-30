#COMPUTER SCIENCE: HOMEWORK #6
#1: CHAPTER 7: DISCUSSION PROBLEM #2
    #An if/else statement is executed if it is true. If it not true, then the elif or else-if statement is executed.
    #In try/except the whole block is exceuted until a match is found with some except. 

#2: CHAPTER 7: PROGRAMMING EXERCISE #3
grade=int(input("Enter your numeric grade: "))
if(grade>=90 and grade<=100):
    print("Your grade is : A")
elif(grade>=80 and grade<=89):
    print("Your grade is : B")
elif(grade>=70 and grade<=79):
    print("Your grade is : C")
elif(grade>=60 and grade<=69):
    print("Your grade is : D")
elif(grade<=60):
    print("Your grade is : F")

#3: CHAPTER 7: PROGRAMMING EXERCISE #7
def main():
    print("This program calculates the babysoitting bill for a babysittier")
    stime= str(input("Enter the starting time: "))
    if "PM" in stime or "AM" in stime:
        etime=str(input("Enter the ending time: "))
        if "PM" in etime or "AM" in etime:
            print("Total time: ", stime, "-", etime)
            time(stime, etime)
    else:
        print("[Error] You must enter in the format #:## PM/AM")
        return
    stime,etime = time(stime, etime)
def time(stime, etime):
    if "AM" in stime:
        stime=stime.replace("AM","")
        stime=stime.replace(":","")
        stime=int(stime)
    else:
        stime=stime.replace("PM","")
        stime=stime.replace(":","")
        stime=int(stime)+1200
    if "AM" in etime:
        etime=etime.replace("AM", "")
        etime=etime.replace(":","")
        etime=int(etime)
    else:
        etime=etime.replace("PM","")
        etime=etime.replace(":","")
        etime=int(etime)+1200
    return stime,etime
def pay(stime,etime):
    total_time=etime.replace("PM","")
    rate=2.50
    ratedrop=1.75
    if etime<=2100:
        total_pay=total_time*rate
    if etime>2100:
        deltatime=(etime-2100)/100
        total_pay=((deltatime)*ratedrop)+((total_time-deltatime)*rate)
    total_pay=pay(stime, etime)
    print("Total pay: $", total_pay, sep="")
    return total_pay
    time(stime, etime)
if __name__ == "__main__":
    main()

#4: CHAPTER 7: PROGRAMMING EXERCISE #8
def main():
    age=int(input("Enter your age: "))
    citizen_years=int(input("Enter the number of years you have been a citizen: "))
    if age>=30 and citizen_years>=9:
        print("You are eligible to run for the Senate or the House of Representatives.")
    elif age>=25 and citizen_years>=7:
        print("You are eligible ot run for the House of Representatives but not the Senate.")
    else:
        print("You are not eligible to run for the Senate or the House of representative.")
main()
            

#5: An error can occur if the variables are not correctly defined in a code. For instance, in #4, if citizen_years was misspelled an error would occur.
#Another error that can occur is from improper syntax. For instance, when defining variables there cannot be spaces but rather underscores.
#If an underscore was missing from citizen_years then it would be improper syntaz and the code will not run. 

