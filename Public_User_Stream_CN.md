# Websocket账户接口 (2019-12-12)

# 基本信息
* 本篇所列出REST接口的baseurl **wss://stream.zg.com/connect**
* 发送ws消息 {"type":"\<listenKey\>@userDataStream"}完成订阅
* 每个到stream.zg.com的链接有效期不超过24小时，请妥善处理断线重连。
* 账户数据流的消息**不保证**严格时间序; **请使用 E 字段进行排序**

# 与Websocket账户接口相关的REST接口

## 生成listenKey
```
POST /api/external/engine/v1/create_listenkey
```
创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。


#鉴权参考restful签名api
**参数:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
timestamp | LONG | YES |

**响应:**
```javascript
{
  "listen_key": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"
}
```

# websocket推送事件

## 账户更新
账户更新事件的 event type 固定为 `outboundAccountInfo`
当账户信息有变动时，会推送此事件

**Payload:**
```javascript
{
"e":"outboundAccountInfo", // 事件类型
"E":1576744500562, // 事件时间
"m":0,  // 挂单费率
"t":0, // 吃单费率
"T":true,// 是否允许交易
"W":true, // 是否允许提现
"D":true, // 是否允许充值
"u":1576744499968,  // 账户末次更新时间戳
"B":
  [
    {
      "a":"BCD",// 资产名称
      "f":"0.17682716",  // 可用余额
      "l":"0.00000000" // 冻结余额
    },
    {
      "a":"AMIO",
      "f":"0.07554569",
      "l":"0.00000000"
    }        
  ]
}
```

## 订单/交易 更新
当有新订单创建、订单有新成交或者新的状态变化时会推送此类事件

event type统一为 `executionReport`

具体内容需要读取 `x`字段 判断执行类型


**Payload:**
```javascript
{
    "e":"execution_report", // 事件类型
    "E":1576137067374,// 事件时间
    "s":"ZG_USDT",// 交易对
    "S":"SELL",// 订单方向
    "o":"LIMIT",// 订单类型
    "q":"24867.7",// 订单原始数量
    "p":"0.008",// 订单原始价格
    "X":"NEW",// 订单的当前状态
    "r":"", // 订单被拒绝的原因
    "i":"13baee9c705d43898ec9d0cb76d799c9",// 订单ID
    "z":"0",// 订单累计已成交数量
    "O":1576137067374// 订单创建时间
}
```

**可能的执行类型:**

* NEW 新订单
* CANCELED 订单被取消
* REJECTED 新订单被拒绝
* TRADE 订单有新成交
