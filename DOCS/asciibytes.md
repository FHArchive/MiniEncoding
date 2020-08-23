Module miniencoding.asciibytes
==============================
Ascii Bytes representations. Stores ascii as a bitarray in ascii8 form

Classes
-------

`AsciiBytes()`
:   Ascii Bytes representations. Stores ascii as a bitarray in ascii8 form

    ### Methods

    `fromAscii7(self, ascii7bytes)`
    :   Convert from a stream of ascii7 chars to a stream of
        ascii chars e.g.
        AA + padding (0b10000011 00000100) -> AA (0b01000001 01000001)
        
        Args:
                ascii7bytes (bytes): an array of ascii7 bytes

    `fromAscii8(self, ascii8bytes)`
    :   Convert from a regular stream of ascii8 chars to a stream of
        ascii chars e.g. AA (0b01000001 01000001)
        
        Args:
                ascii8bytes (bytes): an array of ascii8 bytes

    `fromDecSixBit(self, ascii6bytes)`
    :   Convert from a stream of ascii6 chars to a stream of
        ascii chars e.g.
        AA + padding (0b10000110 00010000) -> AA (0b01000001 01000001)
        
        Args:
                ascii6bytes (bytes): an array of ascii6 bytes

    `fromICL(self, ascii6bytes)`
    :   Convert from a stream of ascii6 chars to a stream of
        ascii chars e.g.
        AA + padding (0b10000110 00010000) -> AA (0b01000001 01000001)
        
        Args:
                ascii6bytes (bytes): an array of ascii6 bytes

    `fromSixBitAscii(self, ascii6bytes)`
    :   Convert from a stream of ascii6 chars to a stream of
        ascii chars e.g.
        AA + padding (0b00000100 00010000) -> AA (0b01000001 01000001)
        
        Args:
                ascii6bytes (bytes): an array of ascii6 bytes

    `toAscii7(self)`
    :   Convert from the internal ascii representation to ascii7
        e.g.
        AA (0b01000001 01000001) -> AA + padding (0b10000011 00000100)
        
        Returns:
                bytes: an array of ascii7 bytes

    `toAscii8(self)`
    :   Convert from the internal ascii representation to ascii8
        e.g. AA (0b01000001 01000001)
        
        Returns:
                bytes: an array of ascii8 bytes

    `toDecSixBit(self, ignorecase=True)`
    :   Convert from the internal ascii representation to ascii6
        e.g.
        AA (0b01000001 01000001) -> AA + padding (0b10000110 00010000)
        
        Returns:
                bytes: an array of ascii6 bytes

    `toICL(self, ignorecase=True)`
    :   Convert from the internal ascii representation to ascii6
        e.g.
        AA (0b01000001 01000001) -> AA + padding (0b10000110 00010000)
        
        Returns:
                bytes: an array of ascii6 bytes

    `toSixBitAscii(self, ignorecase=True)`
    :   Convert from the internal ascii representation to ascii6
        e.g.
        AA (0b01000001 01000001) -> AA + padding (0b00000100 00010000)
        
        Returns:
                bytes: an array of ascii6 bytes