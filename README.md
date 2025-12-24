# Instacheck
Instacheck is a tool that allows you to extract basic information from instagrams accounts</br>

## 🛠️ Installation

### With Github

```bash
git clone https://github.com/hypo112111/instacheck.git
cd instacheck/
python3 setup.py install
```

## 📚 Usage:

### Find information from a username

```
instacheck -u username -s instagramsessionid
```

### Find information from an Instagram ID

```
instacheck -i instagramID -s instagramsessionid
```

## 📈 Example

```
Informations about     : username
Full Name              : usernames | userID : 123456789
Verified               : False | Is buisness Account : False
Is private Account     : False
Follower               : xxx | Following : xxx
Number of posts        : x
Number of tag in posts : x
External url           : http://example.com
IGTV posts             : x
Biography              : example biography
Public Email           : public@example.com
Public Phone           : +00 0 00 00 00 00
Obfuscated email       : me********s@examplemail.com
Obfuscated phone       : +00 0xx xxx xx 00
------------------------
Profile Picture        : https://scontent-X-X.cdninstagram.com/
```
