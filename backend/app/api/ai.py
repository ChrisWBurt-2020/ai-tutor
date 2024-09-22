# app/api/ai.py
from flask import request, jsonify
from app.api import bp
from app.ai_engine import answer_question

@bp.route('/openai', methods=['POST'])
def openai_assistant():
    data = request.get_json()
    prompt = data.get('prompt')
    subject = data.get('subject', 'General')

    if not prompt:
        return jsonify({'error': 'Prompt is required.'}), 400

    try:
        response = answer_question(prompt, subject)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
