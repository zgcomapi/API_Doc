# API相关
```
版本号： v0.0.6
日期：   2019-08-02
更新日志: /private/order/finished 接口，请求参数去除side字段，不再支持按买卖方向查询。 
```
## 行情API
### 获取交易所市场数据
GET /tickers 

https://api1.zg.com/tickers

##### 示例
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
##### 字段说明

字段名| 说明 
-| :-
timestamp | 时间戳(毫秒)
buy  | 最佳BID
high | 最高价
last | 最新价
low  | 最低价
sell | 最佳ASK
vol  | 成交量(24小时)
symbol | 交易对
change | 涨跌幅(百分比)
--------------------- 

### 深度

GET /depth 

https://api1.zg.com/depth


##### 示例 

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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
symbol | 交易对 (大小写敏感) | string
size | 返回深度的数量 | int

##### 响应字段说明

字段名| 说明 
-| :- 
asks | ASK深度 [价格,数量]
bids  | bid深度 [价格,数量]
--------------------- 

### 最新成交记录

GET /trades 获取最新成交记录

https://api1.zg.com/trades

##### 示例

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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
symbol | 交易对 (大小写敏感) | string
size | 返回成交数的数量 | int

##### 响应字段说明

字段名| 说明 
-| :- 
amount | 成交数量
price  | 成交价
side   | 买卖方向
timestamp | 时间戳(秒)
--------------------- 

### K线

GET /kline

https://api1.zg.com/kline

##### 示例
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

##### 响应字段说明

```
相应字段按顺序:
[
        1558842299000,      //时间戳(毫秒)
	"0.1989",           //开
	"0.1999",           //高
	"0.1989",           //低
	"0.1999",           //收
	"78041.8835"        //交易量
]
```
##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
symbol | 交易对 (大小写敏感) | string
size | 返回K线的数量 | int
type | 分时参数，可以为1min,5min,15min,30min,hour,day,week
--------------------- 

### 交易对信息
GET /exchangeInfo

https://api1.zg.com/exchangeInfo

##### 示例

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

##### 响应字段说明

字段名| 说明 
-| :- 
baseAsset | 基础货币
baseAssetPrecision  | 基础货币精度
quoteAsset   | 计价货币精度
status | 交易状态
symbol | 交易对
---------------------

## 交易API

### 重要说明
* **所有的参数都需要使用form-data的形式提交数据，接口都为[POST]形式。**
* **交易API需要进行签名验证，除sign参数外所有的参数都必须进行签名，所有参数必须根据字母表按照参数名进行排序。**
* **sign需要转换为大写字母（大小写敏感）**

举例:
若请求参数为
```
{
	"api_key": "c821db84-6fbd-11e4-a9e3-c86000d26d7c ",
	"sign": "5C263F54B613EEFE02BB596879D1DDF3",
	"symbol": "BTC_USDT",
	"side": 1,
	"price": "50",
	"amount": "0.02"
}
字符串为: amount=1.0&api_key=c821db84-6fbd-11e4-a9e3-c86000d26d7c&price=680&side=1&symbol=BTC_USDT

MD5签名 生成MD5签名必须要secretKey,在以上生成的字符串后面添加secret_key以生成最终的字符串，例如
amount=1.0&api_key=c821db84-6fbd-11e4-a9e3-c86000d26d7c&price=680&side=1&symbol=BTC_USDT&secret_key=secretKey 
```

<font color=red size=3>***注意：sign 必须转换为大写字母***</font>


### 获取用户资产
POST /private/user

https://api1.zg.com/private/user

```
# Request
POST https://api1.zg.com/private/user

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 

##### 响应字段说明

字段名| 说明 
-| :- 
available | 可用余额
freeze  | 交易冻结金额
other_freeze   | 其他冻结金额(包括C2C和提币冻结)
recharge_status | 充值状态：0-不可充值，1-可充值
withdraw_fee | 提币手续费 
withdraw_max | 最大提币金额
withdraw_min | 最小提币金额
withdraw_status | 提笔状态：0-不可提币，1-可提币
---------------------

### 限价交易
POST /private/trade/limit

https://api1.zg.com/private/trade/limit


##### 示例
```
# Request
POST https://api1.zg.com/private/trade/limit

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
market |交易对(大小写敏感)|string
side |1-ASK卖出，2-BID买入|int
amount | 数量|string
price | 价格 |string

##### 响应字段说明

字段名| 说明 
-| :- 
amount | 数量
ctime  | 创建时间
deal_fee   | 成交手续费
deal_money | 成交金额
deal_stock | 成交资产 
id | 订单号
left | 剩余
maker_fee | maker手续费
market | 交易对
mtime | 发布到市场时间
price | 价格
side | 1为ASK卖出，2为BID买入
source | 来源
taker_fee | taker手续费
type| 交易类型，1为限价，2为市价
user| 用户编号
---------------------

