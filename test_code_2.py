# a = {}
# a[1] = {'x':[1,2,3],
#         'y':[2,3,4]}
# print(a[1])
# for i in range(1,10):
#         print(i)
big_data = {}
c = 1
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
for i in range(0,len(a),19):
    x = []
    y = []
    for j in range(i+1,i+10):
        x.append(a[j])
    for h in range(i+10,i+19):
        y.append(a[h])
    print(x)
    print(y)
    big_data[c] = {'x':x,
                   'y':y
                   }
    c = c + 1
    print(i)
print(big_data)