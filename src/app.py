from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return '''
    <title>Flask Home </title>
    <h1>This is The Home Page Flask</h1>
    '''

@app.route("/hello/<string:i>")
def helloWorld(i):
    return ( 'Hello ' + i )

if (__name__ == "__main__"):
    app.run(debug=True,host='0.0.0.0')
