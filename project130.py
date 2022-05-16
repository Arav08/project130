import pandas as pd
import csv

df = pd.read_csv("dwarf_merged.csv")

print(df.shape)

df.to_csv("dwarf_merged_2.csv")