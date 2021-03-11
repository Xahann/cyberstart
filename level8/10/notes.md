Missing 4 bytes when try to unzip 


using xxd we can see it is missing the 4 byte zip file header

https://www.wikiwand.com/en/List_of_file_signatures

https://fireshellsecurity.team/isitdtu-drill/

printf "\x50\x4B\x03\x04" | cat - FILE > FILE.zip

unzipping and running ./masterkey gives us the flag
