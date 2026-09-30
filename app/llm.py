import ollama


def generate_answer(context, question):
    prompt = f"""
You are an AI document question-answering assistant.

Answer the user's question using ONLY the information provided in the context.

Context:
{context}

Question:
{question}

If the answer is not available in the context, say:
"I could not find this information in the document."

Answer clearly and concisely.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]