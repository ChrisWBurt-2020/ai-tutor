# app/api/evaluate.py
from flask import request, jsonify
from app.api import bp
from app.ai_engine import evaluate_code

@bp.route('/evaluate_code', methods=['POST'])
def evaluate_code_endpoint():
    data = request.get_json()
    code = data.get('code')
    subject = data.get('subject', 'Programming')
    topic = data.get('topic', 'General')

    if not code:
        return jsonify({'error': 'Code is required.'}), 400

    try:
        feedback = evaluate_code(code, subject, topic)
        return jsonify({'feedback': feedback}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
