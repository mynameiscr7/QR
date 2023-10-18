from MyQR import myqr
import os
import datetime

url = "https://1.1.1.1/desktopQR?seat="
path = f"{os.environ['USERPROFILE']}\\Desktop\\qr\\"
if not os.path.exists(path):
    os.makedirs(path)
print(datetime.datetime.now())
with open('seat.txt', 'r', encoding='utf-8') as fr:
    for seat in fr.readlines():
        seat = seat.strip()
        #print(seat)
        myqr.run(
            words=f'{url}{seat}',
            save_name=f"{seat}.png",
            save_dir=path,
            # picture="工位标识.png",
            colorized=True,
        )
print(datetime.datetime.now())
