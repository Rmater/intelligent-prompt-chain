# Step 2: Breakdown User Story into Technical Tasks

## 👤 Role: Agile Software Engineer

## 🎯 Purpose
Convert a business user story into technical tasks mapped to relevant components.

## 🧠 Prompt
You are a senior software engineer in an Agile team.

Based on the user story from `input/user_story.yaml` and architecture from `output/analysis.md`:
- Extract core features, requirements, and constraints.
- Decompose the story into tasks grouped by:
  - Frontend (Angular)
  - Backend (.NET 8, ABP AppService, DTOs)
  - Database (EF Core or SQL changes)
  - Testing
- Include edge cases, security rules, and validations.

💡 Inputs:  
- `input/user_story.yaml`  
- `output/analysis.md`  

📝 Output: `output/tasks.md`
