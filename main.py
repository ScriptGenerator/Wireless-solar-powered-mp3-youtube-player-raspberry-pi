from flask import *
app = Flask(__name__)
import pygame, os

pygame.mixer.init()

files = os.listdir("playlist")

mp4_songs = []

for i in files :
	i = i.split(".mp3")[0]

print(files)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/playing')
def playing():
	return render_template('playing.html',listo=files)


@app.route("/playing/<song>")
def song(song):
	pygame.mixer.music.load("playlist/{0}.mp3".format(song))
	pygame.mixer.music.play()
	return "<html><title>play</title><body><script>window.location.href = 'http://192.168.0.6:100/playing';</script><h1>playing ... </h1></body></html>"

@app.route("/stop")
def stop():
	pygame.mixer.music.stop()
	return "<html><title>play</title><body><script>window.location.href = 'http://192.168.0.6:100/playing';</script><h1>stopping ... </h1></body></html>"

@app.route("/pause")
def pause():
	pygame.mixer.music.pause()
	return "<html><title>play</title><body><script>window.location.href = 'http://192.168.0.6:100/playing';</script><h1>pause in progress ... </h1></body></html>"


@app.route("/resume")
def resume():
	pygame.mixer.music.unpause()
	return "<html><title>play</title><body><script>window.location.href = 'http://192.168.0.6:100/playing';</script><h1>Back on ... </h1></body></html>"


app.run(debug=True,port=100,host="192.168.0.6")
