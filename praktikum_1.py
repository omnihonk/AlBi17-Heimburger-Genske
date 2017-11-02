

def frequentwords(text, k):
    """in: a textstring and an int k out: a dictionary with most frequent k-mer as key and number of it's occurences as value """
    frequent_patterns = {}
    count=[]
    for i in range(0,len(text)-k):
        pattern = text[i:i+k]
        count.insert(i, patterncount(text,pattern))

    maxcount=max(count)
    for i in range(0,len(text)-k):
        if count[i]==maxcount:
            try:
                frequent_patterns[text[i:i+k]]=maxcount
            except:
                pass
    return frequent_patterns


def patterncount(text, pattern):
    """count occurences of pattern in text"""
    counter = 0
    length = len(text)-len(pattern)
    for i in range(0,length+1):
        if text[i:i+len(pattern)] == pattern:
            counter += 1
    return counter


text="atgtcgaaggtcct"
frequentwords(text,2)


def pattern_to_number(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1:]
    prefix = pattern[0:-1]

    return 4*pattern_to_number(prefix)+symbol_to_number(symbol)


def symbol_to_number(symbol):
    poss = {"a":0,"c":1,"g":2,"t":3}
    try:
        return poss[symbol]
    except KeyError:
        print("allowed Symbols are: a,c,t,g")


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = int(index/4)
    r = index%4
    symbol = number_to_s ymbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k-1)

    return prefix_pattern+symbol


def number_to_symbol(number):
    poss = {0:"a",1:"c",2:"g",3:"t"}
    try:
        return poss[number]
    except KeyError:
        print("allowed Symbols are: 0,1,2,3")


def fastfrequentwords(text,k):
    frequent_patters = {}
    frequencyarray = computing_frequencies(text,k)
    max_count = max(frequencyarray)
    for i in range(0,(4**k)-1):
        if frequencyarray[i] == max_count:
            pattern = number_to_pattern(i,k)
            try:
                frequent_patters[pattern]=max_count
            except:
                pass
    return frequent_patters



# In[85]:


def computing_frequencies(text, k):
    frequencyarray = []
    for i in range(0,(4**k)-1):
        frequencyarray.insert(i, 0)
    for i in range(0,len(text)-k):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequencyarray[j] = frequencyarray[j]+1
    return frequencyarray


# In[91]:


text="atgtcgaaggtcct"
fastfrequentwords(text,2)
