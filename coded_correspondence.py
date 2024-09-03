alphabet = "abcdefghijklmnopqrstuvwxyz"
coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = " "

for character in coded_message:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_message += alphabet[(character_value + 10) % 26]
    else:
        translated_message += character
print(translated_message)



def caesar_decode(message, offset):
    translated_message = ""
    
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            translated_message += alphabet[(character_value + offset) % 26]
        else:
            translated_message += character
            
    return translated_message


def caesar_encode(message, offset):
  translated_message = ""
    
  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      translated_message += alphabet[(character_value - offset) % 26]
    else:
      translated_message += character
            
  return translated_message



unknown_offset = list(range(1, 30))
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
  
for i in unknown_offset:
    print("\t {}".format(caesar_decode(brute_force_message, i)))

message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

caesar_decode(message, 7)


def vigenere_decode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0
    for letter in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if letter in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += letter

    decoded_message = ''
        
    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += message[i]
    return decoded_message

vigenere_decode('aiwfeyq ayc adcsvke!', 'cat')


  
def vigenere_encode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0
    for letter in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if letter in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += letter

    encoded_message = ''
        
    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index - offset_index) % 26]
            encoded_message += new_character
        else:
            encoded_message += message[i]
    return encoded_message

vigenere_encode('you are awesome!', 'cat')

vigenere_decode('wob yrl ywlqotc!', 'cat')
