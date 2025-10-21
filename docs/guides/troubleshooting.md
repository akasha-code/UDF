# Troubleshooting Guide

Common issues and their solutions when working with the Unified Delivery Framework.

## Getting Started Issues

### Cannot Clone Repository

**Problem**: Git clone fails with authentication error

**Solution**:
```bash
# Check Git version
git --version

# Use HTTPS instead of SSH
git clone https://github.com/akasha-code/UDF.git

# Or set up SSH keys
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Add key to GitHub account
```

### Template Not Found

**Problem**: Cannot find expected template in repository

**Solution**:
```bash
# List available templates
ls templates/

# Pull latest changes
git pull origin main

# Check if in correct branch
git branch

# Verify repository structure
tree -L 2
```

## Configuration Issues

### Environment Variables Not Loading

**Problem**: Application not reading environment variables

**Symptoms**:
- Undefined configuration values
- Default values always used
- Connection failures

**Solution**:

1. **Verify .env file exists**:
```bash
ls -la .env
```

2. **Check file format**:
```bash
# Correct format
DB_HOST=localhost
DB_PORT=5432

# Incorrect (no spaces around =)
DB_HOST = localhost
```

3. **Load dotenv early**:
```javascript
// Must be at the very top of your entry file
require('dotenv').config();
```

4. **Check environment**:
```bash
node -e "require('dotenv').config(); console.log(process.env.DB_HOST)"
```

### Wrong Configuration Loaded

**Problem**: Application using incorrect environment configuration

**Solution**:
```bash
# Check NODE_ENV
echo $NODE_ENV

# Set correct environment
export NODE_ENV=development

# Verify configuration files exist
ls config/

# Test configuration loading
node -e "console.log(require('./config'))"
```

### Configuration Validation Errors

**Problem**: Configuration fails validation at startup

**Solution**:

1. **Check error message**:
```bash
# Look for validation details
npm start 2>&1 | grep -i "validation"
```

2. **Validate schema**:
```javascript
// Add detailed logging
const config = require('./config');
console.log('Loaded configuration:', JSON.stringify(config, null, 2));
```

3. **Check required fields**:
```bash
# Verify all required environment variables
cat .env.example
cat .env
```

## Build Issues

### Build Fails

**Problem**: Build process fails with errors

**Common Causes**:

1. **Missing dependencies**:
```bash
# Install dependencies
npm install
# or
pip install -r requirements.txt
```

2. **Outdated dependencies**:
```bash
# Update dependencies
npm update
# or
pip install --upgrade -r requirements.txt
```

3. **Node version mismatch**:
```bash
# Check Node version
node --version

# Use nvm to switch versions
nvm use 18
```

4. **Build cache issues**:
```bash
# Clear build cache
npm run clean
npm cache clean --force
```

### Linting Errors

**Problem**: Code fails linting checks

**Solution**:
```bash
# Check linting rules
cat .eslintrc.json

# Run linter with fix
npm run lint -- --fix
# or
eslint --fix src/

# Check specific file
eslint src/myfile.js
```

## Testing Issues

### Tests Failing

**Problem**: Tests fail unexpectedly

**Diagnosis Steps**:

1. **Run tests with verbose output**:
```bash
npm test -- --verbose
```

2. **Run specific test**:
```bash
npm test -- tests/specific-test.js
```

3. **Check test environment**:
```bash
# Ensure test database exists
echo $TEST_DB_NAME

# Reset test database
npm run test:db:reset
```

### Test Coverage Issues

**Problem**: Coverage below threshold

**Solution**:
```bash
# Generate coverage report
npm run test:coverage

# View detailed report
open coverage/lcov-report/index.html

# Identify untested code
npm run test:coverage -- --coverage-thresholds
```

## Deployment Issues

### Deployment Fails

**Problem**: Deployment to environment fails

**Check**:

1. **Verify credentials**:
```bash
# AWS
aws sts get-caller-identity

# Azure
az account show

# GCP
gcloud auth list
```

2. **Check deployment logs**:
```bash
# View CI/CD logs
# GitHub Actions
gh run view <run-id> --log

# Local deployment
./deploy.sh 2>&1 | tee deploy.log
```

3. **Verify environment**:
```bash
# Check target environment exists
kubectl get namespaces
# or
aws eks list-clusters
```

### Service Not Starting

**Problem**: Deployed service fails to start

**Solution**:

1. **Check logs**:
```bash
# Kubernetes
kubectl logs deployment/my-app

# Docker
docker logs container-name

# System logs
journalctl -u my-service -n 50
```

2. **Verify health checks**:
```bash
# Check health endpoint
curl http://localhost:8080/health

# Check readiness
curl http://localhost:8080/health/ready
```

3. **Check resource limits**:
```bash
# Kubernetes
kubectl describe pod my-app

# Docker
docker stats container-name
```

## Database Issues

### Cannot Connect to Database

**Problem**: Application cannot connect to database

**Solution**:

1. **Verify database is running**:
```bash
# PostgreSQL
pg_isready -h localhost -p 5432

# MySQL
mysqladmin ping -h localhost

# MongoDB
mongosh --eval "db.adminCommand('ping')"
```

