#!/usr/bin/env python3

import requests
import socket

def check_localhost():
   localhost = socket.gethostbyname('localhost')
   if localhost == "127.0.0.1":
      return True
   else:
      return False

def check_connectivity():
   request = requests.get("http://www.google.com")
   status_code = request.status_code
   if status_code == 200:
      print ("SUCCESS")
      return True
   else:
      print ("ERROR")
      return False
