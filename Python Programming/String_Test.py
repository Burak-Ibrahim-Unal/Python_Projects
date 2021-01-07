name="Burak Ibrahim Una"
s1="nal"
s2="bur"
s3="Bur"

if name.endswith(s1):
    print("{} ifadesi {} ile biter. ".format(name,s1))
else:
    print("{} ifadesi {} ile bitmez. ".format(name, s1))

if name.startswith(s2):
    print("{} ifadesi {} ile başlar. ".format(name,s2))
else:
    print("{} ifadesi {} ile başlamaz. ".format(name, s2))

if name.startswith(s3):
    print("{} ifadesi {} ile başlar. ".format(name,s3))
else:
    print("{} ifadesi {} ile başlamaz. ".format(name, s3))


print("bu ne{}".format(name.isalpha()))
