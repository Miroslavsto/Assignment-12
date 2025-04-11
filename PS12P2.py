# Parallel arrays: last names, salaries, and exam scores
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
salaries = [55000, 62000, 48000, 71000, 53000, 59000, 60000, 58000, 65000, 54000]
exam_scores = [88, 92, 75, 85, 79, 90, 83, 78, 91, 87]

# Function to display names
def display_names(names):
    print("Employee Last Names:")
    for name in names:
        print(name)

# Function to display names in reverse order
def display_names_reverse(names):
    print("Employee Last Names (Reverse Order):")
    for name in reversed(names):
        print(name)

# Function to display last names, salaries, and exam scores
def display_all_info(names, salaries, scores):
    print("Employee Info (Name - Salary - Exam Score):")
    for name, salary, score in zip(names, salaries, scores):
        print(f"{name}: ${salary}, Exam Score: {score}")

# Function to find and display the employee with the highest salary
def find_highest_paid(names, salaries):
    max_salary = max(salaries)
    index = salaries.index(max_salary)
    print(f"\nHighest Paid Employee: {names[index]} with a salary of ${max_salary}")

# Function to sum and display total of all salaries
def display_total_salaries(salaries):
    total = sum(salaries)
    print(f"\nTotal of All Salaries: ${total}")

# Function to search for an employee by last name
def search_employee(names, salaries, scores):
    while True:
        search_name = input("\nEnter employee last name to search (or type 'exit' to quit): ").strip()
        if search_name.lower() == 'exit':
            break
        if search_name in names:
            index = names.index(search_name)
            print(f"{search_name}: Salary = ${salaries[index]}, Exam Score = {scores[index]}")
        else:
            print("Employee Not Found")

# Run all functions
display_names(last_names)
display_names_reverse(last_names)
display_all_info(last_names, salaries, exam_scores)
find_highest_paid(last_names, salaries)
display_total_salaries(salaries)
search_employee(last_names, salaries, exam_scores)
