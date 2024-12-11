def kathleen_citron ():

    choice = 0

    while choice != 4:

        print(f"Hello! My name is Kathleen C. Citron")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                print(f"i like vegetables.")
                print(f"i'm 19 years old.")
                pint(f"i love playing online games.")

            case 2:
                print(f"my goal is to be a successful person.")
                print(f"improving my codingg skills.")
            case 3:
                print(f"opinionsss:")
            case 4:
                return