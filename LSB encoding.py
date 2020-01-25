binary_data = open("lb.bmp","rb") # Open the file binary mode
binary_data.seek(54)  #seek to 54 bytes these bytes does not contain any data
data = binary_data.read() # read the binary data
l = []
for i in data:
    l.append(bin(i)[-1])  #make a list of LSB bit
for i in range(0,500,8):
    print(chr(int(''.join(l[i:i+8]),2)),end='') # print the character
