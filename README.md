Convert Logins from 1Password to KeepassX File
==============================================

1Password
---------

* Open 1Password 
* Enter your Password
* Click File > Export 
* Select Tab-Delimited Text
* Select "All Logins"
* Export to logins.txt


Script
------

Start script with:

    python convert.py logins.txt > keepass.xml


KeePassX
--------

* Import keepass.xml


