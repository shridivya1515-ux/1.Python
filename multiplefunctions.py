class multiplefunctions():
	def subfields ():
     		print("The Sub-fields in AI are:")
     		lists=['Machine Learning','Neural Networks','vision','Robotics','speech processing','Natural language processing']
     		for num in lists:
         		print(num)
         		Aifield=num
     		return Aifield
	def oddeven():
        	num=int(input("Enter a number:"))
        	if(num%2==0):
            		message=print(num,"is even number")
        	else:
            		message=print(num,"is odd number")
        	return message
	def eligible():
        	gender=input("your gender:")
        	age=int(input("your age:"))
        	if (gender=="male" and age >= 21) or(gender=="female" and age >= 18):
            		print("Eligible")
            		msg="eligible"
        	else:
            		print("Not Eligible")
            		msg="Not eligible"
        	return msg
	def percentage():
        	subject1=int(input("subject1:"))
        	subject2=int(input("subject2:"))
        	subject3=int(input("subject3:"))
        	subject4=int(input("subject4:"))
        	subject5=int(input("subject5:"))
        	total=subject1+subject2+subject3+subject4+subject5
        	print("total:",total)
        	percentage =total/500 *100
        	print("percentage:",percentage)
        	return percentage
	def triangle():
        	height=int(input("Height:"))
        	breadth=int(input("Breadth:"))
        	Area = (height*breadth)/2
        	print("Area of triangle:",Area)
        	height1=int(input("Height1:"))
        	height2=int(input("Height2:"))
        	breadth=int(input("Breadth:"))
        	parameter=height1+height2+breadth
       		print("Parameter of Triangle:",parameter)
        	return Area,parameter
