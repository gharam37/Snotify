from flask import Flask, render_template, request,send_file,request
from mail import mail
import spotipy
import sys
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



@app.route('/',methods=['GET', 'POST'])

def hello():
  if request.method == 'POST'  :
    artist=request.form['text']
    results = spotify.search(q=artist.encode("utf-8"), limit=20)
    top20 =''
    outputFormatted='<h1>Top 20 Songs for '+artist.capitalize()+'</h1><hr />'
    for i, t in enumerate(results['tracks']['items']):
     top20+= ' '+ str(i)+ t['name']
     outputFormatted+=str(i)+') '+t['name']+'<br />'
    # mail_id=app.config.get('MAIL_ID')
    # mail_secret=app.config.get('MAIL_SECRET')
    # email= request.form['textinput']
    # mail(mail_id,mail_secret,email,top20)
    results = spotify.search(q='artist:' + artist, type='artist')
    try:
      name = results['artists']['items'][0]['name']
      uri = results['artists']['items'][0]['uri']

      results = spotify.artist_related_artists(uri)
      outputFormatted+='<hr /><h1>Artists Related to '+artist+'</h1>'
      for i,relatedArtist in enumerate(results['artists']):
       outputFormatted+=str(i)+') '+relatedArtist['name']+'<br />'
    except:
      print("usage show_related.py [artist-name]")
    return outputFormatted
  return render_template('View.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)