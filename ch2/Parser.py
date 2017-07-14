import optparse
parser = optparse.OptionParser('usage %prog -H' + \
                               '<target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', \
                  help='speciry target host')
parser.add_option('-p', dest='tgtPort', type='int', \
                  help='specify target port')
(option, arge) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)
