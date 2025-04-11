# Load data from file into parallel arrays
def load_data_from_file(filename):
    last_names = []
    scores = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name = parts[0]
                    score = int(parts[1])
                    last_names.append(name)
                    scores.append(score)
    except FileNotFoundError:
        print("File not found.")
    return last_names, scores

# Function to display all names and scores
def display_names_and_scores(names, scores):
    print("Student Scores:")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

# Function to find and display highest score
def display_highest_score(names, scores):
    high_var = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
    print(f"\nHighest Score: {names[high_index]} with {high_var}")

# Function to find and display lowest score
def display_lowest_score(names, scores):
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Lowest Score: {names[low_index]} with {low_var}")

# Main program
file_name = "students.txt"
last_names, scores = load_data_from_file(file_name)

if last_names and scores:
    display_names_and_scores(last_names, scores)
    display_highest_score(last_names, scores)
    display_lowest_score(last_names, scores)
else:
    print("No data to display.")
