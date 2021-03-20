
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test_get')
def index_test_get():
    return 'test get is finished!!'

@app.route('/test_post', methods=['POST'])
def index_test_post():
    insertValues = request.get_json()
    value = insertValues['value']
    return jsonify({'return': str(value)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)