import pandas as pd
from dta_pkt.models import Week
from dta_pkt import db
xls = pd.ExcelFile('data.xlsx')
sheet = pd.read_excel(xls, 'data')
df = pd.DataFrame(sheet)

for index, row in df.iterrows():
    entry = Week(dia = row['Dia'] , hora = row['Hora'], act = row['Actividad'])
    db.session.add(entry)
    db.session.commit()
