# Design Patterns

Common design patterns and solutions used within the Unified Delivery Framework.

## Overview

This document catalogs proven design patterns that solve recurring problems in software delivery. These patterns are implemented across UDF templates and examples.

## Structural Patterns

### 1. Template Pattern

**Problem**: Need consistent starting points for similar projects

**Solution**: Provide pre-configured templates with common structure and configuration

**Implementation**:
```
template/
├── README.md              # Usage instructions
├── .gitignore            # Standard ignore patterns
├── src/                  # Source structure
├── config/               # Configuration templates
└── .github/workflows/    # CI/CD pipelines
```

**Benefits**:
- Rapid project initialization
- Consistency across projects
- Embedded best practices
- Reduced setup errors

**When to Use**:
- Starting new projects
- Standardizing project structure
- Onboarding new team members

### 2. Configuration Hierarchy Pattern

**Problem**: Managing configuration across multiple environments

**Solution**: Layered configuration with clear precedence rules

**Implementation**:
```
1. Default configuration (template defaults)
2. Environment configuration (dev/staging/prod)
3. Application configuration (app-specific)
4. Runtime configuration (environment variables)
```

**Code Example**:
```yaml
# config/default.yml
app:
  name: my-app
  port: 8080

# config/production.yml
app:
  port: 443
  ssl: enabled
```

**Benefits**:
- Clear configuration precedence
- Environment-specific overrides
- Secrets separation
- Easy testing

### 3. Infrastructure as Code Pattern

**Problem**: Manual infrastructure setup is error-prone and not reproducible

**Solution**: Define infrastructure using declarative code

**Implementation**:
```
infrastructure/
├── modules/              # Reusable infrastructure modules
├── environments/         # Environment-specific configs
│   ├── dev/
│   ├── staging/
│   └── production/
└── shared/              # Shared resources
```

**Benefits**:
- Version-controlled infrastructure
- Reproducible environments
- Automated provisioning
- Documentation through code

## Behavioral Patterns

### 4. Pipeline Pattern

**Problem**: Complex delivery process with multiple stages

**Solution**: Define delivery as a series of automated stages

**Implementation**:
```
┌────────┐   ┌───────┐   ┌──────┐   ┌────────┐   ┌─────────┐
│ Build  │──>│ Test  │──>│ Scan │──>│ Deploy │──>│ Monitor │
└────────┘   └───────┘   └──────┘   └────────┘   └─────────┘
```

**Example CI/CD**:
```yaml
name: Delivery Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        run: npm run build
      - name: Test
        run: npm test
      - name: Security Scan
        run: npm audit
      - name: Deploy
        run: ./deploy.sh
```

**Benefits**:
- Automated delivery
- Consistent process
- Quality gates
- Fast feedback

### 5. Feature Toggle Pattern

**Problem**: Need to deploy incomplete features or test in production

**Solution**: Use configuration to enable/disable features at runtime

**Implementation**:
```javascript
// Feature toggle configuration
const features = {
  newDashboard: process.env.FEATURE_NEW_DASHBOARD === 'true',
  betaFeature: process.env.FEATURE_BETA === 'true'
};

// Usage in code
if (features.newDashboard) {
  return renderNewDashboard();
} else {
  return renderOldDashboard();
}
```

**Benefits**:
- Safe feature deployment
- A/B testing capability
- Quick rollback
- Progressive rollout

### 6. Health Check Pattern

**Problem**: Need to verify system health and readiness

**Solution**: Implement standardized health check endpoints

**Implementation**:
```javascript
// Health check endpoint
app.get('/health', (req, res) => {
  const health = {
    status: 'ok',
    timestamp: new Date(),
    checks: {
      database: checkDatabase(),
      cache: checkCache(),
      externalApi: checkExternalApi()
    }
  };
  
  const status = Object.values(health.checks)
    .every(check => check.status === 'ok') ? 200 : 503;
  
  res.status(status).json(health);
});
```

**Benefits**:
- Automated health monitoring
- Deployment verification
- Load balancer integration
- Debugging support

## Integration Patterns

### 7. API Gateway Pattern

**Problem**: Multiple microservices need unified access point

**Solution**: Single entry point that routes to appropriate services

**Structure**:
```
┌─────────┐
│ Client  │
└────┬────┘
     │
┌────▼──────────┐
│  API Gateway  │
└───┬───┬───┬───┘
    │   │   │
┌───▼─┐ ▼ ┌─▼───┐
│Svc A│...│Svc N│
└─────┘   └─────┘
```

