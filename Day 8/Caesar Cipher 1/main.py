alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #shift(1) a=b
    #shift(2) a=c
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(text, shift, direction):
    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text. Dentro de la función 'encrypt()', desplaza cada letra del 'texto_original' hacia adelante en el alfabeto
    # por la cantidad de desplazamiento e imprime el texto encriptado.
    resultado = ""

    if direction == "decode".lower():
        shift = shift * -1
        print(f"{shift}")

    for position in text:
        if position.isalpha() == True: #and direction == "encode".lower():
            nueva_position = (alphabet.index(position) + shift) % len(alphabet)
            nueva_letra = alphabet[nueva_position]
            resultado += nueva_letra

        elif position.isalpha() == False:
            resultado += position

    return resultado

resultado_final = encrypt(text, shift, direction)
print(resultado_final)
       

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
