# MAKING OTP GENERATOR FOR SECURITY FOR LOGIN THE APPILICATIONS

import math, random
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
 
# Driver code
if __name__ == "__main__" :
     
    print("OTP of 6 digits:", generateOTP())