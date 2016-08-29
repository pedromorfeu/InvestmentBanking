from FpML import Leg, fpml

import os
import sys

# x = Leg(2, 3)
# print(x)
# print(x.ccy)
# print(x.amount)

trade = fpml.Trade(fpml.TradeHeader(fpml.PartyTradeIdentifier()))
print(trade)
print(type(trade.tradeHeader.partyTradeIdentifier))
print(trade.tradeHeader.partyTradeIdentifier)

trade.tradeHeader.partyTradeIdentifier.tradeId = fpml.TradeId()
print(type(trade.tradeHeader.partyTradeIdentifier.tradeId.id))
print(trade.tradeHeader.partyTradeIdentifier.tradeId.id)

x = fpml.TradeId("EUR", tradeIdScheme = "http://www.citi.com/fx/trade-id")
# x.tradeIdScheme = "http://www.citi.com/fx/trade-id"
print(x.toxml("utf-8", element_name='TradeId'))
