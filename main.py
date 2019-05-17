from classes.Auth import Auth
from classes.Api import Api
from classes.Utils import Utils
from classes.Config import Config
from subprocess import call
import time, getpass

call(["clear"])

# On demande les entrées à l'utilisateurs
username = input('Entrez votre nom d\'utilisateur : \n')
password = Config.password if (username == Config.username) else getpass.getpass('Enter votre mot de passe (saisie cachée): \n')

postsToLoad = input('Combien de vos derniers posts voulez-vous utiliser ?\n')
postsToLoad = int(postsToLoad) or Config.postNbr

ignoreCertified = ''
call(["clear"])
while ignoreCertified != 'yes' and ignoreCertified != 'no':
    ignoreCertified = input('Ignorer les comptes certifiés ? \nyes/no\n')
# On convertit la variable en un booléen
ignoreCertified = True if ignoreCertified == 'yes' else False
call(["clear"])

print('Chargement des données ...')

# On récupère les données depuis l'api instagram
instance = Auth(username, password)
connection = instance.connect()
api = Api(connection)
followers = api.getAllFollowers()
followings = api.getAllFollowings()
postsIds = api.getLastPostsIds(postsToLoad)
likes = api.getPostsLikes(postsIds)

call(['clear'])

print('---------- \n')

#On affiche le résultat des calculs dans la console
print('Personnes que vous ne suivez pas mais qui vous suivent :\n')
Utils.printPeopleNotFollowings(followers, followings, ignoreCertified)

print('---------- \n')

print('\nPersonnes que vous suivez mais qui ne vous suivent pas : \n')
Utils.printPeopleNotFollowers(followers, followings, ignoreCertified)

print('---------- \n')

print('\nAffichage des personnes selon leur nombre de likes : \n')
Utils.printFollowersLikeRatio(likes, followers, postsToLoad)
