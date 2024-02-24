'''name = "Shubham"
age = 14

print("NAME:-",name)
print("AGE:-",age)'''




"""
firstname = "Tony"
lastname = "Stark"
age = 51

is_genius = True

print("Name:-" + firstname , lastname)
print("Age:-" , age)
print("Tony is genius:-" , is_genius)"""





"""name = input("What is your name?")
print("My name is " + name)"""





"""super = input("What is your Superhero name?")

print("My Superhero name is " + super)"""





"""old_age = input("Enter your Birth Year:")
new_age = input("Enter Present Year:")
print ("You are " , int(new_age) - int(old_age) , "year old." )"""





"""rint = "Techpath"

print(rint.upper())
print(rint.swapcase())"""





"""find = "Techpath . biz"

print(find.find("i"))"""





"""replace = "Techpath . biz"

print(replace.replace(" . biz" , "Coding Center"))"""





"""findTF = "Techpath . biz"

print("k" in findTF)
"""




"""x = 10
y = 2

print(x ** y)"""




"""x = 10
x *= 2

print(x)"""





"""result = 2 * 5 // 2 
print (result)"""




"""print(3 >= 3)"""



"""a = int(input("enter your percentage: "))

if a <= 0:
    print("Error percentage between 0 to 100")
elif a <= 20:
    print("Bad")
elif a <= 40:
    print("Good")
elif a <= 60:
    print("Very Good")
elif a <= 80:
    print("Excellent")
elif a <= 100:
    print("Outstanding")
else:
    print("Error percentage between 0 to 100")"""



"""i = 20
while i >= 2:
    print(i * "*")
    i = i - 2"""

"""a = int(input("Enter your First value : "))
b = input("Enter your Operator / , * , + , - : ")
c = int(input("Enter your Second value : "))

if b == "/":
   print(int(a / c))
elif b == "*":
   print(int(a * c))
elif b == "+":
   print(int(a + c))
else:
   print(int(a - c))"""


"""for a in range (20):
   print(a * 2 + 2)"""

"""a = {"Apple" , "Banana" , "Mango" , "Orange"}
print(a)
"""

"""a = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus assumenda accusamus ipsam consequuntur praesentium dolores, provident consectetur quis ullam neque iusto eos. Minima nam cumque consectetur suscipit non, deleniti quos."
print(len(a))"""


'''a = 'hello'
b = 'world'
c= a + ' ' + b
print(c)'''

"""age = 34
text = "my name is abcd, i am {} "
print(text.format(age))"""

"""a = 200
b = 303

if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")"""

"""x = "hello"
y = "14"
print(bool(y))
print(bool(x))"""

"""a = int(input("Enter your First Value :"))
b = input("Enter your operator : / , * , + , - :")
c = int(input("Enter your Second Value :"))

if b == "/":
    print(int(a / c))
elif b == "*":
    print(int(a * c))
elif b == "+":
    print(int(a + c))
else:
    print(int(a - c))"""
"""fruits = ["apple" , "banana" , "car" , "den"]
#list = [x for x in range(11) if x>5]
#newlist = [x.upper() for x in fruits]
#newlist = ['bad' for x  in fruits]
fruits.remove("apple") 
print(fruits)"""

"""fruits = ["apple" , "banana" ,"cherry" ,"kiwi" , "orange"]
newlist = [x for x in fruits if x != "i"]

print(newlist)        """

"""thelist =["apple" , "banana" , "cherry"]
[print (x) for x in range(11) if x<=3]"""



"""print ("Enter your marks 0 to 40")
h = int(input("Enter your HINDI marks : "))
e = int(input("Enter your ENGLISH marks : "))
m = int(input("Enter your MATH marks : "))
s = int(input("Enter your SCIENCE marks : "))
ss = int(input("Enter your SOCIAL SCIENCE marks : "))
san = int(input("Enter your SANSKRIT marks : "))
tm = int(h+e+m+s+ss+san)
print("total number : " , tm)
tp = (int(tm) / 240)*100
print("Your percentage : " , tp)

if tp <= 0:
    print("Error Your marks 0 to 40")
elif tp <= 25:
    print("Grade : Fail")
elif tp <= 50:
    print("Grade : Third")
elif tp <= 75:
    print("Grade : Second")
elif tp <= 100:
    print("Grade : First")
else:
    print("Error Your marks 0 to 40")"""



"""x = range(10)

for n in x:
    print(n*2+2)"""


