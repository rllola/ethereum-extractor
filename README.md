# Ethereum extractor POC

Proof of concept for extracting data from a chain export.

Export the data chain:
```
$ geth export chain.dat
```

**Notes**: The repo come with an example of chain.dat generated using a private network (doesnt match any real data).

Read it:
```
$ pip install rlp pycryptodome py-evm
$ python3 script.py
```

## Benchmarking

```
Block #0-0x550c..9734
Block #1-0x5905..c76c
Block #2-0x8f08..0a84
Block #3-0xb409..e954
Block #4-0x467d..2130
Execution Time : 0.012305
{'jsonrpc': '2.0', 'id': 1, 'result': '0x4'}
completion: 100.00% (n° 4/4)
Execution Time : 0.388193
```

