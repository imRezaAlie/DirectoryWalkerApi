import bottle
from bottle import post, get, put
import os
import json
app=application=bottle.default_app()
def ls_files(dir):
    files = list()
    for item in os.listdir(dir):
        abspath = os.path.join(dir, item)
        try:
            if os.path.isdir(abspath):
                files = files + ls_files(abspath)
            else:
                files.append(abspath)
        except FileNotFoundError as err:
            print('invalid directory\n', 'Error: ', err)
    return files

@get('/AllDirectories')
def AllDirectories():
    listis=ls_files("D:/storage/")    
    return listis



if __name__ == '__main__':
    bottle.run(host='127.0.0.1',port='8585')