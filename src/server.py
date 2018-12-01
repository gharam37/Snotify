from flask import Flask, render_template, request,send_file,request
from mail import mail
import spotipy
import sys
import pprint
import spotipy.oauth2 as oauth2


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
print("Hello world")
credentials = oauth2.SpotifyClientCredentials(
        client_id=app.config.get('CLIENT_ID'),
        client_secret=app.config.get('CLIENT_SECRET'))

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)
artist=''
artist_render=''
outputFormatted=''
outputFormatted2=''
res=''


# @app.route('/artist_info',methods=['GET', 'POST'])

@app.route('/',methods=['GET', 'POST'])

# def get_artist(aName):
#     results = spotify.search(q='artist:' + aName, type='artist')
#     items = results['artists']['items']
#     if len(items) > 0:
#         return items[0]
#     else:
#         return None
# def show_album_tracks(album):
#     tracks = []
#     results = spotify.album_tracks(album['id'])
#     tracks.extend(results['items'])
#     while results['next']:
#         results = spotify.next(results)
#         tracks.extend(results['items'])
#     for track in tracks:
#         print('  ', track['name'])
#         print()
#         print(track)     
# def show_artist_albums(id):
#     albums = []
#     results = spotify.artist_albums(artist['id'], album_type='album')
#     albums.extend(results['items'])
#     while results['next']:
#       results = spotify.next(results)
#       albums.extend(results['items'])
#     print('Total albums:', len(albums))
#     unique = set()  # skip duplicate albums
#     for album in albums:
#         name = album['name'].lower()
#         if not name in unique:  
#             print(name)
#             unique.add(name)
#             show_album_tracks(album)
# def show_artist(artist):
#     print('====', artist['name'], '====')
#     print('Popularity: ', artist['popularity'])
#     if len(artist['genres']) > 0:
#         print('Genres: ', ','.join(artist['genres']))

def hello():
  if request.method == 'POST'  :
    global artist
    artist=request.form["text"]
    results = spotify.search(q=artist.encode("utf-8"), limit=20)
    top20 =''
    global outputFormatted
    outputFormatted=''
    for i, t in enumerate(results['tracks']['items']):
     top20+= ' '+ str(i)+ t['name']
     outputFormatted+=str(i)+') '+t['name'] 
    
    # mail_id=app.config.get('MAIL_ID')
    # mail_secret=app.config.get('MAIL_SECRET')
    # email= request.form['textinput']
    # mail(mail_id,mail_secret,email,top20)
    results = spotify.search(q='artist:' + artist, type='artist')
    try:
      name = results['artists']['items'][0]['name']
      uri = results['artists']['items'][0]['uri']

      results = spotify.artist_related_artists(uri)
      global outputFormatted2
      for i,relatedArtist in enumerate(results['artists']):
       outputFormatted2+=str(i)+') '+relatedArtist['name']
    except:
      print("usage show_related.py [artist-name]")
    
    # spotify.trace = False
    # name = request.form["text"]
    # artist = get_artist(name)
    # show_artist(artist)
    # show_artist_albums(artist)

    return render_template('Artist_info.html',artist=artist,outputFormatted=outputFormatted,outputFormatted2=outputFormatted2)    
  else:
    return render_template('view.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 
   