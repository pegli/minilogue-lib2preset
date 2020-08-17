#!/usr/bin/python

import sys
import zipfile, os, shutil
import xml.etree.ElementTree as ET

try:
    fileroot = sys.argv[1]
except:
    fileroot = raw_input("File Name (without extension): ")

libext = '.mnlgxdlib'
presetext = '.mnlgxdpreset'
 
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)
    return
    
if fileroot.endswith(libext):
    fileroot = fileroot[:-len(libext)]

libname = fileroot + libext
print('Converting "{}" to preset file'.format(libname))
presetname = fileroot + presetext
if not os.path.exists('presetarchive'):
    os.mkdir('presetarchive')
libname = fileroot + libext
unzip((libname), 'presetarchive')
os.remove('presetarchive/FavoriteData.fav_data')
shutil.copy('template/FileInformation.xml', 'presetarchive')

tree = ET.parse('template/PresetInformation.xml')
root = tree.getroot()
for i, elem in enumerate(root):
    elem.text = raw_input("{}: ".format(elem.tag))

tree.write('presetarchive/PresetInformation.xml')
shutil.make_archive(fileroot,'zip','presetarchive')
os.rename(fileroot + '.zip', presetname)

print("Cleaning Up...")
shutil.rmtree('presetarchive')

print('Preset file is "{}"'.format(presetname))