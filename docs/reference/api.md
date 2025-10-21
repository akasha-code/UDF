# API Reference

Reference documentation for APIs, interfaces, and integration points in the Unified Delivery Framework.

## Overview

This document provides technical reference for working with UDF components programmatically. As UDF is primarily a guideline and template framework, this reference focuses on common patterns and interfaces used across templates.

## Configuration API

### Loading Configuration

#### Node.js

```javascript
const config = require('config');

// Access configuration values
const port = config.get('app.port');
const dbHost = config.get('database.host');

// Check if configuration exists
if (config.has('features.newFeature')) {
  const enabled = config.get('features.newFeature');
}

// Get with default value
const timeout = config.get('api.timeout') || 30000;
```

#### Python

```python
import os
from typing import Any, Optional

class Config:
    @staticmethod
    def get(key: str, default: Optional[Any] = None) -> Any:
        """Get configuration value"""
        return os.getenv(key, default)
    
    @staticmethod
    def require(key: str) -> str:
        """Get required configuration value"""
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Required config {key} not set")
        return value

# Usage
port = Config.get('PORT', 8080)
db_host = Config.require('DB_HOST')
```

## Template Interface

### Template Structure

Templates follow a standard interface:

```typescript
interface Template {
  name: string;
  version: string;
  description: string;
  prerequisites: string[];
  configuration: Configuration;
  setup(): Promise<void>;
  validate(): Promise<boolean>;
}

interface Configuration {
  required: ConfigField[];
  optional: ConfigField[];
}

interface ConfigField {
  name: string;
  type: 'string' | 'number' | 'boolean';
  description: string;
  default?: any;
}
```

## Health Check API

### Standard Health Check Endpoints

#### Liveness Probe

**Endpoint**: `GET /health/live`

**Purpose**: Check if service is running

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Status Codes**:
- `200`: Service is alive
- `503`: Service is not responding

#### Readiness Probe

**Endpoint**: `GET /health/ready`

**Purpose**: Check if service is ready to accept traffic

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00Z",
  "checks": {
    "database": {
      "status": "ok",
      "responseTime": 15
    },
    "cache": {
      "status": "ok",
      "responseTime": 5
    }
  }
}
```

**Status Codes**:
- `200`: Service is ready
- `503`: Service is not ready

#### Health Check Implementation

**Node.js/Express**:
```javascript
app.get('/health/live', (req, res) => {
  res.status(200).json({
    status: 'ok',
    timestamp: new Date().toISOString()
  });
});

app.get('/health/ready', async (req, res) => {
  const checks = {
    database: await checkDatabase(),
    cache: await checkCache()
  };
  
  const allHealthy = Object.values(checks)
    .every(check => check.status === 'ok');
  
  res.status(allHealthy ? 200 : 503).json({
    status: allHealthy ? 'ok' : 'degraded',
    timestamp: new Date().toISOString(),
    checks
  });
});
```

## Logging API

### Structured Logging

#### Log Levels

- `debug`: Detailed debugging information
- `info`: General information
- `warn`: Warning messages
- `error`: Error messages
- `fatal`: Fatal errors

#### Log Format

```json
{
  "timestamp": "2024-01-15T10:30:00.000Z",
  "level": "info",
  "message": "User logged in",
  "context": {
    "userId": "12345",
    "ip": "192.168.1.1",
    "userAgent": "Mozilla/5.0..."
  },
  "traceId": "abc-123-def-456"
}
```

#### Implementation

**Node.js**:
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'app.log' })
  ]
});

// Usage
logger.info('User action', {
  userId: user.id,
  action: 'login',
  ip: req.ip
});
```

**Python**:
```python
import logging
import json

class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        
    def info(self, message: str, **context):
        self.logger.info(json.dumps({
            'message': message,
            'context': context
        }))

# Usage
logger = StructuredLogger(__name__)
logger.info('User action', userId=user.id, action='login')
```

## Metrics API

### Standard Metrics

#### Application Metrics

```javascript
// Request duration histogram
const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status']
});

// Request counter
const httpRequestTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status']
});

// Active connections gauge
const activeConnections = new Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});
```

#### System Metrics

```javascript
// Memory usage
const memoryUsage = new Gauge({
  name: 'memory_usage_bytes',
  help: 'Memory usage in bytes'
});

// CPU usage
const cpuUsage = new Gauge({
  name: 'cpu_usage_percent',
  help: 'CPU usage percentage'
});
```

