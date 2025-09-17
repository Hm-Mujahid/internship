str="malayalam"
for i in range(len(str)//2):
    if str[i]!=str[len(str)-1-i]:
        print("not palindrome")
        break
    else:
        print("palindrome")
        break
#for string with spaces and alphanumerics use- s = ''.join(ch.lower() for ch in s if ch.isalnum())