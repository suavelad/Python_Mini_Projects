
#! /usr/bin/python3 

"""
This GPA application will help you calculate your
GP using 5.0 scale

"""
print("  ")
print(" Hi, Insert your course, grade and unit using this format :")
print("Example: MTH101,A,5  ")
print("  ")
print("************************************************************")
print("The System calculates the GP once you have inserted the")
print("grades for all the courses")
print("************************************************************")    
print("  ")

def gpcalculator():
    fullgrades=[]
    units = 0
    try:
        total=0

              
        try:

            number= int(input("How many course did you offer? >> "))
        except ValueError:
            print ("It requires an integer")
                                 
        
        for a in range(number):
            
            stuff= (input(">> ")).upper()

            course,grade,unit = stuff.split(',')
            # courses.append(course)
            # grades.append(grade)
            units+=int(unit)
            fullgrade = (course +"                " +unit+"               " + grade)
            fullgrades.append(fullgrade)
      
            if grade=="A" :
                tot = 5 * int(unit)
                total+=tot

            elif grade=="B" :
                tot = 4 * int(unit)
                total+=tot


            elif grade=="C" :
                tot = 3 * int(unit)
                total+=tot
                print (tot)
                print(total)


            elif grade=="D"  :
                tot = 2 * int(unit)
                total+=tot

            elif grade=="E" :
                tot = 1 * int(unit)
                total+=tot

            elif grade=="F" :
                tot = 0 * int(unit)
                total+=tot
            
            else:
                print ("Invalid Input. Check your input")
                retry= input("Do you want to start again? y or n >>").lower()
                if retry=="y" :
                    gpcalculator()
                
                elif retry=="n" :
                    exit
                else:
                    exit
        print("************************************************************")
        print("These are the courses, unit and grades you inserted :")
        print("  ") 
        print("Courses             Units           Grades")
        for each in fullgrades:
            print (each)

       
        gp =float(total/units)
        print("  ")
        print("************************************************************")
        print ("Your GP is:%f "%(gp))
        print("************************************************************")
        print(" ")


    except (NameError,ValueError ):
        print ("Check what you inputted and try again")
        retry= input("Do you want to start again? y or n >>").lower()
        if retry=="y" :
            gpcalculator()
        
        elif retry=="n":
            exit
        else:
            exit



gpcalculator()
