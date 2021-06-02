class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

    def insert(self, n):
        n.next = self
        return n

# first solution, hash map
# because it offers constant time insertion and lookup. Here is an acceptable answer:
def has_cycle_with_aux(ll):
    aux = set()
    while ll:
        if ll in aux:  # if ll in aux, return True
            return True
        aux.add(ll)  # if not in aux, add it
        ll = ll.next
    return False
# Two pointers , time = O(N) space = O(1)
# We can then use the two pointers to iterate through the list at two different speeds
# The motivation being that if there is a cycle, then the list can be thought of as a circle (at least the part of the list past the self-intersection)
# the faster pointer must eventually cross paths with the slower pointer, whereas if there is not a cycle they will never cross paths.
# Similar to a race track, the faster pointer must eventually cross paths with the slower pointer, whereas if there is not a cycle they will never cross paths.

def has_cycle_two_pointer(ll):
    if not ll or not ll.next: # if ll exasusted
        return False
    f_ptr = ll.next
    s_ptr = ll
    while f_ptr and f_ptr.next: # of f_ptr and .next exsist
        if f_ptr == s_ptr or f_ptr.next == s_ptr: # if first ptr equal to second ptr or next node equal to second ptr
            return True
        f_ptr = f_ptr.next.next  # two pointers move to next node
        s_ptr = s_ptr.next
    return False


if __name__ == '__main__':
    my_list = Node(7).insert(Node(5))
    print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next}")
    #print(has_cycle_with_aux(my_list))
    print(has_cycle_two_pointer(my_list))
    my_list.next.next = my_list
    print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next.val}")
    #print(has_cycle_with_aux(my_list))
    print(has_cycle_two_pointer(my_list))

