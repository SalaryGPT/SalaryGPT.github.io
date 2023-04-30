from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = "your_openai_api_key_here"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    offer_letter = data['offerLetter']
    prompt = f"Calculate the take-home monthly salary (CTC-bonus-variable components) from this offer letter and follow the new Indian tax regime and form 16/16A: {offer_letter}"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50, n=1, stop=None, temperature=0.5)
    generated_text = response.choices[0].text.strip()
    # Assuming the generated text is a number, you might need to parse the response to get the desired output.
    take_home_monthly_amount = float(generated_text)
    return jsonify({'takeHomeMonthlyAmount': take_home_monthly_amount})

if __name__ == '__main__':
    app.run(debug=True)
