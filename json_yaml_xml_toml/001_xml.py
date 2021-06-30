import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET module

for (name, member) in getmembers(ET, isclass):
    if name:
        print(name)
print()

tree = ET.parse('001_xml.xml')
root = tree.getroot()
print(ET.tostring(root))
print()

# Get 'coin' attribute
coin = root.get('coin')
print('Crypto name = {val}'.format(val=coin))

# Set 'launched' attribute
root.set('launched', '20210101')

# Save updated XML
tree.write('001_xml.xml')

# Add 'id' attribute to each investor
id = 1
for investor in tree.findall('investor'):
    investor.set('id', str(id))
    id += 1

# Save updated XML
tree.write('001_xml.xml')

# Delete 'id' attributes
for investor in tree.findall('investor')[:-1]:
    del(investor.attrib['id'])

# Save updated XML
tree.write('001_xml.xml')

# Add investor #1 BAD
# investor1 = ET.fromstring("<investor>Allen Duffy</investor>")
# root.append(investor1)

# Add investor #2
investor2 = ET.Element('investor')
investor2.text = 'Karl Amber'
root.append(investor2)

# Save updated XML
tree.write('001_xml.xml')
