# Changelog

All notable changes to the Polaris project will be documented in this file.

## [Current] - 2025-10-04

### build(railway): migrate from Nixpacks to Dockerfile for deployment

- Add multi-stage Dockerfile with UV package manager support
- Add .dockerignore to optimize Docker build context
- Update railway.json to use DOCKERFILE builder instead of NIXPACKS
- Fix start command to use correct polaris.main:app module path
- Optimize for production with non-root user and minimal runtime image

### build(railway): add Railway deployment configuration and dependencies

- Add railway.json with Nixpacks builder configuration
- Add .env.example with database, Redis, and secret key templates
- Move requirements.txt to root for Railway deployment compatibility
- Configure uvicorn start command for Railway with dynamic port binding
- Set restart policy with failure handling and max retries

## [2025-10-03]

### docs: add GNU AGPL v3 license and comprehensive project README

- Add LICENSE.md with full GNU Affero General Public License v3 text
- Add README.md with project overview, features, tech stack, and quickstart guide
- Establish AGPL licensing for network copyleft protection

### chore(init): initial project setup for Python/FastAPI ADHD-friendly task manager

- Add project structure with backend Python package layout
- Add FastAPI dependencies and development tools in pyproject.toml
- Add comprehensive CLAUDE.md with development guidelines and patterns
- Add POLARIS_PYTHON_CONTEXT.md with architecture decisions and MVP roadmap
- Add extensive documentation for Flutter frontend, fullstack integration, dogfooding strategy, and quickstart guide
- Add custom Claude Code /commit command for conventional commits
- Add .gitignore for Python, UV, Docker, Flutter, and development artifacts
- Add Python 3.12 version specification
- Add mise.toml for development environment configuration
- Add placeholder backend entry point (main.py) and package structure
