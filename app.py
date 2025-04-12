from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['data']
    # Your Python logic here
    d = pd.date_range(user_input, periods=30)
    df = pd.DataFrame(np.random.randn(30,50), index=d)
    result_html = df.to_html()
    result = f"<h2>Processed Data:</h2> {result_html}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
