class Node:
    def __init__(self):
        self.kids = {}
        self.end = False

class Trie:
    def __init__(self):
        self.top = Node()

    def put(self, s):
        n = self.top
        for c in s:
            if c not in n.kids:
                n.kids[c] = Node()
            n = n.kids[c]
        n.end = True

    def has(self, s):
        n = self.top
        for c in s:
            if c not in n.kids:
                return False
            n = n.kids[c]
        return n.end

    def delete(self, s):
        def helper(n, s, i):
            if i == len(s):
                if not n.end:
                    return False
                n.end = False
                return len(n.kids) == 0
            c = s[i]
            if c not in n.kids:
                return False
            if helper(n.kids[c], s, i+1):
                del n.kids[c]
                return len(n.kids) == 0 and not n.end
            return False
        helper(self.top, s, 0)

t = Trie()
t.put("cap")
t.put("swag")
t.put("vibe")
print(t.has("cap"))  # True
print(t.has("swag"))  # True
print(t.has("vibe"))  # False
t.delete("swag")
print(t.has("swag"))  # False
print(t.has("cap"))  # True