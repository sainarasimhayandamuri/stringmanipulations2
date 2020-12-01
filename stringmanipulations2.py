"""
Stringmanipulations part 2

"""
sai = "students#"
t1 = sai.partition("students")
print(t1)
sai1 = "123457s"
l1 = sai1.isalnum() #islnum() is a function which returns true if it contains numbers and alphabets i.e aplhanumerics and it will give false if it contains space or special characters in a string
l2 = sai.isalnum()
print(l1)
print(l2)
"""
String List Conversion
str.join(iterable) 
Change a list, tuple or sequence into a string by concatenating elements and use str as seperator.
"""
res = ",".join("automation")
print(res)
l1 = ['1','2',"3",'4','5']
res1 = " ".join(l1)
print(res1)
t1 = ('1','2','7','8','9')
print("*".join(t1))

r1 = str.split("sep",maxsplit=10)
print(r1)
