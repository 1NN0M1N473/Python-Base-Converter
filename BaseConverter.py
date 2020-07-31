#Python program to convert between well-known bases
#May add lesser-known bases in the future

#import the stuff i didnt feel like writing
import menu
import time

## Functions first ##

#decimal functions

#decimal to binary function
def decimal_to_binary(dec):
    decimal = int(dec)
    print(decimal, "in Binary(base 2) is", bin(decimal))

#decimal to octal function
def decimal_to_octal(dec):
    decimal = int(dec)
    print(decimal, "in Octal(base 8) is", oct(decimal))

#decimal to hexadecimal function
def decimal_to_hex(dec):
    decimal = int(dec)
    print(decimal, "in Hexadecimal(base 16) is", hex(decimal))

#binary functions

#binary to octal function
def binary_to_octal(bin):
    binary = bin(bin)
    print(binary, "in Octal(base 8) is", oct(binary))

#binary to decimal function
def binary_to_decimal(bin):
    binary = bin(bin)
    print(binary, "in Decimal(base 10) is", int(binary))

#binary to hexadecimal function
def binary_to_hex(bin):
    binary = bin(bin)
    print(binary, "in Hexadecimal(base 16) is", hex(binary))

#octal functions

#octal to binary function
def octal_to_binary(oct):
    octal = oct(oct)
    print(octal, "in Binary(base 2) is", bin(octal))

#octal to decimal funtion
def octal_to_decimal(oct):
    octal = oct(oct)
    print(octal, "in Decimal(base 10) is", int(octal))

#octal to hexadecimal function
def octal_to_hex(oct):
    octal = oct(oct)
    print(octal, "in Hexadecimal(base 16) is", hex(octal))

#hexadecimal functions

#hexadecimal to binary function
def hex_to_binary(hex):
    hexadecimal = hex(hex)
    print(hexadecimal, "in Binary(base 2) is", bin(hexadecimal))

#hexadecimal to octal function
def hex_to_octal(hex):
    hexadecimal = hex(hex)
    print(hexadecimal, "in Octal(base 8) is", oct(hexadecimal))

#hexadecimal to decimal function
def hex_to_decimal(hex):
    hexadecimal = hex(hex)
    print(hexadecimal, "in Decimal(base 10) is", int(hexadecimal))

## Now for the interactive part ##

#Pretty display stuff & menu options
print()
print()
print("+-------------------------------------------------------+")
print("| Welcome to Matt's Lightweight Base Converter Program! |")
print("+-------------------------------------------------------+")
print()
print("Select an operation from the following menu options:")
print()
menu = {}
menu['000']='+----Decimal Conversions----+ 000'
menu['--']=''
menu['1] ']="Decimal to Binary"
menu['2] ']="Decimal to Octal"
menu['3] ']="Decimal to Hexadecimal"
menu['---']=''
menu['001']='+----Binary Conversions----+ 001'
menu['----']=''
menu['4] ']="Binary to Octal"
menu['5] ']="Binary to Decimal"
menu['6] ']="Binary to Hexadecimal"
menu['-----']=''
menu['002']='+----Octal Conversions----+ 002'
menu['------']=''
menu['7] ']="Octal to Binary"
menu['8] ']="Octal to Decimal"
menu['9] ']="Octal to Hexadecimal"
menu['-------']=''
menu['003']='+----Hexadecimal Conversions----+ 003'
menu['--------']=''
menu['10] ']="Hexadecimal to Binary"
menu['11] ']="Hexadecimal to Octal"
menu['12] ']="Hexadecimal to Decimal"
menu['---------']=''
menu['99] ']="Exit the Program"
print()

#loops and shiz, along with if statements to make the menu options actually do somethin
while True:
    options=menu.keys()
    for entry in options:
        print(entry, menu[entry])

    print()
    selection=input("Type your selection: ")
    if selection =='1':
        time.sleep(1)
        print()
        dec = input("OK, enter the number you wish to convert: ")
        print()
        time.sleep(1)
        decimal_to_binary(dec)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' : ")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='2':
        time.sleep(1)
        print()
        dec = input("OK, enter the number you wish to convert: ")
        print()
        time.sleep(1)
        decimal_to_octal(dec)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' : ")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='3':
        time.sleep(1)
        print()
        dec = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        decimal_to_hex(dec)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='4':
        time.sleep(1)
        print()
        bin = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        binary_to_octal(bin)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='5':
        time.sleep(1)
        print()
        bin = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        binary_to_decimal(bin)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='6':
        time.sleep(1)
        print()
        bin = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        binary_to_hex(bin)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='7':
        time.sleep(1)
        print()
        oct = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        octal_to_binary(oct)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='8':
        time.sleep(1)
        print()
        oct = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        octal_to_decimal(oct)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='9':
        time.sleep(1)
        print()
        oct = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        octal_to_hex(oct)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='10':
        time.sleep(1)
        print()
        hex = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        hex_to_binary(hex)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='11':
        time.sleep(1)
        print()
        hex = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        hex_to_octal(hex)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='12':
        time.sleep(1)
        print()
        hex = input("OK, now enter the number you wish to convert: ")
        print()
        time.sleep(1)
        hex_to_decimal(hex)
        print()
        print()
        time.sleep(1)
        prompt = input("Is that all? Type 'yes' or 'no' :")
        if prompt == 'yes':
            print()
            print("OK, thanks for using the program! Bye!")
            time.sleep(1)
            print()
            print()
            break
        elif prompt == 'no':
            print()
            print("OK, here's the menu again.")
            time.sleep(1)
            print()
        else:
            print()
            print("Hmmm....not sure what you mean. Exiting. ")
            time.sleep(1)
            print()
            print()
            break
    elif selection =='99':
        time.sleep(1)
        print("OK, thanks for using the program! Bye!")
        print()
        print()
        break
    else:
        time.sleep(1)
        print()
        print("Now you and I both know that's not a valid option....")
        time.sleep(1)
        print()
    
