# create a video converter


import subprocess
import logging
import logging.config
import logging.handlers


class videoConverter:
  def __init__(self):
    self.logger = logging.getLogger(__name__)
    self.logger.info("videoConverter class initialized successfully")

  def convert(self, input_file, output_file):
    self.logger.info("converting video file")
    try:
      command = "ffmpeg -i " + input_file + " " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToMp4(self, input_file, output_file):
    self.logger.info("converting video file to mp4")
    try:
      command = "ffmpeg -i " + input_file + " -c:v libx264 -c:a aac -strict -2 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToMp3(self, input_file, output_file):
    self.logger.info("converting video file to mp3")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec libmp3lame -ac 2 -ab 192k -ar 44100 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToWav(self, input_file, output_file):
    self.logger.info("converting video file to wav")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec pcm_s16le -ac 1 -ar 16000 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToFlac(self, input_file, output_file):
    self.logger.info("converting video file to flac")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec flac " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToOgg(self, input_file, output_file):
    self.logger.info("converting video file to ogg")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec libvorbis -aq 60 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToWma(self, input_file, output_file):
    self.logger.info("converting video file to wma")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec wmav2 -ac 2 -ab 192k -ar 44100 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToAac(self, input_file, output_file):
    self.logger.info("converting video file to aac")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec aac -ac 2 -ab 192k -ar 44100 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

  def convertToM4a(self, input_file, output_file):
    self.logger.info("converting video file to m4a")
    try:
      command = "ffmpeg -i " + input_file + " -vn -acodec aac -ac 2 -ab 192k -ar 44100 " + output_file
      self.logger.info("command: " + command)
      subprocess.call(command, shell=True)
      self.logger.info("video file converted successfully")
    except Exception as e:
      self.logger.error("error converting video file: " + str(e))
      raise e

    # USE FUNCTIONAL PROGRAMMING TO CONVERT TO MP3
    convert_to_mp3 = lambda input_files, output_files: self.convert(input_files, output_files)

    # USE FUNCTIONAL PROGRAMMING TO CONVERT TO MP4
    convert_to_mp4 = lambda input_file, output_file: self.convert(input_file, output_file)
