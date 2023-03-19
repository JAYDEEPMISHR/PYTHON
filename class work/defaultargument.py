def test(a=35,b=20,c=10,d=14):                    #default argument is given. It follows right to left formation.
    print("A :",a, "B :",b, "C :",c, "D :",d)
test(1,2,3,4)
test(1,2,3,4)
test(1,2,3)
test(1,2)
test(1)
test()
test(b=100,d=200)      #Keyword argument
