users_info = {}

def age_category(age):
    if 3 <= age <= 12:
        return "child"
    elif 13 <= age <= 19:
        return "teenager"
    elif 20 <= age <= 39:
        return "young adult"
    elif 40 <= age <= 64:
        return "middle aged"
    elif age >= 65:
        return "senior"
    else:
        return "unknown"

while True:
    if len(users_info) == 10:
        print("Limit reached. Stopping input.")
        break

    # --- NAME VALIDATION ---
    while True:
        name = input("Enter name (or type 'STOP' to quit): ").strip()
        
        if name.lower() == "stop":
            print("Stopping input...")
            break
        
        if name == "":
            print("Name cannot be empty.")
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")
        else:
            break

    if name.lower() == "stop":
        break

    # --- AGE VALIDATION ---
    while True:
        age_input = input("Enter age: ").strip()

        if not age_input.isdigit():
            print("Age must be a valid number.")
            continue

        age = int(age_input)
        if age <= 0:
            print("Age must be greater than 0.")
        else:
            break

    # --- GENDER VALIDATION ---
    while True:
        gender = input("Enter gender (male/female/other): ").strip().lower()

        if any(char.isdigit() for char in gender):
            print("Gender cannot contain numbers.")
            continue

        if gender not in ["male", "female", "other"]:
            print("Invalid gender. Choose male, female, or other.")
        else:
            break

    # Categorize age
    category = age_category(age)

    # Store in dictionary
    users_info[name] = [age, category, gender]

print("\nFinal Output:")
print(users_info)
