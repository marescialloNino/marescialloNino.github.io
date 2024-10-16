GUIDE TO DEPLOY

# Regenerate the static site with production settings
pelican content -s publishconf.py

# Deploy the generated output to the main branch of GitHub Pages
ghp-import -n -p -f output