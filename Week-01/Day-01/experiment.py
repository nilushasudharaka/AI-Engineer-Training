class AIService:
    def generate_response(self, user_message):
        """
        Simulates an AI model response.
        """

        if not user_message.strip():
            return "Please provide a message."

        return f"AI Response: I received your message: '{user_message}'"


def main():
    # Get user input
    user_message = input("User: ")

    # Create AI service
    ai_service = AIService()

    # Generate response
    response = ai_service.generate_response(user_message)

    # Display response
    print(response)


if __name__ == "__main__":
    main()