# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2020 - 2020/08/21
- First release
- Features ascii8, ascii7 ascii6 (DEC Six Bit, ICL, Six Bit ascii)
- Supports 10 6/7 bit encodings with miniencoding.tables

## 2020.1 - 2020/09/10
- Supports 21 6/7 bit encodings with miniencoding.tables (+11). Those are:
```python
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
```
