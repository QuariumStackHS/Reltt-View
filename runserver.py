"""
This script runs the RELTT_Editor application using a development server.
"""
import threading
from os import environ
import sys
import time

from cfg import *
if __name__ == '__main__':
    db.create_all()
    app.run(HOST, PORT,debug=True)
    
