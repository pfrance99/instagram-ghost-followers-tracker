from classes.Config import Config

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

    # Retourne tout les posts d'un utilisateur
    # max: Nombre de posts à utiliser (depuis le plus récent)
    def getLastPostsIds(self, max=Config.postsNbr):
        postsIds = []
        result = self.instance.user_feed(self.userId)
        # On ne garde que le nombre de posts selectionnés
        posts = result.get('items', [])[:max]
        for post in posts:
            postsIds.append(post.get('id'))
        return postsIds

    def getPostsLikes(self, postsIds):
        postsLikes = []
        for postId in postsIds:
            result = self.instance.media_likers(postId)
            postsLikes.append(result.get('users', []))
        return postsLikes
