#!/usr/bin/env python
# coding: utf-8

import time
import json
import codecs
import subprocess

error1 = "The above user ID is not found {}."
error2 = "The upline code is found here {}."
verified_str = "{} {}"
#exclude_list = [‘192.168.1.56‘,‘192.168.1.200‘,‘192.168.1.100‘,‘192.168.1.300‘,‘127.0.0.1‘]
exclusion_list = ['18666575750', '13141191091', '15456457984']
def main():
    global member_data, verified_data
    member_data = json.load(codecs.open('member.json','r','utf-8-sig'))
    verified_data = json.load(codecs.open('verified.json','r','utf-8-sig'))
    username = input("🛑 Enter username phone number:")
    findById(username)

def findById(number):
    global target_user
    for user in member_data:
        if number == user['username']:
            target_user = user
            break
    try:
       userUp = target_user
    except NameError:
       print(error1.format(number))
       return
    else:
     uplineCode = target_user['invitecode']
     userUp = target_user
     messagecp = ''
     while userUp != None:
       userUp = findUserByInviteCode(uplineCode)
       if userUp != None:
          nameNum = userUp['username']
          uplineCode = userUp['invitecode']
          if nameNum in exclusion_list:
            continue
          else:
           data_verified = getNameByUid(userUp['id'])
           line = verified_str.format(nameNum,data_verified)
           messagecp=messagecp + line + '\n'
           print(line)

     subprocess.run("pbcopy", universal_newlines=True, input=messagecp)
     print('====== all data is copied to the clipboard =======')

def findUserByInviteCode(invitecode):
    #print(error2.format(invitecode))
    for lus in member_data:
       if str(lus['id']) == str(invitecode):
            return lus
    return None
       
def getNameByUid(uid_check):
  for r in verified_data['rows']:
       if str(r['uid']) == str(uid_check):
            return verified_str.format(r['name'], r['idcardnum'])
  return "n/a"


main()