2. **Check connection string**:
```bash
# Print (without password)
echo "Host: $DB_HOST, Port: $DB_PORT, DB: $DB_NAME"

# Test connection
psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME
```

3. **Verify network access**:
```bash
# Test connectivity
telnet $DB_HOST $DB_PORT
# or
nc -zv $DB_HOST $DB_PORT
```

### Migration Failures

**Problem**: Database migrations fail

**Solution**:
```bash
# Check migration status
npm run migrate:status

# Rollback last migration
npm run migrate:rollback

# Run migrations with verbose output
npm run migrate -- --verbose

# Check migration files
ls migrations/
```

## Performance Issues

### Slow Response Times

**Problem**: Application responding slowly

**Diagnosis**:

1. **Check logs for slow queries**:
```bash
grep "slow query" logs/app.log
```

2. **Profile application**:
```bash
# Node.js
node --prof app.js
node --prof-process isolate-*.log > processed.txt
```

3. **Check resource usage**:
```bash
# CPU and memory
top -p $(pgrep -f "node app.js")

# Network
netstat -an | grep ESTABLISHED | wc -l
```

**Solutions**:
- Add database indexes
- Implement caching
- Optimize queries
- Scale horizontally

### Memory Leaks

**Problem**: Memory usage continuously increasing

**Diagnosis**:
```bash
# Monitor memory over time
watch -n 1 'ps aux | grep node'

# Heap snapshot (Node.js)
node --inspect app.js
# Use Chrome DevTools Memory profiler
```

**Solutions**:
- Close connections properly
- Clear event listeners
- Review cache implementations
- Use memory profiling tools

## Security Issues

### Security Scan Failures

**Problem**: Security vulnerabilities detected

**Solution**:
```bash
# Check vulnerabilities
npm audit

# Fix automatically
npm audit fix

# Force fix (may break compatibility)
npm audit fix --force

# Review specific vulnerability
npm audit --json | jq '.vulnerabilities'
```

### Secrets Exposed

**Problem**: Secrets accidentally committed

**Immediate Action**:
```bash
# Rotate compromised secrets immediately
# Remove from Git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (use with caution)
git push --force --all
```

## CI/CD Issues

### Pipeline Failing

**Problem**: CI/CD pipeline fails

**Solution**:

1. **Check pipeline logs**:
```bash
# GitHub Actions
gh run view --log

# View specific job
gh run view <run-id> --job <job-id> --log
```

2. **Reproduce locally**:
```bash
# Run same commands locally
npm install
npm run build
npm test
```

3. **Check environment secrets**:
- Verify all required secrets are set
- Check secret names match configuration
- Ensure secrets have correct values

### Cache Issues

**Problem**: CI/CD cache causing build issues

**Solution**:
```bash
# Clear cache in GitHub Actions
# Go to Actions -> Caches -> Delete cache

# Force fresh install
npm ci --cache .npm --prefer-offline
```

## Network Issues

### API Timeouts

**Problem**: External API calls timing out

**Solution**:

1. **Test connectivity**:
```bash
curl -v https://api.example.com/health
```

2. **Check timeout configuration**:
```javascript
// Increase timeout
axios.get(url, { timeout: 30000 })
```

3. **Implement retry logic**:
```javascript
const retry = require('axios-retry');
retry(axios, { retries: 3 });
```

### CORS Errors

**Problem**: Browser blocking API requests

**Solution**:
```javascript
// Enable CORS in Express
const cors = require('cors');
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS,
  credentials: true
}));
```

## Getting Help

### Debug Mode

Enable debug mode for detailed logging:

```bash
# Node.js
DEBUG=* npm start

# Application-specific
LOG_LEVEL=debug npm start
```

### Collect Information

When reporting issues, include:

1. **Environment information**:
```bash
node --version
npm --version
git --version
echo $NODE_ENV
```

2. **Error messages**:
```bash
# Full error stack trace
npm start 2>&1 | tee error.log
```

3. **Configuration** (sanitized):
```bash
# Remove secrets before sharing
cat config/default.yml
```

### Resources

- [GitHub Issues](../../../issues) - Report bugs
- [Discussions](../../../discussions) - Ask questions
- [Wiki](../../../wiki) - Extended troubleshooting
- [Best Practices](./best-practices.md) - Prevent issues

## Troubleshooting Checklist

When encountering issues:

- [ ] Check error messages carefully
- [ ] Verify environment variables
- [ ] Confirm correct environment (dev/staging/prod)
- [ ] Check dependencies are installed
- [ ] Review recent changes
- [ ] Check logs for details
- [ ] Verify network connectivity
- [ ] Test with minimal configuration
- [ ] Search existing issues
- [ ] Enable debug logging
- [ ] Try to reproduce locally
- [ ] Document findings

## Prevention

### Best Practices

- Regular dependency updates
- Comprehensive testing
- Monitoring and alerting
- Documentation maintenance
- Code reviews
- Security scanning
- Performance testing

### Health Checks

Regularly verify:
```bash
# Run all checks
npm run check:all

# Individual checks
npm run lint
npm run test
npm run build
npm audit
```

## Next Steps

- [Best Practices](./best-practices.md) - Avoid common pitfalls
- [Configuration Guide](./configuration.md) - Proper configuration
- [GitHub Wiki](../../../wiki) - Extended troubleshooting guides
