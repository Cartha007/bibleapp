from flask import Flask, render_template, redirect, url_for, flash, request
import json

app = Flask(__name__)



# Load Bible data
with open(file_path, 'r') as file:
            self.data = json.load(file)






if __name__ == "__main__":
    app.run(debug=True)