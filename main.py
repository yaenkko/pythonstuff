import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    def show_menu():
        messagebox.showinfo("Game Menu", "1. Start Game\n2. Settings\n3. Quit")

    def show_settings():
        messagebox.showinfo("Game Settings", "Add your settings options here")

    def start_game():
        messagebox.showinfo("Game", "Starting the game...")
        # hier muss das actual game dann rein
        

    def main():
        while True:
            show_menu()
            choice = messagebox.askquestion("Game Menu", "Enter your choice:")

            if choice == "yes":
                start_game()
            elif choice == "no":
                show_settings()
            else:
                messagebox.showerror("Invalid choice", "Please try again.")

    if __name__ == "__main__":
        main()