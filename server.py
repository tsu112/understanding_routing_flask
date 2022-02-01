from flask import Flask
app = Flask(__name__)

# 1.
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# 2.
# @app.route('/dojo')
# def dojo():
#     return 'Dojo!'

# 3.
# @app.route('/say/<name>')
# def say_name(name):
#     return f'Hi {name.capitalize()}!'

# 4


@app.route('/repeat/<int:num>/<string:word>')
def say_word(num, word):
    output = ''

    for i in range(0, num):
        output += f"<p>{word}</p>"

    return output


if __name__ == "__main__":
    app.run(debug=True)
