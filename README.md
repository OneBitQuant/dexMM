
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
[auth example(in Python)](https://github.com/onebit-quant/dealerMaker-API/blob/master/signature_example.py)

## Endpoints

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
       'makerAssetAmount': 36944866,
       'takerAssetAmount': 100000000000000000,
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
    - sender: taker address
    - nonce = nonce of the broadcasted transaction
- response :
    - result : confirmed