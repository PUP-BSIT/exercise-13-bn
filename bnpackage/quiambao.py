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
                print("I'm 20 yearss old now.")
            case 2:
                print("Continuosly acquire new skill. While further improving my coding skill.")
            case 3:
                pass
                # Ex: print("Comment -Name")
                # TODO Ynion
                print("Goodluck! -PJ")
                # TODO Delima
                # TODO Kath
            case 4:
                return
