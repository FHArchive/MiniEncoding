"""Ascii Bytes representations. Stores ascii as a bitarray in ascii8 form
"""

from bitstring import BitArray


class AsciiBytes:
	"""Ascii Bytes representations. Stores ascii as a bitarray in ascii8 form
	"""
	def __init__(self):
		self.bitarray = BitArray()

	####################################################################
	# CONVERT TO ASCII8
	####################################################################

	def fromAscii8(self, ascii8bytes):
		"""Convert from a regular stream of ascii8 chars to a stream of
		ascii chars e.g. AA (0b01000001 01000001)

		Args:
			ascii8bytes (bytes): an array of ascii8 bytes
		"""
		self.bitarray = BitArray(ascii8bytes)

	def fromAscii7(self, ascii7bytes):
		"""Convert from a stream of ascii7 chars to a stream of
		ascii chars e.g.
		AA + padding (0b10000011 00000100) -> AA (0b01000001 01000001)

		Args:
			ascii7bytes (bytes): an array of ascii7 bytes
		"""
		self.bitarray = BitArray()
		ascii7bits = BitArray(ascii7bytes)
		for char in range(0, len(ascii7bits) // 7):
			self.bitarray.append(bytes([ascii7bits[char * 7:(char+1) * 7].uint]))

	def fromDecSixBit(self, ascii6bytes):
		"""Convert from a stream of ascii6 chars to a stream of
		ascii chars e.g.
		AA + padding (0b10000110 00010000) -> AA (0b01000001 01000001)

		Args:
			ascii6bytes (bytes): an array of ascii6 bytes
		"""
		self.bitarray = BitArray()
		ascii6bits = BitArray(ascii6bytes)
		for char in range(0, len(ascii6bits) // 6):
			self.bitarray.append(bytes([ascii6bits[char * 6:(char+1) * 6].uint + 0x20]))

	def fromICL(self, ascii6bytes):
		"""Convert from a stream of ascii6 chars to a stream of
		ascii chars e.g.
		AA + padding (0b10000110 00010000) -> AA (0b01000001 01000001)

		Args:
			ascii6bytes (bytes): an array of ascii6 bytes
		"""
		self.bitarray = BitArray()
		ascii6bits = BitArray(ascii6bytes)
		for char in range(0, len(ascii6bits) // 6):
			charAsInt = ascii6bits[char * 6:(char+1) * 6].uint
			if charAsInt < 0x10:
				charAsInt += 0x30 # 0x30 <= ascii < 0x40
			elif charAsInt < 0x20:
				charAsInt += 0x10 # 0x20 <= ascii < 0x30
			else:
				charAsInt += 0x20 # 0x40 <= ascii
			self.bitarray.append(bytes([charAsInt]))

	def fromSixBitAscii(self, ascii6bytes):
		"""Convert from a stream of ascii6 chars to a stream of
		ascii chars e.g.
		AA + padding (0b00000100 00010000) -> AA (0b01000001 01000001)

		Args:
			ascii6bytes (bytes): an array of ascii6 bytes
		"""
		self.bitarray = BitArray()
		ascii6bits = BitArray(ascii6bytes)
		for char in range(0, len(ascii6bits) // 6):
			charAsInt = ascii6bits[char * 6:(char+1) * 6].uint
			if charAsInt < 0x20:
				charAsInt += 0x40 # 0x40 <= ascii < 0x60
			self.bitarray.append(bytes([charAsInt]))

	####################################################################
	# CONVERT FROM ASCII8
	####################################################################

	def toAscii8(self):
		"""Convert from the internal ascii representation to ascii8
		e.g. AA (0b01000001 01000001)

		Returns:
			bytes: an array of ascii8 bytes
		"""
		return self.bitarray.tobytes()

	def toAscii7(self):
		"""Convert from the internal ascii representation to ascii7
		e.g.
		AA (0b01000001 01000001) -> AA + padding (0b10000011 00000100)

		Returns:
			bytes: an array of ascii7 bytes
		"""
		ascii7bits = BitArray()
		for char in self.bitarray.tobytes():
			if char >= 0x80: # out of 7 bits range
				char = 0x3f # '?'
			ascii7bits.append(BitArray(bytes([char]))[1:])
		return ascii7bits.tobytes()

	def toDecSixBit(self, ignorecase=True):
		"""Convert from the internal ascii representation to ascii6
		e.g.
		AA (0b01000001 01000001) -> AA + padding (0b10000110 00010000)

		Returns:
			bytes: an array of ascii6 bytes
		"""
		ascii6bits = BitArray()
		chars = self.bitarray.tobytes()
		if ignorecase:
			chars = chars.upper()
		for char in chars:
			char -= 0x20
			if not (0 <= char < 0x40): # out of 6 bits range
				char = 0x1f # '?'
			ascii6bits.append(BitArray(bytes([char]))[2:])
		return ascii6bits.tobytes()

	def toICL(self, ignorecase=True):
		"""Convert from the internal ascii representation to ascii6
		e.g.
		AA (0b01000001 01000001) -> AA + padding (0b10000110 00010000)

		Returns:
			bytes: an array of ascii6 bytes
		"""
		ascii6bits = BitArray()
		chars = self.bitarray.tobytes()
		if ignorecase:
			chars = chars.upper()
		for char in chars:
			if 0x30 <= char < 0x40:
				char -= 0x30
			elif 0x20 <= char < 0x30:
				char -= 0x10
			else:
				char -= 0x20
			if not (0 <= char < 0x40): # out of 6 bits range
				char = 0xf # '?'
			ascii6bits.append(BitArray(bytes([char]))[2:])
		return ascii6bits.tobytes()

	def toSixBitAscii(self, ignorecase=True):
		"""Convert from the internal ascii representation to ascii6
		e.g.
		AA (0b01000001 01000001) -> AA + padding (0b00000100 00010000)

		Returns:
			bytes: an array of ascii6 bytes
		"""
		ascii6bits = BitArray()
		chars = self.bitarray.tobytes()
		if ignorecase:
			chars = chars.upper()
		for char in chars:
			if 0x40 <= char < 0x60 or char < 0x20: # We don't want acsii8 < 0x20
				char -= 0x40
			if not (0 <= char < 0x40): # out of 6 bits range
				char = 0x3f # '?'
			ascii6bits.append(BitArray(bytes([char]))[2:])
		return ascii6bits.tobytes()
