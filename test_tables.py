"""Test the miniencoding lib

A decent testing approach is to test the round trip with a random, valid
string of bytes. by taking this approach, the same error/ bug would have to be
present in both the 'from' and 'to' functions which whilst possible is unlikely
"""
# pylint: disable=invalid-name
import random
import string
from miniencoding.tables import *


def test_CDC1604_MAGTAPE_len():
	""" Test CDC1604_MAGTAPE length """
	assert len(CDC1604_MAGTAPE) == 64


def test_CDC1604_MAGTAPE():
	""" Test CDC1604_MAGTAPE round trip """
	testString = "?1234567890#@??? /STUVWXYZ?,%???-JKLMNOPQR0$*???&ABCDEFGHI0.¤???"
	assert toUnicode(CDC1604_MAGTAPE, toCharset(CDC1604_MAGTAPE,
	testString)) == testString


def test_CDC1604_PUNCHCARD_len():
	""" Test CDC1604_PUNCHCARD length """
	assert len(CDC1604_PUNCHCARD) == 64


def test_CDC1604_PUNCHCARD():
	""" Test CDC1604_PUNCHCARD round trip """
	testString = "?1234567890=-??? /STUVWXYZ?,(???—JKLMNOPQR0$*???+ABCDEFGHI0.)???"
	assert toUnicode(CDC1604_PUNCHCARD, toCharset(CDC1604_PUNCHCARD,
	testString)) == testString


def test_CDC1612_len():
	""" Test CDC1612 length """
	assert len(CDC1612) == 64


def test_CDC1612():
	""" Test CDC1612 round trip """
	testString = ":1234567890=≠≤![ /STUVWXYZ],(→≡~—JKLMNOPQR%$*↑↓>+ABCDEFGHI<.)≥?;"
	assert toUnicode(CDC1612, toCharset(CDC1612, testString)) == testString


def test_DEC_SIXBIT_len():
	""" Test DEC_SIXBIT length """
	assert len(DEC_SIXBIT) == 64


def test_DEC_SIXBIT():
	""" Test DEC_SIXBIT round trip """
	testString = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"
	assert toUnicode(DEC_SIXBIT, toCharset(DEC_SIXBIT, testString)) == testString


def test_EMCA1_len():
	""" Test EMCA1 length """
	assert len(EMCA1) == 64


def test_EMCA1():
	""" Test EMCA1 round trip """
	testString = " \t\n\v\f\r\x0e\x0f()*+,-./0123456789:;<=>?\x00ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]\x1b\x7f"
	assert toUnicode(EMCA1, toCharset(EMCA1, testString)) == testString


def test_ICL_len():
	""" Test ICL length """
	assert len(ICL) == 64


def test_ICL():
	""" Test ICL round trip """
	testString = "0123456789:;<=>? !\"#£%&'()*+,-./@ABCDEFGHIJKLMNOPQRSTUVWXYZ[$]↑←"
	assert toUnicode(ICL, toCharset(ICL, testString)) == testString


def test_SIXBIT_len():
	""" Test SIXBIT length """
	assert len(SIXBIT) == 64


def test_SIXBIT():
	""" Test SIXBIT round trip """
	testString = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?"
	assert toUnicode(SIXBIT, toCharset(SIXBIT, testString)) == testString


def test_GOST_len():
	""" Test GOST length """
	assert len(GOST) == 64


def test_GOST():
	""" Test GOST round trip """
	testString = "0123456789+-/,. ⏨↑()×=;[]*‘’≠<>:АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ\x7f"
	assert toUnicode(GOST, toCharset(GOST, testString)) == testString


def test_GSM7_len():
	""" Test GSM7 length """
	assert len(GSM7) == 128


def test_GSM7():
	""" Test GSM7 round trip """
	testString = "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x07ÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
	assert toUnicode(GSM7, toCharset(GSM7, testString)) == testString


def test_ASCII7_len():
	""" Test ASCII7 length """
	assert len(ASCII7) == 128


def test_ASCII7():
	""" Test ASCII7 round trip """
	testString = bytes(range(0, 128)).decode("utf-8")
	assert toUnicode(ASCII7, toCharset(ASCII7, testString)) == testString


def test_IBM48_len():
	""" Test IBM48 length """
	assert len(IBM48) == 64


