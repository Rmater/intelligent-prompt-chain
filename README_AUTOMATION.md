
# 🚀 Intelligent Prompt Chain with Azure DevOps Integration

This project provides a fully automated, AI-powered development workflow using GitHub Copilot and prompt chaining, with direct integration to fetch user stories from Azure DevOps by ID.

---

## 📁 Project Structure

```
.ai/
├── prompts/                  # All prompt files for each stage
├── scripts/
│   └── fetch_user_story.py   # Script to pull user story from Azure
├── .env.example              # Example env variables for Azure API access
input/
├── user_story.yaml           # Generated automatically from Azure
output/
├── structure.md              # Generated tree structure
├── analysis.md               # Analyzed architecture
├── tasks.md                  # User story breakdown
├── instructions.md           # Dev instructions
├── test_plan.md              # QA test coverage
├── pipeline.yaml             # DevOps integration plan
README.md
```

---

## ⚙️ Setup Instructions

### 1. 🔐 Configure Azure Access

Create a `.env` file at the root of `.ai/` and fill in your Azure DevOps credentials:

```
AZURE_ORG=your-organization-name
AZURE_PROJECT=your-project-name
AZURE_PAT=your-personal-access-token
```

> 💡 Your PAT should have permission to read work items from Azure Boards.

---

### 2. 🧠 Fetch a User Story by ID

From terminal or VSCode Copilot workspace, run:

```bash
cd .ai/scripts
pip install requests python-dotenv pyyaml
python fetch_user_story.py <STORY_ID>
```

This will:
- Connect to Azure DevOps
- Retrieve the work item by ID
- Save it as `input/user_story.yaml`

---

### 3. 🤖 Trigger Prompt Chain

Open each file inside `.ai/prompts/` with Copilot Chat or Copilot CLI, and run:

```bash
# Example
Prompt: "Use input/user_story.yaml and generate breakdown."
```

Repeat through the chain:
- 0_tree → 1_analysis → 2_userstory → 3_instruction → 4_tests → 5_devops

Or automate the whole chain using your preferred script engine or Copilot Workspace macros.

---

## 💡 Pro Tips
- You can also convert this into a GitHub Codespace template for team-wide use.
- Use `meta.yaml` to describe input/output relationships for scripting or AI agent orchestration.

---

## 🔗 Related Tools
- GitHub Copilot Chat / CLI
- Azure DevOps Boards API
- ABP.NET Zero (backend)
- Angular 15+ (frontend)

---

Happy prompting! ⚡
