from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    feedback = request.form['feedback']
    prompt = f"""
    you are sentiment classification model refer below example and classify feedback into 'p' or 'n' category return only category in output
    feedback: what a lovely product
    sentiment: p
    feedback: fuck your product
    sentiment: n
    feedback: {feedback}
    sentiment:
    """
    response = model.generate_content(prompt)
    sentiment = response.text if response else "Error"

    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
