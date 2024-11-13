# python area_volume_cricumferce_circle_sphere.py #

r = int(input("enter the radius"))
print("1. area of circle")
print("2. circumference of circle")
print("3. volume of sphere")
ch = int(input("enter the ch"))
match ch :
        case 1 :
                areaofcircle=r*r
                print("area of circle = ",areaofcircle)
        case 2 :
                circumferenceofcircle=2*3.14*r
                print("circumference of circle = ",circumferenceofcircle)
        case 3 :
                volumeofsphere=(4/3)*3.14*r*r*r 
                print("volume of sphere = ",volumeofsphere)
        case _:
              print("default value")        