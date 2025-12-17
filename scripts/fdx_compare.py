import xml.etree.ElementTree as ET

def extract_elements(fdx_path):
    tree = ET.parse(fdx_path)
    root = tree.getroot()
    scenes = []
    characters = []
    for para in root.iter('Paragraph'):
        ptype = para.attrib.get('Type', '')
        text = ''.join(para.itertext()).strip()
        if ptype == 'Scene Heading':
            scenes.append(text)
        elif ptype == 'Character':
            characters.append(text)
    return scenes, characters

fdx1 = 'fdx_samples/test_scriptparser_ok.fdx'
fdx2 = 'fdx_samples/rovo_failed.fdx'

scenes1, chars1 = extract_elements(fdx1)
scenes2, chars2 = extract_elements(fdx2)

print("=== Scene Headings (Script Parser) ===")
for s in scenes1:
    print(s)
print("\n=== Scene Headings (Rovo) ===")
for s in scenes2:
    print(s)

print("\n=== Characters (Script Parser) ===")
for c in set(chars1):
    print(c)
print("\n=== Characters (Rovo) ===")
for c in set(chars2):
    print(c)
