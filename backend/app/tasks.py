# app/tasks.py
from app import create_app
from app.ai_engine import evaluate_code
from app import db
from app.models import User, Feedback, Progress, Lesson

app = create_app()
celery = app.celery

@celery.task
def evaluate_code_task(code, user_id, subject, topic):
    feedback = evaluate_code(code, subject, topic)
    user = User.query.get(user_id)

    # Store feedback
    new_feedback = Feedback(
        user_id=user_id,
        subject=subject,
        topic=topic,
        code=code,
        feedback_text=feedback
    )
    db.session.add(new_feedback)

    # Get or create the lesson
    lesson = Lesson.query.filter_by(subject=subject, topic=topic).first()
    if not lesson:
        # Create a dummy lesson if it doesn't exist
        lesson = Lesson(subject=subject, topic=topic, content='')
        db.session.add(lesson)
        db.session.commit()

    # Update user progress
    progress = Progress.query.filter_by(user_id=user_id, lesson_id=lesson.id).first()
    if progress:
        progress.attempts += 1
        if feedback.lower().startswith('correct') or feedback.lower().startswith('great job'):
            progress.completed = True
    else:
        progress = Progress(
            user_id=user_id,
            lesson_id=lesson.id,
            attempts=1,
            completed=feedback.lower().startswith('correct') or feedback.lower().startswith('great job')
        )
        db.session.add(progress)

    db.session.commit()
    return feedback