def test_IBM48():
	""" Test IBM48 round trip """
	testString = " 1234567890#@????/STUVWXYZ?,%???-JKLMNOPQR?$*???&ABCDEFGHI?.⌑???"
	assert toUnicode(IBM48, toCharset(IBM48, testString)) == testString


def test_IBM704_len():
	""" Test IBM704 length """
	assert len(IBM704) == 64


def test_IBM704():
	""" Test IBM704 round trip """
	testString = "0123456789?#@???&ABCDEFGHI?.⌑???-JKLMNOPQR?$*??? /STUVWXYZ?,%???"
	assert toUnicode(IBM704, toCharset(IBM704, testString)) == testString


def test_IBM7090_len():
	""" Test IBM7090 length """
	assert len(IBM7090) == 64


def test_IBM7090():
	""" Test IBM7090 round trip """
	testString = "0123456789?=\"???&ABCDEFGHI0.)???-JKLMNOPQR0$*??? /STUVWXYZ±,(???"
	assert toUnicode(IBM7090, toCharset(IBM7090, testString)) == testString


def test_IBM1401_len():
	""" Test IBM1401 length """
	assert len(IBM1401) == 64


def test_IBM1401():
	""" Test IBM1401 round trip """
	testString = " 1234567890#@:>√¢/STUVWXYZ‡,%='\"-JKLMNOPQR!$*);Δ&ABCDEFGHI?.⌑(<⯒"
	assert toUnicode(IBM1401, toCharset(IBM1401, testString)) == testString


def test_GBCD_len():
	""" Test GBCD length """
	assert len(GBCD) == 64


def test_GBCD():
	""" Test GBCD round trip """
	testString = "0123456789[#@:>? ABCDEFGHI&.](<\\^JKLMNOPQR-$*);'+/STUVWXYZ_,%=\"!"
	assert toUnicode(GBCD, toCharset(GBCD, testString)) == testString


def test_BURROUGHS_B5500_len():
	""" Test BURROUGHS_B5500 length """
	assert len(BURROUGHS_B5500) == 64


def test_BURROUGHS_B5500():
	""" Test BURROUGHS_B5500 round trip """
	testString = "0123456789#@?:>≥+ABCDEFGHI.[&(<←×JKLMNOPQR$*-);≤ /STUVWXYZ,%≠=]\""
	assert toUnicode(BURROUGHS_B5500, toCharset(BURROUGHS_B5500, testString)) == testString


def test_CP353_len():
	""" Test CP353 length """
	assert len(CP353) == 64


def test_CP353():
	""" Test CP353 round trip """
	testString = " 1234567890#@:>√␢/STUVWXYZ‡,%γ\\⧻-JKLMNOPQR!#*];Δ&ABCDEFGHI?.⌑[<⯒"
	assert toUnicode(CP353, toCharset(CP353, testString)) == testString


def test_CP355_len():
	""" Test CP355 length """
	assert len(CP355) == 64


def test_CP355():
	""" Test CP355 round trip """
	testString = " 1234567890#????@/STUVWXYZ‡,?γ??-JKLMNOPQR<$????&ABCDEFGHI).????"
	assert toUnicode(CP355, toCharset(CP355, testString)) == testString


def test_CP357_len():
	""" Test CP357 length """
	assert len(CP357) == 64


def test_CP357():
	""" Test CP357 round trip """
	testString = " 1234567890=????'/STUVWXYZ‡,????-JKLMNOPQR!$????+ABCDEFGHI?.????"
	assert toUnicode(CP357, toCharset(CP357, testString)) == testString


def test_CP358_len():
	""" Test CP358 length """
	assert len(CP358) == 64


def test_CP358():
	""" Test CP358 round trip """
	testString = " 1234567890'????!/STUVWXYZ‡,????-JKLMNOPQR<;????=ABCDEFGHI>.????"
	assert toUnicode(CP358, toCharset(CP358, testString)) == testString


def test_CP359_len():
	""" Test CP359 length """
	assert len(CP359) == 64


def test_CP359():
	""" Test CP359 round trip """
	testString = " 1234567890#????@/STUVWXYZ?,????-JKLMNOPQR?$????&ABCDEFGHI?.????"
	assert toUnicode(CP359, toCharset(CP359, testString)) == testString
