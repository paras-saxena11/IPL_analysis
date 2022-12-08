def seats():
    print("Number of tickects required ")
    print("1, 1")
    print("2, 2")
    print("3, 3")
    print("4, 4")
    t = int(input("choose your option: "))
    print("How do wish to pay")
    print("1, Net banking")
    print("2, Credit Card")
    print("3, UPI")
    p = int(input("choose your option: "))
    print("Thank you, You'r tickets are confirmed")
    return 0

def center():
	print("Which stand ")
	print("1, VIP Box")
	print("2, Platinum Seating")
	print("3,Premuim Seating")
	a = int(input("choose your option: "))
	seats()
	return 0

# this function is used to select city
def city():
	print("Welcome to ticket booking: ")
	print("Which match do you want to watch:")
	print("1,MI vs CSK")
	print("2,RCB vs KKR ")
	print("3,SRH vs DC ")
	match = int(input("choose the match you want to watch: "))
	if match == 1:
	    center()
	elif match == 2:
	    center()
	elif match == 3:
	    center()
    
	else:
	    print("wrong choice")


city() # it calls the function city
