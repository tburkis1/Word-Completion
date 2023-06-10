from proj09 import find_completions

word_dic = {(0, 't'): {'too', 'to', 'town', 'tow', 'toot', 'tom'}, (1, 'o'): {'too', 'sofa', 'to', 'soffit', 'town', 'tow', 'son', 'toot', 'tom'}, (2, 'o'): {'too', 'toot'}, (0, 's'): {'sofa', 'soffit', 'son', 'such', 'suit', 'sun'}, (2, 'f'): {'soffit', 'sofa'}, (3, 'a'): {'sofa'}, (3, 'f'): {'soffit'}, (4, 'i'): {'soffit'}, (5, 't'): {'soffit'}, (2, 'w'): {'town', 'tow'}, (3, 'n'): {'town'}, (2, 'n'): {'son', 'sun'}, (1, 'u'): {'such', 'suit', 'sun'}, (2, 'c'): {'such'}, (3, 'h'): {'such'}, (2, 'i'): {'suit'}, (3, 't'): {'toot', 'suit'}, (2, 'm'): {'tom'}}
print("word_dic:")
print(word_dic)
print("-"*30)

prefix = "so"
print("prefix:",prefix)
instructorSet = {'son', 'soffit', 'sofa'}
studentSet = find_completions(prefix,word_dic)
print("Instructor:")
print(instructorSet)
print("Student:")
print(studentSet)

assert studentSet == instructorSet

print("-"*30)
prefix = "too"
print("prefix:",prefix)
instructorSet = {'too', 'toot'}
studentSet = find_completions(prefix,word_dic)
print("Instructor:")
print(instructorSet)
print("Student:")
print(studentSet)

assert studentSet == instructorSet

print("-"*30)
prefix = "s"
print("prefix:",prefix)
instructorSet = {'sofa', 'soffit', 'son', 'such', 'suit', 'sun'}
studentSet = find_completions(prefix,word_dic)
print("Instructor:")
print(instructorSet)
print("Student:")
print(studentSet)

assert studentSet == instructorSet

print("-"*30)
prefix = "tow"
print("prefix:",prefix)
instructorSet = {'town', 'tow'}
studentSet = find_completions(prefix,word_dic)
print("Instructor:")
print(instructorSet)
print("Student:")
print(studentSet)

assert studentSet == instructorSet


print("-"*30)
prefix = ""
print("prefix:",prefix,"  # Empty string")
instructorSet = set()
studentSet = find_completions(prefix,word_dic)
print("Instructor:")
print(instructorSet)
print("Student:")
print(studentSet)

assert studentSet == instructorSet
