age = 18
if age < 18:
    print('Chua du tuoi')
    print('Moi ve')
elif age == 18:
    print('tang free ve')
else:
    print(age, 'Du tuoi roi')
    print('Moi vao xem phim')
    if age % 3 == 0:
        print('nam tuoi')
    else:
        print('nam binh thuong')

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        
print(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

s = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        #print(i)
        s = s + i #lăp
print(s)
