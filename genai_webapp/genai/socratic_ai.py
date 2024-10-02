# genai_webapp/genai/socratic_ai.py

from openai import OpenAI
client = OpenAI(api_key="")

def socratic_guidance(content):
    """
    Sends content (code or quiz) to the GenAI API using the new chat interface and retrieves Socratic questions.
    """
    try:
        # # Use the newer chat-based API with OpenAI 1.0+
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",  # or "gpt-4" if available
        #     messages=[
        #         {"role": "system", "content": "You are an AI tutor that uses the Socratic method to help users learn."},
        #         {"role": "user", "content": f"Help me understand this content:\n\n{content}"}
        #     ],
        #     max_tokens=500,
        #     temperature=0.7
        # )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are an AI tutor that uses the Socratic method to help users learn."
                )},
                {"role": "user", "content": f"Help me understand this content:\n\n{content}"}
            ]
        )
        ai_message = response.choices[0].message.content        
        
        # Extract the AI-generated Socratic questions
        socratic_questions = ai_message
        
        return socratic_questions

    except Exception as e:
        return f"An error occurred while processing the input: {str(e)}"
