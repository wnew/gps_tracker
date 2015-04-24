import os

config_file_path = "./gps_tracker.conf"

conf_file = open(config_file_path, 'r')


class config():
    gps_poll_time=30
    def __init__(self, poll_time):
        self.gps_poll_time = poll_time;


class gps_tracker_server():

    config = config(30)
    new_config = 0;

    def __init__(self):
        config.gps_poll_time=30
        #
    def read_config(self):
        print 'x'

    def push_config(self):
        print 'x'

if __name__ == "__main__":
    tracker = gps_tracker_server()
    print tracker.config.gps_poll_time

