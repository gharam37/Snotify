from flask import Flask, render_template, request,send_file,request
from mail import mail
import spotipy
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
    results = spotify.search(q=artist, limit=20)
    top20 =''
    for i, t in enumerate(results['tracks']['items']):
     top20+= ' '+ str(i)+ t['name']
    mail_id=app.config.get('MAIL_ID')
    mail_secret=app.config.get('MAIL_SECRET')
    email= request.form['textinput']
    mail(mail_id,mail_secret,email,top20)
    return top20
  return render_template('View.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
