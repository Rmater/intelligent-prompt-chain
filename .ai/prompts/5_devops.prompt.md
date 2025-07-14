# Step 5: Generate DevOps Integration Plan

## 👤 Role: DevOps Engineer

## 🎯 Purpose
Create a CI/CD pipeline to automate build, test, and deployment using DevOps best practices.

## 🧠 Prompt
You are a DevOps engineer building pipelines for a full-stack project.

Based on `output/test_plan.md`, generate a GitHub Actions or Azure DevOps YAML pipeline:
- Install dependencies
- Build frontend and backend
- Run tests
- Deploy if successful (to dev/test environment)

Ensure:
- Secrets and configs are handled securely
- Failures halt the pipeline

💡 Input: `output/test_plan.md`  
📝 Output: `output/pipeline.yaml`
