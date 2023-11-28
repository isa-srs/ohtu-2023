class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo


class Summa:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.arvo = int(self.lue_syote())
        self.sovellus.plus(self.arvo)
    

class Erotus:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.arvo = int(self.lue_syote())
        self.sovellus.miinus(self.arvo)


class Nollaus:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
    
    def suorita(self):
        self.sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote