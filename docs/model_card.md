# Model Card: AI-Guided Learning Assistant

## Model Overview

**Model Name:** Claude 3 (Anthropic)  
**Interface:** Claude in Compute  
**Primary Use Case:** Interactive Computer Skills Education  

This model card documents the capabilities, limitations, and best practices for using Claude in our AI-Guided Learning Assistant project.

## Capabilities

### Application Support
- **LibreOffice Calc:** Spreadsheet operations, formulas, formatting
- **Terminal:** Command-line operations, file management
- **Firefox:** Web navigation, bookmarks, settings
- **PDF Viewer:** Document navigation, annotations
- **Text Editor:** File editing, text manipulation
- **Image Editor:** Basic image operations
- **Calculator:** Mathematical operations

### Teaching Features
1. **Interactive Demonstrations**
   - Real-time skill demonstrations
   - Step-by-step guidance
   - Visual feedback

2. **Adaptive Teaching**
   - Responds to questions
   - Provides clarifications
   - Adjusts to user level

3. **Multi-modal Interaction**
   - Text instructions
   - Visual demonstrations
   - Interactive feedback

## Limitations

### Technical Constraints
- **Session Duration:** Limited by compute environment
- **Context Window:** Conversation history limitations
- **Application Access:** Limited to installed software
- **Response Time:** May vary with complexity

### Teaching Limitations
- Cannot retain user progress between sessions
- Requires specific prompt formatting

## Best Practices

### For Optimal Results
1. **Clear Instructions**
   - Use specific, focused prompts
   - Break complex tasks into steps
   - Request demonstrations explicitly

2. **Session Management**
   - Plan sessions within token and time limits
   - Restart for fresh context

3. **Learning Approach**
   - Start with basics
   - Build complexity gradually
   - Request clarification when needed
   - Practice demonstrated skills

## Usage Guidelines

### Recommended Prompts
```
Format: "Show me how to [specific task] in [application]"
Example: "Show me how to create a SUM formula in LibreOffice Calc"
```

### Session Structure
1. Choose specific learning objective
2. Request demonstration
3. Ask clarifying questions
4. Practice with guidance
5. Confirm understanding

## Performance Notes

- Best suited for beginner to intermediate tasks
- Most effective with clear, specific requests
- Excels at step-by-step demonstrations
- Strong at explaining concepts during demonstration