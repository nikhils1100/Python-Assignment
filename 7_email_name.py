email_id = input("Enter Email Id in username@company.com format : ")

index1 = 0
index2 = 0

for i in range(len(email_id)):
    if email_id[i] == '@':
        index1 = i+1
    elif email_id[i] == '.':
        index2 = i

print(email_id[index1:index2])