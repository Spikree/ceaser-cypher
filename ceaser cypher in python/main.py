decofalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cypher(plain_text, shift_amount, shift_amount2):
   
   if direction == "encode":
    cipher_text = ""
    for letters in plain_text:
      position = alphabet.index(letters)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f"The new encrypted letter is {cipher_text}")

   elif direction == "decode":
     plain_text2 = ""
     for letters in plain_text:
       position = alphabet.index(letters)
       new_position = position - shift_amount2
       new_letter = alphabet[new_position]
       plain_text2 += new_letter
     print(f"The decrypted letter is {plain_text2}")

shift = shift % 26


cypher(plain_text=text, shift_amount=shift, shift_amount2=shift)    

resut = print("Do you want continue using the program, yes or no ")
if resut == "no":
  should_continue = False
  print("goodbye!")    
