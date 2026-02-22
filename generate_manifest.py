#!/usr/bin/env python3
"""
Screenshot Manifest Generator

Run this script after adding new screenshots to auto-generate the manifest.
The portfolio will then automatically display all images.

Usage:
    python generate_manifest.py

Or set up a GitHub Action to run this on push (see README).
"""

import os
import json
from pathlib import Path

ASSETS_DIR = Path("assets/projects")
MANIFEST_FILE = ASSETS_DIR / "manifest.json"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def generate_manifest():
    """Scan screenshot folders and generate manifest.json"""
    manifest = {}
    
    if not ASSETS_DIR.exists():
        print(f"Creating {ASSETS_DIR}")
        ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Scan for project folders
    for item in ASSETS_DIR.iterdir():
        if item.is_dir():
            project_id = item.name
            images = []
            
            # Find all images in this folder
            for file in sorted(item.iterdir()):
                if file.suffix.lower() in IMAGE_EXTENSIONS:
                    images.append(file.name)
            
            if images:
                manifest[project_id] = images
                print(f"  {project_id}: {len(images)} image(s)")
    
    # Write manifest
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✅ Manifest written to {MANIFEST_FILE}")
    print(f"   {len(manifest)} project(s) with images")
    
    return manifest


if __name__ == "__main__":
    print("Scanning for screenshots...\n")
    generate_manifest()
