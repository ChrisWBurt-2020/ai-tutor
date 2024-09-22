import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_lesson_content(subject, topic):
    prompt = f"Provide a detailed lesson on {topic} in {subject}. Include examples and explanations suitable for a beginner."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )
    lesson_content = response.choices[0].text.strip()
    return lesson_content

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
