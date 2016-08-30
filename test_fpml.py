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
print(x.toxml("utf-8", element_name='TradeId'))

y = fpml.PartyReference(href="party1")
print(y.toxml("utf-8", element_name='PartyReference'))


ti = fpml.TradeIdentifier(tradeId=[x], partyReference=y, versionedTradeId=None, accountReference=None)
print(ti.tradeId)
print(ti.toxml("utf-8", element_name='TradeIdentifier'))


pti = fpml.PartyTradeIdentifier(tradeId=[x], partyReference=y, versionedTradeId=None, accountReference=None, linkId=None, allocationTradeId=None, blockTradeId=None)

tradeHeader = fpml.TradeHeader(partyTradeIdentifier=[pti], partyTradeInformation=None, tradeDate="2001-10-23", clearedDate=None)
print(tradeHeader.toxml("utf-8", element_name='TradeHeader'))

fxsl = fpml.FxSingleLeg()
print(fxsl.toxml("utf-8", element_name='FxSingleLeg'))



trade = fpml.Trade(tradeHeader=tradeHeader, otherPartyPayment=None, brokerPartyReference=None, determiningParty=None, hedgingParty=None,
                   collateral=None, documentation=None, governingLaw=None, allocations=None, calculationAgent=None, calculationAgentBusinessCenter=None,
                   product=None)
# print(trade.toxml("utf-8", element_name='Trade'))
