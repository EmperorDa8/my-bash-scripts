from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    # Ensure our port matches the PORT environment variable for Cloud Run
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
