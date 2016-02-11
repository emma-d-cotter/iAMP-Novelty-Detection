from struct import *
from pprint import pprint as pp
import socket               # Import socket module


def unpacker(fmt, buff):
    size = calcsize(fmt)
    return unpack(fmt, buff[:size]), buff[size:]


def get_tracks(buffer):
    while len(buffer):
        track, buffer = unpacker('HffffffiHffff', buffer)

        print("id:", track[0])
        print("size:", track[1])
        print("speed:", track[2])
        print("min_range:", track[3])
        print("max_range:", track[4])
        print("min_angle", track[5])
        print("max_angle", track[6])
        print("first ping", track[7])
        print("self.pings_visible", track[8])
        print("range",  track[9])
        print("angle", track[10])
        print("width", track[11])
        print("height", track[12])


if __name__ == "__main__":

    s = socket.socket()         # Create a socket object
    host = 'localhost' # Get local machine name
    port = 5000                # Reserve a port for your service.

    s.connect((host, port))
    while True:
        buf = s.recv(4096)
        get_tracks(buf)
    s.close
