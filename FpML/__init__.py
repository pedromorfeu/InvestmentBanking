class Leg:
    def __init__(self, _ccy, _amount):
        self.ccy = _ccy
        self.amount = _amount

class PartyTradeIdentifier:
    tradeId = ""
    def __init__(self, tradeId):
        self.tradeId = tradeId

class TradeHeader:
    pti = None
    tradeDate = ""
    def __init__(self, pti, tradeDate):
        self.pti = pti
        self.tradeDate = tradeDate

class Trade:
    th = None
    fxSingleLeg = None
    def __init__(self, th, fxSingleLeg):
        self.th = th
        self.fxSingleLeg = fxSingleLeg

class RequestConfirmation:
    trade = None
    def __init__(self, trade):
        self.trade = trade

class ExchangedCurrency:
    currency = ""
    amount = ""
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

class QuotedCurrencyPair:
    currency1 = ""
    currency2 = ""
    quoteBasis = ""
    def __init__(self, currency1, currency2, quoteBasis):
        self.currency1 = currency1
        self.currency2 = currency2
        self.quoteBasis = quoteBasis

class ExchangeRate:
    qcp = None
    rate = ""
    def __init__(self, qcp, rate):
        self.qcp = qcp
        self.rate = rate

class FxSingleLeg:
    exchangedCurrency1 = None
    exchangedCurrency2 = None
    valueDate = ""
    exchangeRate = None
    def __init__(self, exchangedCurrency1, exchangedCurrency2, valueDate, exchangeRate):
        self.exchangedCurrency1 = exchangedCurrency1
        self.exchangedCurrency2 = exchangedCurrency2
        self.valueDate = valueDate
        self.exchangeRate = exchangeRate

