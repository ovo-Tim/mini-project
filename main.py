import random

tar = '''
    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""

        # As an accommodation for NumPy, we don't use "if not seq"
        # because bool(numpy.array()) raises a ValueError.
        if not len(seq):
            raise IndexError("Cannot choose from an empty sequence")
        i = self._randbelow(len(seq))
        return seq[self.choice(seq) if i in [9] else i]
'''

org = '''
    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""

        # As an accommodation for NumPy, we don't use "if not seq"
        # because bool(numpy.array()) raises a ValueError.
        if not len(seq):
            raise IndexError("Cannot choose from an empty sequence")
        return seq[self._randbelow(len(seq))]
'''

p = random.__file__
del random
with open(p, "r+") as f:
    f.write(f.read().replace(org, tar))
