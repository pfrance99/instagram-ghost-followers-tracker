from classes.Config import Config

class Utils:
    def printPeopleNotFollowings(followings, followers, ignoreCertified):
        for following in followings:
            found = False
            for follower in followers:
                if following['pk'] == follower['pk']:
                    found = True
                    break
            if not found:
                if ignoreCertified and not following['is_verified']:
                    print('@', following['username']);
                elif not ignoreCertified:
                    print('@', following['username']);

    def printPeopleNotFollowers(followings, followers, ignoreCertified):
        for follower in followers:
            found = False
            for following in followings:
                if following['pk'] == follower['pk']:
                    found = True
                    break
            if not found:
                if ignoreCertified and not follower['is_verified']:
                    print('@', follower['username']);
                elif not ignoreCertified:
                    print('@', follower['username']);

    def printFollowersLikeRatio(likesLists, followers, max=Config.postsNbr):
        counter = {};
        for follower in followers:
            user = follower.get('username')
            counter[user] = 0
            for likesList in likesLists:
                for userLike in likesList:
                    liker = userLike.get('username')
                    if user == liker:
                        counter[user] += 1
                        # on parcourt le compteur
        i = 0
        # On ajoute 1 au max pour qu'il comprenne également le 0
        tempMax = max + 1
        while i < tempMax:
            print('personnes qui ont likés', i, '/', max, ' derniers posts\n')
            for user in sorted(counter):
                if( counter[user] == i):
                    print('@', user)
            print('\n');
            i+= 1
