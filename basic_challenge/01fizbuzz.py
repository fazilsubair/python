# fizubzz
# if a number is divisible by 3 , print fizz
# if a number is divisible by 5, print buzz
# if a number is divisible by both 3 & 5 , print fizzbuzz

for i in range(1,101):
    
    # number =  int(input("enter a number "))

    if (i%3==0 and i%5==0):
        print("fizzBuzz " , i)
    elif (i%3==0) :
        print("Fizz ", i)
    elif (i%5==0) :
        print("Bizz ", i)