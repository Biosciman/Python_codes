import xml.dom.minidom
from xml.dom.minidom import parse
import xml.etree.ElementTree

# minidom解析xml
DOMTree = xml.dom.minidom.parse(r'Human_Chymotrypsin.xml')
doc = DOMTree.documentElement

for i in doc.childNodes[1].childNodes:
    if i.nodeName == 'Seq-entry':
        for j in i.childNodes:
            if j.nodeName == 'Seq-entry_seq':
                for k in j.childNodes:
                    if k.nodeName == 'Bioseq':
                        for a in k.childNodes:
                            if a.nodeName == 'Bioseq_id':
                                continue

                            if a.nodeName == 'Bioseq_descr':
                                continue

                            if a.nodeName == 'Bioseq_inst':
                                for b in a.childNodes:
                                    if b.nodeName == 'Seq-inst':
                                        for c in b.childNodes:
                                            if c.nodeName == 'Seq-inst_repr':
                                                print(c.getAttribute('value'))
                                            if c.nodeName == 'Seq-inst_mol':
                                                print(c.getAttribute('value'))
                                            if c.nodeName == 'Seq-inst_length':
                                                print(c.childNodes[0].data)
                            if a.nodeName == 'Bioseq_annot':
                                continue

# etree解析xml
root = xml.etree.ElementTree.parse(r'Human_Chymotrypsin.xml')
nodes = root.getiterator() # 新版本用 nodes = root.iter() 或者 nodes = list(root.iter())
for node in nodes:
    if node.tag == 'Seq-inst_length':
        print(node.tag, node.text)

ele_findall = root.findall('Bioseq-set_seq-set')
print(type(ele_findall))
print(ele_findall[0].tag)

for i in root.iter('Seq-inst_length'):
    print(i.text)