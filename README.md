
# 🤖 Intelligent Prompt Chain (Automated AI Workflow)

This repository allows you to automate the transformation of **Azure DevOps user stories** into:
- Project analysis
- Task breakdown
- Developer instructions
- Testing plans
- CI/CD DevOps pipelines

Powered by **GitHub Copilot** or any LLM that supports prompt chaining.

---

## 🔧 How It Works (Fully Automated Chain)

### 1. Fetch a user story from Azure DevOps:

```bash
cd .ai/scripts
python fetch_user_story.py <WORK_ITEM_ID>
```

It will store your story as `input/user_story.yaml`.

---

### 2. Add your project structure tree

Export your folder layout using:

```bash
tree /F > input/project_structure.txt
```

---

### 3. Run the AI Prompts in Sequence

You can use GitHub Copilot Chat or Claude to open each prompt and ask:

> “Use the input and generate the next file in `output/`.”

| Step | Prompt File | Description |
|------|-------------|-------------|
| 0️⃣ | `.ai/prompts/0_tree.prompt.md` | Analyze project structure |
| 1️⃣ | `.ai/prompts/1_analysis.prompt.md` | Extract architecture |
| 2️⃣ | `.ai/prompts/2_userstory.prompt.md` | Break down the user story |
| 3️⃣ | `.ai/prompts/3_instruction.prompt.md` | Write dev instructions |
| 4️⃣ | `.ai/prompts/4_tests.prompt.md` | Generate test cases |
| 5️⃣ | `.ai/prompts/5_devops.prompt.md` | Build CI/CD pipeline |

---

## 📂 File Structure

```
.ai/
├── prompts/        # All AI prompt steps
├── scripts/        # Azure DevOps integration
│   └── fetch_user_story.py
├── meta.yaml       # (Optional) prompt dependency flow
input/
├── project_structure.txt
├── user_story.yaml
output/
├── structure.md → analysis.md → tasks.md → instructions.md → test_plan.md → pipeline.yaml
```

---

## 💡 Tips

- Use Copilot Chat in VSCode or Copilot CLI
- Keep each prompt open and trigger generation using file context
- Use this in any .NET + Angular or Node/React project

---

Made for modern software teams using GitHub Copilot + Azure DevOps
