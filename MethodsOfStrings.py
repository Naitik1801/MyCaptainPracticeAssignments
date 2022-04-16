txt = "hello world"
x = txt.capitalize()
print (x)

#--------------------------------------------------------------------#

txt = "Hello World"
x = txt.casefold()
print(x)

#--------------------------------------------------------------------#

txt = "Hello"
x = txt.center(20)
print(x)

#--------------------------------------------------------------------#

txt = "You are my friend, and a friend in need is a friend indeed."
x = txt.count("friend")
print(x)

#--------------------------------------------------------------------#

txt = "I am Naitik"
x = txt.encode()
print(x)

#--------------------------------------------------------------------#

txt = "Hello world."
x = txt.endswith(".")
print(x)

#--------------------------------------------------------------------#

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#--------------------------------------------------------------------#

txt = "Hello, My name is Naitik."
x = txt.find("name")
print(x)

#--------------------------------------------------------------------#

txt = "For only {price:.2f} rupees!"
print(txt.format(price = 100))

#--------------------------------------------------------------------#

txt = "Hello, My name is Naitik."
x = txt.index("name")
print(x)

#--------------------------------------------------------------------#

txt = "LM10"
x = txt.isalnum()
print(x)

#--------------------------------------------------------------------#

txt = "CR7"
x = txt.isalpha()
print(x)

#--------------------------------------------------------------------#

txt = "\u0033" 
x = txt.isdecimal()
print(x)

#--------------------------------------------------------------------#

txt = "380009"
x = txt.isdigit()
print(x)

#--------------------------------------------------------------------#

txt = "Hello"
x = txt.isidentifier()
print(x)

#--------------------------------------------------------------------#

txt = "hello world!"
x = txt.islower()
print(x)

#--------------------------------------------------------------------#

txt = "3800079"
x = txt.isnumeric()
print(x)

#--------------------------------------------------------------------#

txt = "Hello! Are you Naitik?"
x = txt.isprintable()
print(x)

#--------------------------------------------------------------------#

txt = "    "
x = txt.isspace()
print(x)

#--------------------------------------------------------------------#

txt = "Hello, My name is Naitik."
x = txt.istitle()
print(x)

#--------------------------------------------------------------------#

txt = "HELLO WORLD"
x = txt.isupper()
print(x)

#--------------------------------------------------------------------#

myTuple = ("Harry", "Peter", "Mary")
x = ",".join(myTuple)
print(x)

#--------------------------------------------------------------------#

txt = "Apple"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#--------------------------------------------------------------------#

txt = "Hello my name is NAITIK"
x = txt.lower()
print(x)

#--------------------------------------------------------------------#

txt = "     apple    "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#--------------------------------------------------------------------#

txt = "Hello Captain!"
mytable = txt.maketrans("C", "P")
print(txt.translate(mytable))

#--------------------------------------------------------------------#

txt = "I could eat apples all day"
x = txt.partition("apples")
print(x)

#--------------------------------------------------------------------#

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#--------------------------------------------------------------------#

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#--------------------------------------------------------------------#

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#--------------------------------------------------------------------#

txt = "Apple"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#--------------------------------------------------------------------#

txt = "I could eat apples all day, apples are my favorite fruit"
x = txt.rpartition("apples")
print(x)

#--------------------------------------------------------------------#

txt = "apple, love, bananas, hate"
x = txt.rsplit(", ")
print(x)

#--------------------------------------------------------------------#

txt = "     apple     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#--------------------------------------------------------------------#

txt = "Hello my name is Naitik"
x = txt.split()
print(x)

#--------------------------------------------------------------------#

txt = "Thank you for the help\nWelcome to my house"
x = txt.splitlines()
print(x)

#--------------------------------------------------------------------#

txt = "Hello my name is Naitik."
x = txt.startswith("Hello")
print(x)

#--------------------------------------------------------------------#

txt = "     apple     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#--------------------------------------------------------------------#


txt = "Hello My Name Is Naitik"
x = txt.swapcase()
print(x)

#--------------------------------------------------------------------#

txt = "Welcome to my home"
x = txt.title()
print(x)

#--------------------------------------------------------------------#

mydict = {83:  80}
txt = "Hello Akshat!"
print(txt.translate(mydict))

#--------------------------------------------------------------------#

txt = "Hello my name is Naitik"
x = txt.upper()
print(x)

#--------------------------------------------------------------------#

txt = "100"
x = txt.zfill(10)
print(x)
