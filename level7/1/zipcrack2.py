import zipfile
import itertools
import time
import string
# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception, e:
        pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'data.zip'
# The first part of the password.
first_half_password = 'Cola'
# We don't know what characters they add afterwards...
# This is case sensitive!
alphabet = 'abcdefghijklmnopqrstuvwxyz' + string.ascii_uppercase + '0123456789'
zip_file = zipfile.ZipFile(zipfilename)

# We know they always have 3 characters after the first half of the password
# For every possible combination of 3 letters from alphabet...
for c in itertools.product(alphabet, repeat=3):
    # Slowing it down on purpose to improve performance in web terminal.
    # Remove this line at your peril
    # Add the three letters to the first half of the password.
    password = first_half_password+''.join(c)
    # Try to extract the file.
    # print "Trying: %s" % password
    # If the file was extracted, you found the right password.
    if extractFile(zip_file, password):
        print '*' * 20
        print 'Password found: %s' % password
        print 'Files extracted...'
        exit(0)

# If no password was found by the end, let us know!
print 'Password not found.'
