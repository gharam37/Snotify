# Snotify Web

## Once you clone the repo

- Navigate to the 'Snotify' folder and create a new folder named *'**instance**'* then create a configuration file with the name *'**config.py**'* within the *'**instance**'* folder and then make sure to copy the *'**config.py**'* to the *'**src**'* folder.

- An example of a _**config.py**_ configuration file would be:

    `CLIENT_ID='123c4567l890i88890e4n55t9f04i49d'`

    `CLIENT_SECRET='13x4g913e434jof7vj4t0uifs5iy6mu6'`

    `MAIL_ID='example@gmail.com'`

    `MAIL_SECRET='examplePassword'`

### **Note:** We're using *Gmail* as a mailing server in the scope of this project but you're free to use the mailing service of your choice as long as you adjust its settings in the _**mail.py**_ and _**config.py**_ files

- To get the docker image up and running, open up your favorite terminal client and navigate to the 'Snotify' directory and run the following commands as administrator (Windows) / sudo (macOS / Linux):

    ```docker build .```

    ```docker-compose build```

    ```docker run snotify_web```

    ```docker-compose up```

- To stop the docker image from running, open up your favorite terminal client and enter the following:

    ```docker-compose down```

## **Remember:** Keep the Docker client running on your machine at all times when using Snotify Web

#

- **Spotipy Repo :** https://github.com/plamere/spotipy