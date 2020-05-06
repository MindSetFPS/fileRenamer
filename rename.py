import os 


#/TV Shows/ShowName/Season 02/ShowName – s02e17 – Optional_Info.ext

s = 's01e'

for f in os.listdir():
    if f == "rename.py":
        continue
    f_name, f_ext = os.path.splitext(f)
    la, patrona, num = f_name.split()
    num = num.zfill(3)

    new_name = '{} {} - {}{}{}'.format(la, patrona, s, num, f_ext )

    os.rename(f, new_name)
    # print(f)#
