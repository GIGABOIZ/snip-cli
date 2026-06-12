# ✂️ Snip CLI

Never forget a complex terminal command again. **Snip** is a lightweight, blazing-fast CLI tool to save, tag, and search your terminal snippets right from the command line.

## 🚀 Features
* **Lightning Fast:** Built in pure Python with zero heavy dependencies.
* **Tagging System:** Organize your snippets by context (e.g., `git`, `docker`, `sql`).
* **Instant Search:** Find exactly what you need with simple keyword searches.
* **Local Storage:** Everything is saved safely on your machine in `~/.terminal_snippets.json`.

## 🛠️ Installation

Clone the repository and install it globally using `pip`:

\`\`\`bash
pip install git+https://github.com/GIGABOIZ/snip-cli.git
\`\`\`

## 📖 Usage

**1. Add a Snippet**
\`\`\`bash
snip add -t "Undo last commit" -g "git" -c "git reset HEAD~1"
\`\`\`

**2. List All Snippets**
\`\`\`bash
snip list
\`\`\`

**3. Search Snippets**
\`\`\`bash
snip search git
\`\`\`
