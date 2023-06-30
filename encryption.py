import math
import numpy as np
import time
import random

letters = ' abcdefghijklmnopqrstuvwxyz`1234567890-=~!@#$%^&*()_+\\{}[]|;:,./<?>'

def affineCypherEncrypt(unencryptedMessage, key1, key2):
    if key2 > len(letters)-2:
        raise Exception("key2 value cannot be above " + str(len(letters)))
    def reduce(num, div2=0, sub=0):
        if num <= len(letters)-2:
            num = math.floor(num)
            return num, div2, sub
        else:
            if num >= 2*(len(letters)-1):
                div2 += 1
                return reduce(num/2, div2, sub)
            else:
                sub += 1
                return reduce(num-(len(letters)-1), div2, sub)
        
    def affineApply(num, k1, k2):
        return k1*num + k2
    
    final = []
    
    for char in unencryptedMessage:
        newChar, div2, sub = reduce(affineApply(letters.index(char.lower()), key1, key2))
        newChar = letters[newChar]
        final.append([newChar, div2, sub])

    return final

def affineCypherDecrypt(encryptedMessageList, key1, key2):
    final = []
    for char, div2, sub in encryptedMessageList:
        num = letters.index(char.lower())
        num += 66*sub
        num *= 2**div2
        num -= key2
        num = math.ceil(num/key1)
        final.append(letters[num])
    return "".join(final)

def linTransDecrypt(transmission):
    xStretch = float(transmission[:4])
    yStretch = float(transmission[4:8])
    transmission = transmission[8:]
    coords = []
    while len(transmission) > 0:
        coordsTemp = []
        for b in range(2):
            neg = transmission[0]
            if neg == '1': 
                coordsTemp.append(-1 * float(transmission[1] + "." + transmission[2:4]) )
            else:
                coordsTemp.append(float(transmission[1] + "." + transmission[2:4]) )
            transmission = transmission[4:]
        coords.append(coordsTemp)
    final = []
    for pair in coords:
        x = pair[0]
        y = pair[1]
        z = round(math.sqrt((x/xStretch)**2 + (y/yStretch)**2), 1)
        angle = math.atan(y/x)
        if angle < 0:
            angle += (math.pi)
        index = int(round((angle * len(letters) / (2*math.pi)), 0))
        final.append(letters[index])
    return "".join(final)
        
    
    
    

def linTransEncrypt(unencryptedMessage, z, xStretch, yStretch):
    z = round(max(min(z, 2.00), 0), 2) 
    xStretch = float(round(max(min(xStretch, 1.99), 0), 2))
    yStretch = float(round(max(min(yStretch, 1.99), 0), 2))
    final = [str(xStretch) + "0"*(4-len(str(xStretch))), str(yStretch) + "0"*(4-len(str(yStretch)))]
    # potential weak point, since assignment of theta is linear
    for char in unencryptedMessage:
        char = char.lower()
        theta = letters.index(char) * ((2*math.pi)/ len(letters))
        r = z / ((math.cos(theta) / xStretch)**2 + (math.sin(theta) / yStretch)**2)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        xneg = int(x<0)
        yneg = int(y<0)
        x = abs(x)
        y = abs(y)
        temp = [str(xneg),
                "".join([str(round(x, 2))[a]if str(round(x, 2))[a] not in ['-', '.'] else "" for a in range(len(str(round(x, 2))))]) + "0"*(4-len(str(round(x, 2)))),
                str(yneg),
                "".join([str(round(y, 2))[a] if str(round(y, 2))[a] not in ['-', '.'] else "" for a in range(len(str(round(y, 2))))]) + "0"*(4-len(str(round(y, 2))))]
        final.append("".join(temp))
    return "".join(final)
    
    

encrypted1 = linTransEncrypt("I didnt drive over them it was from this truck in front of me", 2, 1, 1)
decrypted1 = linTransDecrypt(encrypted1)
print(decrypted1)
