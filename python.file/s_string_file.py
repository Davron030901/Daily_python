# from pathlib import Path

# yangi_fayl = Path("yangi_fayl.txt")

# yangi_fayl.touch()

s=input('File nomini kiriting: ')
with open(s, "w") as fayl:
    fayl.write('true')
# import os

# os.mknod("yangi_fa.txt")