from google import genai

client = genai.Client()

def ask_cypher(query):
    try:
        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=query
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, my AI system is temporarily unavailable. Please try again."


if __name__ == "__main__":
    print("CYPHER is online.")

    question = input("You: ")
    answer = ask_cypher(question)

    print("CYPHER:", answer)