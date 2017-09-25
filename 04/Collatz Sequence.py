def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return number*3+1

x = int(input('Enter number:'))
if x == 1:
    print (x)
while x > 1:
    print (collatz(x))
    x = collatz(x)
if x < 1:
    print ('The number is less than 1, I don"t care')
