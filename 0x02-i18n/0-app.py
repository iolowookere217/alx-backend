#!/usr/bin/env python3
"""This moduke sets up a basic Flask app"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    """This function defines a route for the root URL ('/')"""
    return render_template("0-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5080")
