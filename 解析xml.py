import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree = xml.dom.minidom.parse('Human_Chymotrypsin.xml')

doc = DOMTree.documentElement

for i in doc.childNodes[1].childNodes:
    if i.nodeName == 'Seq-entry':
        for j in i.childNodes:
            if j.nodeName == 'Seq-entry_seq':
                for k in j.childNodes:
                    if k.nodeName == 'Bioseq':
                        for a in k.childNodes:
                            if a.nodeName == 'Bioseq_id':
                                print(a.v)
