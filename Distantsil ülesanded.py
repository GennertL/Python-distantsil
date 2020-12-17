#Distantsil Iseseisvad ülesanded
#17.12.2020
#Gennert Lensment

#Ülesanne 3
print("“jutumärgid”")
print("Kaldu \//")
print("Kas ‘”kirjutad’ “\” samamoodi?")

#Ülesanne 6
num = int(input("Sisesta arv: "))
flag = num%2
if flag == 0:
    print(num, "on paaris arv")
elif flag == 1:
    print(num, "on paaritu arv")


#Ülesanne 7
string=input(("Sisesta tekst:"))
if(string==string[::-1]):
      print("See on palindrome")
else:
      print("See ei ole palindrome")

#Ülesanne 10
k, n = 5, 66

print(*(','.join(map(str, range(i, i+k))) for i in range(1, n+1, k)), sep='\n')

#Ülesanne 11
print([n for n in range(0, 66) if not n % 3])