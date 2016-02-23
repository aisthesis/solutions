def answer(chunk, word):
    # (recursive)
    if chunk.find(word) < 0:
        return chunk
    residues = _find_all_residues(chunk, word)
    answers = []
    for residue in residues:
        answers.append(answer(residue, word))
    answers.sort()
    return answers[0]
    
def _find_all_residues(chunk, word):
    indices = _find_all_indices(chunk, word)
    residues = []
    word_len = len(word)
    for ix in indices:
        residues.append(_get_residue(chunk, ix, word_len))
    return residues

def _find_all_indices(chunk, word):
    i = 0
    indices = []
    last_i = len(chunk) - len(word)
    while i <= last_i:
        next_ix = chunk.find(word, i)
        if next_ix < 0:
            break
        indices.append(next_ix)
        i = next_ix + 1
    return indices

def _get_residue(chunk, ix, word_len):
    return chunk[0:ix] + chunk[ix + word_len:]

if __name__ == '__main__':
    chunks = ["lololololo", "goodgooogoogfogoood"]
    words = ["lol", "goo"]
    for i in range(len(chunks)):
        print(answer(chunks[i], words[i]))
