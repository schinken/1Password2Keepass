__author__ = 'Schinken'

import csv
import datetime

map1Pass = ['title','notes','username', 'password', 'url']

keepassEntry = '<entry>\n\
   <title>%s</title>\n\
   <username>%s</username>\n\
   <password>%s</password>\n\
   <url>%s</url>\n\
   <comment></comment>\n\
   <icon>1</icon>\n\
   <creation>%s</creation>\n\
   <lastaccess>%s</lastaccess>\n\
   <lastmod>%s</lastmod>\n\
   <expire>Never</expire>\n\
</entry>\n'

def read1PasswordFile( filename ):

    handle = open( filename, 'r' )
    parsed = csv.reader( handle, delimiter = '\t' )

    parsed.next()

    data = []
    for row in parsed:
        data.append( { map1Pass[x] : y for x,y in enumerate( row ) } )

    return data

def renderKeepassEntry( data, dtiso ):

    return keepassEntry % ( data['title'], data['username'], data['password'],
                            data['url'], dtiso, dtiso, dtiso )

def writeKeepassFile( strdata, template = 'keepass_template.xml' ):

    tpl = open( template, 'r' )
    print tpl.read() % ( strdata )

def main():

    entries = read1PasswordFile('logins.txt')
    dt      = datetime.datetime.now().replace( microsecond = 0 )
    dtiso   = dt.isoformat()

    result  = ''
    for row in entries:
        result += renderKeepassEntry( row, dtiso )

    writeKeepassFile( result )

if __name__ == '__main__':
    main()
