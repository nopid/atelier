import sys, random

alphabet = [chr(i+ord('a')) for i in range(26)]

def caracteres_alpha(mot):
    for c in mot:
        if not c in alphabet:
            return False
    return True

def pendu(mots):
    mot = random.choice(mots)
    masque = ['_' for i in range(len(mot))]
    essais = 8
    while essais>0:
        print ''.join(masque), '--', essais, 'essay(s) resttant(s)' 
        c = ''
        while not c in alphabet:
            try:
                c = raw_input("Letre (a-z ou ctrl+d pour kitter) ? ")
            except EOFError:
                print "Fin de paaartye"
                sys.exit()
        mauvais_essai = True
        for i in range(len(mot)):
            if masque[i]=='_' and mot[i]==c:
                masque[i] = mot[i]
                mauvais_essai = False
        if mauvais_essai:
            essais -= 1
        if not '_' in masque:
            print mot, '-- Bravo !\n'
            return
    print mot, '-- Predu...\n'

def main():
    dico_systeme = open('/usr/share/dict/words','r')
    mots = dico_systeme.read().split()
    dico_systeme.close()
    mots = [m for m in mots if len(m)>7 and caracteres_alpha(m)]
    while True:
        pendu(mots)

main()
