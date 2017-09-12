import Menu

menu = Menu.db_menu()


def main():
    run_prog = True
    while run_prog:
        show_menu()
        selection = input()
        run(selection)
        more = input("Would you like to continue? (y/n)")
        if more.lower() == 'n':
            print("Shutting down...")
            run_prog = False

def show_menu():
    print('-' * 20)
    print('1 ------ Create Table (Auto Generated)')
    print('2 ------ Add New Entry')
    print('3 ------ Update Entry')
    print('4 ------ Delete Entry')
    print('5 ------ Show Table')
    print('6 ------ Show Entry')
    print('7 ------ Test: Drop Table :Test')
    print('-' * 20)
    print("Select a menu option by typing the corresponding number: ")

def run(choice):

    if choice == '1':
        menu.create()
    elif choice == '2':
        menu.add()
    elif choice == '3':
        menu.update()
    elif choice == '4':
        menu.delete()
    elif choice == '5':
        menu.display_all()
    elif choice == '6':
        menu.show_entry()
    elif choice == '7':
        menu.delete_table()
    else:
        menu.close_db()
        print("Shutting down...")
        exit()

main()
