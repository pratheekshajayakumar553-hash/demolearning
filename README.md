# 📝 To-Do List App

## 📌 About the Project

The To-Do List App is a simple web application built using Python and Flask. It helps users manage their daily tasks easily.

## ✨ Features

* Add new tasks
* View all tasks
* Delete tasks
* Simple and user-friendly interface
* Access through a web browser

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS

## 📂 Project Structure

```text
todo-list-app/
├── app.py
└── README.md
```

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Visit the following address:

```text
http://127.0.0.1:5000
```

## ☁️ AWS Deployment

To run the application on an AWS EC2 instance:

1. Install Python and Flask.
2. Run `python3 app.py`.
3. Allow inbound TCP traffic on port `5000` in the EC2 security group, preferably restricted to your IP for testing.
4. Open `http://YOUR-PUBLIC-IP:5000` in your browser.

## ⚠️ Note

Tasks are stored temporarily in memory. They will be lost when the application restarts.

## 🎯 Future Improvements

* Mark tasks as completed
* Edit existing tasks
* Store tasks in a database
* Add user login and registration

## 👩‍💻 Author

Created as a beginner-friendly Python web development project.
