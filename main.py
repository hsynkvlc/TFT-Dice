import tkinter as tk
from tkinter import messagebox
import random

level_probabilities = {
    1: [1.0, 0.0, 0.0, 0.0, 0.0],
    2: [1.0, 0.0, 0.0, 0.0, 0.0],
    3: [0.75, 0.25, 0.0, 0.0, 0.0],
    4: [0.55, 0.30, 0.15, 0.0, 0.0],
    5: [0.45, 0.33, 0.20, 0.02, 0.0],
    6: [0.30, 0.40, 0.25, 0.05, 0.0],
    7: [0.19, 0.35, 0.35, 0.10, 0.01],
    8: [0.18, 0.25, 0.36, 0.18, 0.03],
    9: [0.10, 0.20, 0.25, 0.35, 0.10],
    10: [0.05, 0.10, 0.20, 0.40, 0.25],
    11: [0.01, 0.02, 0.12, 0.50, 0.35],
}

tier_colors = {
    1: "gray",
    2: "green",
    3: "blue",
    4: "pink",
    5: "gold",
}

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        master.title("Dice Roller App")

        self.level = 1
        self.result_label = tk.Label(master, text=f"Level {self.level}: Tier results of the rolled dice:")
        self.result_label.grid(row=0, column=0, columnspan=5)  # grid ile yerleştirildi

        self.probability_label = tk.Label(master, text=self.format_probabilities(level_probabilities[self.level]))
        self.probability_label.grid(row=1, column=0, columnspan=5, pady=10)  # grid ile yerleştirildi

        self.roll_button = tk.Button(master, text="Roll the Dice", command=self.roll_and_display_result)
        self.roll_button.grid(row=2, column=0, columnspan=5, pady=10)  # grid ile yerleştirildi

        self.increase_level_button = tk.Button(master, text="Increase Level", command=self.increase_level)
        self.increase_level_button.grid(row=3, column=0, pady=10)  # grid ile yerleştirildi

        self.decrease_level_button = tk.Button(master, text="Decrease Level", command=self.decrease_level)
        self.decrease_level_button.grid(row=3, column=1, pady=10)  # grid ile yerleştirildi

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=2, pady=10)  # grid ile yerleştirildi

        master.bind('d', lambda event: self.roll_and_display_result())

        self.tier_labels = []

    def roll_dice(self):
        return [random.random() for _ in range(5)]

    def choose_character(self):
        dice_results = self.roll_dice()
        selected_characters = []

        for dice_result in dice_results:
            cumulative_probability = 0
            for tier, probability in enumerate(level_probabilities[self.level], start=1):
                cumulative_probability += probability
                if dice_result <= cumulative_probability:
                    selected_characters.append(tier)
                    break

        return selected_characters

    def roll_and_display_result(self):
        selected_characters = self.choose_character()
        result_text = f"Level {self.level}: Tier results of the rolled dice: {selected_characters}"
        self.result_label.config(text=result_text)
        self.set_tier_colors(selected_characters)

    def increase_level(self):
        if self.level < 11:
            self.level += 1
            self.result_label.config(text=f"Level {self.level}: Tier results of the rolled dice:")
            self.probability_label.config(text=self.format_probabilities(level_probabilities[self.level]))

    def decrease_level(self):
        if self.level > 1:
            self.level -= 1
            self.result_label.config(text=f"Level {self.level}: Tier results of the rolled dice:")
            self.probability_label.config(text=self.format_probabilities(level_probabilities[self.level]))

    def set_tier_colors(self, selected_characters):
        # Temizleme işlemi
        for label in self.tier_labels:
            label.destroy()
        self.tier_labels = []

        # Yatay olarak etiketleri yerleştirme
        for i, tier in enumerate(selected_characters):
            label = tk.Label(self.master, text=f"Tier {tier}", fg="white", bg=tier_colors[tier])
            label.grid(row=4, column=i, padx=5, pady=5)
            self.tier_labels.append(label)

    def format_probabilities(self, probabilities):
        return "Probabilities: " + ", ".join([f"{prob * 100}%" for prob in probabilities])

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
