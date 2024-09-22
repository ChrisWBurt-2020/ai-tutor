import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_lesson_content(subject, topic):
       prompt = f"Create a comprehensive lesson on {topic} for the subject {subject}."

       try:
           response = openai.Completion.create(
               engine="text-davinci-003",
               prompt=prompt,
               max_tokens=1500,
               n=1,
               stop=None,
               temperature=0.7,
           )
           content = response.choices[0].text.strip()
           return content
       except Exception as e:
           # Handle exceptions such as API errors
           print(f"Error generating lesson content: {e}")
           return "Sorry, we couldn't generate the lesson content at this time."

def evaluate_code(code, subject, topic):
    prompt = f"As an expert in {subject}, evaluate the following code for the topic '{topic}'. Provide feedback and suggestions for improvement.\n\nCode:\n{code}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    feedback = response.choices[0].text.strip()
    return feedback

def answer_question(question, subject):
    prompt = f"As an AI tutor specializing in {subject}, answer the following question:\n\n{question}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    return answer
