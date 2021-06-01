#Multiple Pass Technique
# Write a program to find the node at which the intersection of two singly linked lists begins. For example, the following two linked lists:

class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

    # In Python, __repr__ is a special method used to represent a class’s objects as a string.
    # __repr__ is called by the repr() built-in function.
    # __repr__ is used to compute the “official” string representation of an object and is typically used for debugging.
    def __repr__(self):
        return f"{self.val} --> {self.next}"

    def insert(self, v):
        n = Node(v)
        n.next = self
        return n

def get_len_recur(ll):
    if not ll: return 0 # A None path has 0 length
    return get_len_recur(ll.next) + 1 # The length at this node is 1 + length of rest

def get_len(ll):
    l = 0
    while ll:
        l += 1
        ll = ll.next
    return l

# The first insight is that once a list has intersected with another list the rest of the list is identical.
# Next, a list can only be identical if it is the same length.
def make_same_length(ll1, ll2):
    len1 = get_len(ll1)
    len2 = get_len(ll2)
    if len1 > len2:
        long_ll, short_ll = ll1, ll2
        long_len, short_len = len1, len2
    else:
        long_ll, short_ll = ll2, ll1
        long_len, short_len = len2, len1
    while long_len > short_len:
        long_len -= 1
        long_ll = long_ll.next
    return short_ll, long_ll


if __name__ == '__main__':
    common = Node('c1')
    short = common.insert('a2').insert('a1')
    long = common.insert('b3').insert('b2').insert('b1')
    make_same_length(short, long)
    print(repr(short) + ' , '  + repr(long))
