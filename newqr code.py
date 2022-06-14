import qrcode
import random as r
link=input("enter the musseg or link ")
print(dir(r))
randr=r.randint(1,1000)
#print(randr)
img=qrcode.make(link)
#img.save("D:\varad\qr.png") you can't give the path of the in open folder
x=str(randr)
#print(type(x))
z="D:\qr"+x+".png"
#print(type(z))
img.save(z)
