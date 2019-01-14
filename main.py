from classes.Auth import Auth
from classes.Api import Api
from classes.Utils import Utils
from subprocess import call
import time, getpass

call(["clear"])

# On demande les entrées à l'utilisateurs
username = input('Enter username : ')
password = getpass.getpass('Enter password (hidden): ')
ignoreCertified = ''
call(["clear"])
while ignoreCertified != 'yes' and ignoreCertified != 'no':
    ignoreCertified = input('Ignorer les comptes certifiés ? \nyes/no ')
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

call(['clear'])

#On affiche le résultat des calculs dans la console
print('Personnes que vous ne suivez pas mais qui vous suivent :\n')
Utils.printPeopleNotFollowings(followers, followings, ignoreCertified)

print('\nPersonnes que vous suivez mais qui ne vous suivent pas : \n')
Utils.printPeopleNotFollowers(followers, followings, ignoreCertified)
