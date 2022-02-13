from task_manager import app


if __name__ == "__main__":
    app.run(debug=True, port=5000, load_dotenv=True)
