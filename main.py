# Palindrome

vrai="It's a palindrome"
faux="Sad, that's a regular word"

mot = input("Enter your word: ")
tableau =[]
longueur = len(mot)
milieu = longueur//2
tableau = list(mot)

if longueur%2!=0:       
    print(milieu)
    del tableau[milieu]
print(tableau)
    
 
alpha=tableau[0:milieu]
bravo=tableau[-milieu:]
bravo.reverse() 
print(alpha, bravo)

if alpha == bravo:
    print(vrai)
else:
    print(faux)
