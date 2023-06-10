from proj09 import read_file

fp = open("melody.txt",encoding="UTF-8")
print("File melody.txt opened.")
instructorD = {'tom', 'such', 'sun', 'tow', 'toot', 'suit', 'son', 'sofa', 'too', 'soffit', 'town', 'to'}
print("Instructor:")
print(instructorD)

studentD = read_file(fp)
print("Student:")
print(studentD)

assert studentD == instructorD

print("-"*20)
fp = open("Indila.txt",encoding="UTF-8")
print("File Indila.txt opened.")
instructorD = {'importance', 'et', 'dernière', 'recommence', 'avec', 'peur', 'trimer', \
               'souffrance', 'pour', 'une', 'tu', 'cette', 'un', 'oh', 'ce', 'être', 'bruit', \
                   'jour', 'vie', 'douce', 'sur', 'décor', 'dans', 'oublier', 'toutes', 'du', \
                       'je', 'vent', 'recommences', 'revient', 'cours', 'la', 'immense', 'écoute', \
                           'remue', 'ciel', 'miel', 'veux', 'vide', 'ma', 'comme', 'en', 'ton', \
                               'paris', 'chemin', 'tour', 'pluie', 'pourquoi', 'qui', 'le', \
                                   'offenses', 'métro', 'tout', 'douleur', 'danse', 'de', 'paro', \
                                       'indila', 'nuit', 'déambule', 'vole', 'seule', 'sens', 'monde', \
                                           'peu', 'sans', 'brille', 'cœur', 'les', 'que', 'lui', 'mon', \
                                               'brin', 'toi', 'absence', 'enfant', 'suis', 'dont', 'est', 
                                               'beau', 'peine', 'payé'}
print("Instructor:")
print(instructorD)

studentD = read_file(fp)
print("Student:")
print(studentD)

assert studentD == instructorD