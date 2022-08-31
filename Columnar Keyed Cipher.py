def encrypt(p, k, l_num):
    l1 = list(k)  # Unsorted List
    a, b = [], []

    for i in range(l_num):
        a = list(p[:len(k)])  # Slices The Plain Text Into Letters Of Length len(key)
        b.append(a)  # Contains A Secondary List Of The Elements Of The Rows
        p = p[len(k):]  # Shifts The Plaintext By len(k)

    l2 = sorted(l1)  # Sorted List
    print("Cipher Text Is : ", end='')
    for i in range(len(k)):
        h = l1.index(l2[i])  # Gets The Index Of The Character From Unsorted List
        for j in range(l_num):
            cd = b[j][h]
            print(cd, end='')


def decrypt(p, k, l_num):
    a, b, c, d, t = [], [], [], [], 0
    count = 0
    dic = {}
    # List b Contains The Encrypted Word Segregated Into Parts Of Length 'The Number Of Rows'
    for i in range(len(k)):
        a = p[:l_num]
        b.append(a)
        p = p[l_num:]

    l1 = list(k)  # Unsorted List
    l2 = sorted(l1)  # Sorted List
    for i in range(len(k)):
        dic.update({l2[i]: b[i]})   # This Contains Keys(Characters) & Their Values

    for i in range(len(k)):
        c.append(dic.get(l1[i]))
    while t != len(k):
        for i in range(len(k)):
            d.append(c[i][count])   # This Contains The Decrypted Text
        count += 1
        t += 1
        if count >= len(c[0]):
            break
    print("Deciphered Text Is :", ''.join(d))


print(str('Columnar Keyed Cipher By Aaryan Golatkar').upper())
choice = int(input("Press :-\n1 For Encryption\n2 For Decryption\n"))

if choice == 1:
    plaintext = list(input('Enter A Text : ').replace(' ', ''))
    key = input('Enter The Key : ').upper()

    # If The Length Of Plaintext Is Not Divisible by Length of Key, Then This Makes It Divisible
    if len(plaintext) % len(key) != 0:
        while len(plaintext) % len(key) != 0:
            plaintext.append('x')
    plaintext = ''.join(plaintext)
    list_num = len(plaintext) // len(key)  # Number Of Rows That'll Be Formed
    encrypt(plaintext, key, list_num)

elif choice == 2:
    ciphertext = input('Enter The Cipher Text : ').replace(' ', '')
    key = input('Enter The Key : ').upper()
    list_num = len(ciphertext) // len(key)  # Number Of Rows That'll Be Formed
    decrypt(ciphertext, key, list_num)

else:
    print('Exiting.....')
