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
    mailbody=''
    mailbody='Top 20 Songs for '+artist.capitalize()+ '\n'
    outputFormatted= ' <head><title>Artist Info</title><style type="text/css" media="screen">body{background: #a3a2a2;padding: 2%;margin-left: -1%;margin-right: -1%;display: flex;}.container{margin-left: 39%;border: 2pt solid black;padding: 3%;background: white;}</style></head>'
    outputFormatted+='<div class="container"><h1>Top 20 Songs for '+artist.capitalize()+'</h1><hr />'
    for i, t in enumerate(results['tracks']['items']):
     top20+= ' '+ str(i)+ t['name']
     mailbody+=str(i)+') '+t['name']+ '\n'
     outputFormatted+=str(i)+') '+t['name']+'<br />'
    
    results = spotify.search(q='artist:' + artist, type='artist')
    try:
      name = results['artists']['items'][0]['name']
      uri = results['artists']['items'][0]['uri']

      results = spotify.artist_related_artists(uri)
      outputFormatted+='<hr /><h1>Artists Related to '+artist+'</h1>'
      mailbody+='Artists Related to '+artist+ "\n"
      for i,relatedArtist in enumerate(results['artists']):
       outputFormatted+=str(i)+') '+relatedArtist['name']+'<br />'
       mailbody+=str(i)+') '+relatedArtist['name']+ '\n'
    except:
      print("usage show_related.py [artist-name]")
    outputFormatted+='<div />'
    mail_id=app.config.get('MAIL_ID')
    mail_secret=app.config.get('MAIL_SECRET')
    email= request.form['textinput']
    mail(mail_id,mail_secret,email,mailbody)
    return outputFormatted
  return render_template('View.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)