from app import app, db  # Replace 'your_flask_app' with your actual script name without '.py'

with app.app_context():
    db.create_all()
    print("Database created successfully!")
