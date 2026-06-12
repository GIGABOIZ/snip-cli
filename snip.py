#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

# Setup the hidden storage file in the user's home directory
STORAGE_FILE = Path.home() / ".terminal_snippets.json"

def load_snippets():
    if STORAGE_FILE.exists():
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    return []

def save_snippets(snippets):
    with open(STORAGE_FILE, "w") as f:
        json.dump(snippets, f, indent=4)

def add_snippet(title, tag, command):
    snippets = load_snippets()
    snippets.append({"title": title, "tag": tag.lower(), "command": command})
    save_snippets(snippets)
    print(f"✅ Snippet '{title}' added successfully!")

def list_snippets():
    snippets = load_snippets()
    if not snippets:
        print("📭 No snippets saved yet.")
        return
    
    print("\n📦 Your Saved Snippets:\n" + "-"*30)
    for i, snip in enumerate(snippets, 1):
        print(f"{i}. [{snip['tag'].upper()}] {snip['title']}")
        print(f"   > {snip['command']}\n")

def search_snippets(query):
    snippets = load_snippets()
    query = query.lower()
    results = [s for s in snippets if query in s['title'].lower() or query in s['tag'].lower()]
    
    if not results:
        print(f"🔍 No snippets found matching '{query}'.")
        return

    print(f"\n🔍 Search Results for '{query}':\n" + "-"*30)
    for snip in results:
        print(f"[{snip['tag'].upper()}] {snip['title']}")
        print(f" > {snip['command']}\n")

def main():
    parser = argparse.ArgumentParser(description="Terminal Snippet Manager - Never forget a command again.")
    subparsers = parser.add_subparsers(dest="action", help="Actions")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new snippet")
    add_parser.add_argument("-t", "--title", required=True, help="Description of the snippet")
    add_parser.add_argument("-g", "--tag", required=True, help="Category tag (e.g., git, docker, sql)")
    add_parser.add_argument("-c", "--command", required=True, help="The actual code or command")

    # 'list' command
    subparsers.add_parser("list", help="List all saved snippets")

    # 'search' command
    search_parser = subparsers.add_parser("search", help="Search snippets by title or tag")
    search_parser.add_argument("query", help="Search keyword")

    args = parser.parse_args()

    if args.action == "add":
        add_snippet(args.title, args.tag, args.command)
    elif args.action == "list":
        list_snippets()
    elif args.action == "search":
        search_snippets(args.query)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
