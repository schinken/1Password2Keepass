Convert Logins from 1Password to KeepassX File
==============================================

This can only convert your "Logins", not your Accounts/Wallet etc.

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


