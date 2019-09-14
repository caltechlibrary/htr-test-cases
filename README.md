Test cases for HTR experiments
==============================

This repository contains test images for the Library's studies on handwritten text recognition.

Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#authors-and-acknowledgments)


Introduction
------------

The Caltech Library is working on applications of OCR and HTR (handwritten text recognition) to documents stored in the [Caltech Archives](https://archives.caltech.edu).  The development of software such as [Handprint](https://github.com/caltechlibrary/handprint) requires test cases in the form of images of documents.  This repository holds a collection of such images for the Library's work.

The images are stored in subdirectories that give some indication of their origins and natures; for example, the [caltech](caltech) subdirectory contains images from the Caltech Archives.  The sources of individual images are described in associated XML files containing [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dces/) metadata in [OAI 2.0 DC](http://www.openarchives.org/OAI/openarchivesprotocol.html) format (based on the specification document dated 2015-01-08).  There is a separate `.xml` file for each image file.  An [XML schema is available elsewhere](http://www.openarchives.org/OAI/2.0/oai_dc.xsd) for the format used to store the Dublin Core metadata.


Installation
------------

There is no software in this repository; it contains only image files. You can download the entire set using various methods.  One method is to use GitHub's "Download ZIP" link,

<p align="center">
https://github.com/caltechlibrary/htr-test-cases/archive/master.zip
</p>

in combination with your preferred file download software tool (which could be your browser, or [curl](https://curl.haxx.se), or [wget](https://en.wikipedia.org/wiki/Wget), or similar software). A second method is to use `git` to clone the repository to your local computer:
```sh
git clone https://github.com/caltechlibrary/htr-test-cases.git
```
 

Usage
-----

This is a collection of image files.  You can use them in whatever way you would use other image files.


Known issues and limitations
----------------------------

None at this time.


Getting help
------------

If you find an issue, please submit it in [the GitHub issue tracker](https://github.com/caltechlibrary/htr-test-cases/issues) for this repository.


Contributing
------------

We would be happy to receive your help and participation with enhancing this collection of test images.  Please visit the [guidelines for contributing](CONTRIBUTING.md) for some tips on getting started.


License
-------

Please see the individual image files and subdirectories for applicable copyright and license information.


Authors and history
---------------------------

Mike Hucka started this collection in 2019, with the help of others at the Caltech Library's DLD group, including [Tommy Keswick](https://github.com/t4k) and [Peter Collopy](https://github.com/collopy).


Acknowledgments
---------------

This work was funded by the California Institute of Technology Library.

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src=".graphics/caltech-round.svg">
  </a>
</div>
