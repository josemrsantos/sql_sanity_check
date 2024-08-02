# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added a new output class that outputs to Slack.

### Changed

- Changed code so that the Slack output class can be used.

### Fixed

- Nothing yet

## [0.2.0] - 2024-08-02

### Added

- New connector class for PostgreSQL databases with the name `PostgreSQLConnector`. Also added unit tests for this class, updated the documentation, a few SQL tests and a Python script that serves as an implementation example.

### Changed

- Changed the name of the connector class for sqlite from `SQLite` to `SQLiteConnector`.

### Fixed

- A typo in the Deployment instructions.

## [0.1.0] - 2024-07-11

### Added

- This Changelog file
- Deployment instructions

### Changed

- Refactored the main module sanity_checks to have the default output class, in a different file.
- Improved documentation


## [0.0.1] - 2024-07-10

### Added

- First version of this library in github and as a PyPI package.
