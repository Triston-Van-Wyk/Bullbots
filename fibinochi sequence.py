def fibinochi(length):
    a=1
    b=1
    for x in range (0,length):
        print(a)
        print(b)
        a+=b
        b+=a

fibinochi(int(input("sequence number:")))
