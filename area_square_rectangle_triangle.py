# python area_square_rectangle_triangle.py #

print("1.area of square")
print("2.area of rectangle")
print("3.area of triangle")
print("enter the ch")
ch = int(input())
match ch:
       case 1 :
              side=int(input("enter the side of square"))
              areaofsquare=side*side
              print("area of square",areaofsquare)
       case 2:
              length=int(input("enter the length of rectangle"))       
              breath=int(input("enter the breath of rectangle"))
              areaofrectangle=length*breath
              print("area of rectangle = ",areaofrectangle)
       case 3:
              base=int(input("enter the base of triangle"))       
              height=int(input("enter the height of triangle"))  
              areaoftriangle=(1/2)*base*height    
              print("area of triangle = ",areaoftriangle) 