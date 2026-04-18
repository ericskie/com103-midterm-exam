# 1. Ask for player details
ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

# 2. Hero Roster using a 2D List
heroes = [
    ["Layla", "Marksman"],
    ["Tigreal", "Tank"],
    ["Gusion", "Assassin"],
    ["Kagura", "Mage"],
    ["Chou", "Fighter"]
]

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

# Display roster using a loop
for i in range(len(heroes)):
    print(f" {i+1}. {heroes[i][0]:<10} [{heroes[i][1]}]")

print("==========================================\n")

# Initialize tracking variables
match_history = []
wins = 0
losses = 0
matches_played = 0
best_kda = -1.0
best_match_info = ""