'''import datetime

x = datetime.datetime.now()
print(x)
y = datetime.datetime.now().weekday()
z = "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"  
print(y[z])'''

"""def my_name(a , b):
    sum = a + b
    print(sum)
    return sum

print("print sum a and b")
my_name(52,8) #function call"""

"""def avrage (x,y,z):
    sum = (x+y+z)/3
    print(sum)
    return sum

avrage(5,8,5) """

# print("Shubham",end=" AND ")
# print("Gaurav")

"""def mu_value(a=1,b=10):
    intu = a * b
    print(intu)
    return intu

mu_value()"""

"""a = ["apple", "mango", "banana", "city", "uttar predesh","lohata"]
b = ["apple", "mango", "banana", "city", "uttar predesh","lohata", "hello" , "why"]

def length(length):
    print(len(length))
    return print

length(b)"""

"""a = ["apple", "mango", "banana", "city", "uttar predesh","lohata"]
b = ["apple", "mango", "banana", "city", "uttar predesh","lohata", "hello" , "why"]

def my_list(list):
    for item in list:
        print(item, end=" ")

my_list(b)"""
"""def my_table (*z):
  for a in range(0,10):
    v = a * z + z
    print(v)

my_table(2)"""

"""def dolor(x):
    inr = inr * 83.05
    print(x)
    return x

dolor(20)"""

"""def my_name(a,b):
  v=(a*b)/(a+b)
  print(v)

my_name(5,5)"""

"""num = int(input("enter your number : "))
status = 0

for i in range(2,num):
    if(num % i == 0):
        status = 1
        break

if status == 0:
       print("Prime")
else:
       print("Not Prime")"""

"""def prime(a,status=0):

  for i in range(2,a):
     if(a % i == 0):
        status = 1
        break

  if status == 0:
       print("Prime")
  else:
       print("Not Prime")

prime(input("Enter your number : "))"""



"""def calaulate_avrage (num):
    sum = 0
    for i in num:
        sum += i
    a = sum / (len(num))
    return a

print(calaulate_avrage([2,3,2,3,5]))"""



"""def check_even_odd(argument):

    if (argument % 2 == 0):
        print("Even")
    else:
        print("Odd")   



check_even_odd(23)"""

"""def convert_Temprature(x):
    F = (9/5 * x) + 32
    return F
  

print(convert_Temprature(20))"""

"""def calculate_factorial(i):
    """

"""def find_maximum(x):
    y = max(x)
    print(y)

find_maximum([10,25,5,110,45,1,20,1,0])"""

"""def is_prime(a,count=0):
    for i in range(2,a):
        if (a % i == 0):
            count = 1
            break
    if count == 0:
        print("True")
    else:
        print("False")

is_prime(12)"""

"""def sort_list(integer):
    integer.sort()
    print(integer)
    return sort_list

sort_list([1,5,3,2,4])"""


"""def reverse_string(string):
    string.reverse()
    print(string)

reverse_string(["apple","Mango","Banana"])"""


'''def calculate_power(a,b):
    c = a**b
    print(c)

calculate_power( 2 , 3)'''


"""def calculate_factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial 
    
print(calculate_factorial(3))""" 


    

"""def reverse_string(str):
    for i in str:
      a = str[::-1]
      print(a)
      break

reverse_string(["Shubham","Adarsh","Unnat","Karan","Vedant","Sunny"])"""


"""def check_even_odd_convert_Temprature(eo,status=0,factorial=1):
    
    f = (9/5 * eo) + 32
    print(f)
    if f % 2 == 0:
        print("Even")
    else:
        print("Odd")
    for i in range(2,eo):
        if (eo % i == 0):
            status = 1
            break

    if status == 0:
        print("Prime")
    else:
        print("Not Prime")

    for i in range(1,eo+1):
        factorial = factorial * i
    print(factorial)


check_even_odd_convert_Temprature(3)"""


"""def word_count(a):
    a = len(a)
    print (a)

word_count(input("Enter your words : "))"""

'''def area(a,b,c):
  s = (a+b+c)/2

  import math
  d = math.sqrt(s*(s-a)*(s-b)*(s-c))
  print(d)

area(2,3,4)'''

'''def prime(num, count=0):
    for i in range(2,num):
       if (num % i == 0):
           count = 1
           break 

    if count == 0:
        print("Prime")
    else:
        print("Not Prime")

prime(25)'''
       
