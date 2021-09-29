import pandas as pd
from db_helper import DBhelper
from email_sender import SendMail

db = DBhelper()
em = SendMail()



table = db.import_table()

from_db = []
#formatting database into pandas
for data in table:
  data = list(data)
  from_db.append(data)


columns = ["mcq_id", "hall_name", "tags", "created_at"]
df = pd.DataFrame(from_db, columns=columns)

#formatting dataframe into csv file 
df.to_csv('out.csv', index = False)


em.send_mail('dhakalbibek84@gmail.com')




