# EnergyB-bot
EnergyB-bot is a trading signal reader for cryptocurrency. (TradingView compatible)

## Requirements

* Internet connection
* Gmail account (https://www.google.com/gmail/)
* Bitfinex Account (https://www.bitfinex.com/) - more exchanges coming soon
* Python 3 (https://www.python.org/)
* CCXT Python package (https://github.com/ccxt/ccxt)

## Cryptocurrency list

* Bitcoin
* Ethereum
* EOS
* Litecoin
* Ripple
* Ethereum Classic
* IOTA

## Usage

Enter the information inside the apostrofe:

* /var.py

```
bitfinex_apikey = '' < Bitfinex API key.
bitfinex_secret = '' < Bitfinex API key secret.
imap = '' < IMAP email.
read_email = '' < Email account.
pass_email = '' < Email password.
```

Configure TradingView alerts with the message according the syntax of this bot and run EnergyB-bot.py in Python.

## Email Syntaxe

1. Write 'EnergyB-bot'.
2. Write 'long' for long position or 'short' for short position.
3. Write the trading pair code within the parentheses.
```
'btcusd' for BTC/USD.
'ethusd' for ETH/USD.
'eosusd' for EOS/USD.
'ltcusd' for LTC/USD.
'xrpusd' for XRP/USD.
'etcusd' for ETC/USD.
'iotusd' for IOTA/USD.
```
4. Write the percentage of the balance that will be used within the square brackets.

Example: EnergyB-bot long (btcusd) [5]

## Contribution

```
BTC 1D56RS2GTW8gMFVVJx9DfFTSM5F569mAUw
ETH 0xaEc547E525CB161B094230056676f0bE4B679062
LTC Lbz6b4qS3PsWUqZEentyVN7KnVFa73e2qb
XRP r4QtdtCKz6yRNicxGP2KccxnkBK5XR3wVu
DASH XbnHT1K6ufXWh62CtQPnjjT6wP2jsLg2mA
BNB 0xaEc547E525CB161B094230056676f0bE4B679062
USDT 0xaEc547E525CB161B094230056676f0bE4B679062
TUSD 0xaEc547E525CB161B094230056676f0bE4B679062
```
