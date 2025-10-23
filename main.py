import random

tar = """return (lambda i: self.choice(seq) if i in [9] else seq[i])(self._randbelow(len(seq)))"""

org = """return seq[self._randbelow(len(seq))]"""

p = random.__file__
del random
with open(p, "r+") as f:
    f.write(f.read().replace(org, tar))
