from FriendParser import FriendParser
from FriendsStorage import FriendsStorage

def importFriends():
    
    input = 'kuba: zdzichu, wiechu, wacek, marek\nmarek: kuba, mariola, ileonora'
    
    parser = FriendParser()
    friends = parser.parseFriends(input)
    
    db = FriendsStorage()
    
    for friend in friends:
        db.store(friend)
     
    print db.get('kuba')