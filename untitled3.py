import matplotlib .pyplot as plt
import psutil as p
anl=[]
anpl=[]
empty={}
i=0
for process in p.process_iter():
    i=i+1
    if i <= 6:
        name=process.name()
        cu = p.cpu_percent()
        print("Name: " + name + ". Usage: " + str(cu) + ".")
        empty.update({name:cu})
        anl.append(name)
        anpl.append(cu)
plt.figure(figsize = (15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(anl, anpl, width = 0.6, color=("purple", "green", "red", "blue", "orange", "pink"))
plt.show()
print(anl)
print(anpl)
maxi = max(empty,key=empty.get)
print(maxi)
mini = min(empty,key=empty.get)
print(mini)
maxu = empty.values()
maxuu=max(maxu)
print(maxuu)
minu=empty.values()
minuu=min(minu)
print(minuu)