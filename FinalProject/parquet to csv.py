# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 15:52:44 2025

@author: drewm
"""
from pathlib import Path
import pandas as pd

here = Path(__file__).parent
input = here / "Data" / "fhvhv_tripdata_2025-01.parquet"
output = here / "Data" / "high volume paid trip records.csv"

print(f"Reading from: {input}")
# https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page "High Volume For-Hire Vehicle Trip Records"
df = pd.read_parquet(input, engine='fastparquet')

print(f"Writing to: {output}")
df.to_csv(output)

print("Process complete!")