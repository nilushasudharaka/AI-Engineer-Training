from src.llm_client import create_client
from src.assistant import TextAssistant


def main():

    print("=" * 60)
    print("AI TEXT ASSISTANT")
    print("=" * 60)

    try:
        client = create_client()

        assistant = TextAssistant(client)

        while True:

            print("\nSelect an operation:")
            print("1. Question Answering")
            print("2. Summarization")
            print("3. Rewriting")
            print("4. Extract Entities (JSON)")
            print("5. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                question = input("\nEnter your question:\n")
                answer = assistant.answer_question(question)
                print("\n--- Answer ---")
                print(answer)

            elif choice == "2":
                text = input("\nEnter text to summarize:\n")
                summary = assistant.summarize(text)
                print("\n--- Summary ---")
                print(summary)

            elif choice == "3":
                text = input("\nEnter text to rewrite:\n")
                rewritten = assistant.rewrite(text)
                print("\n--- Rewritten Text ---")
                print(rewritten)

            elif choice == "4":
                text = input("\nEnter text to extract entities from:\n")
                entities = assistant.extract_entities(text)
                print("\n--- Extracted Entities (JSON) ---")
                print(entities)

            elif choice == "5":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid choice. Please select 1, 2, 3, 4, or 5.")

    except Exception as error:

        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()