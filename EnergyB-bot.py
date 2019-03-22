import ccxt
from var import bitfinex_apiKey, bitfinex_secret
from var import imap, read_email, pass_email
import imaplib
import sys
import email
import datetime
import time

###Exchange
bitfinex = ccxt.bitfinex ()
bitfinex.apiKey = bitfinex_apiKey
bitfinex.secret = bitfinex_secret

while True:
    ###Mail
    mail = imaplib.IMAP4_SSL(imap)
    from_email = read_email
    try:
        mail.login(from_email, pass_email)
    except imaplib.IMAP4.error:
        print("Authentication failed.")
        sys.exit()
        
    ###Mark all as read
    mail.select('inbox')
    status, unseen = mail.search(None, '(UNSEEN)')
    unread_msg_nums = unseen[0].split()
    for e_id in unread_msg_nums:
        mail.store(e_id, '+FLAGS', '\Seen')

    ###Read email
    print('Scanning...')
    for stopwatch in range(0,10800):
        try:
            mail.select('inbox')
            status, unseen = mail.search(None, '(UNSEEN)')
            mail.list()
            n = 0
            (retcode, messages) = mail.search(None, '(UNSEEN)')
            if retcode == 'OK':
                for num in messages[0].split():
                    n = n+1
                    typ, data = mail.fetch(num, '(RFC822)')
                    for response_part in data:
                        if isinstance(response_part, tuple):
                            original = email.message_from_bytes(response_part[1])

                            ###Check syntax
                            if original['Subject'].find('EnergyB-bot') >= 0:
                                print(datetime.datetime.now())
                                print(original['From'])
                                print(original['Subject'])
                                
                                ###Check currency
                                if original['Subject'].find('(') >= 0:
                                    if original['Subject'].find(')') >= 0:
                                        c1 = original['Subject'].find('(')+1
                                        c2 = original['Subject'].find(')')
                                        currency = original['Subject'][c1:c2]

                                        ###Check position
                                        reduce_only = 'no'
                                        positions = bitfinex.private_post_positions()
                                        position = bitfinex.filter_by(positions, 'symbol', currency)
                                        amount_position = [position['amount'] for position in position]
                                        a1 = str(amount_position).find("['")+2
                                        a2 = str(amount_position).find("']")
                                        position_amount = str(amount_position)[a1:a2]
                                        if position == []:
                                            position_amount = 0
                                        if original['Subject'].find('long') >= 0:
                                            if float(position_amount) > 0:
                                                reduce_only = 'yes'
                                                print('Reduce only')
                                        if original['Subject'].find('short') >= 0:
                                            if float(position_amount) < 0:
                                                reduce_only = 'yes'
                                                print('Reduce only')

                                        ###Close position
                                        if position != []:
                                            if reduce_only == 'no':
                                                id_position = [position['id'] for position in position]
                                                i1 = str(id_position).find('[')+1
                                                i2 = str(id_position).find(']')
                                                position_id = str(id_position)[i1:i2]
                                                bitfinex.private_post_position_close({'position_id': int(position_id)})

                                        ###Trading
                                        if currency == 'btcusd':
                                            currency = 'BTC/USD'
                                        if currency == 'ethusd':
                                            currency = 'ETH/USD'
                                        if currency == 'eosusd':
                                            currency = 'EOS/USD'
                                        if currency == 'ltcusd':
                                            currency = 'LTC/USD'
                                        if currency == 'xrpusd':
                                            currency = 'XRP/USD'
                                        if currency == 'etcusd':
                                            currency = 'ETC/USD'
                                        if currency == 'iotusd':
                                            currency = 'IOTA/USD'
                                        trading_balance = bitfinex.fetch_balance({'type': 'trading'})
                                        usd = trading_balance['USD']['total']
                                        p1 = original['Subject'].find('[')+1
                                        p2 = original['Subject'].find(']')
                                        percent = original['Subject'][p1:p2]
                                        amount = (usd / bitfinex.fetchTicker(currency)['ask'] * (int(percent) / 100))
                                        if original['Subject'].find('long') >= 0:
                                            if reduce_only != 'yes':
                                                bitfinex.createMarketBuyOrder(currency, amount, {'type': 'market'})
                                        if original['Subject'].find('short') >= 0:
                                            if reduce_only != 'yes':
                                                bitfinex.createMarketSellOrder(currency, amount, {'type': 'market'})
                                        print('Scanning...')

                            ###Mark as read
                            for e_id in unread_msg_nums:
                                mail.store(e_id, '+FLAGS', '\Seen')

            ###Final
            time.sleep(1)
        except mail.abort:
            print("Abort.")
        except e:
            print(e)
