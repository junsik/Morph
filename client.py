import os
import sys
import config
import argparse
from common import *
from xmlrpclib import ServerProxy

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input video file', required=True)
    parser.add_argument('-s', '--resolution', help='resolutions of the output video file', required=True)

    #parser.add_argument('-s', '--resolution', nargs='*', help='resolutions of the output video file', required=True)
    #parser.add_argument('-o', '--output', help='output video file', required=True)
    args = parser.parse_args()
    input_file = args.input
    resolution = args.resolution
    file_path  = ''
    width      = ''
    height     = ''

    if os.path.isfile(input_file) == False:
        print 'error: input file does not exist'
        sys.exit(-1)
    else:
        file_path = input_file

    r = resolution.split('x')
    if len(r) != 2:
        print 'error: resolution format is wrong'
        sys.exit(-1)

    width = r[0]
    height = r[1]

    if width.isdigit() == False or height.isdigit() == False:
        print 'error: resolution format is wrong'
        sys.exit(-1)


    master_ip       = config.master_ip
    master_rpc_port = config.master_rpc_port
    rpc_addr = "http://" + master_ip + ":" + master_rpc_port
    server = ServerProxy(rpc_addr)

    #please replace it with the program command line
    width     = "%04d" % int(width)
    height    = "%04d" % int(height)

    key = server.add_trans_task(file_path, "", width, height)
    print key




