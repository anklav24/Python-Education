import os

for key, values in os.environ.items():
    print(f"{key}: {values}")
print()

print()
print(os.environ['USERNAME'])
print(os.environ['USERDOMAIN'])
print(os.environ.get('I_DONT_EXIST'))
print()

print(os.environ.get('SYSTEMROOT'))
print(os.environ.get('systemMROOT'))
print()

print(os.environ.get('DOWNLOADS'))
print(os.environ.get('I_DONT_EXIST', 'I_AM_DEFAULT'))
print(os.getenv('I_DONT_EXIST', 'I_AM_DEFAULT'))
print()

# Add our env

os.environ['API_KEY'] = 'asdfjklquweiuoijkasdfl'
print(os.environ.get('API_KEY'))
print()

print(os.environ.get('YOUR_API_KEY'))
