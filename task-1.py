print("Select options below:")
print("Press 1 for Encrypt the plain text")
print("Press 2 for Decrypt the text")
user_input=input("Enter the option here:")

#-----------function for encrypt--------------

def encrypt(msg):
    output=""
    for letter in msg:
        change=chr(ord(letter)+3)
        output=output+change
    print("The Encrypted text is:",output)
#----------------------------------------------------
def decrypt(msg):
    output=""
    for letter in msg :
        change=chr(ord(letter)-3)
        output=output+change
    print("The Decrypted text is ",output)
#----------------------------------------------------------
if(user_input==1 or user_input=="1"):
    text=input("Enter the text to Encrypt")
    encrypt(text)
else:
    text=input("Enter the text to Decrypt")
    decrypt(text)

     
