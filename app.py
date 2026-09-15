from flask import Flask 
import os

app = Flask(__name__)
APP_NAME = os.environ.get("APP_NAME", "Student Grade Tracker")

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
            }}

            h1 {{
                text-align: center;
            }}

            input {{
                width: 100%;
                padding: 10px;
                margin: 8px 0 15px;
                box-sizing: border-box;
            }}

            button {{
                width: 100%;
                padding: 12px;
                cursor: pointer;
            }}

            .info {{
                margin-top: 20px;
                padding: 15px;
                border: 1px solid #ccc;
            }}
        </style>
    </head>

    <body>

        <h1>{APP_NAME}</h1>

        <form action="/calculate" method="post">

            <label>Student Name</label>
            <input type="text" name="name" required>

            <label>Student ID</label>
            <input type="text" name="student_id" required>

            <label>Assignment Mark (%)</label>
            <input type="number" name="assignment" min="0" max="100" required>

            <label>Exam Mark (%)</label>
            <input type="number" name="exam" min="0" max="100" required>

            <button type="submit">Calculate Grade</button>

        </form>

    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)