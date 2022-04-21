'''
- File Name: VAT_function.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 21] File Version 1.0
'''

VAT_rate = 10 # 2020: 10%

# Print menu
def menu():
    print("---------------------Menu---------------------\n")
    print("1. Change Value Added Tax Rate(%)")
    print("2. Calculate Service Price($)")
    print("3. Exit")
    print("----------------------------------------------")

# Change Value Added Tax Rate(%)
def changeVAT():
    global VAT_rate

    print("----------------------------------------------\n")
    print("         [Change Value Added Tax Rate(%)]\n")
    print("Current Value Added Tax Rate(%%): %d\n" %VAT_rate)

    while True:

        try:
            VAT_rate = int(input("Changed Value Added Tax Rate(%): "))
        except ValueError:
            print("\nError: Illegal Selection..\n")
        else:
            print("\nChange complete")
            break
 
    print("----------------------------------------------\n")

# Calculate Service Price($)
def calServicePrice():
    global VAT_rate
    result = 0 # Total service price($)
    price = [23, 40, 67] # a: $23, b: $40, c: $67

    print("----------------------------------------------\n")
    print("         [Calculate Service Price($)]\n")

    while True:
        service = input("Select service(A: $23 / B: $40 / C: $67): ")

        if service == 'A' or service == 'B' or service == 'C':
            break
        else:
            print("\nError: Illegal Selection..\n")

    while True:
        option = input("Would you like to include Value Added Tax(Y/N): ")

        if option == 'Y' or option == 'N':
            break
        else:
            print("\nError: Illegal Selection..\n")

    if service == 'A':
        result = price[0]
    elif service == 'B':
        result = price[1]
    else:
        result = price[2]

    if option == 'Y':
        result *= (1 + VAT_rate / 100)

    result = round(result, 1)

    print(f"\nTotal Service price($): ${result}")