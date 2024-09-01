# longest common sequence

str1 = input("Enter the first String : ")
str2 = input("Enter the second String : ")
string = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        if(str1[i] == str2[j]):
            string = string + str1[i]
print("Longest common sequence : ",string)