import enum
from ctypes import c_int32, c_ubyte, c_uint32, c_ushort, Structure, Union

# From: https://github.com/OpenLightingProject/libartnet/blob/master/artnet
#    packets.h (mostly)
#    common.h (a few constants)
# See also http://artisticlicence.com/WebSiteMaster/User%20Guides/art-net.pdf

ARTNET_MAX_PORTS = 4
ARTNET_SHORT_NAME_LENGTH = 18
ARTNET_LONG_NAME_LENGTH = 64
ARTNET_REPORT_LENGTH = 64
ARTNET_DMX_LENGTH = 512
ARTNET_RDM_UID_WIDTH = 6
ARTNET_MAC_SIZE = 6
ARTNET_ESTA_SIZE = 2
ARTNET_IP_SIZE = 4

ARTNET_MAX_RDM_ADCOUNT = 32
ARTNET_MAX_UID_COUNT = 200

# according to the rdm spec, this should be 278 bytes
# we'll set to 512 here, the firmware datagram is still bigger
ARTNET_MAX_RDM_DATA = 512
ARTNET_FIRMWARE_SIZE = 512


class ErrorCodes(enum.IntEnum):
    ARTNET_EOK = 0
    ARTNET_ENET = -1  # network error
    ARTNET_EMEM = -2  # memory error
    ARTNET_EARG = -3  # argument error
    ARTNET_ESTATE = -4  # state error
    ARTNET_EACTION = -5  # invalid action


class artnet_packet_type(enum.IntEnum):
    ARTNET_POLL = 0x2000
    ARTNET_REPLY = 0x2100
    ARTNET_DMX = 0x5000
    ARTNET_ADDRESS = 0x6000
    ARTNET_INPUT = 0x7000
    ARTNET_TODREQUEST = 0x8000
    ARTNET_TODDATA = 0x8100
    ARTNET_TODCONTROL = 0x8200
    ARTNET_RDM = 0x8300
    ARTNET_VIDEOSTEUP = 0xa010
    ARTNET_VIDEOPALETTE = 0xa020
    ARTNET_VIDEODATA = 0xa040
    ARTNET_MACMASTER = 0xf000
    ARTNET_MACSLAVE = 0xf100
    ARTNET_FIRMWAREMASTER = 0xf200
    ARTNET_FIRMWAREREPLY = 0xf300
    ARTNET_IPPROG = 0xf800
    ARTNET_IPREPLY = 0xf900
    ARTNET_MEDIA = 0x9000
    ARTNET_MEDIAPATCH = 0x9200
    ARTNET_MEDIACONTROLREPLY = 0x9300


artnet_packet_type_t = c_ushort


class artnet_poll_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('ttm', c_ubyte),
        ('pad', c_ubyte),
    ]


class artnet_reply_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('ip', c_ubyte * 4),
        ('port', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('subH', c_ubyte),
        ('sub', c_ubyte),
        ('oemH', c_ubyte),
        ('oem', c_ubyte),
        ('ubea', c_ubyte),
        ('status', c_ubyte),
        ('etsaman', c_ubyte * 2),
        ('shortname', c_ubyte * ARTNET_SHORT_NAME_LENGTH),
        ('longname', c_ubyte * ARTNET_LONG_NAME_LENGTH),
        ('nodereport', c_ubyte * ARTNET_REPORT_LENGTH),
        ('numbportsH', c_ubyte),
        ('numbports', c_ubyte),
        ('porttypes', c_ubyte * ARTNET_MAX_PORTS),
        ('goodinput', c_ubyte * ARTNET_MAX_PORTS),
        ('goodoutput', c_ubyte * ARTNET_MAX_PORTS),
        ('swin', c_ubyte * ARTNET_MAX_PORTS),
        ('swout', c_ubyte * ARTNET_MAX_PORTS),
        ('swvideo', c_ubyte),
        ('swmacro', c_ubyte),
        ('swremote', c_ubyte),
        ('sp1', c_ubyte),
        ('sp2', c_ubyte),
        ('sp3', c_ubyte),
        ('style', c_ubyte),
        ('mac', c_ubyte * ARTNET_MAC_SIZE),
        ('filler', c_ubyte * 32),
    ]


class artnet_ipprog_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('OpCode', c_ushort),
        ('ProVerH', c_ubyte),
        ('ProVer', c_ubyte),
        ('Filler1', c_ubyte),
        ('Filler2', c_ubyte),
        ('Command', c_ubyte),
        ('Filler4', c_ubyte),
        ('ProgIpHi', c_ubyte),
        ('ProgIp2', c_ubyte),
        ('ProgIp1', c_ubyte),
        ('ProgIpLo', c_ubyte),
        ('ProgSmHi', c_ubyte),
        ('ProgSm2', c_ubyte),
        ('ProgSm1', c_ubyte),
        ('ProgSmLo', c_ubyte),
        ('ProgPortHi', c_ubyte),
        ('ProgPortLo', c_ubyte),
        ('Spare1', c_ubyte),
        ('Spare2', c_ubyte),
        ('Spare3', c_ubyte),
        ('Spare4', c_ubyte),
        ('Spare5', c_ubyte),
        ('Spare6', c_ubyte),
        ('Spare7', c_ubyte),
        ('Spare8', c_ubyte),
    ]


