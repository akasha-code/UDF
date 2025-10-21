# Installation & Setup

This guide provides detailed instructions for setting up the Unified Delivery Framework (UDF) in your environment.

## System Requirements

### Minimum Requirements

- **Operating System**: Linux, macOS, or Windows (with WSL2 recommended)
- **Git**: Version 2.20 or higher
- **Storage**: At least 100MB free space

### Recommended Tools

- Modern code editor (VS Code, IntelliJ, etc.)
- Terminal emulator with Git support
- Docker (for containerized templates)
- Cloud CLI tools (AWS CLI, Azure CLI, etc.) depending on your deployment target

## Installation Methods

### Method 1: Direct Clone (Recommended)

Clone the repository to access all templates, examples, and documentation:

```bash
# Clone the repository
git clone https://github.com/akasha-code/UDF.git

# Navigate to the directory
cd UDF

# Verify installation
ls -la
```

### Method 2: Sparse Checkout (For Specific Components)

If you only need specific parts of the repository:

```bash
# Initialize repository
git clone --no-checkout https://github.com/akasha-code/UDF.git
cd UDF

# Enable sparse checkout
git sparse-checkout init --cone

# Select specific directories
git sparse-checkout set templates examples

# Checkout the files
git checkout
```

### Method 3: Download Specific Templates

Download individual templates without cloning the entire repository:

```bash
# Using curl (replace [branch] and [template-name])
curl -L https://github.com/akasha-code/UDF/archive/refs/heads/[branch].zip -o UDF.zip
unzip UDF.zip
cd UDF-[branch]/templates/[template-name]
```

## Post-Installation Setup

### 1. Verify Installation

```bash
# Check repository structure
tree -L 2 -d

# Verify documentation is accessible
ls docs/
```

### 2. Configure Git (Optional)

Set up Git hooks or aliases for UDF workflows:

```bash
# Example: Create alias for template copying
git config --global alias.udf-template '!f() { cp -r templates/"$1" "$2"; }; f'

# Usage: git udf-template [template-name] [destination]
```

### 3. Set Up Your Development Environment

#### For Template Development

```bash
# Navigate to templates directory
cd templates

# Create your working directory
mkdir -p ~/projects/my-udf-project

# Copy a template
cp -r [template-name] ~/projects/my-udf-project
```

#### For Contributing

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/[your-username]/UDF.git
cd UDF

# Add upstream remote
git remote add upstream https://github.com/akasha-code/UDF.git

# Create feature branch
git checkout -b feature/my-contribution
```

## Environment-Specific Setup

### Linux/macOS

```bash
# Make scripts executable (if applicable)
chmod +x scripts/*.sh

# Add to PATH (optional)
echo 'export PATH=$PATH:/path/to/UDF/scripts' >> ~/.bashrc
source ~/.bashrc
```

### Windows (PowerShell)

```powershell
# Set execution policy (if needed)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Add to PATH (optional)
$env:Path += ";C:\path\to\UDF\scripts"
```

## Dependency Installation

Different templates may have specific dependencies. Check each template's README for requirements.

### Common Dependencies

```bash
# Example: Node.js project template
npm install

# Example: Python project template
pip install -r requirements.txt

# Example: Docker-based template
docker-compose up -d
```

## Verification

### Test Your Setup

```bash
# Verify you can access documentation
cat docs/getting-started/introduction.md

# Verify templates are available
ls templates/

# Verify examples are available
ls examples/
```

### Run Health Check

```bash
# Check Git configuration
git config --list | grep user

# Check repository status
git status

# Check remote URLs
git remote -v
```

## Updating UDF

Keep your local copy up to date:

```bash
# Pull latest changes
git pull origin main

# If you've made local changes
git stash
git pull origin main
git stash pop
```

## Troubleshooting Installation

### Issue: Clone Fails

```bash
# Check Git installation
git --version

# Check network connectivity
ping github.com

# Try HTTPS instead of SSH
git clone https://github.com/akasha-code/UDF.git
```

### Issue: Permission Denied

```bash
# On Linux/macOS
sudo chown -R $USER:$USER UDF/

# Check file permissions
ls -la
```

### Issue: Disk Space

```bash
# Check available space
df -h

# Clean up if needed
git gc
```

## Next Steps

After installation:

1. [Quick Start Guide](./quick-start.md) - Begin using UDF
2. [Architecture Overview](../architecture/overview.md) - Understand the framework
3. [Best Practices](../guides/best-practices.md) - Learn recommended approaches

## Additional Resources

- [GitHub Wiki](../../../wiki) - Extended setup guides
- [Troubleshooting](../guides/troubleshooting.md) - Common issues and solutions
- [Community Discussions](../../../discussions) - Get help from the community
