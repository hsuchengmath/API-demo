from app import app


@app.route('/')
def index():
    return 'setting finish!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)