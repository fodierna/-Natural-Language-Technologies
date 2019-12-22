from nltk import Tree, Nonterminal
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

def cky(words, grammar):
    dim = len(words)+1
    # create dim x dim matrix. Each element of the matrix is a list (of tree)
    table = [[[] for i in range(dim)] for j in range(dim)]
    for j in range(1, dim):
        # get le lhs of a rule that has a terminal symbol (word[hj-1]) in the rhs
        lhs = get_lhs_lexical_rule(words[j-1], grammar)
        if(lhs is not None):
            #A -> words[j] and create a Tree
            table[j-1][j].append(Tree(lhs, [words[j-1]]))
        for i in reversed(range(0, j - 1)):
            for k in range(i + 1, j):
                if(len(table[i][k])!=0 and len(table[k][j])!=0):
                    #We look for a rule A -> BC in the grammar
                    #such that B is member of table[i][k] and C is member of table[k][j]
                    A, B, C = get_grammar_rule(table[i][k], table[k][j], grammar)
                    if A is not None:
                        table[i][j].append(Tree(A, [B, C]))
    #if S is table[0][len(words)] then we have a tree for the input sentence
    if len(table[0][dim - 1]) != 0:
        return get_final_tree(table[0][dim - 1])
    else:
       print('Cannot derive the sentence')


# looks for a rule A -> word in the grammar. If exists A is returned
def get_lhs_lexical_rule(word, grammar):
    for prod_rule in grammar.productions():
        rhs = prod_rule.rhs()
        if rhs[0] == word:
            lhs = prod_rule.lhs()
            return lhs
    return None


# looks for a rule A -> BC in the grammar. Such that B is member of T1 and C is member of T2. If such a rule exists then A, B, C are returned
def get_grammar_rule(t1, t2, grammar):
    for prod_rule in grammar.productions():
        if (len(prod_rule.rhs()) == 2):
            for B in t1:
                for C in t2:
                    if (prod_rule.rhs()[0] == B.label() and prod_rule.rhs()[1] == C.label()):
                        return prod_rule.lhs(), B, C
    return None, None, None


# looks for S in the table and returns it if exists
def get_final_tree(table):
    for tree in table:
        if tree.label() == Nonterminal("S"):
            #tree.draw()
            return tree
    print("The sentence is not valid")


# given a tree in SVX form, it returns a tree in XSV form
def translate_it_yo(tree):
    SUBJ = [Nonterminal("PRON"), Nonterminal("NP"), Nonterminal("N")]
    VERB = [Nonterminal("VP")]
    yoda_tree = Tree("Yoda", [])
    for i in range(len(tree)):
        if(tree[i].label() in SUBJ):
            yoda_tree.insert(1,tree[i])
        if(tree[i].label() in VERB):
            V = tree[i][0]
            X = tree[i][1]
            yoda_tree.insert(0, X)
            yoda_tree.insert(2, V)
    return yoda_tree

def save_tree(name, tree):
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(), tree)
    cf.add_widget(tc, 10, 10)  # (10,10) offsets
    cf.print_to_file(name+".jpg")
    cf.destroy()