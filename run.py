import subprocess
import sys
from flask import Flask
from app import app

def run_bandit_scan():
    result = subprocess.run(["bandit", "-r", ".", "--exclude", "run.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        raise Exception("Security vulnerabilities detected. Check the output above.")

def run_linter():
    result = subprocess.run(["pylint", "app.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        raise Exception("Linting issues detected. Check the output above.")

if __name__ == "__main__":
    run_bandit_scan()  # Run Bandit security check
    run_linter()  # Run linter for code analysis
    app.run(debug=False)
