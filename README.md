# AWWARDS
## author

 SYLVESTER OMONDI

## Project Description
This is a website application where a user can post a project, view other people's projects and also rank projects. A project can be rated based on 3 different criteria
- Design
- Usability
- Content
## how it works
a user can:
- View posted projects and their details.
- Post a project to be rated/reviewed on design,usability and content
- Rate/ review other users' projects
- Search for projects
- View projects overall score
- View my profile page.

##Setup and installations
- Python3.6
- Virtual environment
- Django
- Pip

To run the application do the following:
- clone this repo by running:
` git clone https://github.com/silver230/awwwwards.git`
- set up a virtual environment
 ` python3.6 -m venv  python3.6 -m venv virtual `
 - activate virtual environment
  ` source virtual/bin/activate `
- to install all requirements
` pip install -r "requirements.txt" `
 - touch a file .env and put in the following configurations:
   ```
      - SECRET_KEY=<secret key>
      - DEBUG=False
      - DB_NAME=<database name>
      - DB_USER='<username>
      - DB_PASSWORD=<your password>
      - DB_HOST='127.0.0.1'
      - MODE='dev'
      - ALLOWED_HOSTS=<your site name>
      - DISABLE_COLLECTSTATIC=1
   ```

- run the application locally with
 ` python manage.py runserver `
## likely bugs
Currently the application has no known bugs.
## Testing
- to run tests run ` python manage.py test app `
## technologies used
The technologies used to build the application are:

- Python3.6 
- Django 1.11
- Postgresql
- Bootstrap4
- css
 

 

## LICENCE
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.