def encrypt(string, shift):
	cipher = ''
	for char in string:
		if char == ' ':
			cipher = cipher + char
		elif char.isupper():
			cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
		else:
			cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
	return cipher
print("\t\t\t\t----------- Product Cipher ----------")
text = input("Enter Your Message => ")
s=int(input("\nEnter Key[Caeser] => "))
ce=encrypt(text,s)
print("Encypted in Caeser Cipher...\n",ce)
key =input("\nEnter Key[Columnar] => ")
col=len(key)
if((len(ce)%col)!=0):
	ce+="x"*(len(ce)%col)
ce= ce.replace(' ','')
o=[]
for i in key:
	o.append(i)
h=[]
for i in range(col):
	h.append(ce[i:len(ce):col])
dic=dict(zip(o,h))
so=sorted(dic.keys())
print("Encypted in Columnar Cipher...")
print(''.join(dic[i] for i in so))
