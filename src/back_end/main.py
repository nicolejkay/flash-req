import os
from flask import Flask
template_dir = os.path.abspath('../../frontend/src/templates')
app = Flask(__name__, template_folder=template_dir)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)