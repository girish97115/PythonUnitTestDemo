import VerifyCard

def test_sum_digits():
    assert VerifyCard.sum_digits(2) == 2
    assert VerifyCard.sum_digits(9) == 9
    assert VerifyCard.sum_digits(11) == 2
    assert VerifyCard.sum_digits(13) == 4


def test_validateCvv():
    assert VerifyCard.validateCvv("314") == True
    assert VerifyCard.validateCvv("615") == True
    assert VerifyCard.validateCvv("91") == False
    assert VerifyCard.validateCvv("1") == False


def test_validateName():
    assert VerifyCard.validateName("Akash") == True
    assert VerifyCard.validateName("Balaji") == True
    assert VerifyCard.validateName("9tghtw") == False
    assert VerifyCard.validateName("Girish23") == False


def test_validateExpiry():
    assert VerifyCard.validateExpiry("06/22") == True
    assert VerifyCard.validateExpiry("03/30") == True
    assert VerifyCard.validateExpiry("12/12") == False
    assert VerifyCard.validateExpiry("07/03") == False


def test_checkCardValidity():
    assert VerifyCard.checkCardValidity(
        "girish", "79927398713", "343", "03/22") == True
    assert VerifyCard.checkCardValidity(
        "Akash", "79927391134", "51", "04/23") == False
    assert VerifyCard.checkCardValidity(
        "Kar3tik", "79927391134", "113", "03/27") == False
    assert VerifyCard.checkCardValidity(
        "Babu34", "79927391134", "823", "03/03") == False
