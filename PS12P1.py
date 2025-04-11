# Assign 10 last names and salaries to parallel arrays
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
salaries = [55000, 62000, 48000, 71000, 53000, 59000, 60000, 58000, 65000, 54000]

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

# Function to display last names and salaries
def display_names_and_salaries(names, salaries):
    print("Employee Names and Salaries:")
    for name, salary in zip(names, salaries):
        print(f"{name}: ${salary}")

# Function to find and display the employee with the highest salary
def find_highest_paid(names, salaries):
    max_salary = max(salaries)
    index = salaries.index(max_salary)
    print(f"\nHighest Paid Employee: {names[index]} with a salary of ${max_salary}")

# Function to sum and display total of all salaries
def display_total_salaries(salaries):
    total = sum(salaries)
    print(f"\nTotal of All Salaries: ${total}")

# Function to repeatedly ask the user for a name and show salary
def search_employee(names, salaries):
    while True:
        search_name = input("\nEnter employee last name to search (or type 'exit' to quit): ").strip()
        if search_name.lower() == 'exit':
            break
        if search_name in names:
            index = names.index(search_name)
            print(f"{search_name}: ${salaries[index]}")
        else:
            print("Employee Not Found")

# Run all functions
display_names(last_names)
display_names_reverse(last_names)
display_names_and_salaries(last_names, salaries)
find_highest_paid(last_names, salaries)
display_total_salaries(salaries)
search_employee(last_names, salaries)
