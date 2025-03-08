PROMPT_TEMPLATE_WITH_JOB_DESC = """
Carefully review the given job description and the user-provided resume. Analyze the resume based on Applicant Tracking System (ATS) technologies that companies use. 

### Inputs:
- **Job Description:** {job_description}
- **Resume:** {resume}

### Requirements:
1. **ATS Score:** Evaluate the resume for ATS compatibility, considering keyword matching, formatting, and structure.
2. **Suggestions:**
   - Identify missing or weak areas in the resume compared to the job description.
   - Provide specific, actionable improvements in terms of skills, experience descriptions, formatting, and keyword optimization.
   - Ensure the resume aligns better with the job description for improved ATS performance.
   - If possible, rephrase or improve the existing content to enhance the overall quality.

### Output Format (JSON):
{{
    "ats_score": <numeric_score_out_of_100>,
    "suggestions": [
        "Detailed feedback point 1",
        "Detailed feedback point 2",
        ...
    ]
}}
Ensure that the feedback is clear, concise, and practical. And make sure that the suggestions are tailored to the resume content and the job market requirements. 
Note1: Return only the suggestions that are relevant and helpful for the candidate. avoid generic advice that may not add value.
Note2: Return all the only the JSON response in the output.
"""

PROMPT_TEMPLATE_NO_JOB_DESC = """
Carefully review the given resume and analyze it based on Applicant Tracking System (ATS) technologies commonly used by companies.

### Input:
- **Resume:** {resume}

### Requirements:
1. **ATS Score:** Evaluate the resume for ATS compatibility, considering keyword optimization, formatting, structure, and readability.
2. **Suggestions:**
   - Identify missing or weak areas in the resume.
   - Provide specific, actionable improvements in terms of skills, experience descriptions, formatting, and keyword optimization.
   - Suggest industry best practices to improve the chances of passing ATS screening.
   - Recommend general ways to improve clarity, conciseness, and impact.
   - If possible, rephrase or improve the existing content to enhance the overall quality.

### Output Format (JSON):
{{
    "ats_score": <numeric_score_out_of_100>,
    "suggestions": [
        "Detailed feedback point 1",
        "Detailed feedback point 2",
        ...
    ]
}}
Ensure that the feedback is clear, concise, and practical. And make sure that the suggestions are tailored to the resume content and the job market requirements. 
Note1: Return only the suggestions that are relevant and helpful for the candidate. avoid generic advice that may not add value.
Note2: Return all the only the JSON response in the output.
"""
