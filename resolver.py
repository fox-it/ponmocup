import fileinput
import zlib
import socket

def convertIpv4ToInt( ipStr ):
	parts = ipStr.split('.')
	ip = (int(parts[3]) << 24) + (int(parts[2]) << 16) + (int(parts[1]) << 8) + int(parts[0])
	return ip & 0xFFFFFFFF

def convertIntToIpv4( ip ):
	retn = list()
	while ip:
		octet = ip & 0xFF
		ip >>= 8
		retn.append(str(octet))
	return ".".join(retn)

def resolvePonmocupIp( dns ):
	crc = zlib.crc32( dns ) & 0xFFFFFFFF
	#print "crc:",hex(crc)

	#if( dns == "claimsreference.net"):
	#	ipstr = "110.20.225.47" #hack in test IP
	#else:
	ipstr = socket.gethostbyname( dns )
	#print "ipstr:",ipstr

	dnsIp = convertIpv4ToInt( ipstr )
	#print "dnsip:",hex(dnsIp),"|",convertIntToIpv4(dnsIp)

	cncIp = crc ^ dnsIp
	#print "cncIp:",hex(cncIp),"|",convertIntToIpv4(cncIp)

	return convertIntToIpv4(cncIp)

print "DNS CNCIP"
for line in fileinput.input():
	line = line.rstrip()
	try:
		print line, resolvePonmocupIp( line )
	except ValueError:
		print line, "error in script"

###Example test case
#resolvePonmocupIp("claimsreference.net")
