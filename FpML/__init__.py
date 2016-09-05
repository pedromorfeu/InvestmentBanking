class Leg:
    def __init__(self, _ccy, _amount):
        self.ccy = _ccy
        self.amount = _amount

class PartyTradeIdentifier:
    def __init__(self, tradeId):
        self.tradeId = tradeId

class TradeHeader:
    def __init__(self, partyTradeIdentifier, tradeDate):
        self.partyTradeIdentifier = partyTradeIdentifier
        self.tradeDate = tradeDate

class Trade:
    def __init__(self, tradeHeader, fxSingleLeg):
        self.tradeHeader = tradeHeader
        self.fxSingleLeg = fxSingleLeg

class RequestConfirmation:
    def __init__(self, trade):
        self.trade = trade

class ExchangedCurrency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

class QuotedCurrencyPair:
    def __init__(self, currency1, currency2, quoteBasis):
        self.currency1 = currency1
        self.currency2 = currency2
        self.quoteBasis = quoteBasis

class ExchangeRate:
    def __init__(self, quotedCurrencyPair, rate):
        self.quotedCurrencyPair = quotedCurrencyPair
        self.rate = rate

class FxSingleLeg:
    def __init__(self, exchangedCurrency1, exchangedCurrency2, valueDate, exchangeRate):
        self.exchangedCurrency1 = exchangedCurrency1
        self.exchangedCurrency2 = exchangedCurrency2
        self.valueDate = valueDate
        self.exchangeRate = exchangeRate

