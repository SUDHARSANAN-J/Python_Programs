s = input("Enter the URL : ")

if(s[0:7] == "http://" or s[0:8] == "https://"):
    print("true")
else:
    print("false")
