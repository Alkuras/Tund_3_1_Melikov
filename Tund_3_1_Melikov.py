#Näidised 
# a=0 
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# for i in range(0,10,1):
#     print(f"{i}. samm")
# for i in range(10):
#     print(f"{i}. samm")



#Ülesanne 1
while True:
    try:
        nimi = input("Sisesta oma nimi ")
        if nimi.isalpha()==True: break
    except:
        print("Viga!")
while True:
    try:
        N = int(input("Sisesta number "))
        if N>0: break
    except:
        print("Viga")
print("FOR")
for i in range(1,N+1,1):
   print(f"Ole tervitatud, {nimi}, {i}. korda.")
print("WHILE TRUE")
i=0
while True:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")
    if i==N: break
i=0
print("WHILE TINGIMUSEGA")
while i<N:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")  



# #Ülesanne 2
from secrets import randbelow


print("WHILE")
j=0
summa=0
while True:
    while True:
        try:
            a=float(input("Sisesta number "))
            break
        except:
            print("Numbri vaja")        
    a=float(a)
    summa+=a
    j+=1
    if j==10: break
print(summa)
print("FOR")
j=0
summa=0
for j in range(10):
    while True:
        try:
            a=float(input("Sisesta number "))
            break
        except:
            print("Numbri vaja")        
    a=float(a)
    summa+=a
print(summa)


# #Ülesanne 2.1
print("WHILE+ENTER")
summa=0
while True:
    number=input("Sisesta arv (Vajuta Enter lõpetamiseks: )")
    if number == "": break
    try:
        number=float(number)
        summa += float(number)
    except:
        print("Viga!")
print(summa)
 
#Ülesanne 3
from secrets import randbelow

õ=0
for i in range(5):
   k=0
   vastus=0
   b= randbelow(5)
   c= randbelow(5)
   bc= b+c
   print(f"{b} + {c} = ")
   while k<5 or vastus == bc:
       try:
        vastus =int(input("Vastus:"))
       except:
           print("Sisesta numbri")
       if vastus == bc:
           print("Õige!Tubli.")
           õ+=1
           print()
           print(f"Õiged vastused: {õ}")
           break
       else:
           print("Vale")
           k+=1
       if k==5:
            print("Sa kaotasid")
            print(f"Õige vastus oli {bc}")

#Ülesanne 4
p=1

try:
    a=int(input("Sisesta number"))
    if a>0:
        while True:
            summ=p*a
            print(f"{p} * {a} = {summ}")
            p+=1

            if p ==11: break
except:
    print("Ainult täisarvud")

# #Ülesanne 5
N=int(input("Sisesta number "))
for j in range(N):
    for i in range(N):
      print("o",end=" ")
    print()



# #Ülesanne 6
q=5
print("5x5")
for i in range(5):
    print("*"*5)
print()

for j in range(5):
    print("*"*j)
print()

for k in range(5):
    print("*"*q)
    q-=1

#Ülesanne 7
print(randbelow(10),randbelow(10),randbelow(10),randbelow(10),randbelow(10),)

#Ülesanne 9
p=1

a=5
while True:
        summ=p*a
        print(f"{p} * {a} = {summ}")
        p+=1
        if p ==11: break


