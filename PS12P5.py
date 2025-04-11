# Function to load player names and batting averages from file
def load_player_data(filename):
    names = []
    averages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    names.append(parts[0])
                    averages.append(float(parts[1]))
    except FileNotFoundError:
        print("File not found.")
    return names, averages

# Function to display players and batting averages
def display_players(names, averages):
    print("Player Batting Averages:")
    for name, avg in zip(names, averages):
        print(f"{name}: {avg:.3f}")

# Function to search for a player by last name with "Name not found" message
def search_player(names, averages):
    while True:
        user_input = input("\nEnter player last name to search (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        if user_input in names:
            index = names.index(user_input)
            print(f"{user_input}: Batting Average = {averages[index]:.3f}")
        else:
            print("Name not found")

# Main Program
file_name = "players.txt"
player_names, batting_averages = load_player_data(file_name)

if player_names and batting_averages:
    display_players(player_names, batting_averages)
    search_player(player_names, batting_averages)
else:
    print("No data available.")
