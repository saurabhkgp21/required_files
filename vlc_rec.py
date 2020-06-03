import subprocess
import sys

def main():
	output_file_name = sys.argv[1]
	stream_dur       = sys.argv[2]
	port_num         = sys.argv[3]
	
	cmd_str = 'cvlc rtp://@:%s --sout=file/ts:%s --run-time %s --stop-time %s vlc://quit &' % (port_num, output_file_name, stream_dur, stream_dur)

	subprocess.call(cmd_str, shell=True)

if __name__ == '__main__':
	main()

