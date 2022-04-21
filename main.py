'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 21] File Version 1.0
'''

import VAT_function

while True:
    VAT_function.menu()

    try:
        choice = int(input("\nSelect the menu: "))
    except ValueError:
        print("\nError: Illegal Selection..\n")
    else:
        if choice == 1:
            VAT_function.changeVAT()
        elif choice == 2:
            VAT_function.calServicePrice()
        elif choice == 3:
            exit()
        else:
            print("\nError: Illegal Selection..\n")