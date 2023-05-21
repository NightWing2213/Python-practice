import optparse
import socket
from socket import *
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('violentPython\r\n')
        results = connSkt.recv(100)
        print("[+]%d/tcp open"% tgtPort)
        print("[+] " + str(results))
        connSkt.close()
    except:
        print("[-]%d/tcp closed"% tgtPort)
    def portScan(tgtHost, tgtPorts):
        try:
            tgtIP = gethostbyname(tgtHost)
        except:
            print("[-] Cannot resolve '%s': Unknown host" %tgtHost)
            return
        try:
            tgtName = gethostbyaddr(tgtIP)
            print("\n[+] Scan Results for: " + tgtName[0])
        except:
            print("\n[+] Scan Result for: " + tgtIP)
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
            print("Scanning Port " + tgtPort)
            connScan(tgtHost, int(tgtPort))

def main():
    parser = optparse.OptionParser("usage%prog "+ "-H <target host> -p <target port>")
    parser.add_option("-H", dest="tgtHst", type='string', help="Specify target host")
    parser.add_option('-p', dest='tgtPrt', type='string', help="Specify target port")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')
    if(tgtHost == None) | (tgtPorts[0] == None):
        print("[-] You must specify a target host and port[s].")
        exit(0)
    
if __name__=="__main__":
    main()