from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api_handler():
    data = request.json  # מקבל את המידע שנשלח אליך
    response = {"status": "success", "message": "Received!", "data": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
