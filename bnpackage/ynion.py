def ynion_mabeamae():
    
    choice = 0
    
    while choice != 4:
        print("\nHello! I'm Ma. Bea Mae Ynion")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("\nDate of Birth : July 29, 2004")
                print("Age : 20")
                print("Email : mabeamaeynion@gmail.com")
                print("Religion : Roman Catholic")
            case 2:
                print("\nGoals: To learn more about programming and improve my problem-solving skills.")
            case 3:
                print("\nComments")
                #TODO DELIMA
                print("Keep up the good work <3 -PJ")
                #TODO QUIAMBAO
                #TODO CITRON
            case 4:
                print("\nExit.")
                return
            