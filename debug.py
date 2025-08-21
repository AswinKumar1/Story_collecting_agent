#!/usr/bin/env python3
"""
Debug script to check if all dependencies are available
Save as debug.py in your storytelling_UA directory
"""

import sys
import os

print(f"Python version: {sys.version}", file=sys.stderr)
print(f"Python executable: {sys.executable}", file=sys.stderr)
print(f"Current working directory: {os.getcwd()}", file=sys.stderr)
print(f"Python path: {sys.path}", file=sys.stderr)

# Check if .env file exists
env_file = ".env"
if os.path.exists(env_file):
    print(f"✅ .env file found", file=sys.stderr)
else:
    print(f"❌ .env file NOT found", file=sys.stderr)

# Try importing each dependency
dependencies = [
    "fastmcp",
    "aiohttp", 
    ("beautifulsoup4", "bs4"),  # package name, import name
    "openpyxl",
    "openai",
    "requests",
    "lxml",
    ("python-dotenv", "dotenv")  # package name, import name
]

print("\nDependency check:", file=sys.stderr)
for dep in dependencies:
    if isinstance(dep, tuple):
        package_name, import_name = dep
        try:
            __import__(import_name)
            print(f"✅ {package_name} (imports as {import_name})", file=sys.stderr)
        except ImportError as e:
            print(f"❌ {package_name}: {e}", file=sys.stderr)
    else:
        try:
            __import__(dep)
            print(f"✅ {dep}", file=sys.stderr)
        except ImportError as e:
            print(f"❌ {dep}: {e}", file=sys.stderr)

print("\nIf all dependencies show ✅, then the main script should work!", file=sys.stderr)

# Try to import the main components
try:
    print("\nTesting main script imports...", file=sys.stderr)
    from fastmcp import FastMCP
    print("✅ FastMCP imported successfully", file=sys.stderr)
except Exception as e:
    print(f"❌ Error importing main components: {e}", file=sys.stderr)