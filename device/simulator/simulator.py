import os
import socket
import sys
import logging
import time
import threading


class GpsTrackerDeviceSimulator():

    def __init__(self):
        self.logger = logging.getLogger('gps_server')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('gps_server.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)


    def connect_to_server(self, server='localhost', port=10000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = (server, port)
        self.sock.connect(server_address)
        print >>sys.stderr, 'connected to %s on port %s' % server_address
        self.logger.debug('connected to %s on port %s' % server_address)
        self.sock.send('hello')


if __name__ == "__main__":
    from optparse import OptionParser
 
    p = OptionParser()
    p.set_usage('gps_tracker.py -p <port>')
    p.set_description(__doc__)
    p.add_option('-p', '--port', dest='port', type=int,
        help='port on which to connect to server')
    p.add_option('-s', '--server', dest='server', type=str,
        help='target server')
    opts, args = p.parse_args(sys.argv[1:])
 
    tracker = GpsTrackerDeviceSimulator()
    tracker.connect_to_server(server='localhost', port=opts.port)
