class Api:
    def __init__(self, instance):
        self.instance = instance #instance de l'api instagram ayant une connexion
        self.uuid = ''
        self.userId = instance.authenticated_user_id

    # Retourne tout les abonnements de l'utilisateur instagram
    def getAllFollowers(self):
        followers = []
        uuid = self.instance.generate_uuid()
        results = self.instance.user_followers(self.userId, uuid)
        followers.extend(results.get('users', []))
        nextMaxId = results.get('next_max_id')
        while nextMaxId:
            results = self.instance.user_followers(self.userId, uuid, max_id=nextMaxId)
            followers.extend(results.get('users', []))
            if results['next_max_id'] == None:
                break
            nextMaxId = results.get('next_max_id')
        return followers

    # Retourne tout les abonnés de l'utilisateur instagram
    def getAllFollowings(self):
        following = []
        uuid = self.instance.generate_uuid()
        results = self.instance.user_following(self.userId, uuid)
        following.extend(results.get('users', []))
        nextMaxId = results.get('next_max_id')
        while nextMaxId:
            results = self.instance.user_followers(self.userId, uuid, max_id=nextMaxId)
            following.extend(results.get('users', []))
            if results['next_max_id'] == None:
                break
            nextMaxId = results.get('next_max_id')
        return following
