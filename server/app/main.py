from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import fitz
import re

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    experience: int
    skills: list
    education: list
    projects: list

app  = FastAPI()

# parse resume function
def parse_resume(file):
    pdf_document = fitz.open(stream=file, filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Extract name
    name_match = re.search(r"Name:\s*(.*)", text)
    name = name_match.group(1) if name_match else "John Doe"

    # Extract email
    email_match = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", text)
    email = email_match.group(1) if email_match else ""

    # Extract phone number
    phone_match = re.search(r"Phone:\s*(\d{10})", text)
    phone = phone_match.group(1) if phone_match else "1234567890"

    # Extract experience
    experience_match = re.search(r"Experience\s*(\d+)", text)
    experience = int(experience_match.group(1)) if experience_match else 5

    # Extract skills
    skills_match = re.search(r"Skills\s*(.*)", text)
    skills = skills_match.group(1).split(", ") if skills_match else ["Python", "Java", "C++"]

    # Extract education
    education_match = re.search(r"Education\s*(.*)", text)
    education = education_match.group(1).split(", ") if education_match else ["B.Tech", "M.Tech"]

    # Extract projects
    projects_match = re.search(r"Projects\s*(.*)", text)
    projects = projects_match.group(1).split(", ") if projects_match else ["Project 1", "Project 2"]

    resume = Resume(
        name=name,
        email=email,
        phone=phone,
        experience=experience,
        skills=skills,
        education=education,
        projects=projects
    )
    
    return [resume, text]

@app.get("/")
async def root():
    return {"message": "This is the root of the Resume optimizer API"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_name = file.filename
    content_type = file.content_type
    file_extension = file.filename.split(".")[-1]

    # create file as a object without saving it

    file_object = file.file.read()
    print(file_object)
    #  parse file contents and extract information from it and store it in resume object
    [resume, text] = parse_resume(file_object)
    print(resume, text)
    

    return {"message": "Resume uploaded successfully", 
            "file name": file_name, 
            "file type": content_type,
            "file_extension": file_extension,
            "resume": resume.dict(),
            }