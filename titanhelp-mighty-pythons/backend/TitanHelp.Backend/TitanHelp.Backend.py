from app import create_app
from app.extensions import db

if __name__ == "__main__":
    app = create_app()
    # ensure tables exist when running the server
    with app.app_context():
        db.create_all()

    app.run(host="127.0.0.1", port=5000, debug=True)

