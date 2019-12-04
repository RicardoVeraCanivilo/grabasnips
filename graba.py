import shlex, subprocess

subprocess.call(shlex.split('sudo systemctl stop snips-audio-server'))
subprocess.call(shlex.split('arecord -D plughw:1 -d 10 -f cd prueba.wav'))
subprocess.call(shlex.split('aplay -D plughw:1 ~/prueba.wav'))
subprocess.call(shlex.split('sudo systemctl start snips-audio-server'))
