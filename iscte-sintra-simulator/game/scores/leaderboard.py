import os

class LeaderBoard:
    def __init__(self):
        self.file = "scores.txt"
        self.leaderboard = []
        
    def load_leaderboard(self):
        """Load the leaderboard from a text file or create it if it doesn't exist."""
        if not os.path.exists(self.file):
            return []
         
        with open(self.file, "r") as file:
            lines = file.readlines()
             
        for line in lines:
            if line.strip() == "":
                continue
            name, course, score = line.strip().split(";")
            self.leaderboard.append({"Nome": name, "Curso": course, "Pontuação": int(score)})
        
        return self.leaderboard
    
    def save_leaderboard(self, leaderboard):
        """Save all scores to the file and print top 10."""
        # Sort the leaderboard by score in descending order
        leaderboard.sort(key=lambda x: x["Pontuação"], reverse=True)
        
        # Save all scores to the file
        with open(self.file, "w") as file:
            for entry in leaderboard:
                file.write(f"{entry['Nome']};{entry['Curso']};{entry['Pontuação']}\n")
        
        # Print the top 10
        print("🏆 Top 10 Players:")
        for idx, entry in enumerate(leaderboard[:10], start=1):
            print(f"{idx}. {entry['Nome']} ({entry['Curso']}) — {entry['Pontuação']} pontos")
            
    def show_leaderboard: