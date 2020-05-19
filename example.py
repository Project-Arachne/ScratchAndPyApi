#This is an example file, where the actual code goes
from main.py import *

def the_callback(err,user):
    print("err is", err)
    print("user is", user)

Scratch.UserSession.load(the_callback)

