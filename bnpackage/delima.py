def justine_delima():
    user_choice = 0

    while user_choice != 4:
        print("Nice to know you! I am Justine Delima")
        print('[1] Basic Information')
        print('[2] Goals')
        print('[3] Comments')
        print('[4] Exit')
        user_choice = int(input("Enter your choice: "))

        match user_choice:
            case 1: #  Basic Info
                print('\nAge: 19')
                print('Birthdate: February 24, 2005')
                print('Current School Attended: Polytechnic University of the Philippines-Taguig\n')
            case 2: # Goal
                print('\nGoal: To have a stable life.\n')
            case 3: # Comments
                pass
                # Ex: print("Comment -Name")
                # TODO Ynion
                # TODO Patricia Joy
                # TODO Patricia Anne
                # TODO Kath
            case 4: # Exit
                print('\nGoodbye!\n')
                return