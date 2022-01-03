# MKDocs Publishing Cheat Sheet

Wiperf documentation is created and published using MKDocs. More info at : https://www.mkdocs.org/#mkdocs

The docs are contained in a GitHub repo and are then built in a GitHub project page. The current published site can be found at: https://wlan-pi.github.io/wlanpi-documentation/

The site can be built locally on your machine and pre-viewed using the 'mkdocs serve' command before pushing to GitHub.

Once edits have been completed, they can be built and pushed to the GitHub project page created to host the final pages. See the following doc for more info: https://www.mkdocs.org/user-guide/deploying-your-docs/

Workflow:
```
1. Setup your environment
    a. Install Python 3 on your local machine (https://www.python.org/downloads/)
    b. Upgrade pip: python -m pip install --upgrade pip
    c. Install MKDocs: pip install mkdocs
    d. Install 'Material' theme: pip install mkdocs-material
    e. Install MKDocs revision date plugin: pip install mkdocs-git-revision-date-localized-plugin
    f. Install Git if you don't already have it: https://git-scm.com/downloads
    g. Change in to a directory where you wish to clone the repo
    h. Clone the repo to allow you to work on it locally: https://github.com/WLAN-Pi/wlanpi-documentation.git
2. Creating or editing docs
    a. Change in to the cloned directory and verify project files exist
    b. Edit files as per the MKDocs guide: https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown
    c. Run the local mkdocs server: mkdocs serve  --dev-addr=0.0.0.0:8081
    c. Once editing is complete, build the site : mkdocs build
    d. Commit & push files from local Git instance (git add, git commit -m, git push)
    e. Push the new docs to the GitHub project page using: mkdocs gh-deploy (see https://www.mkdocs.org/user-guide/deploying-your-docs/)
    f. Check updates all look good at : https://wifinigel.github.io/wiperf/ 
```

Here is an excellent guide to using the MKDocs markup: https://github.com/PegaSysEng/doc.pantheon/blob/master/MKDOCS-MARKDOWN-GUIDE.md

The CSS styling file was borrowed from the Pi-Hole project: https://github.com/pi-hole/docs

## Brief Markup Cheatsheet

```
Headings:
---------
# Heading 1
## Heading 2
#### Heading 3

Emphasis:
---------
*italic*
_also italic_

**bold**
__bold__

Lists:
------
    Unordered:
        *Item 1
        *Item 2
            *Item 2a
            *Item 2b
    Ordered:
        1. Item 1
        2. Item 2
            1. Item 2a
            2. Item 2b

Links:
------
http://github.com - automatic!
[GitHub](http://github.com)
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

    Reference-style (also can be used on non-image links): 
    ![alt text][logo]

    [logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

Blockquotes:
------------
> Blah
> Blah

Inline Code:
------------
This is a piece of `<code>`

Code Block:
-----------
\`\`\`javascript
var s = "JavaScript syntax highlighting";
alert(s);
\`\`\`

Tables:
-------
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

Horizontal Rule
---------------
(3 or more of:)
---
or
***
or
___

YouTube Video:
--------------
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
```