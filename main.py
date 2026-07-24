import pandas as pd

# Read the Excel file
employees = pd.read_excel("Employee Datasheet.xlsx", header=1)

# Count total workers
total_workers = (len(employees))

print(f"Total workers: {total_workers}")

print(employees.columns)

# Count available workers
available_workers = len(employees[employees["Available"] == "O"])

print(f"Available workers: {available_workers}")

# Print the first employee and all their details
print("\nFirst employee:")
print(employees.iloc[0])