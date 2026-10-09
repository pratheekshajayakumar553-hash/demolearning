
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My To-Do App</title>
    <style>
        body {
            font-family: Arial;
            background: #eaf2ff;
            text-align: center;
            padding: 40px;
        }
        .box {
            background: white;
            padding: 25px;
            max-width: 450px;
            margin: auto;
            border-radius: 15px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        li {
            text-align: left;
            margin: 15px;
        }
        a {
            color: red;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>My To-Do List 📝</h1>
        <form action="/add" method="post">
            <input name="task" placeholder="Enter your task" required>
            <button>Add Task</button>
        </form>
        <h3>My Tasks</h3>
        <ul>
        {% for task in tasks %}
            <li>
                {{ task }}
                <a href="/delete/{{ loop.index0 }}">Delete</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    tasks.append(request.form["task"])
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)