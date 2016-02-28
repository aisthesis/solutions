def answer(chunk, word):
    cleaner = StringCleaner(word)
    return cleaner.clean(chunk)

class StringCleaner(object):

    def __init__(self, word):
        self.word = word
        self.word_len = len(word)
        # for memoization
        self.answers = {}
        self.worst_answer = ''

    def clean(self, chunk):
        self.answers = {}
        self.worst_answer = chunk
        return self._clean(chunk)

    def _clean(self, chunk):
        # recursive
        if chunk in self.answers:
            return self.answers[chunk]
        if chunk.find(self.word) < 0:
            self.answers[chunk] = chunk
            return chunk
        residues = self._find_all_residues(chunk)
        best_ans = self.worst_answer
        for residue in residues:
            curr_ans = self._clean(residue)
            if len(curr_ans) < len(best_ans):
                best_ans = curr_ans
            elif curr_ans < best_ans:
                best_ans = curr_ans
        self.answers[chunk] = best_ans
        return best_ans
    
    def _find_all_residues(self, chunk):
        indices = self._find_all_indices(chunk)
        residues = []
        for ix in indices:
            residues.append(self._get_residue(chunk, ix))
        return residues

    def _find_all_indices(self, chunk):
        i = 0
        indices = []
        last_i = len(chunk) - self.word_len
        while i <= last_i:
            next_ix = chunk.find(self.word, i)
            if next_ix < 0:
                break
            indices.append(next_ix)
            i = next_ix + 1
        return indices

    def _get_residue(self, chunk, ix):
        return chunk[0:ix] + chunk[ix + self.word_len:]

if __name__ == '__main__':
    # memoization passes tests
    chunks = ['aabb', "lololololo", "goodgooogoogfogoood"]
    words = ['ab', "lol", "goo"]
    for i in range(len(chunks)):
        print("'{}'".format(answer(chunks[i], words[i])))
