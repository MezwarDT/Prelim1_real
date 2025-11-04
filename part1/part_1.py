# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: [str]):
    for line in tail:
        print(line)

def part_1(size: int):
    """
    Draw the platypus tail

    Parameters:
        size int: Size of the tail

    Returns:
        [String]: The platypus tail drawn
    """
    tail = []
    ### YOUR CODE GOES HERE ###

    size = 3
    largeur = size*2 
    base = size
    hauteur_totale = size*2 + 1
    hauteur_haut = size + 1
    hauteur_bas = size
    
    pattern = "|"
    
    for i in range(largeur-1):
        pattern = pattern + "_."

    pattern = pattern + "_" + "|"       
    
    for i in range(hauteur_haut):
        tail.append(pattern)    
    
    
    
    print(tail)
    return tail
part_1(3)