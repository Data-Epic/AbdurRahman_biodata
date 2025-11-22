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

    name = input("Enter name (or type 'STOP' to quit): ").strip()
    if name.lower() == "stop":
        break

    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    category = age_category(age)

    users_info[name] = [age, category, gender]

print("\nFinal Output:")
print(users_info)