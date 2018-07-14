import os, sys
x = 0
cwd = os.getcwd()
folder = cwd + '\\5'
for filename in os.listdir(folder):
    y = str(x)
    newname = y+".png"
    os.rename(os.path.join(folder, filename), os.path.join(folder, newname))
    x+=1
print 'done'
