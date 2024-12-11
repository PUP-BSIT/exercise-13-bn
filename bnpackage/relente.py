def patricia_relente():
    print("Hi everyone! I am Patricia Joy Relente")
    
    while True:
        print("1. About me")
        print("2. Goal")
        print("3. About my cat")
        print("4. Back")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("I am PJ, a 2nd-year DIT Student from PUP-Taguig Campus.") 
                print("I love petting my cat because it relieves my stress.")
            case 2:
                print("Goal: To have a happy and meaningful life")
            case 3:
                print("About my cat")
                print("> Frico is a 2-year-old tuxedo cat")
                print("> He loves Chimken.")
            case 4:
                return
            case _:
                print("Invalid choice. Please try again.")

patricia_relente()