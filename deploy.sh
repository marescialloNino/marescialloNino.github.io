#!/bin/bash

# Exit on any error
set -e

# Generate static files
pelican content -s publishconf.py

# Commit and push changes in source branch
git add .
git commit -m "Update content before deployment"
git push origin source

# Switch to main branch
git checkout main

# Clean old files
git rm -rf .
git commit -m "Clean old deployment"

# Copy output files from source branch
git checkout source -- output
mv output/* .
rm -rf output

# Commit and push changes
git add .
git commit -m "Deploy updated static files"
git push origin main

# Switch back to source branch
git checkout source

echo "Deployment completed successfully!"