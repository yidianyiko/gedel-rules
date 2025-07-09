# Quick Start Guide

## 5-Minute Setup

### Step 1: Verify System Installation
The project isolation knowledge management system is already installed. Verify by checking:

```bash
ls -la .cursor/projects/
```

You should see:
- `project_registry.json`
- `system_config.json`
- `classification_rules.json`
- `templates/` directory
- `README.md`

### Step 2: Discover Projects
Scan your workspace for projects:

```bash
python .cursor/tool/customs/project_detector.py --scan
```

This will:
- Detect all projects in your workspace
- Register them in the project registry
- Create project-specific knowledge files

### Step 3: View Registered Projects
List all detected projects:

```bash
python .cursor/tool/customs/project_detector.py --list
```

### Step 4: Set Active Project
Set your current working project:

```bash
python .cursor/tool/customs/project_detector.py --set-active your_project_name
```

### Step 5: Start Using the System
You're ready to use the system! Knowledge will be automatically classified as:
- **Global**: General principles, tools, methodologies
- **Project-specific**: Project experiences, configurations, issues

## Common Workflows

### Adding Project Knowledge
When working on a project, knowledge is automatically classified:

1. **Project-specific lessons** go to `{project}/lessons.md`
2. **Project-specific tasks** go to `{project}/todo.md`
3. **Project configuration** goes to `{project}/config.md`

### Adding Global Knowledge
General knowledge automatically goes to global files:
- `.cursor/memory/lessons.md` for global lessons
- `.cursor/think/todo.md` for global tasks
- `.cursor/tool/tools.md` for global tools

### Searching Knowledge
- **Global search**: Searches all knowledge (global + all projects)
- **Project search**: Searches current project + relevant global knowledge
- **Context-aware**: Results are filtered based on current project context

## Key Commands

```bash
# Project management
python .cursor/tool/customs/project_detector.py --scan      # Discover projects
python .cursor/tool/customs/project_detector.py --list      # List projects
python .cursor/tool/customs/project_detector.py --set-active project_name
```

## File Structure

After setup, your project knowledge will be organized like this:

```
.cursor/projects/
├── project_registry.json          # All registered projects
├── system_config.json             # System configuration
├── classification_rules.json      # Classification rules
├── templates/                     # Project file templates
│   ├── lessons.md
│   ├── todo.md
│   ├── config.md
│   └── knowledge_index.json
└── your_project_name/             # Your project knowledge
    ├── lessons.md                 # Project-specific lessons
    ├── todo.md                    # Project-specific tasks
    ├── config.md                  # Project configuration
    └── knowledge_index.json       # Project knowledge graph
```

## Knowledge Classification Examples

### Global Knowledge (Stays in Global Files)
- "Use Git for version control across all projects"
- "Cursor IDE shortcuts and productivity tips"
- "Docker best practices for containerization"
- "Agile development methodology principles"
- "General debugging techniques"

### Project-Specific Knowledge (Goes to Project Files)
- "This React project uses Material-UI v5 with custom theming"
- "API endpoint /api/users returns 500 error in production"
- "Project requires Node.js 18+ and npm 9+"
- "Database migration failed due to foreign key constraint"
- "Custom authentication middleware for this Express app" 