**Benefits**:
- Simplified client access
- Centralized authentication
- Request routing
- Rate limiting

### 8. Service Mesh Pattern

**Problem**: Complex service-to-service communication

**Solution**: Infrastructure layer handling service communication

**Implementation**:
```
services/
├── service-a/
│   ├── deployment.yml
│   └── service.yml
├── service-b/
│   ├── deployment.yml
│   └── service.yml
└── mesh-config/
    ├── virtual-service.yml
    └── destination-rule.yml
```

**Benefits**:
- Traffic management
- Security policies
- Observability
- Resilience

## Operational Patterns

### 9. Circuit Breaker Pattern

**Problem**: Cascading failures from failed dependencies

**Solution**: Detect failures and prevent repeated attempts

**Implementation**:
```javascript
class CircuitBreaker {
  constructor(threshold, timeout) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failures = 0;
    this.state = 'CLOSED';
  }
  
  async execute(operation) {
    if (this.state === 'OPEN') {
      throw new Error('Circuit breaker is OPEN');
    }
    
    try {
      const result = await operation();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }
  
  onSuccess() {
    this.failures = 0;
    this.state = 'CLOSED';
  }
  
  onFailure() {
    this.failures++;
    if (this.failures >= this.threshold) {
      this.state = 'OPEN';
      setTimeout(() => this.state = 'HALF_OPEN', this.timeout);
    }
  }
}
```

**Benefits**:
- Prevents cascading failures
- Fast failure detection
- Automatic recovery
- System resilience

### 10. Blue-Green Deployment Pattern

**Problem**: Zero-downtime deployments with quick rollback

**Solution**: Maintain two identical environments, switching traffic between them

**Process**:
```
1. Blue (current) serves production traffic
2. Deploy new version to Green environment
3. Test Green environment
4. Switch traffic from Blue to Green
5. Keep Blue as instant rollback option
```

**Benefits**:
- Zero-downtime deployment
- Instant rollback
- Production testing
- Reduced risk

### 11. Canary Deployment Pattern

**Problem**: Need to validate new version with subset of users

**Solution**: Gradually roll out to increasing percentages of traffic

**Implementation**:
```yaml
# Traffic split configuration
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  traffic:
    - version: v1
      weight: 90
    - version: v2
      weight: 10
```

**Benefits**:
- Risk mitigation
- Real user validation
- Gradual rollout
- Easy rollback

## Observability Patterns

### 12. Structured Logging Pattern

**Problem**: Unstructured logs are hard to query and analyze

**Solution**: Use consistent, machine-readable log format

**Implementation**:
```javascript
// Structured logging
logger.info({
  event: 'user_login',
  userId: user.id,
  timestamp: new Date(),
  ip: req.ip,
  userAgent: req.headers['user-agent']
});
```

**Benefits**:
- Queryable logs
- Consistent format
- Better analytics
- Easier debugging

### 13. Distributed Tracing Pattern

**Problem**: Debugging issues across multiple services

**Solution**: Trace requests across service boundaries

**Implementation**:
```javascript
// Add trace context
const trace = {
  traceId: generateTraceId(),
  spanId: generateSpanId(),
  parentSpanId: req.headers['x-parent-span-id']
};

// Propagate trace context
await fetch(serviceB, {
  headers: {
    'x-trace-id': trace.traceId,
    'x-span-id': trace.spanId
  }
});
```

**Benefits**:
- End-to-end visibility
- Performance analysis
- Dependency mapping
- Issue diagnosis

## Pattern Selection Guide

| Scenario | Recommended Patterns |
|----------|---------------------|
| New project setup | Template, Configuration Hierarchy |
| Microservices | API Gateway, Service Mesh, Circuit Breaker |
| Deployment | Pipeline, Blue-Green, Canary |
| Configuration | Configuration Hierarchy, Feature Toggle |
| Monitoring | Health Check, Structured Logging, Distributed Tracing |
| Infrastructure | Infrastructure as Code |

## Next Steps

- [Best Practices](../guides/best-practices.md) - Apply patterns effectively
- [Examples](../../examples/) - See patterns in action
- [Template Reference](../reference/templates.md) - Templates using these patterns

## Additional Resources

- [Core Concepts](./core-concepts.md) - Foundation concepts
- [Architecture Overview](./overview.md) - Overall architecture
- [GitHub Wiki](../../../wiki) - Extended pattern library
