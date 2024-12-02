# AI Learning Assistant Project

An interactive learning platform leveraging Claude's computer use capabilities for personalized computer skills education.

## Project Overview

This project addresses the challenge of computer skills education by combining Claude in Compute's capabilities with a structured Streamlit interface. Users can receive interactive, real-time demonstrations of computer skills across multiple applications.

### Supported Applications
- LibreOffice Calc (Spreadsheets)
- Terminal Commands
- Firefox Browser
- PDF Viewer
- Text Editor
- Image Editor
- Calculator

## Setup

1. Set your API key:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

2. Make scripts executable:
```bash
chmod +x scripts/start-claude.sh
chmod +x scripts/start-app.sh
```

## Running the Services

1. Start Claude in Compute:
- Open a terminal
- Run: `./scripts/start-claude.sh`
- Access at: http://localhost:8080

2. Start Streamlit App:
- Open another terminal
- Run: `./scripts/start-app.sh`
- Access at: http://10.0.0.119:8502 (or your network URL)

## Project Structure
```
AI_TUTOR/
├── app/
│   ├── app.py              # Streamlit application
│   └── requirements.txt    # Python dependencies
├── scripts/
│   ├── start-claude.sh     # Claude startup script
│   └── start-app.sh        # Streamlit startup script
├── docs/
│   ├── model_card.md       # Model capabilities documentation
│   ├── analysis.md         # Project analysis and findings
│   └── resources.md        # Additional resources and links
└── README.md
```

## Documentation

Detailed documentation is available in the `docs` folder:
- [Model Card](docs/model_card.md) - Details about Claude's capabilities
- [Analysis](docs/analysis.md) - Project analysis and findings
- [Resources](docs/resources.md) - Additional resources and references

## Development

- Streamlit app code is in `app/app.py`
- The app will auto-reload when you make changes
- Claude in Compute must be restarted manually if needed

## Limitations and Considerations
- Context window has limitations
- Limited to installed applications

## Future Development
- Analytics integration
- Progress tracking
- Additional applications support
- Enhanced feedback mechanisms
