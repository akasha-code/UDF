# Template Reference

Complete reference for all available templates in the Unified Delivery Framework.

## Overview

Templates provide pre-configured starting points for common project types and scenarios. Each template includes:

- Project structure
- Configuration files
- CI/CD pipelines
- Documentation
- Best practices

## Available Templates

### Application Templates

Templates for different application types will be added to the `/templates` directory. Each template follows a consistent structure and includes comprehensive documentation.

#### Template Structure

All templates follow this standard structure:

```
template-name/
├── README.md              # Template documentation
├── .gitignore            # Git ignore patterns
├── src/                  # Source code structure
├── tests/                # Test structure
├── config/               # Configuration templates
├── docs/                 # Additional documentation
├── scripts/              # Utility scripts
└── .github/              # CI/CD workflows
    └── workflows/
```

## Template Categories

### 1. Service Templates

**Purpose**: Microservices and backend services

**Includes**:
- RESTful API structure
- Database integration
- Authentication/Authorization
- Health checks
- Logging and monitoring

**Technologies**: Node.js, Python, Java, Go

### 2. Web Application Templates

**Purpose**: Full-stack web applications

**Includes**:
- Frontend structure
- Backend API
- Database schema
- Authentication
- Deployment configuration

**Technologies**: React, Vue, Angular, etc.

### 3. Infrastructure Templates

**Purpose**: Infrastructure as Code

**Includes**:
- Cloud resource definitions
- Kubernetes manifests
- Docker configurations
- Terraform modules

**Technologies**: Terraform, CloudFormation, Kubernetes

### 4. CI/CD Templates

**Purpose**: Continuous integration and deployment

**Includes**:
- Build pipelines
- Test automation
- Deployment workflows
- Security scanning

**Platforms**: GitHub Actions, GitLab CI, Jenkins

### 5. Documentation Templates

**Purpose**: Project documentation

**Includes**:
- README templates
- API documentation
- Architecture diagrams
- Runbooks

**Formats**: Markdown, OpenAPI, etc.

## Using Templates

### Getting Started

```bash
# Clone the repository
git clone https://github.com/akasha-code/UDF.git
cd UDF

# List available templates
ls templates/

# Copy a template
cp -r templates/[template-name] /path/to/your/project

# Follow template README
cd /path/to/your/project
cat README.md
```

### Customizing Templates

1. **Review the README**: Understand the template's purpose and structure
2. **Update configuration**: Modify `config/` files for your needs
3. **Customize code**: Adapt `src/` to your requirements
4. **Update documentation**: Modify docs to reflect your changes
5. **Configure CI/CD**: Update workflows for your environment

### Template Best Practices

**Do's ✅**:
- Read the template README thoroughly
- Start with minimal customization
- Keep template structure intact initially
- Document your changes
- Test before deploying

**Don'ts ❌**:
- Don't skip the README
- Don't remove essential files
- Don't hardcode values
- Don't skip testing
- Don't ignore security warnings

## Template Structure Details

### README.md

Every template includes a README with:

```markdown
# Template Name

## Overview
Brief description of the template

## Features
Key features and capabilities

## Prerequisites
Required tools and dependencies

## Quick Start
Step-by-step setup instructions

## Configuration
How to configure the template

## Usage
How to use the template

## Deployment
Deployment instructions

## Contributing
How to improve the template

## License
License information
```

### Configuration Files

**config/default.yml**:
```yaml
# Application configuration
app:
  name: ${APP_NAME}
  version: 1.0.0
  port: ${PORT:8080}

# Database configuration
database:
  host: ${DB_HOST}
  port: ${DB_PORT}
  name: ${DB_NAME}
```

**.env.example**:
```bash
# Environment template
APP_NAME=my-app
PORT=8080
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
```

### CI/CD Workflows

**/.github/workflows/ci.yml**:
```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup
        run: npm install
      - name: Build
        run: npm run build
      - name: Test
        run: npm test
```

### Project Scripts

**scripts/setup.sh**:
```bash
#!/bin/bash
# Setup script for new projects
echo "Setting up project..."
cp .env.example .env
npm install
npm run build
echo "Setup complete!"
```

## Template Development

### Creating New Templates

1. **Plan the template**:
   - Define purpose and scope
   - Identify target use cases
   - List required features

2. **Create structure**:
   ```bash
   mkdir -p templates/my-template/{src,tests,config,docs,scripts}
   ```

3. **Add documentation**:
   - README.md with setup instructions
   - Configuration guide
   - Usage examples

4. **Implement features**:
   - Core functionality
   - Configuration
   - Tests
   - CI/CD

5. **Test thoroughly**:
   - Fresh installation
   - Configuration options
   - All workflows

6. **Submit for review**:
   - Create pull request
   - Provide context
   - Include testing notes

### Template Contribution Guidelines

**Requirements**:
- Comprehensive README
- Working example code
- Test coverage
- CI/CD pipeline
- Documentation
- License information

**Standards**:
- Follow existing template structure
- Use environment variables for configuration
- Include security best practices
- Provide clear comments
- Use consistent naming

## Template Maintenance

### Updating Templates

Templates are regularly updated for:
- Security patches
- Dependency updates
- Best practice improvements
- Bug fixes
- New features

### Version Control

Templates follow semantic versioning:
- Major: Breaking changes
- Minor: New features
- Patch: Bug fixes

### Migration Guides

When templates change significantly, migration guides are provided in the template's `docs/` directory.

## Template Support

### Getting Help

- **Documentation**: Check template README
- **Examples**: Review example implementations
- **Issues**: Search existing issues
- **Discussions**: Ask in community discussions

### Reporting Issues

When reporting template issues:

1. Specify template name and version
2. Describe the problem clearly
3. Include error messages
4. Provide reproduction steps
5. Share environment details

## Template Index

### Current Templates

Templates are organized in `/templates/` directory. Check the directory for the latest available templates:

```bash
# List all templates
ls -la templates/

# Get template details
cat templates/[template-name]/README.md
```

### Planned Templates

Upcoming templates (contributions welcome):
- Microservice template
- Serverless function template
- Container application template
- Static site template
- API service template
- Database migration template
- Monitoring stack template

## Quick Reference

### Template Commands

```bash
# List templates
ls templates/

# Copy template
cp -r templates/[name] [destination]

# Initialize from template
cd [destination]
chmod +x scripts/setup.sh
./scripts/setup.sh

# Update template
git pull origin main
```

### Template Structure Checklist

- [ ] README.md with full documentation
- [ ] .gitignore with appropriate patterns
- [ ] src/ directory with code structure
- [ ] tests/ directory with test structure
- [ ] config/ directory with configuration
- [ ] .env.example for environment variables
- [ ] .github/workflows/ for CI/CD
- [ ] scripts/ for utility scripts
- [ ] docs/ for additional documentation
- [ ] LICENSE file

## Next Steps

- [Quick Start Guide](../getting-started/quick-start.md) - Use templates
- [Best Practices](../guides/best-practices.md) - Template best practices
- [Contributing](../../CONTRIBUTING.md) - Contribute new templates

## Additional Resources

- [Examples](../../examples/) - Template usage examples
- [GitHub Wiki](../../../wiki) - Extended template documentation
- [Template Repository](../../templates/) - Browse all templates
