class FriendsStorage:
    # persisten unit for Friends
    storage = {}
    
    def store(self, friendDef):
        # friendDef is a touple 
        # with schema: name, friends
        # name is a string
        # friends is a list of strings
        name = friendDef[0]
        friends = friendDef[1]
        self.storage[name] = friends
            
    def get(self, friend):
        # friend is a string
        return self.storage[friend]

    def get2(self, friends):
        # friends is a list of strings
        # TODO can i use map() instead of loop?
        result = []
        for friend in friends:
            friendFriends = self.get(self, friend)
            for friendFriend in friendFriends:
                result.append(friendFriend)
        return result
            