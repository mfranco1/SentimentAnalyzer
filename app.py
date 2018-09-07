from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/senti/api/v1/GetAllSenti', methods=['GET'])
def get_all_senti():
    pass

@app.route('/')
def index():
    pass

if __name__ == "__main__":
    app.run(debug=True)
