#!/usr/bin/env python3
# =============================================================================
# @file    get.py
# @brief   Download images of notebook
# @author  Michael Hucka <mhucka@caltech.edu>
# @license Please see the file named LICENSE in the project directory
# @website https://github.com/caltechlibrary/htr-test-cases
#
# DO NOT RUN THIS SCRIPT     DO NOT RUN THIS SCRIPT     DO NOT RUN THIS SCRIPT
#
# This script was used to download the files from the archive server.  It is
# here for historical documentation purposes only.  All the files are already
# present in this subdirectory.  You do not need to run this script.
#
# DO NOT RUN THIS SCRIPT     DO NOT RUN THIS SCRIPT     DO NOT RUN THIS SCRIPT
# =============================================================================

import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

dc_template = '''<oai_dc:dc
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
  <dc:title>Page {0} of MIT Notebook II (63 items)</dc:title>
  <dc:description>
    Page {0} of notebook titled "MIT Notebook II". Part of: Donald A Glaser Papers, Series 1: Biographical and Personal; Subseries 2: Journal entries and notes; Box 1, Folder 8.</dc:description>
  <dc:date>1962</dc:date>
  <dc:source>{1}</dc:source>
  <dc:format>pages</dc:format>
  <dc:identifier>{2}</dc:identifier>
  <dc:identifier>{3}</dc:identifier>
  <dc:language>eng</dc:language>
  <dc:rights>
    Materials from the Caltech Archives are made available online for research purposes. Permission for reproduction, distribution, public display, performance, or publication must be obtained in writing from the Head of Archives. The Caltech Archives makes no representation that it is the copyright owner in all of its holdings. It is the responsibility of the user to obtain all necessary rights and clearances for use of materials. For questions, contact Head of Archives.
  </dc:rights>
</oai_dc:dc>
'''

url_base = 'http://glaser.library.caltech.edu/islandora/object/dag%3A{0:03d}/datastream/{1}/view'

# I determined the range by looking at all the pages in the notebook using
# the page viewer on the Archives site, inspecting the HTML, and manually
# writing down the "dag:nnn" number found in the URL.

for i in range(284, 347):
    dc_url = url_base.format(i, 'DC')
    try:
        dc = urllib.request.urlopen(dc_url).read()
        xml = ET.fromstring(dc)
        title = xml.findall('{http://purl.org/dc/elements/1.1/}title')[0].text
    except:
        print('failed to get DC {}'.format(dc_url))

    # The page number unfortunately isn't provided in the DC returned from
    # the Islandora server.  OTOH, the document titles in this particular
    # notebook are things like "DAG_1_1_8_0001", and the last part is the
    # page number, so we can pull it out of the name.

    padded_page_number = re.findall('\d+', title)[-1]
    image_url = url_base.format(i, 'OBJ')
    source = urllib.parse.unquote(image_url)
    page_identifier = title
    dag_identifier = 'dag:{}'.format(i)
    dc_file = 'glaser-mit-notebook-ii-p{}.xml'.format(padded_page_number)
    with open(dc_file, 'w') as f:
        plain_page_number = padded_page_number.lstrip('0')
        f.write(dc_template.format(plain_page_number, source,
                                   page_identifier, dag_identifier))

    image_file = 'glaser-mit-notebook-ii-p{}.tiff'.format(padded_page_number)
    try:
        print('Downloading page {}'.format(plain_page_number))
        urllib.request.urlretrieve(image_url, filename = image_file)
    except:
        print('failed to get image {}'.format(image_url))
