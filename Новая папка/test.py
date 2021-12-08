file1 = open("test_pass.txt", "r")
n=0

lines = file1.readlines()
for line in lines:
    a = line.split(':')
    b = a[0].split()
    simbol = b[0]
    rng = b[1].split('-')
    pswrd = a[1]
    k=0
    for i in pswrd:
        if simbol == i:
            k+=1
            if k >= int(rng[0]) and k<=int(rng[1]):
                n+=1
                break
print(n)

file1.close
