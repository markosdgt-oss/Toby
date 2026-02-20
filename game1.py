import random
import os

def run():

   IMAGES = [ '''
  +---+
  | |
      |
      |
      |
      |
=========''' , '''
  +---+
  | |
  O |
      |
      |
      |
=========''' , '''
  +---+
  | |
  O |
  | |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/| |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
      |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
/ |
      |
=========''' , '''
  +---+
  | |
  O |
/|\ |
/ \ |
      |
=========''' ]
   
   DB = [
        "CAIMAN",
        "PIXELES",
        "BOLIQUESO",
        "CHOMPIRAS",
        "NEZUCO"
    ]
   
   word = random.choice(DB)
   SPACES = ["_"] * len(word)
   attemps = 6

   while True:
       os.sistem("clear")
       for character in SPACES:
           print(character, end=" ")
       print(IMAGES[attemps])
       letter = input("Elige una letra").upper()
           
       found = False
       for idx, character in enumerate(word):
           if character == letter:
               SPACES[idx] = letter
               found = True 

       if not found:
        attemps -= 1    
           
       if "_" not in SPACES:
        os.system("clear")
        print("Ganaste")
        break
       input()

       if attemps == 0:
        os.system("clear")
        print("Ganaste")
        break
       input()

       


   if __name__ =='__main__':
    run()
    print("Gracias por su atencion")