# 📋 Developer Instructions

## Angular
- Open `edit-profile.component.ts`
- Add form control `crNumber` in `FormBuilder`
- Validate using `Validators.pattern(/^[0-9]+$/)`

## ABP Backend
- In `AgentDto`, add `string CrNumber { get; set; }`
- In `AgentAppService`, inside `UpdateAsync()`, allow CR change if `Status == Draft`
- Use `Logger.Info(...)` to track CR number updates