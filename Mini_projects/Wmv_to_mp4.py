# convert wmv to mp4

import os
import sys
import subprocess


def convert_wmv_to_mp4(wmv_file, mp4_file):
  cmd = 'ffmpeg -i ' + wmv_file + ' -vcodec copy -acodec copy ' + mp4_file
  subprocess.call(cmd, shell=True)


def main():
  if len(sys.argv) == 3:
    pass
  else:
    print('Usage: python Wmv_to_mp4.py wmv_file mp4_file')
    sys.exit(1)
  wmv_file = sys.argv[1]
  mp4_file = sys.argv[2]
  while True:
    if os.path.isfile(wmv_file):
      break
    else:
      print('File not found: ' + wmv_file)
      sys.exit(1)

  convert_wmv_to_mp4(wmv_file, mp4_file)


if __name__ == '__main__':
  main()
