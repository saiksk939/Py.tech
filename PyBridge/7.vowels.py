str=input('Enter any word: ')
vowels=0
for i in str:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels+=1  #vowels=vowels+1
print('The no of vowels present in given word is : ', vowels)     