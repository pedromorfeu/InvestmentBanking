from FpML import *

x = RequestConfirmation(
    Trade(
        TradeHeader(
            PartyTradeIdentifier("TRADEID_1000"),
            "2001-10-23"),
        FxSingleLeg(
            ExchangedCurrency("GBP",10000000),
            ExchangedCurrency("USD", 14800000),
            "2011-10-25",
            ExchangeRate(
                QuotedCurrencyPair(
                    "GBP", "USD", "Currency2PerCurrency1"
                ),
                1.48
            ))))

print(x)