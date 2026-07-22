# Contributing to UDF

Thank you for your interest in contributing to the Unified Delivery Framework (UDF)! This document provides guidelines for contributing to this guideline repository.

## 📋 Table of Contents

- [How to Contribute](#how-to-contribute)
- [Types of Contributions](#types-of-contributions)
- [Contribution Guidelines](#contribution-guidelines)
- [Submitting Changes](#submitting-changes)

## 🤝 How to Contribute

We welcome contributions in various forms:

1. **Documentation Improvements** - Fix typos, clarify concepts, or add new guides
2. **Templates** - Add new templates or improve existing ones
3. **Examples** - Share real-world implementation examples
4. **Best Practices** - Document lessons learned and recommended approaches
5. **Community Automation** - Improve public validators, schemas, skills, or interfaces

## 📝 Types of Contributions

### Documentation

- Ensure documentation is clear, concise, and follows the existing style
- Use Markdown formatting consistently
- Include code examples where appropriate
- Update the table of contents when adding new sections

### Templates

Templates should be placed in the `/templates` directory and include:
- Clear naming convention
- Comprehensive comments explaining usage
- Example values or placeholders
- README file explaining the template's purpose

### Examples

Examples should be placed in the `/examples` directory and include:
- Working code that can be executed or adapted
- README file with setup instructions
- Clear comments explaining key concepts
- Dependencies and requirements documented

### Wiki Content

For extended documentation, tutorials, or community-contributed content:
- Edit Markdown under [`wiki/`](wiki/) in this repository (source of truth for numbered wiki pages).
- After merge, **maintainers** publish updates to the [GitHub Wiki](https://github.com/akasha-code/UDF/wiki) by copying files to the `UDF.wiki` git repo; see [WIKI_GUIDE.md](WIKI_GUIDE.md) (section *Syncing wiki/ to the GitHub Wiki*).
- Follow the wiki's structure and guidelines
- Cross-reference with repository documentation where appropriate

### Repository Boundary

This repository contains the public UDF framework and its community resources. Framework definitions belong in `wiki/`; public guidance belongs in `docs/`; executable community assistance belongs in `skills/`, `schemas/`, or `scripts/`.

Commercial manuscripts, complete worked cases, private product roadmaps, customer material, and proprietary implementations are maintained separately and are not accepted through this repository. Do not submit content you do not intend to license under Apache License 2.0.

## 📐 Contribution Guidelines

### File Organization

- Place templates in `/templates` with descriptive subdirectories
- Place examples in `/examples` organized by use case
- Place documentation in `/docs` following the existing structure
- Link material interpretations and examples back to their canonical `wiki/` sources
- Use clear, descriptive filenames

### Markdown Style

- Use headers hierarchically (h1 for title, h2 for sections, etc.)
- Include a table of contents for longer documents
- Use code blocks with language identifiers
- Use relative links for internal references

### Code Style

- Follow language-specific best practices
- Include comments for complex logic
- Use meaningful variable and function names
- Keep examples simple and focused

## 🚀 Submitting Changes

### Process

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/your-contribution`)
3. **Make your changes**
4. **Commit with clear messages** (`git commit -m "Add new deployment template"`)
5. **Push to your fork** (`git push origin feature/your-contribution`)
6. **Open a Pull Request**

### Pull Request Guidelines

- Provide a clear title and description
- Reference any related issues
- Ensure all links work correctly
- Verify that examples run successfully
- Request review from maintainers

## 🔍 Review Process

All contributions will be reviewed by maintainers. We may:
- Request changes or improvements
- Suggest alternative approaches
- Ask for additional documentation

## 💬 Getting Help

If you have questions:
- Check the [documentation](./docs/)
- Browse the [GitHub Wiki](https://github.com/akasha-code/UDF/wiki)
- Open a [Discussion](https://github.com/akasha-code/UDF/discussions)
- Ask in an [Issue](https://github.com/akasha-code/UDF/issues)

## 📄 License

By contributing to UDF, you agree that your contributions will be licensed under the Apache License 2.0.

Thank you for helping make UDF better!
