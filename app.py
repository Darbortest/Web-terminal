# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Sta?e
SSH_PASSWORD = "clico123!"
SSH_USERNAME = "Student"
SSH_HOST = "10.9.2.102"

def execute_command(command):
    # Przygotowanie pe?nej komendy z u?yciem sshpass
    full_command = 'sshpass -p {} ssh {}@{} "powershell {}"'.format(SSH_PASSWORD, SSH_USERNAME, SSH_HOST, command)

    try:
        # Wykonanie komendy
        result_bytes = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result_bytes
    except subprocess.CalledProcessError as e:
        return "Error: {}".format(e.output)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.form["command"]
    
    # Wywo?anie funkcji execute_command z przekazanym has?em
    result = execute_command(command)
    
    return result

if __name__ == "__main__":
    app.run(debug=True)
