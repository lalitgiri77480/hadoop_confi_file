import xml.etree.ElementTree as ET
f=ET.parse('/etc/hadoop/core-site.xml')
r=f.getroot()
print(r)
x=ET.SubElement(r,'property')
n=ET.SubElement(x,'name')
n.text='fs.default.name'
v=ET.SubElement(x,'value')
v.text='hdfs://0.0.0.0:9001'
f.write('/etc/hadoop/core-site.xml')

 
   