print("welcome\n")
def calculate_length():
        print("Great Here you choose Length unit for convert\n")
        print("what you want to convert\n")
        print("1. CM ↔ INCH\n 2.INCH  2.  METER ↔ FEET\n 3. KM ↔ MILES\n")
        try:
            choice2=float(input("Please select  option to perform the task\n"))
        except ValueError:
            print("Please enter a valid option between 1-3\n")
            return
        if choice2==1:
            try:
                    value=float(input("Enter the value for CM <--> INCH\n"))
                    print(f"Your converted value of {value} CM is { value*0.3937 :.2f} INCH\n")
                    print(f"Your converted value of {value} INCH is {value * 2.54 :.2f} CM\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==2:
            try:
                    value=float(input("Enter the value for METER ↔ FEET\n"))
                    print(f"Your converted value of {value} METER is { value*3.2808 :.2f} FEET\n")
                    print(f"Your converted value of {value} FEET is {value * 0.3048 :.2f} METER\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==3:
            try:
                    value=float(input("Enter the value for  KM ↔ MILES\n"))
                    print(f"Your converted value of {value} KM is { value*0.621371:.2f} MILES\n")
                    print(f"Your converted value of {value} MILES is {value *  1.60934:.2f} KM\n")
            except ValueError:
                    print("Please enter a valid details\n")
def calculate_weight():
        print("Great Here you choose  unit weight for convert\n")
        print("what you want to convert\n")
        print("1. KG ↔ POUNDS\n  2. GRAM ↔ OUNCE\n")
        try:
            choice2=float(input("Please select  option to perform the task\n"))
        except ValueError:
            print("Please enter a valid option between 1-2\n")
            return
        if choice2==1:
            try:
                    value=float(input("Enter the value for KG ↔ POUNDS\n"))
                    print(f"Your converted value of {value} is KG{ value*  2.20462 :.2f} POUNDS\n")
                    print(f"Your converted value of {value} POUNDS is {value *0.453592 :.2f} KG\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==2:
            try:
                    value=float(input("Enter the value for  GRAM ↔ OUNCE\n"))
                    print(f"Your converted value of {value} GRAM is { value* 0.035274:.2f} OUNCE\n")
                    print(f"Your converted value of {value} OUNCE is {value * 28.3495 :.2f} GRAM\n")
            except ValueError:
                    print("Please enter a valid details\n")
        
def calculate_Temperature():
        print("Great Here you choose  unit Temperature for convert\n")
        print("what you want to convert\n")
        print("1. Celsius ↔ Fahrenheit \n 2. Celsius ↔ Kelvin\n")
        try:
            choice2=float(input("Please select  option to perform the task\n"))
        except ValueError:
            print("Please enter a valid option between 1-2\n")
            return
        if choice2==1:
            try:
                    value=float(input("Enter the value for  Celsius ↔ Fahrenheit\n"))
                    print(f"Your converted value of {value} celsius is {(value * 9/5) + 32:.2f} fehrenheit\n")
                    print(f"Your converted value of {value} fehrenheit is {(value - 32) * 5/9 :.2f} celsius\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==2:
            try:
                    value=float(input("Enter the value for Celsius ↔ Kelvin\n"))
                    print(f"Your converted value of {value} Celsius is { value + 273.15:.2f} Kelvin\n")
                    print(f"Your converted value of {value} Kelvin is {value-273.15:.2f} Celsius\n")
            except ValueError:
                    print("Please enter a valid details\n")

def calculate_Time():
        print("Great Here you choose  unit Time for convert\n")
        print("what you want to convert\n")
        print("1. seconds ↔ minutes \n 2. minutes ↔ hours\n 3. hours ↔ days\n")
        try:
            choice2=float(input("Please select  option to perform the task\n"))
        except ValueError:
            print("Please enter a valid option between 1-3\n")
            return
        if choice2==1:
            try:
                    value=float(input("Enter the value for seconds ↔ minutes\n"))
                    print(f"Your converted value of {value} seconds is { value / 60 :.2f} minutes\n")
                    print(f"Your converted value of {value} minutes is {value * 60 :.2f} seconds\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==2:
            try:
                    value=float(input("Enter the value for minutes ↔ hours\n"))
                    print(f"Your converted value of {value} minutes is { value/60 :.2f} hours\n")
                    print(f"Your converted value of {value} hours is {value * 60 :.2f} minutes\n")
            except ValueError:
                    print("Please enter a valid details\n")
        elif choice2==3:
            try:
                    value=float(input("Enter the value for hours ↔ days\n"))
                    print(f"Your converted value of {value} hours is { value / 24:.2f} days \n")
                    print(f"Your converted value of {value}  days is {value *  24:.2f} hours\n")
            except ValueError:
                    print("Please enter a valid details\n")
while True:
    print("Here you can convert units\n Your options are: ")
    print(" 1. Lenth \n")
    print("2. Weight\n ")
    print("3. Time \n")
    print("4. Temprature\n ")
    print("5. Exit\n ")

    try:
        choice=float(input("Please select any option between 1-5\n"))
    except ValueError:
        print("Please enter a valid number between 1-5\n")
        continue

    if choice==1:
          calculate_length()

    elif choice==2:
          calculate_weight()
    elif choice==3:
          calculate_Temperature()
    elif choice==4:
          calculate_Time()
    elif choice==5:
          print("Thanks for using our service\n Please visit again, Good bye")
          break
    else:
          print("please enter a valid option")