# this is a small script to convert between n-ary and decimal numbers and between n-ary themselves

def decimal_to_nary(base,number):
    # return int(number,base)
    result = ''
    dividend=number
    while dividend>0:
        remainder=dividend%base
        dividend=dividend//base
        result=str(remainder)+result
    return result

def nary_to_decimal(base,number):
    return int(number,base = base)


def valid_number(base,number):
    for i in number:
        if int(i)>=base :
            return False
    return True

def main():
    try:
        source_ary=int(input("source n-ary: "))
        while source_ary<2:
            print("Invalid input")
            source_ary=int(input("source n-ary: "))
        source_number=input("source sequence: ")
        while (not valid_number(source_ary,source_number)):
            print("Invalid input")
            source_number=input("source sequence: ")
        target_ary=int(input("target n-ary: "))
        while target_ary<2:
            print("Invalid input")
            target_ary=int(input("target n-ary: "))
            
        if source_ary==10:
            result =  decimal_to_nary(target_ary,int(source_number))
            print(result)
        else:
            decimal = nary_to_decimal(source_ary,source_number)
            result = decimal_to_nary(target_ary,decimal)
            print(result)


    except TypeError:
        print("Invalid input")
        exit()


main()