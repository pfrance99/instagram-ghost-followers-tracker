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
                else:
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
                else:
                    print('@', follower['username']);
