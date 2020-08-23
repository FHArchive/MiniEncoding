Module miniencoding.tables
==========================
Convert charsets using a lookup table

https://docs.python.org/2.0/ref/strings.html
https://en.wikipedia.org/wiki/Six-bit_character_code#Types_of_six-bit_codes
https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_/_GSM_03.38
TODO: https://en.wikipedia.org/wiki/BCD_(character_encoding)

Functions
---------

    
`toCharset(charset, string, toUpper=False)`
:   Convert unicode text to various charsets using a lookup table
    
    Args:
            charset (string): lookup table
            string (string): unicode string to convert
            toUpper (bool, optional): Make chars uppercase before converting
            (intended for 6 bit charsets or charsets that do not support uppercase).
            Defaults to False.
    
    Returns:
            bytes: sequence of bytes (split into bits of length

    
`toUnicode(charset, bytestream)`
:   Convert text encoded with various charsets to unicode using a charset
    lookup table
    
    Args:
            charset (string): lookup table
            bytestream (bytes): sequence of bytes (split into bits of length
            log2(len(charset))) to convert
    
    Returns:
            string: unicode string