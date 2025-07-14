
import requests
import yaml
import sys
import os
from dotenv import load_dotenv

# ====== CONFIGURATION ======
load_dotenv()
organization = os.getenv("AZURE_ORG")
project = os.getenv("AZURE_PROJECT")
personal_access_token = os.getenv("AZURE_PAT")

azure_devops_url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems"
headers = {
    "Content-Type": "application/json",
}

def fetch_user_story(story_id):
    url = f"{azure_devops_url}/{story_id}?api-version=7.0"
    response = requests.get(url, auth=("", personal_access_token), headers=headers)
    response.raise_for_status()
    data = response.json()

    fields = data.get("fields", {})
    story = {
        "id": story_id,
        "title": fields.get("System.Title"),
        "description": fields.get("System.Description"),
        "acceptance_criteria": fields.get("Microsoft.VSTS.Common.AcceptanceCriteria"),
        "tags": fields.get("System.Tags", "").split("; "),
        "area": fields.get("System.AreaPath"),
        "story_points": fields.get("Microsoft.VSTS.Scheduling.StoryPoints"),
    }

    os.makedirs("input", exist_ok=True)
    with open("input/user_story.yaml", "w", encoding="utf-8") as f:
        yaml.dump(story, f, allow_unicode=True)

    print(f"✅ User story {story_id} saved to input/user_story.yaml")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_user_story.py <story_id>")
        sys.exit(1)

    story_id = sys.argv[1]
    fetch_user_story(story_id)
