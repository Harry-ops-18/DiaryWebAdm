from datetime import datetime

today = datetime.now()
#print(today)
tgl_wkt = today.strftime('%d-%m-%Y %H:%M:%S')
print(tgl_wkt)