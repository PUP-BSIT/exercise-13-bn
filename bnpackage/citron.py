def kathleen_citron ():

    choice = 0

    while choice != 4:

        print("Hello! My name is Kathleen C. Citron")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments")
        print("4. Back")
        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                print("I like vegetables.")
                print("I'm 19 years old.")
                print("I love playing online games.")

            case 2:
                print("My goal is to be a successful person.")
                print("Improving my coding skills.")
            case 3:
                print("Opinions:")
                print("You don't like vegetables -PJ")
                print("You like online games - Bea")
            case 4:
                return            