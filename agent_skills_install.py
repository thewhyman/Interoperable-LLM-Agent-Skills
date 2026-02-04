#!/usr/bin/env python3
import os
import argparse
import sys
import shutil
from pathlib import Path
import platform
import subprocess

# Standard paths
HOME = Path.home()
ANTIGRAVITY_SKILLS = HOME / ".antigravity" / "skills"
CLAUDE_SKILLS = HOME / ".claude" / "skills"
GEMINI_SKILLS = HOME / ".gemini" / "antigravity" / "skills"

def fix_macos_permissions(path):
    """
    On macOS, downloaded or copied files may have quarantine attributes 
    that prevent agents (like Claude Desktop) from reading them.
    This function runs 'xattr -cr' to clear those attributes.
    """
    if platform.system() != "Darwin":
        return

    try:
        # Check if xattr exists (it should on standard macOS)
        subprocess.run(
            ["xattr", "-cr", str(path)], 
            check=True, 
            capture_output=True
        )
        print(f"  [MACOS] Cleared quarantine attributes for: {path.name}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fail silently or log if critical, but don't crash installation
        pass

# Description and Usage Examples
DESCRIPTION = """
Install LLM Skills to standard agent directories.
By default, this script installs skills to ALL detected standard locations
(Antigravity, Claude Code, Gemini) using a copy/overwrite strategy.
"""

EPILOG = """
examples:
  # Install to all standard locations (default)
  python3 agent_skills_install.py

  # Install only for Claude Code
  python3 agent_skills_install.py --claude-code

  # Install to a specific custom directory
  python3 agent_skills_install.py --target /path/to/custom/skills

  # Use symlinks instead of copying (useful for development)
  python3 agent_skills_install.py --symlink
"""

def load_skills_manifest(manifest_path="skills.yaml"):
    if not os.path.exists(manifest_path):
        print(f"Error: Manifest file '{manifest_path}' not found.")
        sys.exit(1)
    
    skills = []
    current_skill = {}
    
    with open(manifest_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Very basic parsing for list of dicts
            if line.startswith('- name:'):
                if current_skill:
                    skills.append(current_skill)
                current_skill = {'name': line.split(':', 1)[1].strip()}
            elif line.startswith('path:') and current_skill is not None:
                current_skill['path'] = line.split(':', 1)[1].strip()
            elif line.startswith('description:') and current_skill is not None:
                current_skill['description'] = line.split(':', 1)[1].strip().strip('"')
            elif line.startswith('url:') and current_skill is not None:
                current_skill['url'] = line.split(':', 1)[1].strip().strip('"')

        if current_skill:
            skills.append(current_skill)
            
    return {'skills': skills}

def install_skill(skill, target_dir, link=False):
    name = skill.get('name')
    path = skill.get('path')
    
    if not name or not path:
        print(f"Skipping invalid skill entry: {skill}")
        return

    # Resolve source path
    source_path = Path(path).resolve()
    if not source_path.exists():
        print(f"Error: Skill source '{source_path}' does not exist.")
        return

    # Destination path
    dest_path = target_dir / name
    
    # Clean up existing
    if dest_path.exists() or dest_path.is_symlink():
        try:
            if dest_path.is_dir() and not dest_path.is_symlink():
                shutil.rmtree(dest_path)
            else:
                os.remove(dest_path)
        except OSError as e:
            print(f"Error removing existing {dest_path}: {e}")

    try:
        if link:
            os.symlink(source_path, dest_path)
            print(f"  [LINK] {name} -> {dest_path}")
        else:
            shutil.copytree(source_path, dest_path)
            print(f"  [COPY] {name} -> {dest_path}")
            
        # Fix permissions after copy/link
        fix_macos_permissions(dest_path)

    except OSError as e:
        print(f"  [FAIL] Failed to install {name}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--manifest", default="skills.yaml", help="Path to skills.yaml (default: skills.yaml)")
    parser.add_argument("--symlink", action="store_true", help="Install via symlink instead of copy")
    
    # Target selection
    parser.add_argument("--all", action="store_true", help="Install to all standard agent locations (default)")
    parser.add_argument("--antigravity", action="store_true", help=f"Install to {ANTIGRAVITY_SKILLS}")
    parser.add_argument("--claude-code", action="store_true", help=f"Install to {CLAUDE_SKILLS}")
    parser.add_argument("--gemini", action="store_true", help=f"Install to {GEMINI_SKILLS}")
    parser.add_argument("--target", help="Install to a custom directory path")

    args = parser.parse_args()

    # Determine targets
    targets = []
    
    # Check if any specific standard target was requested
    specific_standard_targets = args.antigravity or args.claude_code or args.gemini
    
    # Logic: 
    # 1. Custom target always allowed
    if args.target:
        targets.append(Path(args.target))
    
    # 2. If 'all' explicitly requested OR no specific targets requested, add all standard paths
    if args.all or (not specific_standard_targets and not args.target):
        targets.append(ANTIGRAVITY_SKILLS)
        targets.append(CLAUDE_SKILLS)
        targets.append(GEMINI_SKILLS)
    else:
        # 3. Add specific requested targets
        if args.antigravity: targets.append(ANTIGRAVITY_SKILLS)
        if args.claude_code: targets.append(CLAUDE_SKILLS)
        if args.gemini: targets.append(GEMINI_SKILLS)

    # Dedup just in case
    targets = sorted(list(set(targets)))

    if not targets:
        print("No targets selected.")
        return

    # Load Manifest
    manifest = load_skills_manifest(args.manifest)
    skills = manifest.get('skills', [])
    
    if not skills:
        print("No skills found in manifest.")
        return

    print(f"Found {len(skills)} skills in manifest.")
    print(f"Target Mode: {'SYMLINK' if args.symlink else 'COPY/OVERWRITE'}")
    
    for target_dir in targets:
        print(f"\nTarget: {target_dir}")
        if not target_dir.exists():
            try:
                os.makedirs(target_dir, exist_ok=True)
                print(f"  Created directory: {target_dir}")
            except OSError as e:
                print(f"  Error creating directory {target_dir}: {e}")
                continue
        
        for skill in skills:
            install_skill(skill, target_dir, link=args.symlink)

    print("\nDone.")

if __name__ == "__main__":
    main()
