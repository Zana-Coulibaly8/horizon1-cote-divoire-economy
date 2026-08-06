import wbdata
import pandas as pd
from datetime import datetime

# Define country
country = "CIV"

# Define indicators
indicators = {
    "NY.GDP.MKTP.KD.ZG": "GDP_Growth",
    "FP.CPI.TOTL.ZG": "Inflation",
    "SP.POP.TOTL": "Population"
}

# Define time period
start_date = datetime(2010, 1, 1)
end_date = datetime(2024, 12, 31)

# Retrieve data from World Bank
data = wbdata.get_dataframe(
    indicators,
    country=country,
    date=(start_date, end_date)
)

# Reset index
data = data.reset_index()

# Display first rows
print(data.head())
