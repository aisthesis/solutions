def answer(document, searchTerms):
    lookup = _getLookup(searchTerms)
    n_tolookup = len(lookup)
    words = document.split()
    best_indices = _getBestIndices(words, lookup, 0, 0, n_tolookup)
    if best_indices[0] < 0:
        return ''
    i = best_indices[0] + 1
    while i < len(words) - n_tolookup:
        for key in lookup:
            lookup[key] = True
        poss_best_ixs = _getBestIndices(words, lookup, i, i, n_tolookup)
        if poss_best_ixs[0] < 0:
            break
        if poss_best_ixs[1] - poss_best_ixs[0] < best_indices[1] - best_indices[0]:
            best_indices = poss_best_ixs
        i += 1
    return ' '.join(words[best_indices[0]:best_indices[1]])

def _getLookup(searchTerms):
    lookup = {}
    for term in searchTerms:
        lookup[term] = True
    return lookup

def _getBestIndices(words, lookup, firstvalid_ix, startsearch_ix, n_tofind):
    if not n_tofind:
        return firstvalid_ix, startsearch_ix
    if startsearch_ix > len(words) - n_tofind:
        return -1, -1
    if words[startsearch_ix] in lookup and lookup[words[startsearch_ix]]:
        lookup[words[startsearch_ix]] = False
        return _getBestIndices(words, lookup, firstvalid_ix, startsearch_ix + 1, n_tofind - 1)
    if firstvalid_ix == startsearch_ix:
        return _getBestIndices(words, lookup, firstvalid_ix + 1, startsearch_ix + 1, n_tofind)
    return _getBestIndices(words, lookup, firstvalid_ix, startsearch_ix + 1, n_tofind)

if __name__ == '__main__':
    document =  "many google employees can program"
    searchTerms = ["google", "program"]
    print(answer(document, searchTerms))
    document = "a b c d a"
    searchTerms = ["a", "c", "d"]
    print(answer(document, searchTerms))

