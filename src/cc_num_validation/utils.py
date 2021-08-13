from .consts import issuer_dict

# verify if a number is valid according Luhn algorithm
def luhn(cc_number=0):
    cc_number = cc_number.replace(" ","")
    cc_number = cc_number[::-1]
    every_sec_double = [ int(dig)*2 if idx%2!=0 else int(dig) for idx, dig in enumerate(cc_number)]
    every_sec_double = [ dig//10 + dig-10 if dig>9 and idx%2!=0 else dig for idx, dig in enumerate(every_sec_double)]
    sum_total = sum(every_sec_double, 0)
    if not sum_total%10:
        return True 
    return False

# check the credit card issuer
def check_issuer(cc_number):
    for key, value in issuer_dict.items():
        if cc_number.startswith(value):
            issuer = key.replace("-"," ")
            if issuer[-2] == "_":
                issuer = issuer[:-2]
                return issuer
            return issuer
    if cc_number.startswith("3"):
        return "JCB"
    return ""