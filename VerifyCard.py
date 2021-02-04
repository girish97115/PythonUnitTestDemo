import sys
import re
from datetime import date

#check name validity
def validateName(name):
    exp = r'^[a-zA-Z ]+$'
    if re.search(exp,name):
        return True
    else:
        return False


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

#check number validity
def validateNumber(cc_num):
    cc_num = cc_num[::-1]
    cc_num = [int(x) for x in cc_num]
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list] 
    sum_of_digits = sum(doubled_second_digit_list)
    return sum_of_digits % 10 == 0


#check cvv validity
def validateCvv(cvv):
    exp = r'\d{3}'
    if re.search(exp,cvv):
        return True
    else:
        return False

#check card Date validatity
def validateExpiry(expiryDate):
    today = date.today()
    todayString = str(today)
    todayMM = todayString[5:7]
    todayYY = todayString[2:4]

    expiryMM = expiryDate[0:2]
    expiryYY = expiryDate[3:]

    expiryYYInt = int(expiryYY)
    expiryMMInt = int(expiryMM)
    todayMMInt = int(todayMM)
    todayYYInt = int(todayYY)

   
    print("Today ints", todayMMInt," ", todayYYInt)
    print("Expiry ints", expiryMMInt," ", expiryYYInt)
    
    if(expiryYYInt<todayYYInt):
        return False
    elif(expiryYY == todayYY):
        if(expiryMMInt< todayMMInt):
            return False
        else:
            return True
    else:
        return True

#checking all details of a card
def checkCardValidity(cardName, cardNumber, cardCvv,cardExpiry):
    cardNumValid = validateNumber(cardNumber)
    cardNameValid = validateName(cardName)
    cardCvvValid = validateCvv(cardCvv)
    cardExpiryValid = validateExpiry(cardExpiry)
    return(cardNameValid and cardNameValid and cardCvvValid and cardExpiryValid)

if __name__ == "__main__":
    cardName = "GirishCB"
    cardNumber = "79927398713"
    cardCvv = "388"
    cardExpiry = "07/21"

    print("Card valid?", checkCardValidity(cardName, cardNumber, cardCvv,cardExpiry))
