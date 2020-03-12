from py_weernl import weerLive

place = "Den Haag"
my_api = ""
w = weerLive(api=my_api)

data = w.getData(place)
print(data)
