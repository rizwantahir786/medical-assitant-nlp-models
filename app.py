from flask import Flask, request, jsonify
from transformers import BartForConditionalGeneration, BartTokenizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained("./finetuned_bart_medical")
tokenizer = BartTokenizer.from_pretrained("./finetuned_bart_medical")

def generate_response(user_input):
    # Check for greetings and return hardcoded responses
    greetings = ["hi", "hello", "hey", "greetings", "good day"]
    if user_input.lower() in greetings:
        return "Hello! How can I assist you?"

    # If not a greeting, use the model to generate a response
    input_tensor = tokenizer.encode(user_input, return_tensors="pt")
    output_tensor = model.generate(input_tensor, max_length=150, num_beams=5, early_stopping=True)
    response = tokenizer.decode(output_tensor[0], skip_special_tokens=True)
    return response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print("Received data:", data)
    prompt = data["prompt"]
    response = generate_response(prompt)
    print("Sending response:", response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  
