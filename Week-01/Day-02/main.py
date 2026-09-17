import json

from config import APP_NAME, DEFAULT_ROLE, MAX_USERS
from user_processor import UserProcessor


def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("Error: Name cannot be empty.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if age <= 0:
                print("Error: Age must be greater than 0.")
                continue

            return age

        except ValueError:
            print("Error: Please enter a valid number.")


def get_role():
    role = input(f"Enter your role [{DEFAULT_ROLE}]: ").strip()

    if not role:
        return DEFAULT_ROLE

    return role


def save_to_json(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    print("=" * 40)
    print(APP_NAME)
    print("=" * 40)

    processor = UserProcessor(MAX_USERS)

    try:
        number_of_users = int(
            input(f"How many users do you want to enter? (Max {MAX_USERS}): ")
        )

        if number_of_users <= 0:
            raise ValueError("Number of users must be greater than 0.")

        if number_of_users > MAX_USERS:
            raise ValueError(
                f"You cannot enter more than {MAX_USERS} users."
            )

        for i in range(number_of_users):
            print(f"\n--- User {i + 1} ---")

            name = get_valid_name()
            age = get_valid_age()
            role = get_role()

            processor.add_user(name, age, role)

        processed_users = processor.process_users()

        save_to_json(processed_users)

        print("\nProcessing completed successfully!")
        print("\nProcessed Users:")

        for user in processed_users:
            print(
                f"- {user['name']} | "
                f"Age: {user['age']} | "
                f"Role: {user['role']} | "
                f"Group: {user['age_group']}"
            )

        print("\nUnique Roles:")

        for role in processor.get_roles():
            print(f"- {role}")

        print("\nData saved to data.json")

    except ValueError as error:
        print(f"\nInput Error: {error}")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()