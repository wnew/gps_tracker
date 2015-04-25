import os
import socket
import sys
import logging

config_file_path = "./gps_tracker.conf"

conf_file = open(config_file_path, 'r')


class Config():
    gps_poll_time=30
    def __init__(self, poll_time):
        self.gps_poll_time = poll_time;


class GpsTrackerServer():


    def __init__(self):
        self.config = Config(30)
        self.config.gps_poll_time=30
        self.logger = logging.getLogger('gps_server')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('gps_server.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)


    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = ('localhost', 10000)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        self.logger.debug('starting up on %s port %s' % server_address)
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)

        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        self.connection, self.client_address = self.sock.accept()
   
    def listen(self):
        try:
            print >>sys.stderr, 'connection from', self.client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = self.connection.recv(100)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    self.connection.sendall(data)
                else:
                    print >>sys.stderr, 'no more data from', self.client_address
                    break
                
        finally:
            # Clean up the connection
            self.connection.close()


    def read_config(self):
        pass

    def push_config(self):
        pass

if __name__ == "__main__":
    tracker = GpsTrackerServer()
    print tracker.config.gps_poll_time
    tracker.start_server()
    tracker.listen()
