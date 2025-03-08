import requests as request
import os
import json
from dotenv import load_dotenv
from . import prompts  # Update this import

load_dotenv()

base_ollama_url = os.getenv("OLLAMA_BASE_URL")
ollama_model = os.getenv("OLLAMA_MODEL")
generate_endpoint = '/api/generate'

print("base_ollama_url --------------------------", base_ollama_url)
print("ollama_model --------------------------", ollama_model)

async def base_llm_text_generation_request(prompt, endpoint="api/generate"): 
    response = request.post(f'{base_ollama_url}/{endpoint}', json={"model": ollama_model, "prompt": prompt, "stream": False})
    return response.json()

async def query_llm_to_generate_resume_with_JD(jobdescription, resume): 
    prompt = prompts.ats_score_and_suggestions_prompt.PROMPT_TEMPLATE_WITH_JOB_DESC.format(job_description=jobdescription, resume=resume)
    response = await base_llm_text_generation_request(prompt, generate_endpoint)
    print("query_llm_to_generate_resume_with_JD_response --------------------------", response)
    return json.loads(response["response"])

async def query_llm_to_generate_resume_without_JD(resume): 
    prompt = prompts.ats_score_and_suggestions_prompt.PROMPT_TEMPLATE_NO_JOB_DESC.format(resume=resume)
    response = await base_llm_text_generation_request(prompt, generate_endpoint)
    print("query_llm_to_generate_resume_without_JD_response --------------------------", response)
    return json.loads(response["response"])
