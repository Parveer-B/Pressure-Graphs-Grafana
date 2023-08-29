from flask import *

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST']) #route for the route '/' (normal 127.0.0.1 or localhost:5000) and we are allowed get and post request methods
def postCSV():
    if request.method == 'POST': #flask.request represents the incoming HTTP request made by a client to your web app
        uploaded_file = request.files.get('file')
        if uploaded_file is not None:
            uploaded_file.save('uploads/' + uploaded_file.filename)
            return 'CSV file uploaded successfully'
        else:
            return 'no file to upload'
    if request.method == 'GET':
        file = send_file('uploads/extorrdata.csv', as_attachment=True)
        return file

@app.route('/', methods=['GET', 'POST']) #route for the route '/' (normal 127.0.0.1 or localhost:5000) and we are allowed get and post request methods
def loadroute():
    if request.method == "GET":
        return 'hi'

"""
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
"""

def create_app():
   return app