import os
from rumus import Cylinder, Sphere, RectangularPrism, Cube, Cone

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice():
    print("\n == SELAMAT DATANG DI PROGRAM RUMUS VOLUME ==")
    print("Created by: Arif Pandu Hidayatulloh | 22030001")
    print("==============================================")
    print("\nSilahkan pilih opsi yang ingin dijalankan:")
    print("1. Tabung")
    print("2. Bola")
    print("3. Balok")
    print("4. Kubus")
    print("5. Kerucut")
    print("6. Keluar\n")

def main():
    while True:
        clear_screen()
        choice()
        user_choice = input("Masukkan pilihan Anda: ")

        if user_choice == '1':
            radius = float(input("Masukkan jari-jari tabung: "))
            height = float(input("Masukkan tinggi tabung: "))
            tabung = Cylinder(radius, height)
            print(f"\nVolume Tabung: {tabung.volume():.2f}\n")
            input("\nTekan Enter untuk melanjutkan...")

        elif user_choice == '2':
            radius = float(input("Masukkan jari-jari bola: "))
            bola = Sphere(radius)
            print(f"\nVolume Bola: {bola.volume():.2f}\n")
            input("\nTekan Enter untuk melanjutkan...")

        elif user_choice == '3':
            length = float(input("Masukkan panjang balok: "))
            width = float(input("Masukkan lebar balok: "))
            height = float(input("Masukkan tinggi balok: "))
            balok = RectangularPrism(length, width, height)
            print(f"\nVolume Balok: {balok.volume():.2f}\n")
            input("\nTekan Enter untuk melanjutkan...")

        elif user_choice == '4':
            side = float(input("Masukkan panjang sisi kubus: "))
            kubus = Cube(side)
            print(f"\nVolume Kubus: {kubus.volume():.2f}\n")
            input("\nTekan Enter untuk melanjutkan...")

        elif user_choice == '5':
            radius = float(input("Masukkan jari-jari kerucut: "))
            height = float(input("Masukkan tinggi kerucut: "))
            kerucut = Cone(radius, height)
            print(f"\nVolume Kerucut: {kerucut.volume():.2f}\n")
            input("\nTekan Enter untuk melanjutkan...")

        elif user_choice == '6':
            print("\nKeluar dari program.")
            break

        else:
            print("\nPilihan tidak valid, coba lagi.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
