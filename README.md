# tdd-web-app
Test driven development Python web application 
## Setup

run the following command:
```
pip install -e .
```

this will install this directory as a library, (-e means that this is editable)


to give access to webdrivers:
```shell
xattr -r -d com.apple.quarantine /path/to/geckodriver
ln -s /path/to/geckodriver /usr/local/bin/geckodriver
```