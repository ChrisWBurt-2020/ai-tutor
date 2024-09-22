import sys
import os

# Print current working directory and Python path for debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

try:
    from app import create_app

    from app import create_app, db
    from app.models import User, Lesson
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Lesson': Lesson}

if __name__ == '__main__':
    app.run(debug=True)