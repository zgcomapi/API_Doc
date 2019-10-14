# The API
``` 
Version：v0.0.6
Date： 2019-08-02
Update log: /private/order/finished interface, request parameter exclude side field, separate query of buying or selling is not supported any more.
```
## API Market
### Get exchange market date
GET /tickers 

https://api1.zg.com/tickers

##### Example
```
# Request 
GET https://api1.zg.com/tickers

# Response
{
	"ticker": [{
		"buy": "0.01",
		"high": "0.038",
		"last": "0.038",
		"low": "0.038",
		"sell": "0.038",
		"symbol": "ABO_CNZ",
		"vol": "0",
		"change": "0"
	}, {
		"buy": "0.013",
		"high": "0.0152",
		"last": "0.0141",
		"low": "0.0129",
		"sell": "0.017",
		"symbol": "AEP_CNZ",
		"vol": "4229530.2676",
		"change": "-1.3986013986014"
	}],
	"timestamp": "1558841277902"
}
```
##### Field description

field name| description 
-| :-
timestamp | timestamp(millisecond)
buy  | best bid price	
high | the highest price
last | the latest price
low  | the lowest price
sell | best ASK
vol  | transaction volume(24H)
symbol | trading pairs
change | change(%)
--------------------- 

### Depth

GET /depth 

https://api1.zg.com/depth


##### Example

```
# Request 
GET https://api1.zg.com/depth?symbol=BTC_USDT&size=1

# Response
{
	"asks": [
		[
			"7990.28",
			"0.0065"
		],
		[
			"7990.29",
			"0.0129"
		]
	],
	"bids": [
		[
			"7965.52",
			"0.1974"
		],
		[
			"7965.5",
			"0.0198"
		]
	]
}
```

##### Request field description
Field name| description| type
-| :- | :-
symbol | trading pairs (case sensitive) | string
size | the number of returned depth | int


##### Response field description

Field name| description 
-| :- 
asks | ASK depth [price,amount]
bids  | bid depth [price,amount]
--------------------- 

### The latest transaction records

GET /trades  get the latest transaction record

https://api1.zg.com/trades

##### Example

```
# Request
GET https://api1.zg.com/trades?symbol=BTC_USDT&size=2

# Response
[{
		"amount": "0.1662",
		"price": "7966.71",
		"side": "buy",
		"timestamp": 1558842181
	},
	{
		"amount": "0.1756",
		"price": "7966.01",
		"side": "sell",
		"timestamp": 1558842177
	}
]
```

##### Request field description
Field name| description  | type
-| :- | :-
symbol | trading pairs (case sensitive)  | string
size | the number of return transaction volume| int

##### Response field description

字段名| 说明 
-| :- 
amount | transaction amount
price  | transaction price
side   | ASK and BID
timestamp | timestamp(second)
--------------------- 

### KLine

GET /kline

https://api1.zg.com/kline

##### Example
```
# Request 
GET https://api1.zg.com/kline?symbol=ltc_btc&type=1min&size=100

# Response
[
	[
		1558842299000,
		"0.1989",
		"0.1999",
		"0.1989",
		"0.1999",
		"78041.8835"
	],
	[
		1558842359000,
		"0.1993",
		"0.1994",
		"0.1985",
		"0.1991",
		"37727.4048"
	],
	[
		1558842419000,
		"0.1989",
		"0.1989",
		"0.1981",
		"0.1981",
		"131149.4204"
	],
	[
		1558842479000,
		"0.1981",
		"0.1981",
		"0.1981",
		"0.1981",
		"10318.0212"
	]
]
```

##### Response field description

```
corresponding field in order :
[
        1558842299000,      //timestamp(millisecond)
	"0.1989",           //open
	"0.1999",           //high
	"0.1989",           //low
	"0.1999",           //close
	"78041.8835"        //trading volume
]
```
##### Request field description
Field name| description  | type
-| :- | :-
symbol | trading pairs(case sensitive) | string
size | the number of return Kline | int
type | time division parameter(1min,5min,15min,30min,hour,day,week)
--------------------- 

### Trading pairs information
GET /exchangeInfo