### Metrics Endpoint

**Endpoint**: `GET /metrics`

**Format**: Prometheus format

**Example Response**:
```
# HELP http_request_duration_seconds Duration of HTTP requests
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{method="GET",route="/api/users",status="200",le="0.1"} 100
http_request_duration_seconds_bucket{method="GET",route="/api/users",status="200",le="0.5"} 150
http_request_duration_seconds_sum{method="GET",route="/api/users",status="200"} 45.5
http_request_duration_seconds_count{method="GET",route="/api/users",status="200"} 200
```

## Error Handling API

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input provided",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    },
    "traceId": "abc-123-def-456"
  }
}
```

### Standard Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid input |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Resource conflict |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |

### Error Handler Implementation

```javascript
class APIError extends Error {
  constructor(code, message, statusCode = 500, details = null) {
    super(message);
    this.code = code;
    this.statusCode = statusCode;
    this.details = details;
  }
}

// Error handling middleware
app.use((err, req, res, next) => {
  const error = {
    code: err.code || 'INTERNAL_ERROR',
    message: err.message,
    details: err.details,
    traceId: req.id
  };
  
  logger.error('Request error', {
    error,
    stack: err.stack
  });
  
  res.status(err.statusCode || 500).json({ error });
});
```

## Authentication API

### JWT Authentication

#### Token Structure

```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "user-id",
    "name": "John Doe",
    "role": "admin",
    "iat": 1516239022,
    "exp": 1516242622
  }
}
```

#### Implementation

```javascript
const jwt = require('jsonwebtoken');

// Generate token
function generateToken(user) {
  return jwt.sign(
    {
      sub: user.id,
      name: user.name,
      role: user.role
    },
    process.env.JWT_SECRET,
    { expiresIn: '1h' }
  );
}

// Verify token middleware
function authenticateToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({
      error: { code: 'UNAUTHORIZED', message: 'Token required' }
    });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(401).json({
      error: { code: 'UNAUTHORIZED', message: 'Invalid token' }
    });
  }
}
```

## Middleware API

### Standard Middleware

#### Request ID Middleware

```javascript
function requestId(req, res, next) {
  req.id = req.headers['x-request-id'] || generateId();
  res.setHeader('X-Request-ID', req.id);
  next();
}
```

#### Logging Middleware

```javascript
function requestLogger(req, res, next) {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.info('Request completed', {
      method: req.method,
      path: req.path,
      status: res.statusCode,
      duration,
      requestId: req.id
    });
  });
  
  next();
}
```

#### Rate Limiting Middleware

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: {
    error: {
      code: 'RATE_LIMITED',
      message: 'Too many requests'
    }
  }
});

app.use('/api/', limiter);
```

## Testing API

### Test Utilities

```javascript
// Test setup
async function setupTestEnvironment() {
  // Setup test database
  await setupTestDatabase();
  
  // Load test configuration
  process.env.NODE_ENV = 'test';
  
  // Clear caches
  await clearCaches();
}

// Test teardown
async function teardownTestEnvironment() {
  await cleanupTestDatabase();
  await closeConnections();
}

// Test helpers
class TestHelpers {
  static async createTestUser() {
    return await User.create({
      email: 'test@example.com',
      password: 'password123'
    });
  }
  
  static async authenticateRequest(request, user) {
    const token = generateToken(user);
    return request.set('Authorization', `Bearer ${token}`);
  }
}
```

## Integration Points

### External Service Integration

```javascript
class ExternalServiceClient {
  constructor(config) {
    this.baseURL = config.baseURL;
    this.apiKey = config.apiKey;
    this.timeout = config.timeout || 30000;
  }
  
  async request(method, path, data = null) {
    const response = await fetch(`${this.baseURL}${path}`, {
      method,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: data ? JSON.stringify(data) : undefined,
      timeout: this.timeout
    });
    
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }
    
    return await response.json();
  }
}
```

## Next Steps

- [Template Reference](./templates.md) - Template documentation
- [Glossary](./glossary.md) - Common terms
- [Examples](../../examples/) - API usage examples

## Additional Resources

- [Best Practices](../guides/best-practices.md) - API best practices
- [GitHub Wiki](../../../wiki) - Extended API documentation
