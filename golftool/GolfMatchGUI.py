import random
import tkinter as tk
from tkinter import messagebox

class GolfPairingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Golf Pairing App")

        # Create labels and entry fields for player names
        self.label1 = tk.Label(root, text="First player's name:")
        self.entry1 = tk.Entry(root)
        self.label2 = tk.Label(root, text="Second player's name:")
        self.entry2 = tk.Entry(root)
        self.label3 = tk.Label(root, text="Third player's name:")
        self.entry3 = tk.Entry(root)
        self.label4 = tk.Label(root, text="Fourth player's name:")
        self.entry4 = tk.Entry(root)

        # Create a button to generate pairings
        self.generate_button = tk.Button(root, text="Generate Pairings", command=self.generate_pairings)

        # Pack widgets
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()
        self.label4.pack()
        self.entry4.pack()
        self.generate_button.pack()

    def generate_pairings(self):
        # Get player names from entry fields
        player1 = self.entry1.get()
        player2 = self.entry2.get()
        player3 = self.entry3.get()
        player4 = self.entry4.get()

        # Validate input (ensure all fields are filled)
        if not all([player1, player2, player3, player4]):
            messagebox.showerror("Error", "Please enter all player names.")
            return

        # List of players
        players = [player1, player2, player3, player4]
        random.shuffle(players)
        pairs = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]

        # Select a random golf course
        golf_courses = [
            "Big Spring Country Club",
            "Woodhaven Country Club",
            "Oxmoor Country Club",
            "Crescent Hill Golf Course",
            "Shelby County Country Club",
            "Oldham County Country Club",
            "Polo Fields",
            "Lake Forest",
            "Persimmon Ridge",
        ]
        selected_course = random.choice(golf_courses)

        # Display results
        result_text = f"You will play at: {selected_course}\n\n"
        for pair in pairs:
            result_text += f"Pair: {pair[0]} and {pair[1]}\n"

        # Show results in a message box
        messagebox.showinfo("Pairings", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GolfPairingApp(root)
    root.mainloop()