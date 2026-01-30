#!/usr/bin/env python3
"""
Convert Antigravity Kit skills to OpenCode format
"""

import os
import re
import yaml
from pathlib import Path


def convert_skill_frontmatter(filepath):
    """Convert SKILL.md frontmatter to OpenCode format"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print(f"  ⚠️  No frontmatter found in {filepath.name}")
        return False

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"  ⚠️  YAML parse error in {filepath.name}: {e}")
        return False

    # Extract existing fields
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    version = frontmatter.get("version")

    # Build new frontmatter (OpenCode format)
    new_frontmatter = {
        "name": name,
        "description": description,
        "license": "MIT",
        "compatibility": "opencode",
    }

    # Move version to metadata if exists
    if version:
        new_frontmatter["metadata"] = {"version": version}

    # Generate new YAML
    new_yaml_lines = ["---"]
    for key, value in new_frontmatter.items():
        if key == "metadata":
            new_yaml_lines.append("metadata:")
            for mk, mv in value.items():
                new_yaml_lines.append(f"  {mk}: {mv}")
        else:
            new_yaml_lines.append(f"{key}: {value}")
    new_yaml_lines.append("---")
    new_yaml = "\n".join(new_yaml_lines)

    # Replace frontmatter in content
    new_content = re.sub(r"^---.*?---", new_yaml, content, flags=re.DOTALL, count=1)

    # Write back
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  ✅ Converted: {filepath.parent.name}/{filepath.name}")
    return True


def main():
    skills_dir = Path(".opencode/skills")

    if not skills_dir.exists():
        print("❌ Skills directory not found")
        return 1

    print("🔄 Converting skills to OpenCode format...")
    print()

    converted = 0
    failed = 0

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            print(f"  ⚠️  No SKILL.md in {skill_dir.name}")
            continue

        if convert_skill_frontmatter(skill_md):
            converted += 1
        else:
            failed += 1

    print()
    print(f"✅ Converted: {converted} skills")
    if failed > 0:
        print(f"⚠️  Failed: {failed} skills")

    return 0


if __name__ == "__main__":
    exit(main())
