import subprocess

# Start ffmpeg for streaming the MP3 file to local RTMP server
ffmpeg_command = [
    'ffmpeg',
    '-stream_loop', '-1',  # Loop the input file infinitely
    '-i', 'short_wait.mp3',  # Input file
    '-acodec', 'libmp3lame',  # Audio codec
    '-ar', '44100',  # Audio sample rate
    '-f', 'flv',  # Output format
    'rtmp://192.168.1.112:1937/live'  # Local RTMP server URL with the correct port, 192.168.1.112 172.17.0.1 169.254.243.201 
]

# Start the ffmpeg process
ffmpeg_process = subprocess.Popen(ffmpeg_command)

try:
    ffmpeg_process.wait()  # Wait for the ffmpeg process to complete (it will loop indefinitely)
except KeyboardInterrupt:
    print("Stopping the stream.")
finally:
    ffmpeg_process.terminate()
