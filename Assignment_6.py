#Q1

r=int(input("enter radius of sphere"))
def sphere(r):
    area=4*3.14*r*r
    print(area)
sphere(r)

#Q2

def perfect(number):
      sum=0
      for i in range(1,number):
            if number%i is 0:
                  sum=sum+i

      if sum is number:
            return number
      else:
            return 0


for i in range(1,1001):
      n=perfect(i)
      if n is not 0:
            print(n)


#Q3

def table(n):
    for i in range(1,11):
        print(n,'X',i,'=',n*i)
n=int(input("Enter digit\n"))
table(n)

#Q4

def power(b,e):
    if(e==1):
        return(b)
    if(e!=1):
        return(b*power(b,e-1))
b=int(input("Enter base :- "))
e=int(input("Enter exponential:- "))
print("Result :- ",power(b,e))
