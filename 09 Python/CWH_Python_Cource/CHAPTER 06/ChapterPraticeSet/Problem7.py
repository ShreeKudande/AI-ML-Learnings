#Q.Write a program to find out whether a given post is talking about “Harry” or not. 

post = "hey shree bhai, you are really excellent at coding and math..."

if "Shree".lower() in post.lower():
    print("Its talking about shree")
else:
    print("Its not talking about shree")
