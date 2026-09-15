from flask import Flask, request 
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

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    student_id = request.form['student_id']
    assignment_mark = float(request.form['assignment'])
    exam_mark = float(request.form['exam'])
    total_score = (assignment_mark * 0.4) + (exam_mark * 0.6)

    if total_score >= 80:
        grade='HD'
    elif total_score >= 70:
        grade='D'
    elif total_score >= 60:
        grade='C'
    elif total_score >= 50:
        grade='P'
    else:
        grade='F'

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
                text-align: center;
            }}

            .result {{
                border: 1px solid #ccc;
                padding: 25px;
                margin-top: 20px;
            }}

            a {{
                display: block;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body>

        <h1>{APP_NAME}</h1>

        <div class="result">

            <h2>Grade Result</h2>

            <p><strong>Student:</strong> {name}</p>

            <p><strong>Student ID:</strong> {student_id}</p>

            <p><strong>Assignment:</strong> {assignment_mark}%</p>

            <p><strong>Exam:</strong> {exam_mark}%</p>

            <p><strong>Overall:</strong> {total_score:.1f}%</p>

            <h2>Grade: {grade}</h2>

        </div>

        <a href="/">Calculate another grade</a>

    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)