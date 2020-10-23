# API Token Creator
Creates API token checks in your APIs.
## Tutorial
### Step 1.
Type this into your command prompt or terminal.
```
python -c "import random;print('Your code :',(random.randrange(65,91)+random.randrange(65,91)+random.randrange(65,91)))"
```
#### WARNING: DO NOT SHARE THIS CODE WITH ANYONE! THEY CAN CREATE THEIR OWN KEYS FOR YOUR API.

### Step 2.
Make sure you still have that code. Type this into your command prompt/terminal:

For one key:
```
python gen.py <code>
```

For multiple keys:

```
python keygen.py <code> <token-number>
```

e.g
```
python keygen.py 123 21
```

### Step 3 - API token checking
Make your API look like this:
```
api=None
API_TOKEN = ""

def apiCheck(tkn, code):
    sum=0
    for i in tkn:
        sum+=ord(i)
    if sum==code:return True
    else:return False

def define():
    #Define your functions here
    return {"function" : func}

if not apiCheck(API_TOKEN, <code>):
    print("API Token incorrect - locking out...")
    def define():
        print("Locked out")
else:
    api=define()
```
