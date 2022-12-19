# https://kytta.medium.com/tcp-packets-from-scratch-in-python-3a63f0cd59fe
import array
import socket
import struct

###################
###### Input ######
###################
source_ip = "192.168.1.119"
source_port = 4443

dst_ip = "192.168.1.119"
dst_port = 4444

flag = 0b000101001
###################

def chksum(packet: bytes) -> int:
    if len(packet) % 2 != 0:
        packet += b'\0'

    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff

def createTcpPacket(src_host, src_port, dst_host, dst_port, flags = 0):
    packet = struct.pack(
        '!HHIIBBHHH',
        src_port,  # Source Port
        dst_port,  # Destination Port
        0,              # Sequence Number
        0,              # Acknoledgement Number
        5 << 4,         # Data Offset        
        flags,     # Flags
        8192,           # Window
        0,              # Checksum (initial value)
        0               # Urgent pointer
    )

    pseudo_hdr = struct.pack(
        '!4s4sHH',
        socket.inet_aton(src_host),    # Source Address
        socket.inet_aton(dst_host),    # Destination Address
        socket.IPPROTO_TCP,                 # PTCL
        len(packet)                         # TCP Length
    )

    checksum = chksum(pseudo_hdr + packet)

    packet = packet[:16] + struct.pack('H', checksum) + packet[18:]

    return packet

pak = createTcpPacket(source_ip,source_port,dst_ip,dst_port,flag)

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

s.sendto(pak, (dst_ip, 0))
