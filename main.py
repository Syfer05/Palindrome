# Palindrome

vrai="It's a palindrome"
faux="Sad, that's a regular word"

mot = input("Enter your word: ")
tableau = []
longueur = len(mot)
milieu = longueur//2
tableau = list(mot)

""" Suppresion du caractere du milieu en cas de mot impair """
if longueur%2!=0: 
    del tableau[milieu]
    
 
alpha=tableau[0:milieu]
""" slicing is reversed """
bravo=tableau[:milieu-1:-1]
print(alpha, bravo)

if alpha == bravo:
    print(vrai)
else:
    print(faux)
