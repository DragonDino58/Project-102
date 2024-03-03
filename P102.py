import os, shutil

a = "C:/Users/Maanit Gandhi/OneDrive/Desktop/Whitehatjr/Python/C102"

c = "C:/Users/Maanit Gandhi/OneDrive/Desktop/Whitehatjr/Python/C102/transfer folder"

e = [ '.txt', '.doc', '.docx', '.pdf']


f = os.listdir(a)

for i in f:
    n, x = os.path.splitext(i)
    if(x in e):
        p1 = a+"/"  + i
        p2 = c + "/documents"
        p3 = p2 + "/" + i
        if(os.path.exists(p2)) :
            shutil.move(p1, p3)
        else:
            os.makedirs(p2)   
            shutil.move(p1, p3)