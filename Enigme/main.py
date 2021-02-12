if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    content = fichier.read()
    col=0
    dep=0
    line=0
    result=0

    tabl = content.split('\n')
    for i in tabl:
        #mdp = i.split('.')
        #plage = [int(i) for i in mdp[0].split('-')]
        #lettre = mdp[1].split(':')
        #result = mdp[2].count(lettre[0])
        #poslettre = mdp[2]
        line = line + 1
        col = col + 3


        if col == 30:
            col = 0
        if tabl[line][col] == '#':
            result = result + 1


    print(result)
