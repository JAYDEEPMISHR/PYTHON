def test(a,b,c,*d,**e):                       # * & ** are arbetrary arguments. * make tupple & ** make dictionary.
    print("A :",a, "B :",b, "C :",c, "D :",d, "E :",e)
test(1,2,3,4,5,6,7,8,9,x=14,y=15,z=16)
