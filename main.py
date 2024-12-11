from bnpackage import citron, delima, quiambao, relente, ynion

def menu():
    choice = 0

    while choice != 6:
        print("===== BN GROUP =====")
        print("1 - Kathleen Citron")
        print("2 - Justine Delima")
        print("3 - Ma. Patricia Anne Quiambao")
        print("4 - Patricia Joy Relente")
        print("5 - Ma. Bea Mae Ynion")
        print("6 - Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                relente.patricia_relente()
            case 5:
                pass
            case 6: 
                break

menu()