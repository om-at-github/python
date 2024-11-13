# python cylinder_area_volume.py #

r = float(input("enter the r"))
h = float(input("enter the h"))

surface_area = 2*3.14*r*r+2*3.14*r*h
volume = 3.14*r*r*h

print(surface_area)
print(volume)