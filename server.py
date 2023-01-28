from flask import Flask

app=Flask(__name__,instance_relative_config=True)

app.route('/')
def index():
    return 'Dool'


@app.route('login',method=['POST', 'GET'])
def login():
    pass

@app.route('/addcontact')


app.run(host="0.0.0.0",port=7018,debug=True)

