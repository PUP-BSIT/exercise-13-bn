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
                citron.kathleen_citron()
            case 2:
                delima.justine_delima()
            case 3:
                quiambao.patricia_quiambao()
            case 4:
                relente.patricia_relente()
            case 5:
                ynion.ynion_mabeamae()
            case 6: 
                break

menu()