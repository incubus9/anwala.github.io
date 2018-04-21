import assignment8_1
from subprocess import check_output


c = assignment8_1.naivebayes(assignment8_1.getwords)

check_output(['rm', 'rdill.db'])

c.setdb('rdill.db')

assignment8_1.spamTrain(c)





file1 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam11.txt')
email1 = file1.read()
print( c.classify(email1) )

file2 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam12.txt')
email2 = file2.read()
print( c.classify(email2) )

file3 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam13.txt')
email3 = file3.read()
print( c.classify(email3) )

file4 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam14.txt')
email4 = file4.read()
print( c.classify(email4) )

file5 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam15.txt')
email5 = file5.read()
print( c.classify(email5) )

file6 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam16.txt')
email6 = file6.read()
print( c.classify(email6) )

file7 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam17.txt')
email7 = file7.read()
print( c.classify(email7) )

file8 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam18.txt')
email8 = file8.read()
print( c.classify(email8) )

file9 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam19.txt')
email9 = file9.read()
print( c.classify(email9) )

file10 = open('/home/ryan/Desktop/CS432/Assignment8/Test/NotSpam20.txt')
email10 = file10.read()
print( c.classify(email10) )

file11 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam11.txt')
email11 = file11.read()
print( c.classify(email11) )

file12 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam12.txt')
email12 = file12.read()
print( c.classify(email12) )

file13 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam13.txt')
email13 = file13.read()
print( c.classify(email13) )

file14 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam14.txt')
email14 = file14.read()
print( c.classify(email14) )

file15 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam15.txt')
email15 = file15.read()
print( c.classify(email15) )

file16 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam16.txt')
email16 = file16.read()
print( c.classify(email16) )

file17 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam17.txt')
email17 = file17.read()
print( c.classify(email17) )

file18 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam18.txt')
email18 = file18.read()
print( c.classify(email18) )

file19 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam19.txt')
email19 = file19.read()
print( c.classify(email19) )

file20 = open('/home/ryan/Desktop/CS432/Assignment8/Test/Spam20.txt')
email20 = file20.read()
print( c.classify(email20) )
