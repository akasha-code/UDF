# Configuration Guide

Comprehensive guide to configuring projects within the Unified Delivery Framework.

## Overview

UDF uses a hierarchical configuration approach that supports multiple environments while maintaining security and flexibility.

## Configuration Hierarchy

Configuration is applied in the following order (later overrides earlier):

```
1. Default values (in code)
2. Configuration files (config/*.yml)
3. Environment-specific files (config/env/*.yml)
4. Environment variables
5. Command-line arguments
```

## Configuration Structure

### Directory Layout

```
project-root/
├── config/
│   ├── default.yml          # Default configuration
│   ├── development.yml      # Development overrides
│   ├── staging.yml         # Staging overrides
│   ├── production.yml      # Production overrides
│   └── custom/             # Custom configurations
├── .env.example            # Environment variable template
└── .env                    # Local environment variables (not committed)
```

## Configuration Files

### Default Configuration

**Purpose**: Base configuration that applies to all environments

**File**: `config/default.yml`

```yaml
# Application Configuration
app:
  name: my-application
  version: 1.0.0
  port: 8080
  logLevel: info

# Database Configuration
database:
  host: localhost
  port: 5432
  name: myapp
  poolSize: 10
  timeout: 5000

# API Configuration
api:
  rateLimit:
    windowMs: 900000
    max: 100
  timeout: 30000

# Features
features:
  newDashboard: false
  betaFeatures: false
```

### Environment-Specific Configuration

**Purpose**: Override defaults for specific environments

**Development** (`config/development.yml`):
```yaml
app:
  logLevel: debug
  
database:
  name: myapp_dev
  
features:
  betaFeatures: true
```

**Production** (`config/production.yml`):
```yaml
app:
  port: 443
  logLevel: warn
  
database:
  poolSize: 50
  ssl: true
  
api:
  rateLimit:
    windowMs: 900000
    max: 1000
```

## Environment Variables

### Using Environment Variables

**Purpose**: Store sensitive data and environment-specific settings

**File**: `.env` (not committed to version control)

```bash
# Environment
NODE_ENV=development

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
DB_USER=dbuser
DB_PASSWORD=secret_password

# API Keys
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
JWT_SECRET=jwt_secret_here

# External Services
REDIS_URL=redis://localhost:6379
SENTRY_DSN=https://key@sentry.io/project

# Feature Flags
FEATURE_NEW_DASHBOARD=false
FEATURE_BETA=false
```

### Environment Variable Template

**File**: `.env.example` (committed to version control)

```bash
# Environment
NODE_ENV=development

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# API Keys (obtain from appropriate sources)
API_KEY=your_api_key
SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret

# External Services
REDIS_URL=redis://localhost:6379
SENTRY_DSN=your_sentry_dsn

# Feature Flags
FEATURE_NEW_DASHBOARD=false
FEATURE_BETA=false
```

### Loading Environment Variables

**JavaScript/Node.js:**
```javascript
require('dotenv').config();

const config = {
  database: {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    name: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD
  }
};
```

**Python:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'database': {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'name': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }
}
```

## Secret Management

### Best Practices

1. **Never commit secrets to version control**
2. **Use secret management services**
3. **Rotate secrets regularly**
4. **Apply least privilege**
5. **Audit secret access**

### Secret Management Tools

#### AWS Secrets Manager

```javascript
const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

async function getSecret(secretName) {
  const data = await secretsManager.getSecretValue({
    SecretId: secretName
  }).promise();
  
  return JSON.parse(data.SecretString);
}
```

#### HashiCorp Vault

```javascript
const vault = require('node-vault')({
  endpoint: 'http://127.0.0.1:8200',
  token: process.env.VAULT_TOKEN
});

async function getSecret(path) {
  const result = await vault.read(path);
  return result.data;
}
```

#### Kubernetes Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  database-password: <base64-encoded-password>
  api-key: <base64-encoded-key>
```

## Configuration by Component

### Database Configuration

```yaml
# Connection settings
database:
  host: ${DB_HOST}
  port: ${DB_PORT}
  name: ${DB_NAME}
  user: ${DB_USER}
  password: ${DB_PASSWORD}
  
  # Connection pool
  pool:
    min: 2
    max: 10
    acquireTimeout: 30000
    idleTimeout: 10000
  
  # SSL/TLS
  ssl:
    enabled: true
    rejectUnauthorized: true
    
  # Performance
  logging: false
  benchmark: false
```

### Logging Configuration

```yaml
logging:
  level: info
  format: json
  
  # Console output
  console:
    enabled: true
    colorize: true
  
  # File output
  file:
    enabled: true
    path: logs/app.log
    maxSize: 10485760  # 10MB
    maxFiles: 5
  
  # Remote logging
  remote:
    enabled: true
    service: sentry
    dsn: ${SENTRY_DSN}
```

