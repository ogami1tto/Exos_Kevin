
class Carre:
    """Classe 'carré' caractérisée par son côté en centimètres"""

    count = 0 # compteur de carrés créés

    def __init__(self, cote):
        """"constructeur de classe"""
        Carre.count = count
        print("Création d'un carré de", cote, "cm de côté...")
        self.side = cote
        self.perimetre = self.perimeter()
        self.aire = self.area()
        self.__class__.count += 1

    def perimeter(self):
        """Méthode retournant le périmètre d'un carré"""
        return self.side * 4

    def area(self):
        """"Méthode permettant d'afficher l'aire d'un carré"""
        return self.side **2

    def __repr__(self):
        return "Le carré à un côté d'une longueur de {}cm, une aire de {}cm2 et un périmètre de {}cm".format(self.side, self.aire, self.perimetre)

    def factor(self, x):
        """Méthode permettant de retourner un carré x fois plus grand que celui en cours"""
        return Carre(self.side * x)

    def __add__(self, other):
        """Méthode permettant d'additionner deux carrés."""
        return Carre(self.side + other.side)

    def __sub__(self, other):
        """Méthode permettant de soustraire deux carrés."""
        sub_square = self.side - other.side
        return Carre(sub_square)

    def __lt__(self, other):
        """Méthode permettant de vérifier si un premier carré est plus petit qu'un autre."""
        lower = self.side < other.side
        return bool(lower)

    def __gt__(self, other):
        """Méthode permettant de vérifier si un premier carré est plus grand qu'un autre."""
        greater = self.side > other.side
        return bool(greater)

    def __le__(self, other):
        """Méthode permettant de vérifier si un premier carré est plus petit ou égal à un autre."""
        lower_eq = self.side <= other.side
        return bool(lower_eq)

    def __ge__(self, other):
        """Méthode permettant de vérifier si un premier carré est plus grand ou égal à un autre."""
        greater_eq = self.side >= other.side
        return bool(greater_eq)

    def __eq__(self, other):
        """Méthode permettant de vérifier si un premier carré est strictement égal à un autre."""
        equal = self.side == other.side
        return bool(equal)


if __name__ == "__main__":
    c1 = Carre(5)
    # print(c1)
    # print("Le périmètre du carré est de {}cm.".format(c1.perimeter()))
    # # print("L'aire du carré est de {}cm2.".format(c1.area()))
    # # print(c1.area())
    # c2 = c1.factor(3)
    c3 = Carre(2)
    c7 = Carre(8)
    # print(c3)
    # c4 = Carre(5) - Carre(2)
    # print(c4)
    # print(Carre(3) <= Carre(2))
    # print(Carre(4) >= Carre(5))
    # print(Carre(5) == Carre(5))
    print(Carre.count)
    print(c3.count)
