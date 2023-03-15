d={100:"Jaydeep",200:"Jigar",300:"Sunny",400:"Sashank"}

print(d)
d1=d.copy()
print(d1)

print(d.get(400))
print([200])
print(d[200])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(200))
print(d)
d2={500:"Mountain",600:"Peak",700:"Table",800:"Lie"}
d.update(d2)
print(d)
d[900]="Chair"
print(d)

for i in d:
    print(i)
    
for i in d:
    print(i," : ",d[i])
