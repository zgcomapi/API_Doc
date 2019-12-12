# REST行情与交易接口 (2019-11-20)
# 基本信息
* 本篇列出REST接口的baseurl **https://api.zg.com**
* 所有接口的响应都是JSON格式
* 所有时间、时间戳均为UNIX时间，单位为毫秒

* 每个接口都有可能抛出异常，异常响应格式如下：
```javascript
{
  "code": -1022,
  "msg": "signature error."
}
```

# 访问限制


# 接口鉴权类型
* 每个接口都有自己的鉴权类型，鉴权类型决定了访问时应当进行何种鉴权
* 如果需要 API-key，应当在HTTP头中以`X-MBX-APIKEY`字段传递
* API-key 与 API-secret 是大小写敏感的


# 需要签名的接口 (TRADE相关)
* 调用这些接口时，除了接口本身所需的参数外，还需要传递`signature`即签名参数。
* 签名使用`HMAC SHA256`算法. API-KEY所对应的API-Secret作为 `HMAC SHA256` 的密钥，其他所有参数作为`HMAC SHA256`的操作对象，得到的输出即为签名。



## POST /api/external/engine/v1/new_order 的示例

以下是在linux bash环境下使用 echo openssl 和curl工具实现的一个调用接口下单的示例
apikey、secret仅供示范

Key | Value
------------ | ------------
apiKey | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
secretKey | NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j


参数 | 取值
------------ | ------------
symbol | BTC_USDT
side | BUY
order_type | LIMIT
quantity | 1
price | 0.1
timestamp | 1499827319559


### 示例: 所有参数需要通过 request body 发送
* **requestBody:** symbol=BTC_USDT&side=BUY&type=LIMITquantity=1&price=0.1&timestamp=1499827319559
* **HMAC SHA256 签名:**

    ```
    [linux]$ echo -n "symbol=BTC_USDT&side=BUY&type=LIMITquantity=1&price=0.1&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    (stdin)= 4c8bdb0a6a05e4403d8e5fbc9a9cd435670dc3a4822ca53216914fb6fe32f3ad
    ```


* **curl 调用:**

    ```
    (HMAC SHA256)
    [linux]$ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.zg.com/api/external/engine/v1/new_order' -d 'symbol=BTC_USDT&side=BUY&type=LIMITquantity=1&price=0.1&timestamp=1499827319559&signature=4c8bdb0a6a05e4403d8e5fbc9a9cd435670dc3a4822ca53216914fb6fe32f3ad'
    ```


## GET /api/external/engine/v1/get_orders的示例

以下是在linux bash环境下使用 echo openssl 和curl工具实现的一个调用接口下单的示例
apikey、secret仅供示范

Key | Value
------------ | ------------
apiKey | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
secretKey | NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j

**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId | LONG | NO |
client_request_id | STRING | NO |
timestamp | LONG | YES |

### 示例 : 所有参数通过 query string 发送
* **queryString:** symbol=BTC_CNZ&timestamp=46234764637&order_id=cfe03b64574240b58baeb61108633927
* **HMAC SHA256 签名:**

    ```
    [linux]$ echo -n "symbol=BTC_CNZ&timestamp=46234764637&order_id=cfe03b64574240b58baeb61108633927" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    (stdin)= 5c68bae55c3a314d3fd65879d932a169d60ff937324ef3e54398d6cfa2ac142b
    ```


* **curl 调用:**

    ```
    (HMAC SHA256)
    [linux]$ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X GET 'https://api.zg.com/api/external/engine/v1/get_orders?symbol=BTC_CNZ&timestamp=46234764637&order_id=cfe03b64574240b58baeb61108633927&signature=5c68bae55c3a314d3fd65879d932a169d60ff937324ef3e54398d6cfa2ac142b'
    ```


# 公开API接口




### 交易对基础信息
```
GET /market/api/v1/symbols
```

**Parameters:**
NONE

