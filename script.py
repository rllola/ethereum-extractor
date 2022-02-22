import time

import rlp
from eth.vm.forks.london.blocks import LondonBlock

MAX_BYTES_FOR_SIZE = 8

with open('chain.dat', 'rb') as f:
  data = f.read()

#print(data.hex())

start = 0
end = 0

while end < len(data):
  kek = rlp.codec.consume_length_prefix(data[start:start+MAX_BYTES_FOR_SIZE], 0)
  end = start + kek[2] + kek[3]
  tmp = data[start:end]
  kek = rlp.decode(tmp, sedes=LondonBlock)
  print(kek)
  #print(kek.__dict__)
  #print(kek.transactions[0].__dict__)

  start = end