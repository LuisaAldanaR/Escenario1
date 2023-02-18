import re

"""
Metodo que permite verificar si la frase o palabra dada por parametro es o no un palindromo
@param sentence Frase o palabra que se quiere verificar
@return True si la frase es palindroma o False en caso contrario
"""

# Método

def checkPalindrome(sentence):

    sentence = re.sub(r'\W+', '', sentence).lower() # Se eliminan los caracteres no alfanuméricos y se pasa a minúsculas
    start = 0                                       # Representa el índice inicial
    final = len(sentence) - 1                       # Representa el índice final

    for i in range(0, len(sentence)):

      if sentence[start] == sentence[final]: 
        start += 1
        final -= 1
      else:
        
        return False

    return True

# Pruebas

print(checkPalindrome('race car'))
print(checkPalindrome('not a palindrome'))
print(checkPalindrome('A man, a plan, a canal. Panama'))
print(checkPalindrome('never odd or even'))
print(checkPalindrome('nope'))
print(checkPalindrome('almostomla'))

word = ''

while word != '0' :
   
  word = input('Ingrese la palabra que desea verificar o ingrese 0 para salir: ')
    
  if word != '0':
      print(checkPalindrome(word))
  else:
      print("Saliendo...")