'''def palidrome_check(a):
    b = a[::-1]
    if a == b:
        print("This is PALIDROME")
    else:
        print("This is no PALIDROME")

palidrome_check("malayalam")'''

'''def anagram_Check(a,b):
    c = str(a.split())
    d = str(b.split())
    if c == d:
        print("YES")
    else:
        print("NO")

anagram_Check("listen","silent")'''

'''double = lambda b:b*2

print(double(6))

cube = lambda b:b*b*b
print(cube(2))

def double_cube(a,b):
    x = a*b
    print(x)

double_cube(cube(20),cube(25))'''

"""sales = {500:"india",400:"China",300:"Us",000:"ps",-200:"vs"}

a = sorted(sales)
print(a)"""

'''a = int(input("Enter you FIRST number : "))
b = input("Enter your oprator :- /,*,+,- : ")
c = int(input("Enter your SECOND number : "))

if b == "/":
    print(a / c)
elif b == "*":
    print(a * c)
elif b == "+":
    print(a + c)
else:
    print(a - c)'''

'''x = "Q. What is the Capital of INDIA?"
a = "A. U.P."
b = "B. Delhi"
c = "C. Luckhnow"
d = "D. Varanasi"
f = x,a,b,c,d,
for i in f:
    print(i)

x = input("Your Answer :- a,b,c,d : ")

if x == "b":
    print("Corrrct Answer")
else:
    print("Wrong Answer")'''

'''# First Question
x = "Q. What is the Capital of INDIA?"
f = "A. u.p.","B. delhi","C. luckhnow","D. varanasi"
print(x)
for i in f:
    print(i)


x = input("Your Answer :- a,b,c,d : ")


if x == "b":
    c = "Corrrect Answer"
    print(c)
    if c == "Correct Answer":
        print("You Win 1cr.")
else:
    w = "Wrong Answer"
    print(w)
    if w == "Wrong Answer":
        print("You Win 0.")

y = input("Next Qoestion :- Yes,No : ")

# Second Question
if y == "Yes":
    x = "Q. What is the Capital of PAKISTAN?"
    f = "A. karachi","B. lahore","C. punjab","D. pulgama"
    print(x)

    for i in f:
       print(i)
    
    x = input("Your Answer :- a,b,c,d : ")
    if x == "b":
      c = "Corrrect Answer"
      print(c)
      if c == "Correct Answer":
        print("You Win 1cr.")
    else:
         w = "Wrong Answer"
         print(w)
         if w == "Wrong Answer":
            print("You Win 0.")

# Third Question
if y == "Yes":
    x = "Q. What is the Capital of PAKISTAN?"
    f = "A. karachi","B. lahore","C. punjab","D. pulgama"
    print(x)

    for i in f:
       print(i)
    
    x = input("Your Answer :- a,b,c,d : ")
    if x == "b":
      c = "Corrrect Answer"
      print(c)
      if c == "Correct Answer":
        print("You Win 1cr.")
    else:
         w = "Wrong Answer"
         print(w)
         if w == "Wrong Answer":
            print("You Win 0.")

# Forth Question
if y == "Yes":
    x = "Q. What is the Capital of PAKISTAN?"
    f = "A. karachi","B. lahore","C. punjab","D. pulgama"
    print(x)

    for i in f:
       print(i)
    
    x = input("Your Answer :- a,b,c,d : ")
    if x == "b":
      c = "Corrrect Answer"
      print(c)
      if c == "Correct Answer":
        print("You Win 1cr.")
    else:
         w = "Wrong Answer"
         print(w)
         if w == "Wrong Answer":
            print("You Win 0.")

# Fifth Question
if y == "Yes":
    x = "Q. What is the Capital of PAKISTAN?"
    f = "A. karachi","B. lahore","C. punjab","D. pulgama"
    print(x)

    for i in f:
       print(i)
    10
 .054130574530542   x = input("Your Answer :- a,b,c,d : ")
    if x == "b":
      c = "Corrrect Answer"
      print(c)
      if c == "Correct Answer":
        print("You Win 1cr.")
    else:
         w = "Wrong Answer"
         print(w)
         if w == "Wrong Answer":
            print("You Win 0.") '''         

'''time = int(input("Enter Your Time : "))

if time in range(6,12):
    print("Good Morning")
elif time in range(12,15):
    print("Good Afternoon")
elif time in range(15,18):
    print("Good Evening")
else:
    print("Good Night")'''

'''import datetime

x = datetime.datetime.now()
print(x)
y = datetime.datetime.now().weekday()
z = "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
print(y[z]) '''

