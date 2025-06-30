# Windsurf Template Approach for Sequential Autonomous Development

## Overview

This document outlines a streamlined approach for using Windsurf and Cascade to efficiently develop multiple autonomous software projects in sequence. By utilizing a template-based approach, each new project can be rapidly initialized with all necessary autonomous development tooling and configurations, allowing you to focus on the unique aspects of each project rather than repetitive setup.

## Template Architecture

### Project Template Structure

```
autodev-template/
├── .roo/                      # Configuration root
│   ├── mcp.json               # Pre-configured MCP servers
│   ├── sparc-config.json      # SPARC executor settings
│   ├── orchestrator/          # BatchTool orchestrator configs
│   │   └── config.json
│   └── monitoring/            # Monitoring configs
│       └── config.json
├── .env.template              # API keys template
├── docs/                      # Documentation
│   ├── developer_guide.md     # Development guidelines
│   └── workflow.md            # Project workflow documentation
├── scripts/                   # Automation scripts
│   ├── init-project.sh        # Project initialization
│   ├── start-services.sh      # Start MCP servers
│   └── create-checkpoint.sh   # Create review checkpoints
└── project-config.json        # Project configuration template
```

### Key Configuration Files

#### 1. MCP Server Configuration (`.roo/mcp.json`)
```json
{
  "mcpServers": {
    "safla": {
      "command": "python3",
      "args": ["./safla/safla_mcp_server.py"],
      "env": {
        "SAFLA_REMOTE_URL": "https://safla.fly.dev",
        "SAFLA_API_KEY": "${SAFLA_API_KEY}",
        "MEMORY_PERSISTENCE": "true",
        "VECTOR_DB_PATH": "./.roo/safla/vector_db"
      }
    },
    "qudag": {
      "command": "node",
      "args": ["./qudag/qudag_mcp_server.js"],
      "env": {
        "QUDAG_SECRET": "${QUDAG_SECRET}",
        "QUDAG_CONFIG": "./qudag/config.json",
        "QUANTUM_RESISTANT_MODE": "true"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-fs"]
    },
    "terminal": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-terminal"]
    },
    "swarm": {
      "command": "node",
      "args": ["./claude-flow/src/mcp/swarm-server.js"],
      "env": {
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
        "SWARM_CONFIG": "./claude-flow/config/swarm.json"
      }
    }
  }
}
```

#### 2. SPARC Executor Configuration (`.roo/sparc-config.json`)
```json
{
  "enableTDD": true,
  "memoryUsage": "optimized",
  "qualityThreshold": 0.85,
  "phases": {
    "specification": { "autoValidate": true },
    "pseudocode": { "requireDiagrams": true },
    "architecture": { "includePatterns": true },
    "refinement": { "testCoverage": 0.9 },
    "completion": { "generateDocs": true }
  },
  "integrations": {
    "safla": { "enabled": true, "memorySync": true },
    "qudag": { "enabled": true, "secureComms": true }
  }
}
```

#### 3. Project Configuration (`project-config.json`)
```json
{
  "name": "PROJECT_NAME",
  "description": "PROJECT_DESCRIPTION",
  "agentTeam": {
    "architect": true,
    "coder": true,
    "tdd": true,
    "security": true,
    "devops": true,
    "documentation": true
  },
  "checkpoints": {
    "specification": true,
    "architecture": true,
    "implementation": true,
    "testing": true,
    "deployment": true
  },
  "tddSettings": {
    "enabled": true,
    "coverageTarget": 90
  }
}
```

## Project Initialization Workflow

### 1. Create New Project from Template

```bash
# create-project.sh
#!/bin/bash
PROJECT_NAME=$1
PROJECT_DESC=$2
TEMPLATE_DIR="/path/to/autodev-template"

# Create new project from template
echo "Creating new project: $PROJECT_NAME"
cp -r $TEMPLATE_DIR $PROJECT_NAME
cd $PROJECT_NAME

# Update project configuration
sed -i "s/PROJECT_NAME/$PROJECT_NAME/" project-config.json
sed -i "s/PROJECT_DESCRIPTION/$PROJECT_DESC/" project-config.json

# Initialize environment
cp .env.template .env
echo "Please edit .env to add your API keys"

# Initialize git repository
git init
git add .
git commit -m "Initial project setup from autodev template"

echo "Project created successfully. Open with Windsurf using:"
echo "windsurf open $PROJECT_NAME --profile=autodev"
```

