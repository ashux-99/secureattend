# GitHub Actions Workflows

This directory contains all GitHub Actions workflows for SecureAttend, organized by category.

## Core CI/CD Workflows

- **ci.yml** - Main CI pipeline with linting, testing, and build verification
- **docker-build.yml** - Docker image building, testing, and registry push
- **release.yml** - Automated release creation with package building
- **publish-pypi.yml** - PyPI package publishing

## Security Workflows

- **codeql.yml** - CodeQL security analysis
- **security.yml** - Trivy vulnerability scanning
- **dependency-review.yml** - Dependency security review

## Quality Assurance Workflows

- **coverage.yml** - Coverage reporting and badge generation
- **performance.yml** - Performance benchmarking
- **validate-pr.yml** - PR validation (title, branch, conflicts)
- **check-commits.yml** - Commit message format checking

## Maintenance Workflows

- **stale.yml** - Stale issue/PR management
- **label.yml** - Auto-labeling for issues and PRs
- **sync-branches.yml** - Branch synchronization
- **update-dependencies.yml** - Automated dependency updates
- **backup.yml** - Repository backups
- **auto-merge.yml** - Auto-merge dependency PRs

## Documentation & Release

- **docs.yml** - Documentation building
- **changelog.yml** - Automated changelog generation
- **notify.yml** - Release notifications
- **build-package.yml** - Package building with artifacts

## Workflow Triggers

- **Push events**: Most workflows trigger on push to main/develop
- **Pull requests**: CI, security, and validation workflows
- **Scheduled**: Backup, stale management, security scans (weekly/daily)
- **Manual dispatch**: Backup, docs, build-package, docker-build, publish-pypi

## Permissions

Workflows use minimal required permissions following security best practices.
