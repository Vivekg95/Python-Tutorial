Python 3.7.0b1 (v3.7.0b1:9561d7f, Jan 31 2018, 07:26:34) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> matcher=re.finditer("a","aabca")
>>> for match in matcher:
	print(match.start(),"....",match.group())