https://api1.zg.com/exchangeInfo

##### Example

```
# Request
GET https://api1.zg.com/exchagneInfo
# Response
[{
		"baseAsset": "ZRX",
		"baseAssetPrecision": 4,
		"quoteAsset": "USDT",
		"quoteAssetPrecision": 2,
		"status": "trading",
		"symbol": "ZRX_USDT"
	},
	{
		"baseAsset": "ZRX",
		"baseAssetPrecision": 4,
		"quoteAsset": "CNZ",
		"quoteAssetPrecision": 4,
		"status": "trading",
		"symbol": "ZRX_CNZ"
	}
]
```

##### Response field description

Field name | description 
-| :- 
baseAsset | baseAsset
baseAssetPrecision  | baseAssetPrecision
quoteAsset   | quoteAsset
status | trading status
symbol | trading pairs
---------------------

## API transaction

### Important
* **All parameters need to submit data in the form of form-data and all the interfaces are in the form [POST].**
* **API transaction needs to be validated by signature. All parameters,excluding sign parameter, must sign and put parameter name in alphabetical order.**
* **Sign have to convert case.(case sensitive)**

Example: If request parameter is
```
{
	"api_key": "c821db84-6fbd-11e4-a9e3-c86000d26d7c ",
	"sign": "5C263F54B613EEFE02BB596879D1DDF3",
	"symbol": "BTC_USDT",
	"side": 1,
	"price": "50",
	"amount": "0.02"
}
String: amount=1.0&api_key=c821db84-6fbd-11e4-a9e3-c86000d26d7c&price=680&side=1&symbol=BTC_USDT

MD5 signature, secretKey was need to generate MD5signature, adding secret_key after the above strings to generate the final strings. For example 

amount=1.0&api_key=c821db84-6fbd-11e4-a9e3-c86000d26d7c&price=680&side=1&symbol=BTC_USDT&secret_key=secretKey 
```

<font color=red size=3>***Note：sign must be converted to uppercase***</font>


### Get users’ assets
POST /private/user

https://api1.zg.com/private/user

```
# Request
POST https://api1.zg.com/private/user

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"USDT": {
			"available": "10718.74453852",
			"freeze": "0.10999996",
			"other_freeze": "0",
			"recharge_status": 0,
			"trade_status": 1,
			"withdraw_fee": "0.1",
			"withdraw_max": "1000",
			"withdraw_min": "0.001",
			"withdraw_status": 1
		},
		"ETH": {
			"available": "395.196",
			"freeze": "0",
			"other_freeze": "0",
			"recharge_status": 1,
			"trade_status": 1,
			"withdraw_fee": "0.01",
			"withdraw_max": "100000",
			"withdraw_min": "0.001",
			"withdraw_status": 1
		}
	}
}
```

##### Request field description
Field name| description | type
-| :- | :-
api_key | api_key | string
sign | signature| string 

##### Response field description

Field name| description
-| :- 
available | available balance
freeze  | trading frozen assets 
other_freeze   | other frozen assets (including C2C and withdrawal)
recharge_status | recharge status：0-No，1-Yes
withdraw_fee | withdraw fee 
withdraw_max | withdraw max amount
withdraw_min | withdraw minimum amount
withdraw_status | withdraw status：0-No，1-Yes
---------------------

### Limit trade
POST /private/trade/limit

https://api1.zg.com/private/trade/limit


##### Example
```
# Request
POST https://api1.zg.com/private/trade/limit

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"amount": "1",
		"ctime": 1535537926.246487,
		"deal_fee": "0",
		"deal_money": "0",
		"deal_stock": "0",
		"id": 32865,
		"left": "1",
		"maker_fee": "0.001",
		"market": "BTC_USDT",
		"mtime": 1535537926.246487,
		"price": "10",
		"side": 2,
		"source": "web,1",
		"taker_fee": "0.001",
		"type": 1,
		"user": 670865
	}
}
```

