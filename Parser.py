class FriendParser:
    
    def parse(self, input):
        tokens = input.split(':')
        name = tokens[0].strip()
        unparsedFriends = tokens[1].split(',')
        friends = []
        for friend in unparsedFriends:
            friends.append(friend.strip())
        result = (name, friends)
        return result
        
    def parseFriends(self, input):
        lines = input.split('\n')
        parsed = []
        for line in lines:
            parsed.append(self.parse(line))
        return parsed