from flask import Flask, send_from_directory, Response
import os
from datetime import datetime
import time

app = Flask(__name__)

react_folder = 'streaming-tutorial'
directory= os.getcwd()+ f'/{react_folder}/build/static'


@app.route('/')
def index():
    ''' User will call with with thier id to store the symbol as registered'''
    path= os.getcwd()+ f'/{react_folder}/build'
    print(path)
    return send_from_directory(directory=path,path='index.html')

#
@app.route('/static/<folder>/<file>')
def css(folder,file):
    ''' User will call with with thier id to store the symbol as registered'''
    
    path = folder+'/'+file
    return send_from_directory(directory=directory,path=path)

@app.route('/stream')
def stream():

    def get_data():

        while True:
            #gotcha
            time.sleep(1)
            yield f'data: {datetime.now().second} \n\n'

    return Response(get_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)