import xml.etree.ElementTree as ET
f=ET.parse('/etc/hadoop/hdfs-site.xml')
r=f.getroot()
print(r)
x=ET.SubElement(r,'property')
n=ET.SubElement(x,'name')
n.text='dfs.name.dir'
v=ET.SubElement(x,'value')
v.text='/nn'
f.write('/etc/hadoop/hdfs-site.xml')

 
   