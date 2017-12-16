#scanning list of 3 values for minimum value. 

#taking list and finding the minimum number using for loop.
x =[]
user = 0
index = 0
run = 0
run2 = 1
var1 = 0
var2 = 0
var3 = 0
num = len(x)
user = int(raw_input("Enter 1st number: "))
user2 = int(raw_input("Enter 2nd number: "))
user3 = int(raw_input("Enter 3rd number: "))
x.append(user)
x.append(user2)
x.append(user3)
print x
for var in x:
    if x[index] <= x[num-run2] and x[index] <= x[num-run]:
        print index
        print num
        print x[num-1]
        print "Min1 is: %s " % x[index]
        run += 1
        run2 += 1
        var1 = x[index]
    elif x[num-run2] < x[num] and x[num-run2] < x[index]:
        print "Min2 is %s" % x[num-run2]
        var2 = x[num-run2]
    else:
        print "Min3 is %s" % x[num]
        var3 = x[num]

index += 1

print "Mininum is: %s " % var1
print "Minimum is: %s " % var2
print "Minimum is: %s " % var3
