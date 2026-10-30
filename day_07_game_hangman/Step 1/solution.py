import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task.hangman_words import word_list
from task.hangman_art import stages, logo


print(f"Bienvenido al juego {logo}")


placeholder = ""
letter = ""
lives = 6
display = ""


chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word) #Calcula la longitud de la palabra 

for position in range(word_length):
    placeholder += "_"
print(placeholder)
    
letras_acertadas = []
while display != chosen_word:
        
        display = ""
        #gameover = False
        guess = input("Ingrese una letra: ").lower()

        if guess in chosen_word:
            print(f"Total vidas: {lives} es Correcto")
        elif lives <= 1:
            print(f"Total vidas: 0 Tu perdiste {stages[0]} era la palabra {chosen_word}")
            break
            
        else:
            "_" not in display
            lives -= 1
            print(f"Total vidas: {lives} es Incorrecto {stages[lives]}")

    
        for position in chosen_word:
            if position == guess:
               letras_acertadas.append(guess)
               display += guess

            elif position in letras_acertadas:
                 display += position
            else:
                display += "_"
                  
        print(display)
           
