#Q.What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

print(s, len(s))

#Output :
#{20, '20'} 2
# Because 20 and 20.0 are equal just like 1 == 1.0

