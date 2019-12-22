from utilities import *
from nltk import CFG

def main():
    source = "./grammar.cfg"

    sentences = ["skywalker sarà tuo apprendista",              #tuo apprendista skywalker sarà
                 "tu avrai novecento anni di età",              # novecento anni di età tu avrai
                 "tu hai amici lì",                             # amici lì tu hai
                 "noi siamo illuminati",                        # illuminati noi siamo
                 "il lato oscuro è arduo da vedere",            # arduo da vedere il lato oscuro è
                 "tu hai molto da apprendere ancora",           # molto da apprendere ancora tu hai
                 "skywalker corre veloce",                      # veloce Skywalker corre
                 "il futuro di questo ragazzo è nebuloso"]      # nebuloso il futuro di questo ragazzo è

    with open(source, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())
        #print(grammar)

    i=0
    if grammar.is_chomsky_normal_form():
        for sent in sentences:
            it_tree = cky(sent.split(), grammar)
            save_tree("it"+str(i), it_tree)
            it_tree.draw()
            if(it_tree is not None):
                yoda_tree = translate_it_yo(it_tree)
                save_tree("yo" + str(i), yoda_tree)
                yoda_tree.draw()
            i+=1
    else:
        exit('Error: the grammar must be in Chomsky Normal Form')


if __name__ == '__main__':
    main()