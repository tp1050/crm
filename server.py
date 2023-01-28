from flask import Flask , render_template

app=Flask(__name__,instance_relative_config=True)

app.route('/')
def index():
    return 'Dool'


@app.route('/login',methods=['POST', 'GET'])
def login():
    pass

@app.route('/addagent')
def addagent():
    return render_template ('addagent.html')

@app.route('/addcontact')
def addcontact():
    return render_template ('addcontact.html')

@app.route('/login')
def login():
    return render_template ('login.html')

@app.route('/contactview')
def contactview():
    return render_template ('contactview.html')

app.run(host="0.0.0.0",port=7018,debug=True)

