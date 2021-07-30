# FastAPI Study
## First step (step 0)
I followed all the code in here for creating my first FastAPI backend service:
https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app

## Step 1
Clone the code
## Step 2
Run all the commands:

Create a new virtual environment inside the newly created directory using virtualenv. If you haven't already installed virtualenv
```bash
pip install virtualenv
```
Now, create a new virtual environment.
```bash
virtualenv env
```
Windows users can run this command to activate env
```bash
.\env\Scripts\activate
```
 You are ready to install FastAPI, run the following command
```bash
pip install fastapi
```
Since FastAPI doesn't come with inbuilt service, you need to install uvicorn for it to run.
Install uvicorn using the command
```bash
pip install uvicorn
```
