---
description: Create a conventional commit message for staged changes
argument-hint: [type] [scope] [description]
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git commit:*), Bash(git add:*), Read, Edit
---

Please help me create a conventional commit for STAGED changes only, following the Conventional Commits specification.

Arguments provided: $ARGUMENTS

IMPORTANT: Only work with staged changes. Do not stage any unstaged changes.

First, check for staged changes:

1. Run `git diff --cached --stat` to see what files are staged
2. If no files are staged, inform me that I need to stage changes first with `git add`
3. Run `git diff --cached` to understand the staged changes

If no arguments are provided and there are staged changes, please:

1. Analyze the staged changes
2. Automatically determine the most appropriate commit type using these rules:
   - **test**: Changes primarily to test files (test/, spec/, **tests**, *.test.*, *.spec.*)
   - **docs**: Documentation-only changes (*.md,*.txt, docs/, README, CHANGELOG)
   - **fix**: Bug fixes (look for keywords: fix, correct, resolve, patch, repair in diff or new functionality that corrects issues)
   - **feat**: New features (new files, significant new functionality, major additions)
   - **refactor**: Code restructuring without changing functionality (similar insertion/deletion ratios, moved code, renamed variables/functions)
   - **perf**: Performance improvements (optimizations, caching, algorithm improvements)
   - **build**: Build system or dependency changes (package.json, requirements.txt, Makefile, webpack, etc.)
   - **ci**: CI/CD configuration changes (.github/, .gitlab-ci.yml, .travis.yml, jenkinsfile, etc.)
   - **chore**: Other maintenance changes (linting, formatting, gitignore, etc.)
   - **style**: Code style changes (whitespace, formatting, semicolons) without logic changes
3. Inform the user of the automatically selected commit type and proceed with creating the commit

If arguments are provided, parse them as:

- First argument: commit type (feat, fix, docs, etc.)
- Second argument (optional): scope (component or area of change)
- Remaining arguments: description

Then:

1. Analyze the staged changes using `git diff --cached`
2. Suggest a properly formatted conventional commit message:
   - Format: `<type>(<scope>): <description>`
   - Or without scope: `<type>: <description>`
3. If there are breaking changes, add them to the commit body
4. **Update CHANGELOG.md**:
   - Only update CHANGELOG.md if it already exists. DO NOT create a new file.
   - Read the current CHANGELOG.md file
   - Add a new entry at the top under `## [Current] - YYYY-MM-DD` with today's date
   - Include the commit type, scope (if present), and description
   - Add any relevant details from the staged changes
   - Stage the updated CHANGELOG.md with `git add CHANGELOG.md`
5. Create the commit with the conventional commit message

Please ensure the commit message:

- Has a clear, concise description in present tense
- Includes a scope if it makes sense for the change
- Follows the conventional commit format exactly
- Adds any necessary context in the commit body

DO NOT stage any unstaged files - only work with what is already staged.
