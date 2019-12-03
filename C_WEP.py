s = []
k = []
numero_c = []
clave = 'fedcba9876'
vi = 'abcdef'
temperatura = 16.5
temperatura = str(temperatura)

key = vi + clave

for i in range(256):
	s.append(i)

#print(key)
#print(s)
j = 0
for i in range(256):
	k.append(key[j:j+2])
	if j == 14:
		j = 0
	else:
		j = j + 2

#print("\n")
#print(k)

j = 0
for i in range(256):
	j = j + s[i] + int(k[i],16)
	j = j%256
	aux_1 = s[i] 
	aux_2 = s[j]
	s[i] = aux_2
	s[j] = aux_1

#print('\n')
#print(s) 

i = 0
j = 0
for l in range(len(temperatura)):
	i = i + 1 
	j = (j + s[i])%256
	aux_1 = s[i] 
	aux_2 = s[j]
	s[i] = aux_2
	s[j] = aux_1
	t = (s[i] + s[j])%256
	k = s[t]
	numero = ord(temperatura[l])
	numero_c.append(k^numero)
print(numero_c)