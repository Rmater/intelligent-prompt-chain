# 🧪 Test Plan

## Unit Tests
- Validate `AgentAppService.UpdateAsync()` allows CR change in Draft only
- Reject CR updates in Submitted or Approved statuses

## Frontend Tests
- CR field accepts only numbers
- Error shown for invalid input
- Form submission includes CR
