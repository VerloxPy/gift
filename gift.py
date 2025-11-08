from flask import Flask, render_template, request

app = Flask(__name__)

num = 4


@app.route('/', methods=['GET', 'POST'])
def index():
    global num
    if request.method == 'POST':
        num += 1
        return render_template('index.html', num=num)

    return render_template('index.html', num=num)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
