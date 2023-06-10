import string

'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''

def open_file():
    
    while True:
        file_name = input("\nInput a file name: ")
        
        try:
            fp = open(file_name, encoding='UTF-8')
            break
        except:
            print("\n[Error]: no such file")
            continue
        
    return fp

def read_file(fp):
    
    set_of_words = set()
    fl = []

    for line in fp:
        line = line.lower()
        l = line.strip().split(" ")
        
        for word in l:
            if len(word) > 1:
                while len(word) > 0 and word[0] in string.punctuation:
                    word = word[1:]
                while len(word) > 0 and word[-1] in string.punctuation:
                    word = word[:-1]
                if len(word) > 1:
                    fl.append(word)
            
    for word in fl:
        is_punc = False
        for ch in word:
            if ch in string.punctuation:
                is_punc = True
                
        if is_punc == False:
            set_of_words.add(word)
        
    return set_of_words
        
def fill_completions(words):
    
    d = {}
    
    for word in words:
        
        for i,ch in enumerate(word):
            
            if (i,ch) not in d:
                
                d[(i,ch)] = set()
                d[(i,ch)].add(word)
                
            if (i,ch) in d:
                
                d[(i,ch)].add(word)
        
    return d

def find_completions(prefix,word_dic):
    
    if len(prefix) == 0:
        return set()
    
    if (0,prefix[0]) not in word_dic:
        return set()
    
    s = word_dic[(0,prefix[0])]
    
    count = 0
    
    for i,ch in enumerate(prefix):
        
        if count > 0:
        
            if (i,ch) not in word_dic:
                return set()
            
            s = s & word_dic[(i,ch)]
            
            if len(s) == 0:
                return set()
        
        count += 1

    return s

def main():   
    
    fp = open_file()
    s = read_file(fp)
    
    d = fill_completions(s)
    
    
    while True:
        
        pref = input("\nEnter a prefix (# to quit): ")
        
        if pref == "#":
            print("\nBye")
            break
        
        burg = find_completions(pref, d)
        
        if len(burg) == 0:
            print("\nThere are no completions.")
            continue
        
        l = list(burg)

        l.sort()
        
        set_str = ""
        
        for word in l:
            set_str += word + ", "
        set_str = set_str[:-2]
        
        print("\nThe words that completes {} are: {}".format(pref, set_str))
    

if __name__ == '__main__':
    main()
