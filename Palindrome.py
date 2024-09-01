Str = input("Enter the Sentence : ").lower()
Palindrome = ""
Sentence = ""
ls = Str.split()
Palindrome_ls = []


for k in ls:
    alpha = k.strip(",.:;<>/?'|\[]{}_+-=!@#$%^&*()~`""")
    Palindrome_ls.append(alpha)


for i in range(0,len(Palindrome_ls)):
    Sentence = Sentence + Palindrome_ls[i]

for j in range(len(Palindrome_ls)-1,-1,-1):
    Palindrome = Palindrome + Palindrome_ls[j][::-1]

if(Palindrome == Sentence):
    print("True")
else:
    print("False")