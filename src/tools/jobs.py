import requests
import json
# I recommend using the config variables, but if you want to hardcode for testing, that's fine.
from src.config import FRAPPE_URL, API_KEY 
import re

def get_public_jobs(job_title: str = None) -> str:
    """
    Fetches a list of active public job openings from Turiya.
    """
    # You can switch back to the config variables when ready
    endpoint = f"{FRAPPE_URL}/api/method/top.top_one_backend.external_api.api.get_public_jobs"
    
    headers = {
        "X-API-Key": API_KEY,
        "Accept": "application/json"
    }
    
    params = {}
    if job_title:
        params["job_title"] = job_title

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        
        raw_result = response.json()
        
        # --- FIX STARTS HERE ---
        # Frappe wraps the response in a 'message' key. We need to extract it.
        if "message" in raw_result:
            result = raw_result["message"]
        else:
            result = raw_result
        # -----------------------
        
        if not result.get("status"):
            return "Error: The API returned a failure status."
            
        jobs = result.get("data", [])
        
        if not jobs:
            return "No active jobs found matching your criteria."

        # Format output for the LLM
        output = [f"Found {len(jobs)} active job(s):"]
        for job in jobs:
            title = job.get("job_title", "Unknown Role")
            company = job.get("company_name", "Unknown Company")
            job_id = job.get("id", "N/A")
            
            # Clean up Location (it comes as a list ['Mumbai'])
            loc_data = job.get("location", [])
            location = ", ".join(loc_data) if isinstance(loc_data, list) else str(loc_data)
            
            # Handle None values for link
            link = job.get("application_link") or "No Link Available"
            
            output.append(
                f"- **{title}** at {company} (ID: {job_id})\n"
                f"  Location: {location}\n"
                f"  Apply: {link}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Error connecting to Recruitment Service: {str(e)}"
    
def to_url_slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)      # remove non-alnum/space/hyphen [web:3]
    text = re.sub(r"[\s_]+", "-", text)           # spaces/underscores -> hyphen [web:3]
    text = re.sub(r"-+", "-", text)               # collapse multiple hyphens [web:3]
    text = re.sub(r"^-|-$", "", text)             # trim leading/trailing hyphen [web:3]
    return text

def get_job_apply_link(job_id: str, company_name: str) -> str:
    """
    Fetches the application link for a specific job ID.
    """
    company_slug = to_url_slug(company_name)
    return f"app.turiyaskills.co/jobs/{company_slug}/{job_id}"


if __name__ == "__main__":
    print(get_public_jobs())

# import requests
# from src.config import FRAPPE_URL, API_KEY
# import json

# def get_public_jobs(job_title: str = None) -> str:
#     """
#     Fetches a list of active public job openings from Turiya.
    
#     Args:
#         job_title (str, optional): Filter jobs by title (case-insensitive substring).
#     """
#     # endpoint = f"{FRAPPE_URL}/api/method/top.top_one_backend.external_api.api.get_public_jobs"
#     endpoint = "https://dev-app.turiyaskills.co/api/method/top.top_one_backend.external_api.api.get_public_jobs"
#     headers = {
#         # "X-API-Key": API_KEY,
#         "X-API-Key": "top_5992edd9c2da4106a79ade0023eab1cf",
#         "Accept": "application/json"
#     }
    
#     params = {}
#     if job_title:
#         params["job_title"] = job_title


#     try:
#         response = requests.get(endpoint, headers=headers, params=params)
#         print(response.json())
#         response.raise_for_status()
        
#         result = response.json()
        
#         if not result.get("status"):
#             return "Error: The API returned a failure status."
            
#         jobs = result.get("data", [])
        
#         if not jobs:
#             return "No active jobs found matching your criteria."

#         # Format output for the LLM
#         output = [f"Found {len(jobs)} active job(s):"]
#         for job in jobs:
#             title = job.get("job_title", "Unknown Role")
#             company = job.get("company_name", "Unknown Company")
#             job_id = job.get("id", "N/A")
#             location = job.get("location", "Not specified")
#             link = job.get("application_link", "No Link")
            
#             output.append(
#                 f"- **{title}** at {company} (ID: {job_id})\n"
#                 f"  Location: {location}\n"
#                 f"  Apply: {link}"
#             )

#         return "\n\n".join(output)

#     except Exception as e:
#         return f"Error connecting to Recruitment Service: {str(e)}"
    
# if __name__ == "__main__":
#     # Example usage
#     print(get_public_jobs())