from flask import Flask, render_template, request, jsonify

app = Flask("__name__")

@app.route("/bharat", methods=['POST'])
def test():
    return 'Hello Bharat'

if __name__ == '__main__':
    app.run(debug=True)