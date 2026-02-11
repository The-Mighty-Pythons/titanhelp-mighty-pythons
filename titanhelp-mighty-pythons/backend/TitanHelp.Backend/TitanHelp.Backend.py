from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for development (allow Vite frontend)
CORS(app, origins=["http://localhost:5173"])

@app.route("/test")
def test():
    return {"message": "CORS is working!"}

if __name__ == "__main__":
    app.run(debug=True)
