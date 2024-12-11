def patricia_quiambao():

        choice = 0

        while choice != 4:
        
            print("Hi there! I am Patricia Quiambao ")
            print("1. Basic Info")
            print("2. Goals")
            print("3. Comments")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    print("I'm 20 years old now.")
                case 2:
                    print("Continuously acquire new skill. While further improving my coding skill.")
                case 3:
                    pass
                    # Ex: print("Comment -Name")
                    print("Your Potchi is so cute - Bea")
                    print("Goodluck! -PJ")
                    print("Keep up the good work! -Justine")
                    print("Keep it up! - Kath")
                case 4:
                    return
