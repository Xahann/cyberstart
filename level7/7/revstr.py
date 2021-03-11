import requests
link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!
revString = requests.get(link).text[::-1]
#revString = "DHRUIHEKCA"# [::-1]
print(revString)
answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = requests.get(answer).text
print(response)
