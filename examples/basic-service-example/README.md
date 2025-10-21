# Basic Service Example

This example demonstrates how to use the basic-service template from UDF to create a simple REST API service.

## Overview

This example shows:
- How to use the basic-service template
- Setting up configuration
- Implementing health checks
- Creating API endpoints
- Running and testing the service

## What This Example Demonstrates

- ✅ Template usage
- ✅ Environment configuration
- ✅ Health check endpoints
- ✅ Structured logging
- ✅ Error handling
- ✅ Basic API endpoint

## Prerequisites

- Node.js 18+ installed
- Git installed
- Basic understanding of REST APIs

## Getting Started

### Step 1: Use the Template

This example was created using the basic-service template:

```bash
# Copy the template
cp -r templates/basic-service my-service
cd my-service
```

### Step 2: Set Up Environment

```bash
# Copy environment template
cp .env.example .env

# Edit with your configuration
cat > .env << EOF
NODE_ENV=development
PORT=8080
LOG_LEVEL=info
API_PREFIX=/api/v1
HEALTH_CHECK_ENABLED=true
EOF
```

### Step 3: Review the Structure

```
my-service/
├── src/
│   ├── index.js          # Application entry point
│   ├── config.js         # Configuration management
│   └── routes/
│       └── health.js     # Health check endpoints
├── config/
│   └── default.yml       # Default configuration
├── .env                  # Environment variables
└── README.md             # Documentation
```

### Step 4: Run the Service

```bash
# Install dependencies (if using Node.js)
npm install express dotenv

# Start the service
node src/index.js
```

The service will start on http://localhost:8080

### Step 5: Test the Endpoints

```bash
# Test liveness endpoint
curl http://localhost:8080/health/live

# Expected response:
# {"status":"ok","timestamp":"2024-01-15T10:30:00.000Z"}

# Test readiness endpoint
curl http://localhost:8080/health/ready

# Expected response:
# {"status":"ok","timestamp":"2024-01-15T10:30:00.000Z","checks":{}}
```

## Example Implementation

### Minimal Implementation (src/index.js)

```javascript
const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

// Health check endpoints
app.get('/health/live', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString()
  });
});

app.get('/health/ready', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    checks: {}
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## Key Concepts Demonstrated

### 1. Environment-Based Configuration

The example uses environment variables for configuration:

```javascript
const PORT = process.env.PORT || 8080;
const LOG_LEVEL = process.env.LOG_LEVEL || 'info';
```

### 2. Health Check Pattern

Standard health check endpoints:
- `/health/live` - Returns 200 if service is running
- `/health/ready` - Returns 200 if service can handle requests

### 3. Structured Logging

Logging in JSON format for easy parsing:

```javascript
console.log(JSON.stringify({
  timestamp: new Date().toISOString(),
  level: 'info',
  message: 'Server started',
  port: PORT
}));
```

### 4. Error Handling

Graceful error handling:

```javascript
process.on('uncaughtException', (error) => {
  console.error('Uncaught exception:', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled rejection:', reason);
  process.exit(1);
});
```

## Next Steps

After getting the basic service running:

1. **Add Business Logic**
   - Create new route files in `src/routes/`
   - Implement your API endpoints

2. **Add Database**
   - Configure database connection
   - Add models and repositories

3. **Add Authentication**
   - Implement JWT authentication
   - Add authorization middleware

4. **Add Testing**
   - Write unit tests
   - Add integration tests

5. **Set Up CI/CD**
   - Configure GitHub Actions
   - Add deployment workflow

6. **Add Monitoring**
   - Implement metrics collection
   - Set up distributed tracing

## Extending This Example

### Adding a New Endpoint

1. Create a new route file:

```javascript
// src/routes/users.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ users: [] });
});

router.get('/:id', (req, res) => {
  res.json({ id: req.params.id, name: 'John Doe' });
});

module.exports = router;
```

2. Register the route:

```javascript
// src/index.js
const usersRouter = require('./routes/users');
app.use('/api/v1/users', usersRouter);
```

### Adding Database Connection

```javascript
// src/database.js
const { Pool } = require('pg');

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD
});

module.exports = pool;
```

### Adding Structured Logging

```javascript
// src/logger.js
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console()
  ]
});

module.exports = logger;
```

## Common Patterns

### Environment Configuration

```javascript
const config = {
  port: process.env.PORT || 8080,
  env: process.env.NODE_ENV || 'development',
  logLevel: process.env.LOG_LEVEL || 'info'
};
```

### Error Middleware

```javascript
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({
    error: {
      message: err.message,
      code: 'INTERNAL_ERROR'
    }
  });
});
```

### Request Logging

```javascript
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    console.log(JSON.stringify({
      method: req.method,
      path: req.path,
      status: res.statusCode,
      duration: Date.now() - start
    }));
  });
  next();
});
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using the port
lsof -i :8080

# Kill the process
kill -9 <PID>

# Or use a different port
PORT=8081 node src/index.js
```

### Module Not Found

```bash
# Install missing dependencies
npm install express dotenv

# Or install all dependencies
npm install
```

## Resources

- [Basic Service Template](../../templates/basic-service/)
- [Best Practices](../../docs/guides/best-practices.md)
- [Configuration Guide](../../docs/guides/configuration.md)
- [API Reference](../../docs/reference/api.md)

## Contributing

Found ways to improve this example? Contributions are welcome!

See [Contributing Guidelines](../../CONTRIBUTING.md) for details.

## License

This example is part of the UDF project and is licensed under the Apache License 2.0.