'''def Question(x):
    f = "A. u.p.","B. delhi","C. luckhnow","D. varanasi"
    print(x)
    for i in f:
      print(i)


    x = input("Your Answer :- a,b,c,d : ")


    if x == "b":
       c = "Corrrect Answer"
       print(c)
       if c == "Correct Answer":
          print("You Win 1cr.")
    else:
       w = "Wrong Answer"
       print(w)
       if w == "Wrong Answer":
        print("You Win 0.")

Question("Q. What is the Capital of INDIA?")'''

'''def prime_number(a,b):
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num): 
                if (num % i == 0):
                   break
            else:
                  print(num) 

prime_number(1,150)'''

'''n = int(input("Enter your number : "))

if n % 2 != 0:
    print("Weird")
elif n > 2 and n < 5:    
    if n % 2 == 0:
       print("Not Weird")
elif n > 6 and n < 20:
    if n % 2 == 0:
       print("Weird")
elif n > 20:
    if n % 2 == 0:
       print("Not Weird")'''

'''n = int(input("Enter : "))
if 1 < n < 20:
    for i in range(0,n):
        print(i*i)'''

"""def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        print(True)
    elif year % 100 != 0:
        print(False)
    elif year % 400 == 0:
            print(True)

    
    return leap

year = int(input())
print(is_leap(year))"""


'''if __name__ == '__main__':
    
        name = [['Shubham',10],['akshit',20],['Manish',30]]
        for x in name:
           Find_score=[x[1]]
        
           score = sorted(set(Find_score))
           for  n in score:
                 n = [n[1]]
                 print(n)

'''
'''j=int(input("Enter the value : "))
a = 0
b = 1
if (j>=0):
    print("you fibonaaaci series is ",a,b)
    for i in range (20):
      c = a + b
      print("you fibonaaaci series is ",c,end="")
      a = b
      b = c'''

a = str(9956007654)
'''for i in a:
    a = a[::-1]
    print(a)
    break'''
'''while len(a) > -1:
    print(a)
    break'''

'''rev_num = 0
num = int(input("Enter Your Number : "))
while num != 0:
    number = num % 10
    rev = rev_num*10+number
    num //= 10
    print(rev)'''

'''for i in range(10):
    i = i + 1
    print(i)'''

"""a = int(input("Enter the number : "))
if a == 1 :
    print("Not prime number")
if a>1:
    for i in range(2,a):
        if a % 2 == 0:
            print(a," is not prime number")
            break

        else:
            print(a," is prime number")
            break"""


"""def fibonacci(n):
    if n < 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return[0,1]
    a = fibonacci (n-1)
    a.append(a[-1]+a[-2])
    return a
print(fibonacci(int(input("Enter your number : "))))
    """

# def addition(num1, num2):
#     return num1 + num2

# def subtraction(num1, num2):
#     return num1 - num2

# def multiplication(num1, num2):
#     return num1 * num2

# def division(num1, num2):
#     if num2 == 0:
#         return "Error"
#     return num1 / num2

# def modulo(num1, num2):
#     return num1 % num2

# def default(num1, num2):
#     return "incorrect operation"

# operation = {
#     "add": addition,
#     "sub": subtraction,
#     "multi": multiplication,
#     "div": division,
#     "mod": modulo,
    
# }

# def calculator():
#     print("""You can perform operation
#           1. Add
#           2. Subtract
#           3. Multiply
#           4. Divide
#           5. Modulo""")

#     choice = input("Select operation: ")
#     if choice not in operation:
#         print("Invalid choice")
#         return

#     num1 = float(input("Enter First number: "))
#     num2 = float(input("Enter Second number: "))

#     result = operation[choice](num1, num2)
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     calculator()

"""rev_num = 0
num = int(input("Enter Your Number : "))
while num != 0:
    number = num % 10
    rev = rev_num*10+number
    num //= 10
    print(rev)"""

"""def prime(a):
    b = 0
    for i in range(2,a):
        if a % i == 0:
            b = 1
            break

    if b == 0:
        print("prime")
    else:
        print("Not prime")

prime(29)
"""
"""def fibonacci(num):
    a = 0
    b = 1
    print(a)
    for i in range(num):
        i = a + b
        print(i)
        a = b
        b = i
        
fibonacci(101)"""

def count_num(num):
    a = len(str(num))
    print(a)

count_num(100000000000000000000000000000000000000000000000000000000000000000000000000000)





    

    
    


          
