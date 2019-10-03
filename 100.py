ip = input("Enter IP : ")
mask = int(input("Enter mask bits : "))

import string

ip_split = ip.split(".")
number_string = [int(i) for i in ip_split]

list1 = []
for i in range(len(number_string)):
	list1.append(bin(number_string[i])[2:].zfill(8))
	
#print(list1)
list0 = "".join(list1)
list0 = int(list0, 2)

list2 = ''.join(list1)


list3 = list2[:mask]
#print(list3)

s = list(list3)

for n, i in enumerate(s):
	if i == "0":
		s[n] = "1"

s = "".join(s)

s = s.ljust(32, "0")

#counting no of 1's in subnet mask
count = 0
for i in s :
	if i == "1":
		count += 1

#continued on 75


sp2 = int(s, 2)


#for network_id calculation
net_id = list0 & sp2
net_id = bin(net_id)[2:]
#print(net_id)

net_id1 = net_id[:8] + "." + net_id[8:16] + "." + net_id[16:24] + "." + net_id[24:32]
net_id2 = net_id1.split(".")

for i in range(len(net_id2)):
	net_id2[i] = str(int(net_id2[i], 2))
net_id2 = ".".join(net_id2)

print("[Network ID] :", net_id2) #it is the network id

#for subnet calculation
s = s[:8] + "." + s[8:16] + "." + s[16:24] + "." + s[24:32]
sp1 =s.split(".")

for i in range(len(sp1)): 
	sp1[i] = str(int(sp1[i], 2))

sp1 = ".".join(sp1)

print("[Subnet Mask] :" , sp1) #it is the subnet mask


#maximum Subnets
s1 = 32 - mask

#print(count)
print("[Subnet Size] :", 2**s1)
print("[Total Hosts] :" , (2**s1 - 2))


if (count >= 24 and count <= 32):
	subnet_bits = count - 24
elif (count >= 16 and count < 24):
	subnet_bits = count - 16
elif (count >= 8 and count < 16):
	subnet_bits = count - 8
else:
	subnet_bits = count

print("[Subnet Bits] :", subnet_bits)
print("[Total Subnets] :", 2**subnet_bits)



#print(net_id)
print("[Starting Address] :", net_id2)

nett = list(net_id)
for l in range(mask, 32):
	nett[l] = "1"

nett = "".join(nett)

net_id4 = nett[:8] + "." + nett[8:16] + "." + nett[16:24] + "." + nett[24:32]
net_id5 = net_id4.split(".")

for i in range(len(net_id5)):
	net_id5[i] = str(int(net_id5[i], 2))
net_id5 = ".".join(net_id5)




print("[Broadcast Address] :", net_id5)