### 2. Configure Project Environment

After creating the project, configure the project-specific settings:

1. Add required API keys to `.env`
2. Customize the agent team in `project-config.json` based on project needs
3. Adjust SPARC configuration if needed for specific project requirements

### 3. Launch Development Environment

```bash
# Launch Windsurf with the autodev profile
windsurf open $PROJECT_NAME --profile=autodev
```

## Windsurf IDE Configuration

### Autodev Profile Setup

Create a dedicated Windsurf profile optimized for autonomous development:

```json
// autodev-profile.json
{
  "name": "autodev",
  "layout": {
    "mainEditor": {
      "position": "center",
      "size": "70%"
    },
    "agentPanel": {
      "position": "right",
      "size": "30%"
    },
    "terminal": {
      "position": "bottom",
      "size": "20%",
      "defaultCommand": "claude-flow status"
    }
  },
  "extensions": [
    "claude-flow-commands",
    "agent-monitor",
    "checkpoint-manager",
    "mcp-server-manager"
  ],
  "keyBindings": {
    "ctrl+shift+a": "autodev.launchAgentPanel",
    "ctrl+shift+c": "autodev.createCheckpoint",
    "ctrl+shift+s": "autodev.startServices",
    "ctrl+shift+m": "autodev.openMemoryBank"
  }
}
```

### Cascade Integration

Configure Cascade to work seamlessly with the autonomous development workflow:

1. **Project Context Loading**: Automatically load project context when opening a project
2. **Agent Command Integration**: Direct integration with claude-flow commands
3. **Memory Bank Access**: Quick access to project memory bank

## Project Development Workflow

### 1. Start Project Session

```bash
# From within project directory
./scripts/start-session.sh
```

This script performs the following:
- Starts all MCP servers
- Initializes the SPARC executor
- Launches the monitoring dashboard
- Sets up agent memory bank

### 2. Agent Interaction via Cascade

Use Cascade commands directly in the Windsurf editor:

- `@cascade start phase specification` - Begin the specification phase
- `@cascade deploy architect` - Deploy the architect agent
- `@cascade create checkpoint` - Create a human review checkpoint
- `@cascade status` - Check current project status

### 3. Project Completion and Archiving

When finishing a project:

```bash
./scripts/archive-project.sh
```

This script:
1. Exports all project memory for future reference
2. Creates a project completion report
3. Stops all MCP servers
4. Archives project files

## Project Handover Between Projects

When moving from one project to another:

1. Complete the current project using the archive script
2. Initialize the new project from the template
3. Launch the new project in Windsurf

This clean separation ensures no cross-contamination of project contexts or agent memories.

## Template Maintenance

### Regular Updates

Periodically update the project template based on lessons learned:

1. Incorporate workflow improvements
2. Update configuration best practices
3. Add new automation scripts
4. Enhance documentation

### Template Versioning

Keep your template versioned to track improvements:

```bash
# Create a new template version
cp -r autodev-template autodev-template-v1.2
git -C autodev-template-v1.2 init
git -C autodev-template-v1.2 add .
git -C autodev-template-v1.2 commit -m "Version 1.2 of autodev template"
```

## Command Reference

| Command | Description |
|---------|-------------|
| `./create-project.sh <name> <description>` | Create new project from template |
| `./scripts/start-session.sh` | Start development session |
| `./scripts/create-checkpoint.sh` | Create human checkpoint |
| `./scripts/archive-project.sh` | Complete and archive project |
| `@cascade start phase <phase>` | Begin SPARC phase |
| `@cascade deploy <agent>` | Deploy specific agent |
| `@cascade memory <action>` | Interact with memory bank |

## Conclusion

This template-based approach to sequential autonomous development provides:

1. **Consistency**: Each project follows the same well-defined process
2. **Efficiency**: Minimal setup time when starting new projects
3. **Focus**: Clean separation between projects prevents context contamination
4. **Improvement**: Centralized template enables continuous process refinement

By maintaining a high-quality project template and following this workflow, you can maximize productivity and quality across multiple autonomous development projects even when working on them sequentially.
