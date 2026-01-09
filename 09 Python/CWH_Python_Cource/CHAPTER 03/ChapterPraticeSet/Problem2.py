#Q.Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         '''

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''  
       
print(letter.replace("<|Name|>", "Shree").replace("<|Date|>", "10 Nov 2025"))

# Dear Shree, 
# You are selected! 
# 10 Nov 2025 

