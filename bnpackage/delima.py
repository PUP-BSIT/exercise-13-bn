def justine_delima():
    user_choice = 0

    while user_choice != 4:
        print("Nice to know you! I am Justine Delima")
        print('[1] Basic Information')
        print('[2] Goals')
        print('[3] Comments')
        print('[4] Back')
        user_choice = int(input("Enter your choice: "))

        match user_choice:
            case 1: #  Basic Info
                print('\nAge: 19')
                print('Birthdate: February 24, 2005')
                print('Current School Attended: Polytechnic University of the Philippines-Taguig\n')
            case 2: # Goal
                print('\nGoal: To have a stable life.\n')
            case 3: # Comments
                print("Goodluck to your journey! - Bea")
                print("Nice Menu -PJ")
                print("Keep up the good work! - Patricia")
                print("Good job! - Kath")
            case 4: # Exit
                print('\nGoodbye!\n')
                return