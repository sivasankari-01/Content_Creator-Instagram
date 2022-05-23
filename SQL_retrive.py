# Load Streamlit library

import pandas as pd
import csv
from sqlalchemy import create_engine
csv_reading = csv.reader(
    open('C:/Users/sivasankari/Downloads/Snipfeed/read/data/final scrap.csv', 'r', encoding="cp437"))
for row in csv_reading:
    engine = create_engine('sqlite://', echo=False)
    d = pd.read_csv('C:/Users/sivasankari/Downloads/Snipfeed/read/data/final scrap.csv', encoding="cp437")
    d.to_sql('Pred_Data', con=engine)
    result= engine.execute("SELECT COUNT (profileUrl)FROM Pred_Data where followersCount <= 5000").fetchall()
    b = ''.join(str(result).split(','))
    print(b[2:5])
    break

