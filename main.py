
from tools import book
import os
def main():

    while True:
        # os.system('cls')
        print("========== MENU ==========")
        opsi = int(input(f"Pilih opsi berikut:\n1. Reading List\n2. Watch List\n3. Close Program\nPilih opsi: "))
        if opsi == 1:
            book.start()
        elif opsi == 2:
            pass
        elif opsi == 3:
            print("Program ditutup")
            break
        elif opsi == 4:
            pass


if __name__ == "__main__":
    main()