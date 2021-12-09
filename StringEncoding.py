def encode(message):
    final_ans=""
    count=1
    if len(message)==1:
        final_ans+=str(count)+message[0]
    else:
        for i in range(1,len(message)):
            if message[i]==message[i-1]:
                count+=1
            else:
                final_ans+=str(count)+message[i-1]
                count=1
            if i==len(message)-1:
                final_ans+=str(count)+message[i]
    return final_ans
   

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
