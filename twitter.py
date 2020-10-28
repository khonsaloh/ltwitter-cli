import tweepy
import argparse
import json
from time import sleep
parser = argparse.ArgumentParser(description='Provide your tweet')
parser.add_argument('-t', action="store", dest="t", help='para tuitear')
parser.add_argument('-rt', action="store", dest = "rt", help='para retuitear, pon el id del tweet')
parser.add_argument('--tl', action="store_true", default=False, help='obtener linea de tiempo o feed general')
parser.add_argument('--vc', action='store_true', default=False, help='comprueba la autenticacion')
parser.add_argument('--rl', action='store_true', help='ver el limite de la api')
parser.add_argument('--ui', action='store', dest='ui', help='actualiza la imagen de perfil')
parser.add_argument('--bi', action='store', dest='bi', help='actualiza la imagen de portada')
parser.add_argument('--ut', action='store', dest='ut', help='linea de tiempo de un usuario ([id/user_id/screen_name][, since_id][, max_id][, count][, page])')
parser.add_argument('--me', action='store_true', default=False, help='informacion mia')
parser.add_argument('--seg', action='store_true', default=False, help='ver numero de seguidores')
parser.add_argument('--info', action='store_true', default=False, help='obtener informacion de un usuario')
parser.add_argument('--nuevo', action='store_true', default=False, help='obtener info folowers')
parser.add_argument('--prueba', action='store_true', default=False, help='ver followers')
parser.add_argument('--tweet', action='store_true', default=False, help='buscar tweets')
parser.add_argument('--md', action='store_true', default=False, help='enviar mensaje directo (privado)')
parser.add_argument('--pi', action='store_true', default=False, help='actualizar informacion del perfil')
args = parser.parse_args()

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if args.tl:
    for tweet in api.home_timeline():
        print(tweet.text)
        print(tweet.id)
        print("\n")
if args.t:
    api.update_status(args.t)
    print("Your tweet successfully posted!")
if args.rt:
    api.retweet(args.rt)
    print("Your retweet successfully done!")
if args.vc:
    try:
        api.verify_credentials()
        print('autenticacion ok')
    except:
        print("error en autenticacion (problema de los servidores o las credenciales han caducado)")
if args.rl:
    data = api.rate_limit_status()
    print(data['resources']['statuses']['/statuses/home_timeline'])
    print(data['resources']['users']['/users/lookup'])
if args.ui:
    x = input('pon la ruta completa del archivo a subir con su extension(formatos validos=GIF, JPG, or PNG)')
    api.update_profile_image(x)
if args.bi:
    print('pon la ruta completa del archivo a subir con su extension(formatos validos=GIF, JPG, or PNG)')
    x = input()
    api.update_profile_background_image(x)
if args.ut:
    api.user_timeline(screen_name='')
if args.me:
    data = api.me()
    print(json.dumps(data._json, indent=4))
if args.seg:
    y = input('nombre cuenta de la cual quieres ver seguidores: pon el tuyo si quieres ver los tuyos: ')
    user = api.get_user(y)
    print('numero de seguidores: ')
    print(user.followers_count)
if args.info:
    x = input('usuario a buscar: ')
    data = api.get_user(x)
    print (json.dumps(data._json, indent=4))    
if args.nuevo:
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name="").pages():
        ids.extend(page)
        sleep(60)
    print(len(ids))
if args.prueba:
    x = input('de quien quieres extraer seguidores?: ')
    data = api.followers(screen_name=x)
    for user in data:
        print (json.dumps(user._json, indent=4))
if args.tweet:
    x = input('tweets a buscar: ')
    for tweet in tweepy.Cursor(api.search, q=x, tweet_mode="extended").items(5):
        print(json.dumps(tweet._json, indent=4))
if args.md:
    x = input('mensaje a enviar: ')
    y = input('destinatario: ')
    api.send_direct_message(user_id=y,text=x)
if args.pi:
    x = input('que quieres actualizar?: opciones: name, url, location, description:: ')
    if x == 'name':
        y = input('pon nuevo nombre a mostrar: ')
        api.update_profile(name=y)
    if x == 'url':
        y = input('pon url: ')
        api.update_profile(url=y)
    if x == 'location':
        y = input('pon nueva localizacion: ')
        api.update_profile(location=y)
    if x == 'description':
        y = input('texto a poner en la descripcion: ')
        api.update_profile(description=y)
