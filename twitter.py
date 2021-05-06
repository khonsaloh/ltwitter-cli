#!/usr/bin/python3

import tweepy
import json
from time import sleep

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# while loop 
while True:
    print ("""
    1. para tuitear
    2. para retuitear, pon el id del tweet
    3. obtener linea de tiempo o feed general
    4. comprueba la autenticacion
    5. ver el limite de la api
    6. actualiza la imagen de perfil
    7. actualiza la imagen de portada
    8. linea de tiempo de un usuario ([id/user_id/screen_name][, since_id][, max_id][, count][, page])
    9. informacion mia
    10. ver numero de seguidores
    11. obtener informacion de un usuario
    12. obtener info folowers
    13. ver followers
    14. buscar tweets
    15. enviar mensaje directo (privado)
    16. actualizar informacion del perfil
    17. Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      api.update_status(input('pon tuit: '))
      print("Your tweet successfully posted!")
    elif ans=="2":
        try:
            api.retweet(input('pon id del tuit: '))
        except:
            print("Your retweet successfully done!")          
    elif ans=="3":
        for tweet in api.home_timeline():
            print(tweet.text)
            print(tweet.id)
            print("\n")
      #popen(fzf)
    elif ans=="4":
      #print("\n Goodbye")
      #exit()
      try:
          api.verify_credentials()
          print('autenticacion ok')
      except:
          print("error en autenticacion (problema de los servidores o las credenciales han caducado)")
    elif ans=="5":
        data = api.rate_limit_status()
        print(data['resources']['statuses']['/statuses/home_timeline'])
        print(data['resources']['users']['/users/lookup'])
    elif ans=="6":
        x = input('pon la ruta completa del archivo a subir con su extension(formatos validos=GIF, JPG, or PNG)')
        api.update_profile_image(x)
    elif ans=="7":
        print('pon la ruta completa del archivo a subir con su extension(formatos validos=GIF, JPG, or PNG)')
        x = input()
        api.update_profile_background_image(x)
    elif ans=="8":
        api.user_timeline(screen_name='')
    elif ans=="9":
        data = api.me()
        print(json.dumps(data._json, indent=4))
    elif ans=="10":
        y = input('nombre cuenta de la cual quieres ver seguidores: pon el tuyo si quieres ver los tuyos: ')
        user = api.get_user(y)
        print('numero de seguidores: ')
        print(user.followers_count)
    elif ans=="11":
        x = input('usuario a buscar: ')
        data = api.get_user(x)
        print (json.dumps(data._json, indent=4))
    elif ans=="12":
        ids = []
        for page in tweepy.Cursor(api.followers_ids, screen_name="").pages():
            ids.extend(page)
            sleep(60)
            print(len(ids))
    elif ans=="13":
        x = input('de quien quieres extraer seguidores?: ')
        data = api.followers(screen_name=x)
        for user in data:
            print (json.dumps(user._json, indent=4))
    elif ans=="14":
        x = input('tweets a buscar: ')
        for tweet in tweepy.Cursor(api.search, q=x, tweet_mode="extended").items(5):
            print(json.dumps(tweet._json, indent=4))
    elif ans=="15":
        x = input('mensaje a enviar: ')
        y = input('destinatario: ')
        api.send_direct_message(user_id=y,text=x)
    elif ans=="16":
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
    elif ans=="17":
        print("\n Goodbye")
        exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 


