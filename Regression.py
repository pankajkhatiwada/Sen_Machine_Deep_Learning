import pandas as pd
import math
import quandl

df = quandl.get("WIKI/GOOGL")
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
df["HCL_PCT"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100

df = df[["Adj. Close", "HCL_PCT", "PCT_change", "Adj. Volume"]]

forecast_col = "Adj. Close"
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))

df["label"] = df[forecast_col].shift(-forecast_col)

print(df.head())