##### Request field description
Field name| description | type
-| :- | :-
api_key | api_key | string
sign | signature| string 
market |trading pairs(|string
side | 1-ASK sell,2-BID buy|int
amount | amount|string
price | price  |string

##### Response field description

Field name| description
-| :- 
amount | amount
ctime  | creation time
deal_fee   | deal fee
deal_money | deal money
deal_stock | deal stock
id |  order number
left | left
maker_fee | maker fee
market | trading pairs(case sensitive)
mtime |  market time
price |  price
side | 1=ASK sell，2=BID buy
source | source
taker_fee | taker fee
type| trading type 1=limit price   2=market price
user| user ID
---------------------

### Market price trade 
POST /private/trade/limit

https://api1.zg.com/private/trade/market


##### Example
```
# Request
POST https://api1.zg.com/private/trade/market

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"amount": "1",
		"ctime": 1535537926.246487,
		"deal_fee": "0",
		"deal_money": "0",
		"deal_stock": "0",
		"id": 32865,
		"left": "1",
		"maker_fee": "0.001",
		"market": "BTC_USDT",
		"mtime": 1535537926.246487,
		"price": "10",
		"side": 2,
		"source": "web,1",
		"taker_fee": "0.001",
		"type": 1,
		"user": 670865
	}
}
```

##### Request field description
Field name| description| type
-| :- | :-
api_key | api_key | string
sign | signature| string 
market |trading pairs(case sensitive)|string
side |1-ASK sell，2-BID buy|int
amount | amount|string

##### Response field description

Field name| description 
-| :- 
amount | amount
ctime  | creation time
deal_fee   | deal fee
deal_money | deal money
deal_stock | deal stock
id | order number
left | left
maker_fee | maker fee
market | trading pairs
mtime | pending time 
price | price
side | 1=ASK sell，2=BID buy
source |  source
taker_fee | taker fee
type| trading type 1=limit price   2=market price
user| user ID
---------------------

<font color=red size=3>***NOTE：versionv1 [limited order][market order]API. Other value may be null or 0，except id order number. You can call other interface to query order details based on order number if you need.***</font>

##### Error message
If code = 13,
message = 114 //wrong minimum order amount (note：usdt trading pair: price * amount >= 1 usdt ; cnz  trading pairs: price * amount >= 1 cnz)
message = 110 //insufficient balance



### Cancel the transaction
POST /private/trade/cancel

https://api1.zg.com/private/trade/cancel

##### Example

```
# Request
POST https://api1.zg.com/private/trade/cancel

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"amount": "1",
		"ctime": 1535538409.189721,
		"deal_fee": "0.00019607843",
		"deal_money": "0.999999993",
		"deal_stock": "0.19607843",
		"id": 32868,
		"left": "7.000",
		"maker_fee": "0",
		"market": "BTC_USDT",
		"mtime": 1535538409.189735,
		"price": "0",
		"side": 2,
		"source": "web,1",
		"taker_fee": "0.001",
		"type": 2,
		"user": 670865
	}
}
```

##### Request field description
Field name |  description   | type
-| :- | :-
api_key | api_key | string
sign |  signature | string 
market |trading pairs(case sensitive)|string
order_id | order number  |string

##### Response field description

Field name| description 
-| :- 
amount | amount
ctime  | creation time
deal_fee   | deal fee
deal_money | deal money
deal_stock | deal stock
id | order number
left | left
maker_fee | maker fee
market | trading pairs
mtime | pending time
price | price
side | 1=ASK sell, 2=BID buy
source | source
taker_fee | taker fee
type| trading type, 1=limit price，2=market price
user|  user ID
---------------------
##### Error message

code = 10 fail to cancel the order（including repeated cancellations, cancelled orders by system. If you need to confirm the order status, use  pending interface） 
code= 121 cancellation was refused。

### Check transaction details

POST /private/order/deals 

https://api1.zg.com/private/order/deals

###### Example

```
# Request
POST https://api1.zg.com/private/order/deals

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"limit": 20,
		"offset": 0,
		"records": [{
			"amount": "1",
			"deal": "19.96",
			"deal_order_id": 32730,
			"fee": "0.001",
			"id": 25503,
			"price": "19.96",
			"role": 2,
			"time": 1535437951.751402,
			"user": 670865
		}]
	}
}
```

##### Request field description
Field name | description  |  type
-| :- | :-
api_key | api_key | string
sign | signature | string 
order_id | order number |string
offset |  offset  |int
limit |  query the amount of data |int

##### Response field description

Field name| description
-| :- 
limit| the number of queries(maximum value =1000)
offset| offset
records|  records
amount| amount
deal| deal
deal_order_id| deal order id
fee| fee
id| deal id
price| price
role|  role，1=Maker,2=Taker
time| timestamp
user| user ID
---------------------

### Query unfinished order（including partial finished）
POST /private/order/pending 

https://api1.zg.com/private/order/pending

###### Example

```
# Request
POST https://api1.zg.com/private/order/pending

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"limit": 10,
		"offset": 0,
		"records": [{
			"amount": "1",
			"ctime": 1535544362.168106,
			"deal_fee": "0",
			"deal_money": "0",
			"deal_stock": "0",
			"id": 32871,
			"left": "1",
			"maker_fee": "0.001",
			"market": "BTC_USDT",
			"mtime": 1535544362.168106,
			"price": "5.1",
			"side": 2,
			"source": "web,1",
			"taker_fee": "0.001",
			"type": 1,
			"user": 670865
		}],
		"total": 1
	}
}
```

##### Request field description
Field name| description | type
-| :- | :-
api_key | api_key | string
sign | signature | string 
market | trading pairs(case sensitive)|string
offset |  offset   |int
limit | query the amount of data  |int

##### Response field description

Field name| description
-| :- 
amount| amount
ctime|  creation time
deal_fee|  deal fee
deal_money| deal momey
deal_stock| deal stock
id|  Id
left| left 
maker_fee| maker fee
market| market name
mtime| pending time
price|  price
side| 1=ASK sell，2=BID buy
source|source
taker_fee|  taker fee
type| trading type，1=限价limit price，2=market price
user|  user ID
---------------------

### Query finished orders
POST /private/order/finished 

https://api1.zg.com/private/order/finished

###### Examples

```
# Request
POST https://api1.zg.com/private/order/finished

# Response
{
	"code": 0,
	"message": "operation succeeded",
	"result": {
		"limit": 2,
		"offset": 0,
		"records": [{
				"amount": "1",
				"ctime": 1535538409.189721,
				"deal_fee": "0.00019607843",
				"deal_money": "0.999999993",
				"deal_stock": "0.19607843",
				"ftime": 1535538409.189735,
				"id": 32868,
				"maker_fee": "0",
				"market": "BTC_USDT",
				"price": "0",
				"side": 2,
				"source": "web,1",
				"taker_fee": "0.001",
				"type": 2,
				"user": 670865
			},
			{
				"amount": "10",
				"ctime": 1535538403.233823,
				"deal_fee": "0.001109999955",
				"deal_money": "1.109999955",
				"deal_stock": "0.21764705",
				"ftime": 1535538409.189735,
				"id": 32867,
				"maker_fee": "0.001",
				"market": "BTC_USDT",
				"price": "5.1",
				"side": 1,
				"source": "web,1",
				"taker_fee": "0.001",
				"type": 1,
				"user": 670865
			}
		]
	}
}
```

##### Request field description
Field name| description  | type
-| :- | :-
api_key | api_key | string
sign | signature | string 
market |trading pairs(case sensitive)|string
offset | offset  |int
limit | query the amount of data |int
start_time |start time，timestamp(second) |int
end_time |end time，timestamp(second)|int

##### Response field description

字段名| 说明 
-| :- 
amount| amount
ctime| creation time
deal_fee| deal fee
deal_money| deal money
deal_stock| deal stock
id| order number
left|  left
maker_fee| maker fee
market| market name
ftime| finished time
price| price
side|  1=ASK sell，2=BID buy
source|source
taker_fee| taker fee
type| trading type，1=限价limit price，2=market price
user| user ID
---------------------

# 注Notice
* Each IP is allowed to access maximum 1500 times per minute in version * v1 interface User-Agent must be added when request Headers


<font color=red size=3>***Access may be prohibited if the above rules are violated. What’s more, rules may be changed.***</font>
