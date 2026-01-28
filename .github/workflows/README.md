# GitHub Actions Workflows

This directory contains all GitHub Actions workflows for SecureAttend.

## Workflows

### CI/CD Workflows
- **ci.yml** - Main CI pipeline with testing and linting
- **test.yml** - Comprehensive cross-platform testing
- **lint.yml** - Code quality checks with multiple linters
- **docker.yml** - Docker image building and testing
- **docker-build.yml** - Docker build and push to registry
- **build-package.yml** - Python package building

### Release Workflows
- **release.yml** - Automated release creation with package building
- **publish-pypi.yml** - PyPI package publishing
- **notify.yml** - Release notifications

### Security Workflows
- **codeql.yml** - CodeQL security analysis
- **security.yml** - Trivy vulnerability scanning
- **dependency-review.yml** - Dependency security review

### Maintenance Workflows
- **stale.yml** - Stale issue/PR management
- **label.yml** - Auto-labeling for issues and PRs
- **sync-branches.yml** - Branch synchronization
- **update-dependencies.yml** - Automated dependency updates
- **backup.yml** - Repository backups

### Quality Assurance Workflows
- **coverage.yml** - Coverage reporting
- **performance.yml** - Performance benchmarking
- **validate-pr.yml** - PR validation
- **check-commits.yml** - Commit message format checking
- **changelog.yml** - Automated changelog generation
- **docs.yml** - Documentation building
- **matrix-test.yml** - Matrix testing across platforms

## Workflow Triggers

Most workflows trigger on:
- Push to main/develop branches
- Pull requests
- Scheduled runs (cron)
- Manual dispatch (workflow_dispatch)

## Permissions

Workflows use minimal required permissions following security best practices.
