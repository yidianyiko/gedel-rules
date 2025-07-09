# Project Isolation Knowledge Management System

## Overview

The Project Isolation Knowledge Management System is designed to automatically separate global knowledge from project-specific knowledge, ensuring that:

- **Global knowledge** remains accessible across all projects
- **Project-specific knowledge** is isolated within individual project contexts
- **Knowledge relationships** are maintained across boundaries
- **Automatic classification** reduces manual effort
- **Search and retrieval** work seamlessly across all knowledge

## System Architecture

```
.cursor/
├── memory/                    # Global knowledge storage
│   ├── lessons.md            # Global lessons and experiences
│   └── validation_log.md     # Global validation logs
├── think/
│   └── todo.md               # Global tasks and planning
├── tool/
│   ├── tools.md              # Global tools and utilities
│   └── customs/              # Custom tools
├── rules/
│   └── meta-rules.mdc        # System rules and configuration
└── projects/                 # Project-specific knowledge
    ├── project_registry.json # Project registration
    ├── system_config.json    # System configuration
    ├── classification_rules.json # Classification rules
    ├── templates/            # Project file templates
    └── {project_name}/       # Individual project knowledge
        ├── lessons.md        # Project-specific lessons
        ├── todo.md           # Project-specific tasks
        ├── config.md         # Project configuration
```

## Key Features

### 1. Automatic Project Detection
- Scans workspace for projects based on file patterns
- Supports Node.js, Python, Java, React, Vue, FastAPI, Django
- Automatically registers new projects
- Extracts project metadata and dependencies

### 2. Intelligent Knowledge Classification
- Automatically classifies knowledge as global or project-specific
- Uses keyword analysis and context detection
- Provides confidence scores for classifications
- Allows manual override when needed

### 3. Project Isolation
- Each project has its own knowledge files
- Project-specific lessons, tasks, and configurations
- Cross-project references maintained

### 4. Unified Search
- Search across global and project-specific knowledge
- Context-aware filtering based on current project
- Semantic search capabilities
- Fuzzy matching for better results

## Usage Guide

### Getting Started

1. **System Setup**
   ```bash
   # The system is automatically set up when you first use it
   # No manual configuration required
   ```

2. **Project Detection**
   ```bash
   # Automatically detect and register projects
   python .cursor/tool/customs/project_detector.py --scan
   ```

3. **View Registered Projects**
   ```bash
   # List all registered projects
   python .cursor/tool/customs/project_detector.py --list
   ```

4. **Set Active Project**
   ```bash
   # Set the current active project
   python .cursor/tool/customs/project_detector.py --set-active project_name
   ```

### Knowledge Management

#### Adding Knowledge

Knowledge is automatically classified when added:

- **Global Knowledge**: General principles, tools, methodologies
- **Project Knowledge**: Project-specific experiences, configurations, issues

#### Knowledge Classification Rules

**Global Knowledge Examples:**
- Programming principles and best practices
- Tool usage patterns (Cursor, Git, Docker)
- Development methodologies (Agile, Scrum)
- System-level configurations
- Cross-project patterns and templates

**Project-Specific Knowledge Examples:**
- Project architecture decisions
- Project-specific bug fixes and workarounds
- Project configuration details
- Project domain-specific lessons
- Project-specific dependencies and versions

#### Knowledge Quality Standards

Each knowledge entry includes:
- **Verification Level**: [VERIFIED], [TESTING], [HYPOTHESIS]
- **Impact Level**: [CRITICAL], [IMPORTANT], [NICE_TO_HAVE]
- **Scope Tag**: [GLOBAL] or [PROJECT:project_name]
- **Expiration Date**: [EXPIRES:YYYY-MM-DD] (optional)

### Task Management

#### Global Tasks
- Stored in `.cursor/think/todo.md`
- Cross-project planning and coordination
- System-level tasks and improvements

#### Project Tasks
- Stored in `{project}/todo.md`
- Project-specific features and bug fixes
- Project milestones and releases

#### Task Templates

**Feature Development:**
```markdown
- [ ] **Task**: Task name
- [ ] **Description**: Task description
- [ ] **Priority**: [HIGH/MEDIUM/LOW]
- [ ] **Estimated Time**: Time estimate
- [ ] **Dependencies**: [DEPENDS_ON:task_id]
- [ ] **Knowledge Required**: [REQUIRES:knowledge_id]
- [ ] **Knowledge Generated**: [GENERATES:knowledge_id]
- [ ] **Risk Level**: [RISK:HIGH/MEDIUM/LOW]
- [ ] **Status**: [TODO/IN_PROGRESS/REVIEW/DONE]
```

**Bug Fix:**
```markdown
- [ ] **Bug**: Bug description
- [ ] **Severity**: [CRITICAL/HIGH/MEDIUM/LOW]
- [ ] **Steps to Reproduce**: Steps
- [ ] **Expected Behavior**: Expected
- [ ] **Actual Behavior**: Actual
- [ ] **Root Cause**: Root cause
- [ ] **Solution**: Solution
- [ ] **Testing**: Testing plan
```

### Search and Retrieval

#### Global Search
- Search across all knowledge (global + all projects)
- Use semantic search for better results
- Filter by knowledge type, verification level, or impact

#### Project-Specific Search
- Search within current project context
- Automatically includes relevant global knowledge
- Focus on project-specific information

#### Search Examples
```bash
# Search for all knowledge about Docker
# Returns global Docker knowledge + project-specific Docker usage

# Search for React-specific knowledge
# Returns React-related global knowledge + project-specific React lessons

# Search for bug fixes in current project
# Returns project-specific bug fixes + relevant global troubleshooting
```

## Configuration

### System Configuration
File: `.cursor/projects/system_config.json`

Key settings:
- `auto_discovery.enabled`: Enable automatic project detection
- `knowledge_sync.enabled`: Enable knowledge synchronization
- `search.enabled`: Enable search functionality
- `validation.enabled`: Enable knowledge validation

### Classification Rules
File: `.cursor/projects/classification_rules.json`

```

```
