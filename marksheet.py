Hindi = input ()
English = input ()
Maths = input ()
Environment = input ()
Science = input ()

print "Hindi %i"% Hindi
print "English %i" % English
print "Maths %i" % Maths
print "Environment %i" % Environment
print "Science %i" % Science

total_number = Hindi + English + Maths + Environment + Science 

print "total_number %i" % total_number

total_per = total_number * 100/500
print (total_per)

if total_per < 60:
	print "you are fail"
	
else:
	print "you are pass"
		
