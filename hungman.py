import tkinter as tk
from tkinter import messagebox
import random

# Word list
words = ['PYTHON', 'TKINTER', 'HANGMAN', 'DEVELOPER', 'PROGRAMMING']
word = random.choice(words)
guessed_word = ['_' for _ in word]
attempts = 6

def reset_game():
    global word, guessed_word, attempts
    word = random.choice(words)
    guessed_word = ['_' for _ in word]
    attempts = 6
    update_display()

def check_letter():
    global attempts
    letter = entry.get().upper()
    entry.delete(0, tk.END)
    
    if letter and letter.isalpha() and len(letter) == 1:
        if letter in word:
            for index, char in enumerate(word):
                if char == letter:
                    guessed_word[index] = letter
        else:
            attempts -= 1
    
    update_display()
    check_game_status()

def update_display():
    word_label.config(text=' '.join(guessed_word))
    attempts_label.config(text=f'Attempts left: {attempts}')

def check_game_status():
    if '_' not in guessed_word:
        messagebox.showinfo("Hangman", "Congratulations! You won!")
        reset_game()
    elif attempts == 0:
        messagebox.showinfo("Hangman", f"Game Over! The word was: {word}")
        reset_game()

# GUI Setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x450")
root.configure(bg="#222")

header_label = tk.Label(root, text="Hangman Game", font=('Arial', 22, 'bold'), fg="white", bg="#222")
header_label.pack(pady=15)

word_label = tk.Label(root, text=' '.join(guessed_word), font=('Arial', 26, 'bold'), fg="yellow", bg="#222")
word_label.pack(pady=10)

entry = tk.Entry(root, font=('Arial', 16), justify='center', width=5)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_letter, font=('Arial', 14, 'bold'), bg="#28a745", fg="white", width=10)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_game, font=('Arial', 14, 'bold'), bg="#dc3545", fg="white", width=10)
reset_button.pack(pady=5)

attempts_label = tk.Label(root, text=f'Attempts left: {attempts}', font=('Arial', 14, 'bold'), fg="red", bg="#222")
attempts_label.pack(pady=10)

root.mainloop()