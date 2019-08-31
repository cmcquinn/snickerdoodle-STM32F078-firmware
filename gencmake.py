#!/usr/bin/env python

import xml.etree.ElementTree as ET

tree = ET.parse('MDK-ARM/platform-controller.uvprojx')
root = tree.getroot()
sections = []
targets= []

for parts in root:
    for section in parts:
        print(section.tag)

        if section.tag == 'Target':
            targets.append(section)

print(targets)