class artnet_ipprog_reply_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('OpCode', c_ushort),
        ('ProVerH', c_ubyte),
        ('ProVer', c_ubyte),
        ('Filler1', c_ubyte),
        ('Filler2', c_ubyte),
        ('Filler3', c_ubyte),
        ('Filler4', c_ubyte),
        ('ProgIpHi', c_ubyte),
        ('ProgIp2', c_ubyte),
        ('ProgIp1', c_ubyte),
        ('ProgIpLo', c_ubyte),
        ('ProgSmHi', c_ubyte),
        ('ProgSm2', c_ubyte),
        ('ProgSm1', c_ubyte),
        ('ProgSmLo', c_ubyte),
        ('ProgPortHi', c_ubyte),
        ('ProgPortLo', c_ubyte),
        ('Spare1', c_ubyte),
        ('Spare2', c_ubyte),
        ('Spare3', c_ubyte),
        ('Spare4', c_ubyte),
        ('Spare5', c_ubyte),
        ('Spare6', c_ubyte),
        ('Spare7', c_ubyte),
        ('Spare8', c_ubyte),
    ]


class artnet_address_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('shortname', c_ubyte * ARTNET_SHORT_NAME_LENGTH),
        ('longname', c_ubyte * ARTNET_LONG_NAME_LENGTH),
        ('swin', c_ubyte * ARTNET_MAX_PORTS),
        ('swout', c_ubyte * ARTNET_MAX_PORTS),
        ('subnet', c_ubyte),
        ('swvideo', c_ubyte),
        ('command', c_ubyte),
    ]


class artnet_dmx_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('sequence', c_ubyte),
        ('physical', c_ubyte),
        ('universe', c_ushort),
        ('lengthHi', c_ubyte),
        ('length', c_ubyte),
        ('data', c_ubyte * ARTNET_DMX_LENGTH),
    ]


class artnet_input_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('numbportsH', c_ubyte),
        ('numbports', c_ubyte),
        ('input', c_ubyte * ARTNET_MAX_PORTS),
    ]


class artnet_todrequest_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('spare1', c_ubyte),
        ('spare2', c_ubyte),
        ('spare3', c_ubyte),
        ('spare4', c_ubyte),
        ('spare5', c_ubyte),
        ('spare6', c_ubyte),
        ('spare7', c_ubyte),
        ('spare8', c_ubyte),
        ('command', c_ubyte),
        ('adCount', c_ubyte),
        ('address', c_ubyte * ARTNET_MAX_RDM_ADCOUNT),
    ]


class artnet_toddata_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('rdmVer', c_ubyte),
        ('port', c_ubyte),
        ('spare1', c_ubyte),
        ('spare2', c_ubyte),
        ('spare3', c_ubyte),
        ('spare4', c_ubyte),
        ('spare5', c_ubyte),
        ('spare6', c_ubyte),
        ('spare7', c_ubyte),
        ('spare8', c_ubyte),
        ('cmdRes', c_ubyte),
        ('address', c_ubyte),
        ('uidTotalHi', c_ubyte),
        ('uidTotal', c_ubyte),
        ('blockCount', c_ubyte),
        ('uidCount', c_ubyte),
        ('tod', c_ubyte * ARTNET_MAX_UID_COUNT * ARTNET_RDM_UID_WIDTH),
    ]


class artnet_firmware_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('type', c_ubyte),
        ('blockId', c_ubyte),
        ('length', c_ubyte * 4),
        ('spare', c_ubyte * 20),
        ('data', c_ushort * ARTNET_FIRMWARE_SIZE),
    ]


class artnet_todcontrol_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('spare1', c_ubyte),
        ('spare2', c_ubyte),
        ('spare3', c_ubyte),
        ('spare4', c_ubyte),
        ('spare5', c_ubyte),
        ('spare6', c_ubyte),
        ('spare7', c_ubyte),
        ('spare8', c_ubyte),
        ('cmd', c_ubyte),
        ('address', c_ubyte),
    ]


class artnet_rdm_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('rdmVer', c_ubyte),
        ('filler2', c_ubyte),
        ('spare1', c_ubyte),
        ('spare2', c_ubyte),
        ('spare3', c_ubyte),
        ('spare4', c_ubyte),
        ('spare5', c_ubyte),
        ('spare6', c_ubyte),
        ('spare7', c_ubyte),
        ('spare8', c_ubyte),
        ('cmd', c_ubyte),
        ('address', c_ubyte),
        ('data', c_ubyte * ARTNET_MAX_RDM_DATA),
    ]


class artnet_firmware_reply_t(Structure):
    _fields_ = [
        ('id', c_ubyte * 8),
        ('opCode', c_ushort),
        ('verH', c_ubyte),
        ('ver', c_ubyte),
        ('filler1', c_ubyte),
        ('filler2', c_ubyte),
        ('type', c_ubyte),
        ('spare', c_ubyte * 21),
    ]


class artnet_packet_union_t(Union):
    _fields_ = [
        ('ap', artnet_poll_t),
        ('ar', artnet_reply_t),
        ('aip', artnet_ipprog_t),
        ('addr', artnet_address_t),
        ('admx', artnet_dmx_t),
        ('ainput', artnet_input_t),
        ('todreq', artnet_todrequest_t),
        ('toddata', artnet_toddata_t),
        ('firmware', artnet_firmware_t),
        ('firmwarer', artnet_firmware_reply_t),
        ('todcontrol', artnet_todcontrol_t),
        ('rdm', artnet_rdm_t),
    ]


# http://man7.org/linux/man-pages/man7/ip.7.html
class in_addr(Structure):
    _fields_ = [('s_addr', c_uint32)]


# a packet, containing data, length, type and a src/dst address
class artnet_packet_t(Structure):
    _fields_ = [
        ('length', c_int32),
        ('from', in_addr),
        ('to', in_addr),
        ('type', artnet_packet_type_t),
        ('data', artnet_packet_union_t),
    ]
