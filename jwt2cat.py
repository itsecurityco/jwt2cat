#!/usr/bin/env python3
# Author: Juan (@itsecurityco)

import sys
from jwt.utils import base64url_decode
from binascii import hexlify

if len(sys.argv) != 2:
  print("Usage: {} JWT".format(sys.argv[0]))
  sys.exit(0)

jwt = sys.argv[1].split('.')

header    = jwt[0]
payload   = jwt[1]
signature = jwt[2]

hash = hexlify(base64url_decode(signature)).decode('ascii')

print ("{}:{}.{}".format(hash, header, payload))
