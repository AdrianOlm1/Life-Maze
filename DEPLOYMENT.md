# Deploying Life Maze to GitHub Pages

Your game has been built and is ready to deploy! Follow these steps:

## Step 1: Push to GitHub

If you haven't already pushed this repository to GitHub:

```bash
# If you don't have a remote yet
git remote add origin https://github.com/YOUR_USERNAME/Life-Maze.git

# Add and commit the GitHub Actions workflow
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Pages deployment workflow"

# Push to GitHub
git push -u origin main
```

## Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** → **Pages** (in the left sidebar)
3. Under **Source**, select **GitHub Actions**
4. The deployment will start automatically

## Step 3: Wait for Deployment

The GitHub Action will:
- Build your game with pygbag
- Deploy it to GitHub Pages
- Your game will be available at: `https://YOUR_USERNAME.github.io/Life-Maze/`

You can check the progress in the **Actions** tab of your repository.

## Step 4: Get Your Game URL

Once deployed, your game will be accessible at:
```
https://YOUR_USERNAME.github.io/Life-Maze/
```

Use this URL to embed in your React site!

## Embedding in Your React Site

Once your game is deployed, you can embed it in your React site using an iframe. See the `GameEmbed.jsx` example component.

## Local Testing

You can also test the game locally:

```bash
# The built files are in:
build/web/

# To test locally, you can run a simple HTTP server:
cd build/web
python3 -m http.server 8000

# Then visit: http://localhost:8000
```

## Troubleshooting

If the deployment fails:
1. Check the Actions tab for error messages
2. Make sure GitHub Pages is enabled in repository settings
3. Verify that the main branch has the workflow file committed
