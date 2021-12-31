from flask import Flask, send_from_directory, Response
import os
import datetime

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


if __name__ == '__main__':
    app.run(debug=True)