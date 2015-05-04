import os
import socket
import sys
import logging
import time
import threading

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


    def start_server(self, port=10000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = ('', port)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        self.logger.debug('starting up on %s port %s' % server_address)
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)

        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        self.connection, self.client_address = self.sock.accept()
        
        # set to nonblocking mode
        self.connection.setblocking(0)

        self.recv_thread = threading.Thread(target=self._listen, args=(self.connection,))
        self.send_thread = threading.Thread(target=self._send,   args=(self.connection,))

        self.recv_thread.start()
        self.send_thread.start()
   
    def _listen(self, connection):
        print >>sys.stderr, 'connection from', self.client_address

        # Receive the data in small chunks and retransmit it
        while True:
            try:
                data = connection.recv(4096)
                print >>sys.stderr, "%s" % data
            
            except IOError:
                pass

            except Exception:
                print "Other exception....."
                connection.close()
                break

    def _send(self, connection):
       while True:
           try:
               connection.sendall(raw_input() + "\n")

           except Exception:
               print "Send closing connection....."
               connection.close()
               break


    def read_config(self):
        pass

    def push_config(self):
        pass

if __name__ == "__main__":
    from optparse import OptionParser
 
    p = OptionParser()
    p.set_usage('gps_tracker.py -p <port>')
    p.set_description(__doc__)
    p.add_option('-p', '--port', dest='port', type=int,
        help='port on which to listen for client')
    opts, args = p.parse_args(sys.argv[1:])
 
    tracker = GpsTrackerServer()
    tracker.start_server(opts.port)
