from flask import request, jsonify
from app.models import Lesson
from app import db
from app.api import bp
from app.ai_engine import generate_lesson_content

@bp.route('/lessons/<subject>/<topic>', methods=['GET'])
def get_lesson(subject, topic):
    lesson = Lesson.query.filter_by(subject=subject, topic=topic).first()
    if lesson is None:
        content = generate_lesson_content(subject, topic)
        lesson = Lesson(subject=subject, topic=topic, content=content)
        db.session.add(lesson)
        db.session.commit()
    return jsonify({
        'subject': lesson.subject,
        'topic': lesson.topic,
        'content': lesson.content
    }), 200
