# Basic Service Template

A minimal template for creating a basic microservice using the Unified Delivery Framework.

## Overview

This template provides a starting point for building a simple microservice with:
- Health check endpoints
- Structured logging
- Configuration management
- CI/CD pipeline
- Docker support

## Features

- ✅ RESTful API structure
- ✅ Health check endpoints (liveness and readiness)
- ✅ Environment-based configuration
- ✅ Structured logging
- ✅ Error handling
- ✅ Docker containerization
- ✅ CI/CD pipeline (GitHub Actions)
- ✅ Testing structure

## Prerequisites

- Node.js 18+ (or Python 3.8+, depending on your choice)
- Docker (optional, for containerization)
- Git

## Quick Start

### 1. Copy the Template

```bash
cp -r templates/basic-service /path/to/your/project
cd /path/to/your/project
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit with your values
vim .env
```

### 3. Install Dependencies

```bash
# For Node.js
npm install

# For Python
pip install -r requirements.txt
```

### 4. Run Locally

```bash
# For Node.js
npm start

# For Python
python src/main.py
```

### 5. Test

```bash
# Run tests
npm test  # or pytest
```

## Project Structure

```
basic-service/
├── README.md              # This file
├── .gitignore            # Git ignore patterns
├── .env.example          # Environment variable template
├── Dockerfile            # Container definition
├── package.json          # Node.js dependencies (or requirements.txt)
├── src/                  # Source code
│   ├── index.js         # Entry point
│   ├── config.js        # Configuration loader
│   ├── logger.js        # Logging setup
│   └── routes/          # API routes
│       ├── health.js    # Health check endpoints
│       └── api.js       # API endpoints
├── tests/                # Test files
│   └── health.test.js   # Health check tests
├── config/               # Configuration files
│   ├── default.yml      # Default configuration
│   └── production.yml   # Production overrides
├── docs/                 # Documentation
│   └── api.md           # API documentation
├── scripts/              # Utility scripts
│   └── setup.sh         # Setup script
└── .github/              # GitHub Actions
    └── workflows/
        └── ci.yml       # CI/CD pipeline
```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Application
NODE_ENV=development
PORT=8080
LOG_LEVEL=info

# API
API_PREFIX=/api/v1

# Health Check
HEALTH_CHECK_ENABLED=true
```

### Configuration Files

- `config/default.yml` - Default configuration for all environments
- `config/production.yml` - Production-specific overrides

## API Endpoints

### Health Checks

- `GET /health/live` - Liveness probe
- `GET /health/ready` - Readiness probe

### API Endpoints

- `GET /api/v1/status` - Service status
- Add your endpoints here...

## Development

### Running in Development Mode

```bash
npm run dev  # Runs with hot-reload
```

### Running Tests

```bash
npm test              # Run all tests
npm run test:watch    # Run tests in watch mode
npm run test:coverage # Run tests with coverage
```

### Linting

```bash
npm run lint         # Check code style
npm run lint:fix     # Fix code style issues
```

## Docker

### Build Image

```bash
docker build -t basic-service .
```

### Run Container

```bash
docker run -p 8080:8080 --env-file .env basic-service
```

### Using Docker Compose

```bash
docker-compose up
```

## Deployment

### Manual Deployment

1. Build the application
2. Set environment variables
3. Start the service
4. Verify health checks

### CI/CD

The template includes a GitHub Actions workflow that:
- Runs tests on push/PR
- Builds Docker image
- Deploys to staging (configure as needed)

See `.github/workflows/ci.yml` for details.

## Testing

### Unit Tests

```bash
npm test
```

### Integration Tests

```bash
npm run test:integration
```

### End-to-End Tests

```bash
npm run test:e2e
```

## Monitoring

### Health Checks

The service exposes health check endpoints:

```bash
# Check if service is alive
curl http://localhost:8080/health/live

# Check if service is ready
curl http://localhost:8080/health/ready
```

### Logs

Logs are output in JSON format for easy parsing:

```json
{
  "timestamp": "2024-01-15T10:30:00.000Z",
  "level": "info",
  "message": "Server started",
  "context": {
    "port": 8080
  }
}
```

## Customization

### Adding New Endpoints

1. Create route file in `src/routes/`
2. Implement endpoint logic
3. Register route in `src/index.js`
4. Add tests in `tests/`

### Modifying Configuration

1. Update `config/default.yml` for new settings
2. Add to `.env.example` if environment-specific
3. Update README with new variables

### Changing Port or Prefix

Edit `.env` file:
```bash
PORT=3000
API_PREFIX=/api/v2
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port
lsof -ti:8080 | xargs kill -9

# Or use different port
PORT=8081 npm start
```

### Dependencies Not Installing

```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules
npm install
```

### Tests Failing

```bash
# Run with verbose output
npm test -- --verbose

# Run specific test
npm test -- tests/health.test.js
```

## Next Steps

- Add your business logic in `src/`
- Implement additional API endpoints
- Configure database connection
- Add authentication/authorization
- Set up monitoring and logging
- Configure production deployment

## Resources

- [UDF Documentation](../../docs/)
- [Best Practices](../../docs/guides/best-practices.md)
- [Configuration Guide](../../docs/guides/configuration.md)
- [Examples](../../examples/)

## Contributing

Improvements to this template are welcome! See [Contributing Guidelines](../../CONTRIBUTING.md).

## License

This template is part of the UDF project and is licensed under the Apache License 2.0.
