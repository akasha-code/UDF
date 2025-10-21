# UDF Examples

This directory contains real-world examples demonstrating how to use the Unified Delivery Framework in various scenarios.

## Overview

Examples provide practical demonstrations of:
- Template usage
- Framework concepts
- Best practices implementation
- Integration patterns
- Common use cases

## Example Categories

### Basic Examples
Simple, focused demonstrations of core concepts:
- Using templates
- Configuration management
- Basic CI/CD pipeline
- Health checks
- Logging setup

### Intermediate Examples
Common real-world scenarios:
- Microservice architecture
- Database integration
- Authentication and authorization
- API development
- Container deployment

### Advanced Examples
Complex, production-ready implementations:
- Multi-service applications
- Advanced deployment strategies
- Monitoring and observability
- Security implementations
- Performance optimization

### Integration Examples
Combining multiple components:
- Full-stack applications
- Cloud platform integrations
- Third-party service integrations
- Multi-environment setups

## Example Structure

Each example follows a consistent structure:

```
example-name/
├── README.md              # Example documentation
├── src/                   # Implementation code
├── tests/                 # Test cases
├── config/                # Configuration files
├── docs/                  # Additional documentation
│   ├── setup.md          # Setup instructions
│   └── architecture.md   # Architecture overview
└── .env.example          # Environment variables
```

## Using Examples

### Getting Started

1. **Browse available examples**:
   ```bash
   ls examples/
   ```

2. **Read the example README**:
   ```bash
   cat examples/[example-name]/README.md
   ```

3. **Follow setup instructions**:
   ```bash
   cd examples/[example-name]
   cat docs/setup.md
   ```

4. **Run the example**:
   ```bash
   # Install dependencies
   npm install  # or pip install -r requirements.txt
   
   # Configure environment
   cp .env.example .env
   # Edit .env with your values
   
   # Run the example
   npm start  # or python main.py
   ```

### Learning from Examples

**For Beginners**:
1. Start with basic examples
2. Read through the code with comments
3. Try running the example locally
4. Make small modifications to understand behavior
5. Build your own variation

**For Experienced Developers**:
1. Review advanced examples
2. Study architecture decisions
3. Adapt patterns to your needs
4. Combine multiple examples
5. Contribute improvements

## Example Categories Detail

### Template Usage Examples

Demonstrating how to use various templates:
- **basic-template-usage**: Getting started with templates
- **template-customization**: Customizing templates for specific needs
- **template-migration**: Adapting existing projects to templates

### Configuration Examples

Configuration management patterns:
- **environment-config**: Managing multiple environments
- **secret-management**: Handling secrets securely
- **feature-flags**: Implementing feature toggles

### Deployment Examples

Various deployment strategies:
- **blue-green-deployment**: Zero-downtime deployments
- **canary-deployment**: Gradual rollout strategy
- **rolling-update**: Rolling update pattern

### Architecture Examples

Architectural patterns:
- **microservices**: Microservice architecture
- **api-gateway**: API gateway pattern
- **event-driven**: Event-driven architecture

### Monitoring Examples

Observability implementations:
- **structured-logging**: Structured logging setup
- **metrics-collection**: Application metrics
- **distributed-tracing**: Tracing across services

## Prerequisites

Different examples have different requirements. Common prerequisites:

- **Runtime**: Node.js, Python, Java, etc.
- **Tools**: Docker, Kubernetes, Git
- **Services**: Database, cache, message queue
- **Cloud**: AWS, Azure, GCP account (for cloud examples)

Check each example's README for specific requirements.

## Running Examples

### Local Development

Most examples can run locally:

```bash
# Clone repository
git clone https://github.com/akasha-code/UDF.git
cd UDF/examples/[example-name]

# Setup
cp .env.example .env
# Edit .env

# Install dependencies
npm install  # or equivalent

# Run
npm start
```

### Docker

Many examples include Docker support:

```bash
# Build
docker build -t example-name .

# Run
docker run -p 8080:8080 --env-file .env example-name
```

### Kubernetes

For Kubernetes examples:

```bash
# Apply manifests
kubectl apply -f k8s/

# Check status
kubectl get pods

# View logs
kubectl logs deployment/example-name
```

## Contributing Examples

We welcome example contributions! Good examples:

### Characteristics of Good Examples

- **Clear purpose**: Solves a specific problem
- **Well-documented**: Comprehensive README and comments
- **Working code**: Fully functional implementation
- **Tested**: Includes tests
- **Realistic**: Based on real-world scenarios
- **Minimal**: Focused on demonstrating concept

### Contribution Process

1. **Create the example**:
   ```bash
   mkdir -p examples/my-example/{src,tests,config,docs}
   ```

2. **Add documentation**:
   - README.md with overview and usage
   - Setup instructions in docs/setup.md
   - Architecture explanation in docs/architecture.md

3. **Implement working code**:
   - Clean, commented code
   - Error handling
   - Best practices

4. **Add tests**:
   - Unit tests
   - Integration tests if applicable

5. **Create .env.example**:
   - Document all environment variables
   - Provide example values

6. **Submit pull request**:
   - Follow [Contributing Guidelines](../CONTRIBUTING.md)
   - Explain the example's value
   - Include testing notes

### Example Requirements

All examples must include:
- [ ] README.md with clear documentation
- [ ] Working, tested code
- [ ] Setup instructions
- [ ] .env.example file
- [ ] Comments explaining key concepts
- [ ] Dependencies documented
- [ ] License information

## Getting Help

Need help with examples?

- **Documentation**: Check [documentation](../docs/)
- **Issues**: Search [GitHub Issues](../../issues)
- **Discussions**: Ask in [Discussions](../../discussions)
- **Wiki**: Visit the [GitHub Wiki](../../wiki)

## Example Index

Examples will be added here as they are developed. Check this directory for the latest:

```bash
# List all examples
ls -la examples/

# Get example details
cat examples/[example-name]/README.md
```

## Coming Soon

Planned examples (contributions welcome):
- REST API with authentication
- GraphQL service
- Event-driven microservices
- Serverless application
- Container orchestration
- CI/CD pipeline implementation
- Monitoring stack setup
- Multi-cloud deployment

## Best Practices

When using examples:

**Do's ✅**:
- Read the entire README first
- Check prerequisites
- Review the code before running
- Test in isolated environment
- Understand before adapting
- Keep examples updated

**Don'ts ❌**:
- Don't run unknown code in production
- Don't skip setup instructions
- Don't commit example secrets
- Don't modify example without understanding
- Don't ignore security warnings

## Troubleshooting

Common issues:

### Dependencies

```bash
# Clear and reinstall
rm -rf node_modules
npm install
```

### Configuration

```bash
# Verify environment variables
cat .env

# Check configuration loading
node -e "require('dotenv').config(); console.log(process.env)"
```

### Permissions

```bash
# Make scripts executable
chmod +x scripts/*.sh
```

See [Troubleshooting Guide](../docs/guides/troubleshooting.md) for more help.

## Additional Resources

- [Quick Start Guide](../docs/getting-started/quick-start.md)
- [Templates](../templates/)
- [Best Practices](../docs/guides/best-practices.md)
- [GitHub Wiki](../../wiki)

## License

All examples are licensed under the Apache License 2.0. See [LICENSE](../LICENSE) for details.
