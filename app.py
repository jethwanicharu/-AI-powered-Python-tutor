from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")

def get_ai_response(user_input):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly AI tutor helping children learn Python."},
            {"role": "user", "content": user_input}
        ]
    )
    return completion.choices[0].message.content

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.json
    user_input = data.get("question", "")
    response = get_ai_response(user_input)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)

