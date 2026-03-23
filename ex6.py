studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
print("Original student list:")
for name in studentNames:
    print(f"{name} Evans")
new_name = input("Please enter a new name to add: ")
studentNames.append(new_name)
print("\nUpdated student list:")
for name in studentNames:
    print(f"{name} Evans")
