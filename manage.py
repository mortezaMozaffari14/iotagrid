#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import zmq

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # context = zmq.Context()
    # socket = context.socket(zmq.SUB)
    # socket.connect('tcp://localhost:5556')
    # socket.subscribe('tx')
    # print ("Socket connected")
    # #while True:
    # print ("Waiting for events from the IOTA node")
    # print(socket)
    # message = socket.recv()
    # # if(message):
    # #     data = message.split()
    # #     print ("Transaction confirmed by milestone index: ", data[1])
    # #     print ("Transaction hash: ", data[2])
    

    execute_from_command_line(sys.argv)

    

if __name__ == '__main__':
    main()

    
