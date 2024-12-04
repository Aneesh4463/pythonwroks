#armstrong number

def armstrong(num):

    orginal_number=num

    digital_count=len(str(num))

    total=0

    while(num!=0):

     digit=num%10

     armstrong_num=digit**digital_count

     total=total+armstrong_num

     num=num//10

    if orginal_number==total:

     print("is_armstrong")

    else:

        print("not")

armstrong(153)

