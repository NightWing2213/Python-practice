##This program parses the target hostname and port to scan

import optparse ##parses comman line options

parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>') #create parser
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host') #include tgthost option
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port') #include tgtport option
(options, args) = parser.parse_args
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
    print(parser.usage)
    exit(0)