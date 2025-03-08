from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import fitz
import re
from .llm import query_llm_to_generate_resume_without_JD, query_llm_to_generate_resume_with_JD 

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
    
    return text

@app.get("/")
async def root():
    return {"message": "This is the root of the Resume optimizer API"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...), job_description: str = None):
    file_name = file.filename
    content_type = file.content_type
    file_extension = file.filename.split(".")[-1]

    # create file as a object without saving it
    file_object = file.file.read()
    # print(file_object)
    #  parse file contents and extract information from it and store it in resume object
    resume_text = parse_resume(file_object)
    print(resume_text)

    # call ollama service
    if job_description:
        ollama_response = await query_llm_to_generate_resume_with_JD(job_description, resume_text)
    else:   
        ollama_response = await query_llm_to_generate_resume_without_JD(resume_text)
    print(ollama_response)

    return {"message": "Resume uploaded successfully", 
            "file name": file_name, 
            "file type": content_type,
            "file_extension": file_extension,
            "ollama_response": ollama_response
            }