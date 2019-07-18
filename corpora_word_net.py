import nltk
from nltk.corpus import wordnet as wn

print(wn.synset('huge.a.01').similar_tos())
print(wn.synset("transfer.v.01").causes())
print(wn.synset("speak.v.01").verb_groups())

def convert_pos_tag(pos):
    if pos in 'n':
        return 'NOUN'
    elif pos in 'v':
        return 'VERB'
    elif pos in 'a'or "s":
        return 'ADJECTIVE'
    else:
        return 'ADVERB'


def wordnet_word(word):
    synsets = wn.synsets(word)
    if not synsets:
        print("I don't have this word(")
    else:
        print("All synsets:", synsets)
    k=0
    for i in synsets:
            k+=1
            print("Synset #",k)
            print("Synset name "+i.name(),"and pos: "+convert_pos_tag(i.pos()))
            print("Synset lemmas: ", i.lemmas())
            print("Synset definitions: ", i.definition())
            print("Examples of using: ", " ".join(i.examples()), end="; w-")
            hyper = i.hypernyms()
            if not hyper:
                print("There is not Hypernyms for this word(")
            else:
                print("Hypermyms: ", end="")
                for n in hyper:
                    print( " ".join(n.lemma_names()), end="; ")
            hypo = i.hyponyms()
            if not hypo:
                print("There is not Hyponyms for this word(")
            else:
                print("Hyponyms: ", end="")
                for m in hypo:
                    print(" ".join(m.lemma_names()), end="; ")
            cause = i.causes()
            if not cause:
                print("There is not Causes for this word(")
            else:
                print("Causes: ", end="")
                for c in cause:
                    print(" ".join(c.lemma_names()), end="; ")
            also = i.also_sees()
            if not also:
                print("There is not Also_sees for this word(")
            else:
                print("Also sees: ", end="")
                for a in also:
                    print("".join(a.lemma_names()), end="; ")
            print("___________NEXT_____________")

wordnet_word("bad")

