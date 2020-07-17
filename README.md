# IBS-smartCity
# Project Description

This is project on implmenting ID-based security framework for smart cities. 
Architecture file can be found in root directory highlevel_idc_smartcity.pdf
This project uses flask framework - a micro webframework(python) for the backend, it also uses MongoDB as DB.
Used HTML5 for webpages, no other specific frontend libraries/frameworks have used. Only static web pages are present.
## Installation
Rerequired packages and Libraries:
- Recommended IDE : Pycharm - enables virtual environment (venv)
- Python version - 3.x
- pycocks
- flask
- pymongo
- gmpy2
## usage

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required package or else use pycharm itself for the venv.

```bash
pip install <package_name>
```
## Pre-requisites
- Install mongoDB and MondoDBCompass.
- Create DB named PmaMapper.
- Create 2 collections Pkg_List, user_register.
- The MondoDB service should be up and running.
- Use the tool Post man canary, to test API.

## Steps running the code

1. Open the project in an IDE(VsCode/ Pycharm) 
2. Install the necessary packages.
3. Open registation-server.py under Pseudonym-Management-Authority directory.
4. Run the program.
5. Hit the url: http://localhost:5000/register , if the html registration page showed up , the server is up and running successfully.

- user registration: http://localhost:5000/register
- pesudonym generation request:  http://localhost:5000/requestPseudonym - hit with Post Man.
Hit the requestPeudonym url with available registration token as the body using POST method in Postman tool given below:
```json
{
    "regToken" : "52e27990-339a-4773-a56e-17ss329bbbd3b6"
}
````

5. Check the DB for data insertion.
