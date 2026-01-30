# OpenCode Commands

Custom commands for OpenCode TUI, converted from `.agent/workflows/` system.

## Available Commands

| Command | Description | Agent | Subtask |
|---------|-------------|-------|---------|
| `/status` | Show project and agent status | - | - |
| `/preview` | Preview server management (start/stop/restart) | - | - |
| `/brainstorm` | Structured brainstorming for projects | - | - |
| `/plan` | Create project plan with task breakdown | general | ✅ |
| `/create` | Create new application | general | ✅ |
| `/enhance` | Add features to existing application | general | ✅ |
| `/debug` | Systematic problem investigation | - | - |
| `/test` | Test generation and execution | - | - |
| `/deploy` | Production deployment with pre-flight checks | - | - |
| `/orchestrate` | Coordinate multiple agents for complex tasks | general | ✅ |
| `/ui-ux-pro-max` | AI-powered design system with 50+ styles | - | - |

## Usage

### Basic Usage

Type `/` in the OpenCode TUI followed by the command name:

```
/status
/preview start
/brainstorm authentication system
/create todo app
/debug API returns 500 error
/test src/services/auth.ts
/deploy
```

### Commands with Arguments

Many commands accept arguments using `$ARGUMENTS`:

```
/plan e-commerce site with cart
/create blog site with markdown support
/enhance add dark mode
/debug login not working
/test user registration flow
/ui-ux-pro-max fintech dashboard modern
```

### Subcommands

Some commands support subcommands:

```
/preview [start|stop|restart|check]
/deploy [check|preview|production|rollback]
/test [coverage|watch]
```

## Command Details

### `/status` - Project Status

Shows current project information:
- Project name and type
- Tech stack
- Running preview server
- File statistics

### `/preview` - Preview Server Management

Manage development preview servers:
- `/preview` - Show current status
- `/preview start` - Start server
- `/preview stop` - Stop server
- `/preview restart` - Restart server
- `/preview check` - Health check

Auto-detects:
- Next.js (npm run dev)
- Vite (npm run dev)
- Python/FastAPI (uvicorn)
- Python/Flask (flask run)

### `/brainstorm` - Structured Brainstorming

Explore multiple options before implementation:
- Provides 3+ approaches with pros/cons
- Estimates effort levels
- Recommends best approach
- No code, only ideas

### `/plan` - Project Planning

Create detailed project plans:
- Analyzes requirements
- Asks clarifying questions if needed
- Creates `docs/PLAN-{slug}.md`
- Task breakdown with phases
- No code writing, planning only

### `/create` - Create Application

Build new applications from scratch:
- Interactive requirement gathering
- Tech stack selection
- Project structure creation
- Core feature implementation
- Preview setup

### `/enhance` - Add Features

Update existing applications:
- Analyzes current codebase
- Plans changes
- Creates new files
- Updates existing code
- Maintains consistency

### `/debug` - Debug Issues

Systematic problem investigation:
- Gathers error context
- Checks recent changes
- Forms hypotheses
- Tests systematically
- Applies fixes
- Adds prevention measures

### `/test` - Testing

Generate and run tests:
- `/test` - Run all tests
- `/test [file]` - Generate tests for file
- `/test coverage` - Show coverage report
- Supports Jest, Vitest, pytest, Go test

### `/deploy` - Deployment

Production deployment with safety:
- Pre-flight checks (lint, test, build, security)
- Platform detection (Vercel, Railway, Fly, Docker)
- Deployment execution
- Health verification
- Rollback support

### `/orchestrate` - Multi-Agent Coordination

Coordinate multiple agents for complex tasks:
- Minimum 3 parallel tasks
- Two-phase approach (planning → implementation)
- User approval gates
- Comprehensive reporting

### `/ui-ux-pro-max` - Design System

AI-powered design recommendations:
- 50+ UI styles
- 97 color palettes
- 57 font pairings
- 99 UX guidelines
- 25 chart types
- 9 tech stacks

## Tool Mapping

| Original Workflow | OpenCode Tools |
|------------------|----------------|
| Python scripts | ``!`command` `` (shell output) |
| Agent invocation | `task` tool |
| File search | `glob`, `grep` |
| File read | `read` |
| File write | `write` |
| File edit | `edit` |
| Questions | `question` tool |
| Task tracking | `todowrite` tool |

## Features

### Shell Command Execution

Commands can run shell commands and include output:

```bash
!`npm test`
!`ps aux | grep node`
!`git log --oneline -10`
```

### File References

Include file content automatically:

```markdown
Review the component in @src/components/Button.tsx
```

### Positional Arguments

Access individual arguments:

```markdown
$1 - First argument
$2 - Second argument
$3 - Third argument
```

## Architecture

```
.opencode/
└── commands/
    ├── brainstorm.md       # Idea exploration
    ├── create.md           # App creation
    ├── debug.md            # Problem investigation
    ├── deploy.md           # Deployment
    ├── enhance.md          # Feature addition
    ├── orchestrate.md      # Multi-agent tasks
    ├── plan.md             # Project planning
    ├── preview.md          # Server management
    ├── status.md           # Status display
    ├── test.md             # Testing
    └── ui-ux-pro-max.md    # Design system
```

## Best Practices

1. **Start with `/plan`** for complex features
2. **Use `/brainstorm`** before committing to approach
3. **Check `/status`** to understand current state
4. **Run `/test`** before `/deploy`**
5. **Use `/orchestrate`** for multi-domain tasks
6. **Apply `/ui-ux-pro-max`** for design guidance

## Migration Notes

These commands were converted from `.agent/workflows/` system:

- ✅ Maintained all original functionality
- ✅ Adapted to OpenCode's native tools
- ✅ Uses OpenCode's command syntax
- ✅ Supports shell command execution
- ✅ File references and arguments
- ⚠️  Some Python scripts retained (e.g., ui-ux-pro-max)
- ⚠️  Agent system simplified to OpenCode's model

## Support

For issues or questions:
- Check OpenCode docs: https://opencode.ai/docs/commands/
- Review original workflows: `.agent/workflows/`
- Test commands in isolation first
