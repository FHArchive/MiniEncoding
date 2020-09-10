""" Convert charsets using a lookup table

https://docs.python.org/2.0/ref/strings.html
https://en.wikipedia.org/wiki/Six-bit_character_code#Types_of_six-bit_codes
https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_/_GSM_03.38
https://en.wikipedia.org/wiki/BCD_(character_encoding)
"""

from math import log2, ceil
from bitstring import BitArray

# CDC 1604: Magnetic tape BCD codes
CDC1604_MAGTAPE = "?1234567890#@??? /STUVWXYZ?,%???-JKLMNOPQR0$*???&ABCDEFGHI0.¤???"
# CDC 1604: Punched card codes
CDC1604_PUNCHCARD = "?1234567890=-??? /STUVWXYZ?,(???—JKLMNOPQR0$*???+ABCDEFGHI0.)???"
# CDC 1612: Printer codes (business applications)
CDC1612 = ":1234567890=≠≤![ /STUVWXYZ],(→≡~—JKLMNOPQR%$*↑↓>+ABCDEFGHI<.)≥?;"
# DEC SIXBIT
DEC_SIXBIT = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"
# ECMA-1
EMCA1 = " \t\n\v\f\r\x0e\x0f()*+,-./0123456789:;<=>?\x00ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]\x1b\x7f"
# ICL Mainframes
ICL = "0123456789:;<=>? !\"#£%&'()*+,-./@ABCDEFGHIJKLMNOPQRSTUVWXYZ[$]↑←"
# SixBit ASCII (used by AIS)
SIXBIT = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?"
# GOST 10859 § 6-bit code: with only Cyrillic upper case letters
GOST = "0123456789+-/,. ⏨↑()×=;[]*‘’≠<>:АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ\x7f"
# GSM 7-bit default alphabet and extension table of 3GPP TS 23.038 / GSM 03.38
GSM7 = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x07ÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>"
+ "?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà")
# ASCII
ASCII7 = bytes(range(0, 128)).decode("utf-8")
# IBM 48-character BCDIC code
IBM48 = " 1234567890#@????/STUVWXYZ?,%???-JKLMNOPQR?$*???&ABCDEFGHI?.⌑???"
# IBM 704 BCD code
IBM704 = "0123456789?#@???&ABCDEFGHI?.⌑???-JKLMNOPQR?$*??? /STUVWXYZ?,%???"
# IBM 7090/7094 character set
IBM7094 = IBM7090 = "0123456789?=\"???&ABCDEFGHI0.)???-JKLMNOPQR0$*??? /STUVWXYZ±,(???"
# IBM 1401 BCD code
IBM1401 = " 1234567890#@:>√¢/STUVWXYZ‡,%='\"-JKLMNOPQR!$*);Δ&ABCDEFGHI?.⌑(<⯒"
# GBCD code
GBCD = "0123456789[#@:>? ABCDEFGHI&.](<\\^JKLMNOPQR-$*);'+/STUVWXYZ_,%=\"!"
# Burroughs B5500 BCD code
BURROUGHS_B5500 = "0123456789#@?:>≥+ABCDEFGHI.[&(<←×JKLMNOPQR$*-);≤ /STUVWXYZ,%≠=]\""
# Code page 353
CP353 = " 1234567890#@:>√␢/STUVWXYZ‡,%γ\\⧻-JKLMNOPQR!#*];Δ&ABCDEFGHI?.⌑[<⯒"
# Code page 355
CP355 = " 1234567890#????@/STUVWXYZ‡,?γ??-JKLMNOPQR<$????&ABCDEFGHI).????"
# Code page 357
CP357 = " 1234567890=????'/STUVWXYZ‡,????-JKLMNOPQR!$????+ABCDEFGHI?.????"
# Code page 358
CP358 = " 1234567890'????!/STUVWXYZ‡,????-JKLMNOPQR<;????=ABCDEFGHI>.????"
# Code page 359/360
CP360 = CP359 = " 1234567890#????@/STUVWXYZ?,????-JKLMNOPQR?$????&ABCDEFGHI?.????"


def toUnicode(charset, bytestream):
	"""Convert text encoded with various charsets to unicode using a charset
	lookup table

	Args:
		charset (string): lookup table
		bytestream (bytes): sequence of bytes (split into bits of length
		log2(len(charset))) to convert

	Returns:
		string: unicode string
	"""
	unicode = []
	bitsize = ceil(log2(len(charset)))
	asciibits = BitArray(bytestream)
	for char in range(0, len(asciibits) // bitsize):
		unicode.append(charset[asciibits[char * bitsize:(char+1) * bitsize].uint])
	return "".join(unicode)


def toCharset(charset, string, toUpper=False):
	"""Convert unicode text to various charsets using a lookup table

	Args:
		charset (string): lookup table
		string (string): unicode string to convert
		toUpper (bool, optional): Make chars uppercase before converting
		(intended for 6 bit charsets or charsets that do not support uppercase).
		Defaults to False.

	Returns:
		bytes: sequence of bytes (split into bits of length
	"""
	asciibits = BitArray()
	cut = int(8 - log2(len(charset)))
	if toUpper:
		chars = chars.upper()
	for char in string:
		bits = charset.find(char)
		if bits < 0:
			if charset == GOST:
				bits = 25 # use '*' for GOST
			else:
				bits = charset.find("?")
		asciibits.append(BitArray(bytes([bits]))[cut:])
	return asciibits.tobytes()
