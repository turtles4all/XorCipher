# XorCipher
XOR.py will take a given key and use its SHA3-256 hash to XOR a given file. 

Requirements: Python 3.6

Usage: XOR.py [-h] -i FILEIN -o FILEOUT -k KEYSTRING

optional arguments:

  -h, --help    show this help message and exit

Required arguments:

  -i FILEIN     Input File
  -o FILEOUT    Output File
  -k KEYSTRING  Key

Example:

 To encrypt - "XOR.py -i pg100.txt -o pgxored -k password
 
 To decrypt - "XOR.py -i pgxored -o anyfilename.txt -k password
