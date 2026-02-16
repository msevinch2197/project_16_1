def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

matn = input("Matn kiriting: ")
siljitish = int(input("Nechta harfga siljitilsin: "))

shifrlangan = caesar_encrypt(matn, siljitish)
print("Shifrlangan matn:", shifrlangan)

deshifrlangan = caesar_decrypt(shifrlangan, siljitish)
print("Deshifrlangan matn:", deshifrlangan)
