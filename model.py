STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, beseda, crke = None):
        self.geslo = beseda
        self.crke = [] if crke == None else crke
    
    def napacne_crke(self):
        napacne = []
        for znak in self.crke:
            if znak not in self.geslo:
                napacne.append(geslo)
        return napacne
    
    def pravilne_crke(self):
        pravilne = []
        for znak in self.crke:
            if znak in self.geslo:
                pravilne.append(geslo)
            else:
                continue
        return pravilne


    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.pravilne_crke():
                return False
        return True
    
    def poraz(self):
        if len(self.napacne_crke()) >= 10:
            return True
        return False
    
    def pravilni_del_gesla(self):
        nova_beseda = ''
        for znak in self.geslo:
            if znak in self.crke:
                nova_beseda += znak + ' '
            else:
                nova_beseda += '_ '
        return nova_beseda 
    
    def nepravilni_ugibi(self):
        nova_beseda = ''
        for znak in self.crke():
            if znak not in self.geslo:
                nova_beseda += znak + ' '
        return nova_beseda


        


