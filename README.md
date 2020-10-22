
## Description：
- parameters format：
    - _input：str
    - output: str
    - amount: float
    - chunks: int
    - quoteid: str
    - transactionHash: hexstring
    - sender: string
    - nonce: int
    - time:  int, timestamp. unit in seconds
    - client_name: str, given client name
- private endpoint
    /getQuote, /getSignedQuote, /transactionSubmitted requires authentication. Please refer to the below example.
[auth example(in Python)](https://github.com/OneBitQuant/dexMM/blob/master/signature_example.py)

## Endpoints

### /getSupportTokens
- request_params : None
- response :
    - result : 1（return success), 0（return failure)
    - supportTokens: list of support tokens
```
    {
        'result': 1,
        'supportTokens': [
            ['usdc', '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'],
            ['usdt', '0xdAC17F958D2ee523a2206206994597C13D831ec7'],
            ['weth', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2']
        ]
     }
```

### /getQuoteForAllPairs

get the reference price for all support pair with different amounts

- request_params : None
- response :
    - result : 1（return success), 0（return failure)
    - price_list
    - time
```
    {
         'result': 1,
         'price_list': {
             'eth_usdc': [
                   [50, 415.23475892844095],
                   [100, 414.81952416951253],
                   [200, 414.40428941058406],
                   [300, 413.98905465165564],
                   [400, 413.5738198927272],
                   [500, 413.15858513379874]
               ],
              'usdc_eth': [
                   [20000, 0.0024309196953347977],
                   [30000, 0.0024284887756394627],
                   [40000, 0.002426057855944128],
                   [50000, 0.002422411476401126]
               ]
           },
         'time': 1603381227.7482014
     }

```

### /getQuote

get the reference price for a given pair with amount and chunks, returns the reference price for each chunk.
For example: _input = weth, output = usdc, amount = 10, chunk = 5, returns the ref price for [2,4,6,8,10] eth/usdc respectively

- request_params :
    - _input
    - output
    - amount
    - chunks
- response :
    - result : 1（return success), 0（return failure)
    - indic_price: price_list,
    - input
    - output
    - amount
    - chunks
    - time
```
    {
       'result': 1,
       'indic_price': [[2, 372.11598091904625],
        [4, 372.11598091904625],
        [6, 372.11598091904625],
        [8, 372.11598091904625],
        [10, 372.11598091904625]],
       'input': 'weth',
       'output': 'usdc',
       'amount': 10,
       'chunks': 5,
       'time': 1600161154.5012438
     }
```


### /getSignedQuote

get the signed order for the request _input, output and amount.
- request_params :
    - _input
    - output
    - amount
    - sender: taker address
- response :
    - result : 1（return success), 0（return failure)
    - quote_id": request_params for /transactionSubmitted endpoint
    - order_hash
    - order_signature
    - makerAddress
    - takerAddress
    - feeRecipientAddress
    - senderAddress
    - makerAssetAmount
    - takerAssetAmount
    - makerFee
    - takerFee"
    - expirationTimeSeconds
    - salt
    - makerAssetData
    - takerAssetData
```
    {
       'result': 1,
       'quote_id': '1efe85de-f736-11ea-99d6-0a039777dd60',
       'order_hash': '0x52b5714fedd68bf95e9084e502d29e8550e4d80d9669e544178dfc0060e3247d',
       'order_signature': '0x8802d92289cffc1281c1dd9105d57e7822ac15eb14de7357a9386b4b12277c5f37f89ec71e89390c4c3c7ed7c60fbb8c939b28d43e951b7f7f0ea64aadb3cf381c',
       'makerAddress': '0x0726AF16Fb5FB2D6C351B7119f8E54b5cBE1E175',
       'takerAddress': '0x5316af395abaaabcbc06682eff19d9dac92838eb',
       'feeRecipientAddress': '0x0000000000000000000000000000000000000000',
       'senderAddress': '0x0000000000000000000000000000000000000000',
       'makerAssetAmount': '36944866',
       'takerAssetAmount': '100000000000000000',
       'makerFee': 0,
       'takerFee': 0,
       'expirationTimeSeconds': 1600162840,
       'salt': 1600162240852,
       'makerAssetData': '0xf47261b0000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
       'takerAssetData': '0xf47261b0000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
     }
```

### /transactionSubmitted

returns the submitted transaction


- request_params :
    - quoteid: quoteid returns from /getSignedQuote endpoint
    - transactionHash: transaction hash of the broadcasted transaction
    - nonce = nonce of the broadcasted transaction
- response :
    - result : confirmed
```
    {
        'result': 'confirmed'
    }
```

## Exceptions

### NoPrivateKey

Missing private key
- error code : NoPrivateKey
- error msg : client name

### AuthFailed

Authentication failed
- error code : AuthFailed
- error msg : signature invalid / incorrect api key / TIME invalid

### TokenNotSupported

input or output token is not supported
- error code : TokenNotSupported
- error msg : _input/ output token

### SystemError

- error code : SystemError
- error msg : System risk breach! / client is disabled!

### Blacklist

Sender address is in blacklist
- error code : Blacklist
- error msg : sender

### InsufficientBal

Insufficient Balance for output token
- error code : InsufficientBal
- error msg : output
