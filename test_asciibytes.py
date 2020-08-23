"""Test the miniencoding lib

A decent testing approach is to test the round trip with a random, valid
string of bytes. by taking this approach, the same error/ bug would have to be
present in both the 'from' and 'to' functions which whilst possible is unlikely
"""
# pylint: disable=invalid-name
import random
import string
from miniencoding.asciibytes import AsciiBytes


def generator(length):
	"""Generate a random sequence of bytes

	Args:
		length (int): length

	Returns:
		bytes: random sequence of bytes
	"""
	letters = string.printable
	return ''.join(random.choice(letters) for i in range(length)).encode()


def test_ascii8():
	"""Ascii8 has no strange behaviours or edge cases so this should be pretty
	straightforward
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert testAscii.toAscii8() == testString


def test_ascii8Len():
	"""Ascii8 has a length of 1 byte per char
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert len(testAscii.toAscii8()) == 32


def test_ascii7Printable():
	"""Ascii7 has no strange behaviours or edge cases for printable chars so
	this should be pretty straightforward
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii2 = AsciiBytes()
	testAscii.fromAscii8(testString)
	testAscii2.fromAscii7(testAscii.toAscii7())
	assert testAscii2.toAscii8() == testString


def test_ascii7NonPrintable():
	"""ascii7 cannot process ascii values over 127, will replace chars with '?'
	"""
	testAscii = AsciiBytes()
	testAscii2 = AsciiBytes()
	testAscii.fromAscii8(bytes([127, 128]))
	testAscii2.fromAscii7(testAscii.toAscii7())
	assert testAscii2.toAscii8() == bytes([127]) + b"?"


def test_ascii7Len():
	"""Ascii7 has a length of 7/8 byte per char
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert len(testAscii.toAscii7()) == 4 * 7


def test_decSixBit():
	"""Dec Six Bit has edge cases and strange behaviours as shown by the
	inline for loop for the variable 'expected'
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii2 = AsciiBytes()
	testAscii.fromAscii8(testString)
	testAscii2.fromDecSixBit(testAscii.toDecSixBit())
	expected = b"".join([
	bytes([char]) if 0x20 <= char < 0x60 else b'?'
	for char in testString.upper()])
	assert testAscii2.toAscii8() == expected


def test_decSixBitLen():
	"""Dec Six Bit has a length of 6/8 byte per char
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert len(testAscii.toDecSixBit()) == 4 * 6


def test_ICL():
	"""ICL has edge cases and strange behaviours as shown by the
	inline for loop for the variable 'expected'
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii2 = AsciiBytes()
	testAscii.fromAscii8(testString)
	testAscii2.fromICL(testAscii.toICL())
	expected = b"".join([
	bytes([char]) if 0x20 <= char < 0x60 else b'?'
	for char in testString.upper()])
	assert testAscii2.toAscii8() == expected


def test_ICLLen():
	"""ICL has a length of 6/8 byte per char
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert len(testAscii.toICL()) == 4 * 6


def test_sixBitAscii():
	"""Six Bit Ascii has edge cases and strange behaviours as shown by the
	inline for loop for the variable 'expected'
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii2 = AsciiBytes()
	testAscii.fromAscii8(testString)
	testAscii2.fromSixBitAscii(testAscii.toSixBitAscii())
	expected = b"".join([
	bytes([char]) if 0x20 <= char < 0x60 else b'?'
	for char in testString.upper()])
	assert testAscii2.toAscii8() == expected


def test_sixBitAsciiLen():
	"""Six Bit Ascii has a length of 6/8 byte per char
	"""
	testString = generator(32)
	testAscii = AsciiBytes()
	testAscii.fromAscii8(testString)
	assert len(testAscii.toSixBitAscii()) == 4 * 6
