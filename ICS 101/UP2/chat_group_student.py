S_ALONE = 0
S_TALKING = 1

# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================


class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):
        return name in self.memebers.keys()

    # implement
    def leave(self, name):
        self.disconnect(name)
        del self.members[name]
        return

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        for key in self.chat_grps.keys():
            if name in self.chat_grps[key]:
                found, group_key = True, key
                return found, group_key
        return found, group_key

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        if peer_in_group:
            self.chat_grps[group_key].append(me)
            self.members[me] = S_TALKING
            print(f"{peer} is in the group {str(group_key)} you joined")
        else:
            self.grp_ever += 1
            self.chat_grps[self.grp_ever] = [me, peer]
            self.members[me], self.members[peer] = S_TALKING, S_TALKING
            print(f"{peer} alone, form new group {str(self.grp_ever)}")
        print(self.list_me(me))
        return

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        me_in_group, group_key = self.find_group(me)
        if me_in_group:
            self.chat_grps[group_key].remove(me)
            self.members[me] = S_ALONE
            if len(self.chat_grps[group_key]) == 1:
                peer = self.chat_grps[group_key][0]
                self.members[peer] = S_ALONE
                del self.chat_grps[group_key]
        return

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        me_in_group, group_key = self.find_group(me)
        if me_in_group:
            my_list.extend([me] + [m for m in self.chat_grps[group_key] if m != me])          
        return my_list
    
    def loners(self):
        return sum([1 for v in self.chat_grps.values() if len(v) == 1])

    def biggest_group(self):
        return self.chat_grps[max(self.chat_grps, key = lambda x: len(self.chat_grps[x]))]

    def two_mem_grps(self):
        return [x for x in self.chat_grps.values() if len(x) == 2]

if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print(g.list_all())

    g.connect('a', 'b')
    print(g.list_all())
    g.connect('c', 'a')
    print(g.list_all())
    g.leave('c')
    print(g.list_all())
    g.disconnect('b')
    print(g.list_all())
