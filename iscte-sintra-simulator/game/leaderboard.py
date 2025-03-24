
import os

class LeaderBoard:
    def __init__(self):
        self.file = "iscte-sintra-simulator/game/scores.txt"
        self.leaderboard = []
        
        
    def load_leaderboard(self):
        """Load the leaderboard from a text file or create it if it doesn't exist."""
        if not os.path.exists(self.file):
            print("File not found")
            return []
        
        # Clear the leaderboard before loading
        self.leaderboard = [] 
        
        with open(self.file, "r") as file:
            lines = file.readlines()
             
        for line in lines:
            if line.strip() == "":
                continue
            name, course, score = line.strip().split(";")
            self.leaderboard.append({"Nome": name, "Curso": course, "Pontuação": int(score)})
        
        return self.leaderboard
    
    def add_to_leaderboard(self, name, course, score):
        """Add a new player's score to the leaderboard file."""
        with open(self.file, "a") as file:
            file.write(f"{name};{course};{score}\n")
    
    def save_leaderboard(self):
        """Sort and print the top 10 players without overwriting the file."""
        # Sort the leaderboard by score in descending order
        self.leaderboard.sort(key=lambda x: x["Pontuação"], reverse=True)
        
        # Print the top 10
        for idx, entry in enumerate(self.leaderboard[:10], start=1):
            print(f"{idx}. {entry['Nome']} ({entry['Curso']}) — {entry['Pontuação']} pontos")
                
    def get_leaderboard(self):
        
        # Load the leaderboard
        self.load_leaderboard()
        if not self.leaderboard:
            print("Leaderboard is empty!")
        
        self.save_leaderboard()
        
        return self.leaderboard

        y_offset = 300  # Initialize y_offset for text placement

        # Draw top 10 leaderboard entries
        