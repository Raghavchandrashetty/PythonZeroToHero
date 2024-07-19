message = """How you doin?,
 I am Fine """
message1="Karnataka"
print("%s ***  ", message)
print("lenght is %d", len(message))
print("lenght is %d", message[18])
print("lenght is %d", message[0:10])
print("lenght is %d", message1[5:])
print("lenght is %d", message1[:6])
print(type(message))
print(message.lower())
print(message.upper())
print(message.count('a'))
print(message.find('you'))
print(message.find('your'))

print("*********************")
print(message.replace('doin', 'are you doing'))

message2 = 'Hello '
name= 'Michael'

print(message2+name)
message3 = message2+", " + name + " welcome!"
print(message3)

message4 = '{}, {}. Welcome!'.format(message2, name)
print(message4)
message5 = f'{message2}, {name.upper()}. Welcome!'
print(message5)

print(dir(name))
print(help(str.lower))