**响应:**
```javascript
{
"data":
    [
        {
            "s":"ZG_USDT",//交易对
            "b":"ZG",//币
            "c":"USDT",//交易区
            "q":1,//数量单位
            "p":1,//价格单位
            "m":"1.0000000000",//最小下单金额
            "o":"1000000.0000000000",//最大下单数量
            "l":"2000000",//最大下单价格
            "t":0,//交易状态
            "d":true,//是否显示
            "i":false,//是否是明星币
            "e":""//交易对标签
        }
    ]
}
```

## 行情接口
### 深度信息
```
GET /market/api/v1/depth
```

**参数:**

名称 | 类型 | 是否必须 | 描述
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
limit | INT | NO | 默认 100; 最大 1000. 可选值:[5, 10, 20, 50, 100]


**响应:**
```javascript
{
    "data":
    {
        "last_update_id":48,//更新id(非常重要)
        //买
        "bids":
        [
            ["100","4.99"],
            ["99","2"],
            ["97","1"],
            ["10","40"],
            ["1.2","900"],
            ["1","3"]
        ],
        //卖
        "asks":
        [
            ["104","33.3156"]
        ]
    }
}
```

### 成交记录
```
GET /market/api/v1/historicalTrades
```
获取近期成交

**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
limit | INT | NO | Default 500; max 1000.

**响应:**
```javascript
{
    "data":
    [
        {
            "i":18853,// 消息id
            "e":"trade",// 事件类型
            "E":1574243037,// 事件时间
            "s":"BTC_USDT",// 交易对
            "t":6031718,// 交易ID
            "p":"101.47",// 成交价格
            "q":"18.7222",// 成交数量
            "T":1574243037,// 成交时间
            "d":"BUY",// 成交方向
            "m":false
        }
    ]
}
```


### K线数据
```
GET /market/api/v1/klines
```

**K线间隔,resolution:**
1 -> 1分钟;
5 -> 5分钟;
15 -> 15分钟;
30 -> 30分钟;
60 -> 1小时;
240 -> 4小时;
60 -> 1小时;
240 -> 4小时;
D -> 1天;
5D -> 5天;
7D -> 7天;
30D -> 30天;
**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
resolution | ENUM | YES |
from | LONG | YES |
to | LONG | YES |
limit | INT | YES | Default 500; max 1000.

* 缺省返回最近的数据

**响应:**
```javascript
{
  "data":
  [
    {
      "t":1572307200,
      "c":146.18,
      "o":97.36,
      "h":146.59,
      "l":96,
      "v":814026.4405
    }
  ]
}
```

# 鉴权API接口

### 下单  (TRADE)
```
POST /api/external/engine/v1/new_order (HMAC SHA256)
```

**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
side | INT | YES |
order_type | INT | YES |
quantity | DECIMAL | YES |
price | DECIMAL | NO |
timestamp | LONG | YES |


**响应:**
```javascript
{
    "symbol":"BTC_USDT",//交易对
    "order_id":"9714e0b005c846a0b2be7acb228a485d",//订单id
    "client_request_id":"495db148-0b69-11ea-aa36-8a4452f6fd73",//请求id
    "transactTime":1574235741996//处理时间
}
```



### 查询订单 (USER_DATA)
```
GET /api/external/engine/v1/get_orders (HMAC SHA256)
```
**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId | LONG | NO |
client_request_id | STRING | NO |
timestamp | LONG | YES |

注意:
* 至少需要发送 `orderId` 与 `client_request_id`中的一个


**响应:**
```javascript
{
    "symbol":"BTC_CNZ",//交易对
    "order_id":"cfe03b64574240b58baeb61108633927",//订单id
    "client_request_id":"c8987fce-0092-11ea-96bd-1ea1c892e80d",//请求id
    "price":"10",//委托价格
    "orig_qty":"1",//委托数量
    "executed_qty":"1",//成交数量
    "cummulative_quote_qty":"0",
    "status":"NEW",//订单状态
    "type":"LIMIT",//订单类型
    "side":"BUY",//买卖方向
    "time":1573044102096,//订单生成时间
    "update_time":1573044102096//订单更新时间
}
```

