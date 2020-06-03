import subprocess
import sys

def main():
	file_name   = sys.argv[1]
	receiver_ip = sys.argv[2]
	stream_dur  = sys.argv[3]	
	port_num    = sys.argv[4]

	cmd_str = 'cvlc %s --sout "#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100}:duplicate{dst=rtp{dst=%s,port=%s,mux=ts}}" --run-time %s --stop-time %s vlc://quit &' % (file_name, receiver_ip, port_num, stream_dur, stream_dur)

	subprocess.call(cmd_str, shell=True)

if __name__ == '__main__':
	main()