### 市价交易
POST /private/trade/limit

https://api1.zg.com/private/trade/market


##### 示例
```
# Request
POST https://api1.zg.com/private/trade/market

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
market |交易对(大小写敏感)|string
side |1-ASK卖出，2-BID买入|int
amount | 数量|string

##### 响应字段说明

字段名| 说明 
-| :- 
amount | 数量
ctime  | 创建时间
deal_fee   | 成交手续费
deal_money | 成交金额
deal_stock | 成交资产 
id | 订单号
left | 剩余
maker_fee | maker手续费
market | 交易对
mtime | 发布到市场时间
price | 价格
side | 1为ASK卖出，2为BID买入
source | 来源
taker_fee | taker手续费
type| 交易类型，1为限价，2为市价
user| 用户编号
---------------------

<font color=red size=3>***注意：v1 版本[限价下单][市价下单]API 除id订单号外，其他值可能为空或0，如需查询成交情况请使用得到的订单号调用其他接口***</font>

##### 错误信息
当code = 13时,

message = 114 //最小下单金额错误 (注：usdt 交易对: price * amount >= 1 usdt ; cnz 交易对: price * amount >= 1 cnz)

message = 110 //余额不足 



### 取消交易
POST /private/trade/cancel

https://api1.zg.com/private/trade/cancel

##### 示例

```
# Request
POST https://api1.zg.com/private/trade/cancel

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
market |交易对(大小写敏感)|string
order_id | 订单号 |string

##### 响应字段说明

字段名| 说明 
-| :- 
amount | 数量
ctime  | 创建时间
deal_fee   | 成交手续费
deal_money | 成交金额
deal_stock | 成交资产 
id | 订单号
left | 剩余
maker_fee | maker手续费
market | 交易对
mtime | 发布到市场时间
price | 价格
side | 1为ASK卖出，2为BID买入
source | 来源
taker_fee | taker手续费
type| 交易类型，1为限价，2为市价
user| 用户编号
---------------------
##### 错误信息
code = 10 撤单失败（存在情况为：重复撤单，被系统撤掉的订单。如需确定状态，请再拉取挂单接口）
code = 121 撤单被拒绝。

### 查询成交明细

POST /private/order/deals 

https://api1.zg.com/private/order/deals

###### 示例

```
# Request
POST https://api1.zg.com/private/order/deals

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
order_id | 订单号 |string
offset | 偏移量 |int
limit | 查询数据量 |int

##### 响应字段说明

字段名| 说明 
-| :- 
limit| 查询数量(最大值为1000)
offset| 偏移
records| 记录
amount| 数量
deal| 已成交
deal_order_id| 成交的订单id
fee| 手续费
id| 成交id
price| 价格
role| 角色，1为Maker,2为Taker
time| 时间戳
user| 用户编号
---------------------

### 查询未成交订单(包括部分成交)
POST /private/order/pending 

https://api1.zg.com/private/order/pending

###### 示例

```
# Request
POST https://api1.zg.com/private/order/pending

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
market |交易对(大小写敏感)|string
offset | 偏移量 |int
limit | 查询数据量 |int

##### 响应字段说明

字段名| 说明 
-| :- 
amount| 数量
ctime| 创建时间
deal_fee| 成交手续费
deal_money| 成交金额
deal_stock| 成交资产
id| 编号
left| 剩余
maker_fee| maker手续费
market| 市场名
mtime| 发布到市场时间
price| 价格
side| 1为ASK卖出，2为BID买入
source|来源
taker_fee| taker手续费
type| 交易类型，1为限价，2为市价
user| 用户编号
---------------------

### 查询已成交订单
POST /private/order/finished 

https://api1.zg.com/private/order/finished

###### 示例

```
# Request
POST https://api1.zg.com/private/order/finished

# Response
{
	"code": 0,
	"message": "操作成功",
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

##### 请求字段说明
字段名| 说明 | 类型
-| :- | :-
api_key | api_key | string
sign | 签名 | string 
market |交易对(大小写敏感)|string
offset | 偏移量 |int
limit | 查询数据量 |int
start_time |开始时间，秒时间戳|int
end_time |结束时间，秒时间戳|int

##### 响应字段说明

字段名| 说明 
-| :- 
amount| 数量
ctime| 创建时间
deal_fee| 成交手续费
deal_money| 成交金额
deal_stock| 成交资产
id| 订单号
left| 剩余
maker_fee| maker手续费
market| 市场名
ftime| 完成时间
price| 价格
side| 1为ASK卖出，2为BID买入
source|来源
taker_fee| taker手续费
type| 交易类型，1为限价，2为市价
user| 用户编号
---------------------

# 注意事项
* v1版本接口限制为每个IP每分钟最大访问1500次
* 请求Headers 必须添加User-Agent

<font color=red size=3>***若违反以上规则，可能会被禁止访问。并且以上规则可能会产生变化***</font>
