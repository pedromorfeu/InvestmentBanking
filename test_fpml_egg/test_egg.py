import sys

egg_path="FpML-0.0.3-py3.5.egg"

sys.path.append(egg_path)

from FpML import Leg, fpml

import os
import sys

x = Leg(2, 3)
print(x)
print(x.ccy)
print(x.amount)

print(os.getcwd())

x = fpml.ValuationDocument()
print(x)


partyTradeIdentifier = fpml.PartyTradeIdentifier()
partyTradeIdentifier.tradeId = "10"
print(partyTradeIdentifier.tradeId)

# partyTradeIdentifier1 = fpml.PartyTradeIdentifier(tradeId = "10", partyReference = "20")
# print(partyTradeIdentifier1.tradeId)

tradeHeader = fpml.TradeHeader()
print(tradeHeader)


trade = fpml.Trade(tradeHeader)
print(trade.tradeHeader)

tradeAll = fpml.Trade(fpml.TradeHeader(fpml.PartyTradeIdentifier(tradeId = "10")))
print(tradeAll.tradeHeader.partyTradeIdentifier)