from xml.dom import minidom

#open xml file
dom = minidom.parse('D:\\Python\\Selenium2\\info.xml')

#get doc element object
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
