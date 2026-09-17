class UserProcessor:
    def __init__(self, max_users):
        self.max_users = max_users
        self.users = []

    def add_user(self, name, age, role):
        if len(self.users) >= self.max_users:
            raise ValueError("Maximum number of users reached.")

        user = {
            "name": name,
            "age": age,
            "role": role
        }

        self.users.append(user)

    def calculate_age_group(self, age):
        if age < 18:
            return "Minor"
        elif age < 30:
            return "Young Adult"
        elif age < 60:
            return "Adult"
        else:
            return "Senior"

    def process_users(self):
        processed_users = []

        for user in self.users:
            processed_user = user.copy()
            processed_user["age_group"] = self.calculate_age_group(
                user["age"]
            )

            processed_users.append(processed_user)

        return processed_users

    def get_roles(self):
        return set(user["role"] for user in self.users)