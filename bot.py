from flask import Flask, request, jsonify
import spam_call_detection  # Import your spam detection logic
import fraud_detection  # Import your fraud detection logic

app = Flask(__name__)

@app.route('/check_spam', methods=['POST'])
def check_spam():
    phone_number = request.json.get('phone_number')
    result = spam_call_detection.detect(phone_number)
    return jsonify(result)

@app.route('/check_fraud', methods=['POST'])
def check_fraud():
    transaction_details = request.json.get('transaction_details')
    result = fraud_detection.detect(transaction_details)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