### API Configuration

```yaml
api:
  # Server settings
  host: 0.0.0.0
  port: ${PORT}
  
  # Rate limiting
  rateLimit:
    windowMs: 900000  # 15 minutes
    max: 100
    message: "Too many requests"
  
  # CORS
  cors:
    origin: "*"
    methods: ["GET", "POST", "PUT", "DELETE"]
    credentials: true
  
  # Request timeouts
  timeout: 30000
  
  # Body parsing
  bodyParser:
    json:
      limit: "1mb"
    urlencoded:
      limit: "1mb"
      extended: true
```

### Cache Configuration

```yaml
cache:
  # Redis configuration
  redis:
    host: ${REDIS_HOST}
    port: ${REDIS_PORT}
    password: ${REDIS_PASSWORD}
    db: 0
    
  # Cache settings
  ttl: 3600  # 1 hour
  prefix: "app:"
  
  # Clustering
  cluster:
    enabled: false
    nodes:
      - host: redis-1
        port: 6379
      - host: redis-2
        port: 6379
```

## Feature Flags

### Configuration

```yaml
features:
  # New features
  newDashboard: ${FEATURE_NEW_DASHBOARD:false}
  betaApi: ${FEATURE_BETA_API:false}
  
  # A/B testing
  experimentalSearch: ${FEATURE_EXP_SEARCH:false}
  
  # Rollout percentages
  newCheckout:
    enabled: true
    percentage: 50
```

### Usage

```javascript
const features = require('./config/features');

function renderDashboard(req, res) {
  if (features.newDashboard) {
    return res.render('dashboard-v2');
  }
  return res.render('dashboard-v1');
}
```

## Multi-Environment Setup

### Development Environment

```yaml
# config/development.yml
app:
  logLevel: debug
  
database:
  name: myapp_dev
  logging: true
  
features:
  betaFeatures: true
  
api:
  cors:
    origin: "http://localhost:3000"
```

### Staging Environment

```yaml
# config/staging.yml
app:
  logLevel: info
  
database:
  name: myapp_staging
  pool:
    max: 20
  ssl:
    enabled: true
    
features:
  betaFeatures: true
  newDashboard: true
```

### Production Environment

```yaml
# config/production.yml
app:
  logLevel: warn
  
database:
  name: myapp_prod
  pool:
    min: 5
    max: 50
  ssl:
    enabled: true
    rejectUnauthorized: true
    
features:
  betaFeatures: false
  
api:
  rateLimit:
    max: 1000
```

## Configuration Validation

### Schema Validation

```javascript
const Joi = require('joi');

const configSchema = Joi.object({
  app: Joi.object({
    name: Joi.string().required(),
    port: Joi.number().port().required(),
    logLevel: Joi.string().valid('debug', 'info', 'warn', 'error')
  }),
  database: Joi.object({
    host: Joi.string().required(),
    port: Joi.number().port().required(),
    name: Joi.string().required()
  })
});

const { error } = configSchema.validate(config);
if (error) {
  throw new Error(`Configuration validation error: ${error.message}`);
}
```

## Best Practices

### Do's ✅

- Use environment variables for secrets
- Version control configuration files
- Document all configuration options
- Validate configuration at startup
- Use sensible defaults
- Keep production config minimal
- Use feature flags for gradual rollouts

### Don'ts ❌

- Don't commit secrets
- Don't hardcode configuration
- Don't use production config in development
- Don't ignore configuration errors
- Don't over-configure
- Don't use weak default values

## Troubleshooting Configuration

### Common Issues

**Issue**: Configuration not loading
```bash
# Check environment variable
echo $NODE_ENV

# Verify config file exists
ls config/${NODE_ENV}.yml

# Test configuration loading
node -e "console.log(require('./config'))"
```

**Issue**: Environment variables not working
```bash
# Verify .env file
cat .env

# Check if dotenv is loaded
node -e "require('dotenv').config(); console.log(process.env.DB_HOST)"
```

**Issue**: Wrong configuration applied
```bash
# Check which environment is active
echo $NODE_ENV

# Verify configuration hierarchy
node -e "const config = require('config'); console.log(config.util.getConfigSources())"
```

## Next Steps

- [Best Practices](./best-practices.md) - Configuration best practices
- [Troubleshooting](./troubleshooting.md) - Solve configuration issues
- [Examples](../../examples/) - Configuration examples

## Additional Resources

- [Template Reference](../reference/templates.md) - Template configurations
- [GitHub Wiki](../../../wiki) - Extended configuration guides
