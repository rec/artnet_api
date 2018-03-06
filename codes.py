import enum

# See http://artisticlicence.com/WebSiteMaster/User%20Guides/art-net.pdf
# https://github.com/OpenLightingProject/libartnet/tree/master/artnet


class Opcodes(enum.IntEnum):
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


NODE_REPORT_CODES = {
    0x0000: 'RcDebug: Booted in debug mode (Only used in development)',
    0x0001: 'RcPowerOk: Power On Tests successful',
    0x0002: 'RcPowerFail: Hardware tests failed at Power On',
    0x0003: 'RcSocketWr1: Last UDP from Node failed due to truncated length, '
            'Most likely caused by a collision.',
    0x0004: 'RcParseFail: Unable to identify last UDP transmission. '
            'Check OpCode and packet length.',
    0x0005: 'RcUdpFail: Unable to open Udp Socket in last transmission attempt',
    0x0006: 'RcShNameOk: Confirms that Short Name programming via ArtAddress, '
            'was successful.',
    0x0007: ('RcLoNameOk: Confirms that Long Name programming via ArtAddress, '
             'was successful.'),
    0x0008: 'RcDmxError: DMX512 receive errors detected.',
    0x0009: 'RcDmxUdpFull: Ran out of internal DMX transmit buffers.',
    0x000a: 'RcDmxRxFull: Ran out of internal DMX Rx buffers.',
    0x000b: 'RcSwitchErr: Rx Universe switches conflict.',
    0x000c: 'RcConfigErr: Product configuration does not match firmware.',
    0x000d: 'RcDmxShort: DMX output short detected. See GoodOutput field.',
    0x000e: 'RcFirmwareFail: Last attempt to upload new firmware failed.',
    0x000f: ('RcUserFail: User changed switch settings when address locked by '
             'remote programming. User changes ignored.'),
    0x0010: 'RcFactoryRes: Factory reset has occurred.',
}
