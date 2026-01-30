#!/usr/bin/env python3
"""
Convert Antigravity Kit agents to OpenCode format
"""

import os
import re
import yaml
from pathlib import Path

# Agent mode classification
PRIMARY_AGENTS = ["orchestrator", "project-planner"]


# Tools mapping: comma-separated to YAML object
def convert_tools_field(tools_str):
    """Convert 'Read, Grep, Glob' to {read: true, glob: true, grep: true}"""
    if not tools_str or isinstance(tools_str, dict):
        return {}

    tools = {}
    if isinstance(tools_str, str):
        for tool in tools_str.split(","):
            tool = tool.strip().lower()
            # Map Antigravity tool names to OpenCode tool names
            tool_mapping = {
                "read": "read",
                "grep": "grep",
                "glob": "glob",
                "bash": "bash",
                "edit": "edit",
                "write": "write",
                "viewcodeitem": None,  # Not available in OpenCode
                "findbyname": None,  # Not available in OpenCode
                "agent": None,  # Use 'task' tool instead
            }
            if tool in tool_mapping:
                opencode_tool = tool_mapping[tool]
                if opencode_tool:
                    tools[opencode_tool] = True
    return tools


def extract_skills_list(skills_str):
    """Extract skills list from skills field"""
    if not skills_str:
        return []

    if isinstance(skills_str, str):
        return [s.strip() for s in skills_str.split(",")]
    return []


def convert_agent_file(agent_file):
    """Convert agent markdown file to OpenCode format"""
    with open(agent_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print(f"  ⚠️  No frontmatter found in {agent_file.name}")
        return False

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"  ⚠️  YAML parse error in {agent_file.name}: {e}")
        return False

    # Extract fields
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    tools_str = frontmatter.get("tools", "")
    model = frontmatter.get("model", "inherit")
    skills_str = frontmatter.get("skills", "")

    # Determine mode
    agent_name = agent_file.stem
    mode = "primary" if agent_name in PRIMARY_AGENTS else "subagent"

    # Convert tools
    tools = convert_tools_field(tools_str)

    # Extract skills for prompt insertion
    skills_list = extract_skills_list(skills_str)

    # Build new frontmatter (OpenCode format)
    new_frontmatter_lines = [
        "---",
        f"description: {description}",
        f"mode: {mode}",
        f"model: {model}",
        "tools:",
    ]

    # Add tools in YAML format
    if tools:
        for tool, enabled in sorted(tools.items()):
            new_frontmatter_lines.append(f"  {tool}: {enabled}")
    else:
        new_frontmatter_lines.append("  read: true")

    # Add permissions for safety
    new_frontmatter_lines.append("permission:")
    if mode == "primary":
        new_frontmatter_lines.append("  edit: ask")
        new_frontmatter_lines.append("  bash: ask")
    else:
        # Subagents: more restrictive for write operations
        if "write" in tools or "edit" in tools:
            new_frontmatter_lines.append("  edit: ask")
            new_frontmatter_lines.append("  bash: ask")
        else:
            new_frontmatter_lines.append("  bash: ask")

    new_frontmatter_lines.append("---")
    new_frontmatter = "\n".join(new_frontmatter_lines)

    # Replace frontmatter
    new_content = re.sub(
        r"^---.*?---", new_frontmatter, content, flags=re.DOTALL, count=1
    )

    # Insert skills reference into prompt (after frontmatter, before main content)
    if skills_list:
        skills_section = "\n## Available Skills\n\n"
        skills_section += "When relevant, use the `skill` tool to load:\n"
        for skill in skills_list:
            skill_name = skill.strip()
            skills_section += f"- `{skill_name}`\n"
        skills_section += "\n"

        # Insert after the first heading after frontmatter
        # Find the first # heading and insert before it
        heading_match = re.search(r"\n# ", new_content)
        if heading_match:
            insert_pos = heading_match.start()
            new_content = (
                new_content[:insert_pos] + skills_section + new_content[insert_pos:]
            )

    # Write to new location
    output_path = Path(".opencode/agents") / agent_file.name
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(
        f"  ✅ Converted: {agent_file.name} (mode: {mode}, skills: {len(skills_list)})"
    )
    return True


def main():
    agents_dir = Path(".agent/agents")

    if not agents_dir.exists():
        print("❌ Agents directory not found")
        return 1

    print("🔄 Converting agents to OpenCode format...")
    print()

    converted = 0
    failed = 0

    for agent_file in sorted(agents_dir.glob("*.md")):
        if convert_agent_file(agent_file):
            converted += 1
        else:
            failed += 1

    print()
    print(f"✅ Converted: {converted} agents")
    if failed > 0:
        print(f"⚠️  Failed: {failed} agents")

    return 0


if __name__ == "__main__":
    exit(main())
