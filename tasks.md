# ✅ Task Breakdown

## Frontend (Angular)
- Add CR number input field to `edit-profile.component.html`
- Bind field using reactive form control `crNumber`
- Add numeric validation

## Backend (ABP.NET Zero)
- Update `AgentDto` and `UpdateAgentInput` with `CrNumber`
- Modify `AgentAppService.UpdateAsync()` to accept CR updates
- Add validation to ensure it's only editable in Draft

## Database
- Add `CrNumber` column to `Agents` table (if not exists)
- Add audit logging using ABP auditing service