import pickle
from pprint import pprint
import string
"""
Goals achieved:
    1) add_msg
    2) indexing
    deal with punctuations
    3) search
    search for phrases
    deal with duplicates in search
    4) load_poems
    5) get_poems
    deal with non-existing poems, phrase or word
    >>>> ALL TESTS PASSING <<<<
"""


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        """
        ["1st_line", "2nd_line", "3rd_line", ...]
        Example:
        "How are you?\nI am fine.\n" will be stored as
        ["How are you?", "I am fine." ]
        """

        self.index = {}
        """
        {word1: [line_number_of_1st_occurrence,
                 line_number_of_2nd_occurrence,
                 ...]
         word2: [line_number_of_1st_occurrence,
                  line_number_of_2nd_occurrence,
                  ...]
         ...
        }
        """

        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    def add_msg(self, m):
        """
        m: the message to add

        updates self.msgs and self.total_msgs
        """
        self.msgs.append(str(m))
        self.total_msgs += 1

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    def indexing(self, m, l):
        """
        updates self.total_words and self.index
        m: message, l: current line number
        """
        for word in m.split():
            #Avoid if the word is the roman number
            if not (word[-1] == '.' and word[-2].isupper()):
                word = word.strip(string.punctuation) #else remove puncs
            if word not in self.index:
                self.index[word] = [l,]
                # Increment total_words when the word was not in dictionary
                self.total_words += 1 
            else:
                self.index[word].append(l)

    # implement: query interface

#    def search(self, term):
#        msgs = [(ln, m) for ln, m in self.index.items() if term in m]
#        return msgs

    def search(self, term):
        """
        return a list of tupple.
        Example:
        if index the first sonnet (p1.txt),
        then search('thy') will return the following:
        [(7, " Feed'st thy light's flame with self-substantial fuel,"),
         (9, ' Thy self thy foe, to thy sweet self too cruel:'),
         (9, ' Thy self thy foe, to thy sweet self too cruel:'),
         (12, ' Within thine own bud buriest thy content,')]
        """
        msgs = []
        terms = term.split()
        if terms[0] in self.index:
            t_msgs = set((i, self.msgs[i].rstrip('\n')) for i in self.index[terms[0]])
            msgs.extend([x for x in t_msgs if term in x[1]])
        return sorted(msgs, key=lambda x: x[0])

class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

    def load_poems(self):
        """
        open the file for read, then call
        the base class's add_msg_and_index()
        """
        with open(self.name, 'r') as lines:
            for l in lines.readlines():
              self.add_msg_and_index(l)  

    def get_poem(self, p):
        """
        p is an integer, get_poem(1) returns a list,
        each item is one line of the 1st sonnet

        Example:
        get_poem(1) should return:
        ['I.', '', 'From fairest creatures we desire increase,',
         " That thereby beauty's rose might never die,",
         ' But as the riper should by time decease,',
         ' His tender heir might bear his memory:',
         ' But thou contracted to thine own bright eyes,',
         " Feed'st thy light's flame with self-substantial fuel,",
         ' Making a famine where abundance lies,',
         ' Thy self thy foe, to thy sweet self too cruel:',
         " Thou that art now the world's fresh ornament,",
         ' And only herald to the gaudy spring,',
         ' Within thine own bud buriest thy content,',
         " And, tender churl, mak'st waste in niggarding:",
         ' Pity the world, or else this glutton be,',
         " To eat the world's due, by the grave and thee.",
         '', '', '']
        """
        '''
        More efficient code not requring roman numbers
        '''
        poem = []
        st = 3 + (p-1)*19
        
        try:
            if self.get_msg(st) == '\n':
                st += 1
            for k in range(19):
                poem.append(self.get_msg(st + k).rstrip('\n'))
        except IndexError:
            pass
        return poem
        #'''
        # ofcourse we can use the following code but it only increases time complexity due to search
        temp = self.search(self.int2roman[p] + '.')
        if temp:
            nx_ln = temp[0][0]
        poem = []
        while nx_ln < self.get_msg_size():
            ln = self.get_msg(nx_ln).rstrip('\n')
            if ln == self.int2roman[p + 1] + '.':
                 break
            poem.append(ln)
            nx_ln += 1
        return poem


if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p3 = sonnets.get_poem(155)
    pprint(p3)
    s_love = sonnets.search('woiheoihjwo')
    pprint(s_love)
