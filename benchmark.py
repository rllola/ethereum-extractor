import time
import requests

import rlp
from eth.vm.forks.london.blocks import LondonBlock

MAX_BYTES_FOR_SIZE = 8

#######################
#
# Extracting data from export file
#
#######################

start_time = time.perf_counter()
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

end_time = time.perf_counter()
print(f"Execution Time : {end_time - start_time:0.6f}" )

#######################
#
# Extracting data using JSON rpc
#
#######################

START_BLOCK = 0
URL = "http://localhost:8545"

start_time = time.perf_counter()

payload = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
result = requests.post(URL, json=payload)
print(result.json())
stop_block = int(result.json()['result'], 16)

for block_index in range(START_BLOCK, stop_block + 1):
    print("\rcompletion: {:.2%} (n° {}/{})".format((block_index-START_BLOCK)/(stop_block - START_BLOCK),block_index, stop_block), end="")

    payload = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":[hex(block_index), True],"id":1}
    result = requests.post(URL, json=payload)

    block = result.json()['result']

end_time = time.perf_counter()
print(f"\nExecution Time : {end_time - start_time:0.6f}")



