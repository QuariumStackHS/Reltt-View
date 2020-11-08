from RELTT_Editor.dbAPI import * 
from RELTT_Editor import *
from os import environ
HOST = environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555
