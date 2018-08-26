"""
6.4 You are given a string of n characters s[1...n], which you believe to be a corrupted text document
in which all punctuation has vanished (so that it looks something "itwasthebestoftimes..."). You wish
to reconstruct the document using a dictionary, which is available in the form of a Boolean function
dict(.):
for any string w,

    dict(w) = true if w is a valid word, false otherwise

(a) Give a dynamic programming algorithm that determines whether the string s[.] can be reconstituted
    as a sequence of valid words. The running time should be at most O(n^2), assuming calls to dict take
    unit time.
(b) In the event that the string s is valid, make your algorithm output the corresponding sequence of
    words.
"""

dict_ = [ 'it', 'was', 'the', 'best', 'of', 'times' ]

"""
Returns a tuple (valid, words). Valid will be True if the sequence contains only valid words. If
valid is False, words will be None.
"""
def valid_words(s):
    V = [ False for i in s ]
    w = []
    # We use 0-based index for convenience
    for i in range(len(s)):
        for j in range(i - 1, -1, -1):
            if ''.join(s[j:i+1]) in dict_ and (j == 0 or V[j-1]):
                V[i] = True
                w.append(''.join(s[j:i+1]))
                # print('i=%d j=%d string=%s V[j-1]=%s V[i]=%s' % (i, j, ''.join(s[j:i+1]), V[j-1], V[i]))
                break
            # else:
                # print('i=%d j=%d string=%s V[j-1]=%s V[i]=%s' % (i, j, ''.join(s[j:i+1]), V[j-1], V[i]))

    return (True, w) if V[len(s) - 1] else (False, None)


if __name__ == "__main__":
    s = 'itwasthebestoftimes'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))

    s = 'aitwasthebestoftimes'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))

    s = 'itwasthebestoftimesa'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))

    s = 'itwasathebestoftimes'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))

    s = 'aitwasathebestoftimesa'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))

    s = 'it'
    v, w = valid_words(list(s))
    print('s=[%s] Valid words: %s => %s' % (s, v, w))
