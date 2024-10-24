GUIDE TO DEPLOY

# commit and push changes

# Generate static files using Pelican
pelican content -s publishconf.py

# Switch to the main branch (deployment branch)
git checkout main

# Clean old files in the main branch (optional)
git rm -rf .
git commit -m "Clean old deployment"

# Copy output files from the source branch to the main branch
git checkout source -- output
mv output/* .
rm -rf output

# Commit and push changes to GitHub
git add .
git commit -m "Deploy updated static files"
git push origin main

# Switch back to source branch for further development
git checkout source