### 撤销订单 (TRADE)
```
POST /api/external/engine/v1/cancel_order  (HMAC SHA256)
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId | LONG | YES |
timestamp | LONG | YES |


**响应:**
```javascript
{
  "symbol": "LTC_BTC",//交易对
  "order_id": "cfe03b64574240b58baeb61108633927",//订单id
  "client_request_id": "c8987fce-0092-11ea-96bd-1ea1c892e80d",//请求id
  "price": "1.00000000",//委托价格
  "orig_qty": "10.00000000",//委托数量
  "executed_qty": "8.00000000",//成交数量
  "order_type": "LIMIT",//订单类型
  "side": "SELL",//买卖方向
  "transactTime": 1507725176595//处理时间
}
```

### 查看账户当前挂单 (USER_DATA)
```
GET /api/external/engine/v1/get_open_orders  (HMAC SHA256)
```

**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | NO |
timestamp | LONG | YES |

* 不带symbol参数，会返回所有交易对的挂单

**响应:**
```javascript
[
    {
        "symbol":"BTC_CNZ",//交易对
        "order_id":"06a53678af544b99b3a3917e6b748db5",//订单id
        "client_request_id":"b88eb3b1-0161-11ea-b8b5-52ccdae897ca",//请求id
        "price":"10",//委托价格
        "orig_qty":"1",//委托数量
        "executed_qty":"1",//成交数量
        "cummulative_quote_qty":"0",
        "status":"NEW",//订单状态
        "type":"LIMIT",//订单类型
        "side":"BUY",//买卖方向
        "time":1573132980938,//订单生成时间
        "update_time":1573132980938//订单更新时间
    }
]
```

### 查询所有订单（包括历史订单） (USER_DATA)
```
GET /api/external/engine/v1/get_all_orders (HMAC SHA256)
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
startTime | LONG | NO |
endTime | LONG | NO |
limit | INT | YES | Default 500; max 1000.
timestamp | LONG | YES |

**响应:**
```javascript
[
    {
        "symbol":"BTC_CNZ",//交易对
        "order_id":"06a53678af544b99b3a3917e6b748db5",//订单id
        "client_request_id":"b88eb3b1-0161-11ea-b8b5-52ccdae897ca",//请求id
        "price":"10",//委托价格
        "orig_qty":"1",//委托数量
        "executed_qty":"1",//成交数量
        "cummulative_quote_qty":"0",
        "status":"NEW",//订单状态
        "type":"LIMIT",//订单类型
        "side":"BUY",//买卖方向
        "time":1573132980938,//订单生成时间
        "update_time":1573132980938//订单更新时间
    }
]
```

### 查询账户资产信息 (USER_DATA)
```
GET /api/external/engine/v1/get_balance (HMAC SHA256)
```

**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
timestamp | LONG | YES |

**响应:**
```javascript
{
    "can_trade":true,//能否交易
    "can_withdraw":true,//能否提现
    "can_deposit":true,//能否充值
    "balances":
    [
        {
            "asset":"BTC",//币
            "free":"6.93296215",//可用数量
            "locked":"0"//冻结数量
        },
    ]
}
```

### 账户成交历史 (USER_DATA)
```
GET /api/external/engine/v1/get_trades (HMAC SHA256)
```
获取某交易对的成交历史


**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
start_time | LONG | NO |
end_time | LONG | NO |
order_id | STRING | NO |
limit | YES | NO | Default 500; max 1000.
timestamp | LONG | YES |

**响应:**
```javascript
[
    {
        "symbol":"BTC_CNZ",//交易对
        "id":"2918657",//成交id
        "order_id":"2bac0d533ec2455383d6f6bb1d1beb74",//订单id
        "price":"100",//成交价格
        "qty":"1",////成交数量
        "commission":"0",//手续费
        "commission_asset":"",//手续费币种
        "time":1569833792295,//成交时间
        "is_buyer":false,//是否是buyer
        "is_maker":true//是否是maker
    }
]
```
