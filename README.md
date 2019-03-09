# EnergyB-bot
EnergyB-bot is a trading signal reader for cryptocurrency.

## Requirements

* Internet connection
* Email account
* TradingView account (https://tradingview.com/)
* Bitfinex Account (https://www.bitfinex.com/) - more exchanges coming soon
* Python 3.6.8+ (https://www.python.org/)
* CCXT Python package (https://github.com/ccxt/ccxt)

## Cryptocurrency list

* Bitcoin
* Ethereum
* EOS
* Litecoin
* Ripple
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
'iotusd' for IOTA/USD.
```
4. Write the percentage of the balance that will be used within the square brackets.

Example: EnergyB-bot long (btcusd) [5]
