#cerser cypher mean adding 3 ascii of the alphabet eg 'a' will become 'd'

def ceaser_cypher(message):
	new_msg[] #list for removing space value
	for i range (len(message)):
		if(ord(message[i])!= 32):  #32 is ascii value of space
			new_msg.append(message[i])  #removed ascii value
	new_mod=[]  # for cease cypher
	mod=3
	for i in range(len(new_msg)):
		x=((ord(new_msg[i])+mod)%97)%26  # ord() fucnction is used for converting alphabet into it ascii value
		x=x+97
		new_mod.append(chr(x))
		
	print(new_mod)
	
def main():
	message=input('Enter the message')
	ceaser_cypher(message)
main()

# x=((ord(new_msg[i]) _ mod)%97_%26 ascii of z is 122
#x=((122+3)%97)%26  97 is ascii of 'a' and 26 is total no of alpha
#x=(125%97)%26 
#x=(28)%26
#x=(28)%26; x=2+97 ; x=99 which is c
