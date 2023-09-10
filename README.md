
# Advanced Image Renamer

Advanced Image Renamer is a Python script designed to offer a comprehensive solution for batch renaming image files in specified directories. With features like multi-language support, regular expression matching, and configuration file support, it provides a user-friendly yet powerful tool for file management tasks.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Changelog](#changelog)
- [Future Scope](#future-scope)
- [Project Status](#project-status)

## Features
- **Batch Renaming**: Rename multiple files in one go.
- **User-Friendly**: Interactive prompts guide the user through the renaming process.
- **Multi-Language Support**: Supports multiple languages including English, Spanish, Chinese, Russian, German, and French.
- **Regular Expression Support**: Advanced renaming using regular expressions.
- **Configuration File Support**: Semi-automated renaming using a configuration file.
- **Preview & Confirmation**: Preview the new filenames and confirm before proceeding.
- **Undo Feature**: Generate an undo file to revert changes.

## Tech Stack
- Python
- JSON (for localization)
- ConfigParser (for configuration file support)

## Installation
Clone the repository to your local machine:
\```bash
git clone https://github.com/your_username/Advanced-Image-Renamer.git
\```

## Usage
1. Navigate to the project directory.
2. Run the script:
    \```bash
    python imagerenamer.py
    \```
3. Follow the interactive prompts.

## Changelog
### New Features
- **Multi-Language Support**: Allows users to select their preferred language for interaction.
- **Batch Processing**: Enables renaming files across multiple folders.
- **Undo Feature**: Provides an undo mechanism to revert changes.

### Optimizations
- **Code Modularization**: Separated concerns into helper functions for better maintainability.
- **Error Handling**: Improved error handling and logging.

### UI/UX Improvements
- **User Confirmation**: Added a confirmation step before renaming.
- **File Preview**: Preview the renamed files before confirming.

## Future Scope
- Adding more advanced filters for file selection.
- Implementing automated tests for reliability.
- Extending support for more languages.

## Project Status
The project is currently fully functional and feature-rich. 
### Progress :
```
[==============100%==============]
```
