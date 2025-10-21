# UDF Templates

This directory contains reusable templates for various project types and scenarios within the Unified Delivery Framework.

## Overview

Templates provide pre-configured starting points that include:
- Project structure
- Configuration files
- CI/CD pipelines
- Best practices
- Documentation

## Available Templates

Templates will be added to this directory as they are developed. Each template includes:
- **README.md** - Detailed usage instructions
- **Source structure** - Pre-configured directory layout
- **Configuration templates** - Environment and application config
- **CI/CD workflows** - Automated build and deployment pipelines
- **Documentation** - Additional guides and references

## Template Categories

### Application Templates
- **Microservice**: RESTful API service template
- **Web Application**: Full-stack web application
- **Serverless Function**: Cloud function template
- **CLI Tool**: Command-line application

### Infrastructure Templates
- **Kubernetes**: K8s deployment manifests
- **Terraform**: Infrastructure as Code modules
- **Docker**: Container configurations
- **Cloud**: Provider-specific templates

### CI/CD Templates
- **GitHub Actions**: Workflow templates
- **GitLab CI**: Pipeline configurations
- **Jenkins**: Pipeline scripts

### Documentation Templates
- **Project**: Standard project documentation
- **API**: API documentation structure
- **Runbook**: Operational runbooks

## Using Templates

### Quick Start

1. **Browse available templates**:
   ```bash
   ls templates/
   ```

2. **Copy a template to your project**:
   ```bash
   cp -r templates/[template-name] /path/to/your/project
   ```

3. **Follow the template's README**:
   ```bash
   cd /path/to/your/project
   cat README.md
   ```

4. **Customize for your needs**:
   - Update configuration files
   - Modify source structure
   - Adapt CI/CD workflows
   - Update documentation

### Best Practices

- **Read the README first**: Each template includes comprehensive documentation
- **Start minimal**: Begin with the template as-is, then customize
- **Keep structure intact**: Maintain the template's organization initially
- **Document changes**: Note what you've changed from the template
- **Test thoroughly**: Verify all components work after customization

## Template Structure

All templates follow this standard structure:

```
template-name/
├── README.md              # Template documentation
├── .gitignore            # Git ignore patterns
├── src/                  # Source code structure
├── tests/                # Test structure
├── config/               # Configuration templates
│   ├── default.yml       # Default configuration
│   └── production.yml    # Production overrides
├── .env.example          # Environment variable template
├── docs/                 # Additional documentation
├── scripts/              # Utility scripts
│   └── setup.sh         # Setup script
└── .github/              # CI/CD workflows
    └── workflows/
        └── ci.yml        # CI pipeline
```

## Creating New Templates

Want to contribute a new template? Follow these steps:

1. **Plan your template**:
   - Define the use case
   - Identify required features
   - List dependencies

2. **Create the structure**:
   ```bash
   mkdir -p templates/my-template/{src,tests,config,docs,scripts}
   ```

3. **Add documentation**:
   - Comprehensive README
   - Usage examples
   - Configuration guide

4. **Implement features**:
   - Working example code
   - Tests
   - CI/CD pipeline

5. **Submit for review**:
   - Create a pull request
   - Follow [Contributing Guidelines](../CONTRIBUTING.md)

### Template Requirements

All templates must include:
- [ ] README.md with setup instructions
- [ ] Working example implementation
- [ ] Configuration templates
- [ ] .env.example file
- [ ] .gitignore file
- [ ] CI/CD pipeline
- [ ] Test structure
- [ ] Documentation

### Template Standards

- Follow existing template structure
- Use environment variables for configuration
- Include security best practices
- Provide clear comments
- Use consistent naming conventions
- Test thoroughly

## Template Contribution Guidelines

See our [Contributing Guidelines](../CONTRIBUTING.md) for detailed information on:
- Code style
- Documentation requirements
- Review process
- Testing requirements

## Getting Help

Need help with templates?

- **Documentation**: Check [Template Reference](../docs/reference/templates.md)
- **Examples**: Browse [Examples](../examples/)
- **Issues**: Search [GitHub Issues](../../issues)
- **Discussions**: Ask in [Discussions](../../discussions)
- **Wiki**: Visit the [GitHub Wiki](../../wiki)

## Template Updates

Templates are regularly updated for:
- Security patches
- Dependency updates
- Best practice improvements
- Bug fixes
- New features

To update your project with template changes:

1. Check the template's changelog
2. Review the changes
3. Apply relevant updates manually
4. Test thoroughly

## Coming Soon

Planned templates (contributions welcome):
- Node.js microservice
- Python API service
- React web application
- Kubernetes deployment
- Terraform AWS infrastructure
- GitHub Actions workflows
- API documentation template

## Additional Resources

- [Quick Start Guide](../docs/getting-started/quick-start.md)
- [Template Reference](../docs/reference/templates.md)
- [Best Practices](../docs/guides/best-practices.md)
- [Examples](../examples/)

## License

All templates are licensed under the Apache License 2.0. See [LICENSE](../LICENSE) for details.
