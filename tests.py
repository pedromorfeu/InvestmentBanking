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

