from generator import generate_answer


def main():

    print("=" * 60)
    print("GEMINI RAG QUESTION ANSWERING SYSTEM")
    print("=" * 60)

    print("\nAsk a question about the documents.")
    print("Type 'exit' to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":

            print("Goodbye!")
            break

        try:

            answer, context = generate_answer(question)

            print("\nRetrieved Context:")
            print("-" * 60)
            print(context)

            print("\nGenerated Answer:")
            print("-" * 60)
            print(answer)

            print()

        except Exception as error:

            print("\nAn error occurred:")
            print(error)


if __name__ == "__main__":
    main()