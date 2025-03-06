# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-03-06

### Added
- Web Operations module with WebpageLoader class
  - Support for loading single or multiple webpages
  - Metadata extraction including title, language, and meta tags
  - Clean content extraction with script and style removal
  - Configurable parser type (HTML or XML)
- YouTube transcript extraction functionality
  - Support for plain text and timestamped transcripts
  - Comprehensive error handling
- Enhanced documentation with detailed usage examples
- Type hints across all modules

### Changed
- Updated dependencies to latest stable versions
- Improved error handling and logging across modules
- Enhanced README with comprehensive documentation

### Fixed
- Various bug fixes and performance improvements

## [0.1.0] - 2025 (Initial Release)

### Added
- Logger module with:
  - Console and file output
  - Daily rotating file logs
  - Multiple logging levels
  - Automatic log directory creation
- IO Operations module with:
  - Safe file reading with UTF-8 encoding
  - File writing with directory creation
  - File appending with newline handling
  - Comprehensive error handling 