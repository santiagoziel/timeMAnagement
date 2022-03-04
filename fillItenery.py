import pandas as pd
from dta_pkt.models import Moment
from dta_pkt import db
xls = pd.ExcelFile('data.xlsx')
sheet = pd.read_excel(xls, 'data2')
df = pd.DataFrame(sheet)

for index, row in df.iterrows():
    entry = Moment(dia = row['Dia'] , hora = row['Hora'], act = row['Actividad'], user_id = 2)
    db.session.add(entry)
    db.session.commit()
