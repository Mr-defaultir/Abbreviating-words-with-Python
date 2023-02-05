import random
 
name1 = input("1")
name2 = input("2")
name3 = input("3")
Combination = name1 + name2 + name3
print("The main names you entered : " + str(Combination))
Number_letters = 6

Abbreviation1 = ''.join(random.choice(Combination) for _ in range(Number_letters)) 
Abbreviation2 = ''.join(random.choice(Combination) for _ in range(Number_letters)) 
Abbreviation3 = ''.join(random.choice(Combination) for _ in range(Number_letters)) 

print(str(Abbreviation1))
print(str(Abbreviation2))
print(str (Abbreviation3))