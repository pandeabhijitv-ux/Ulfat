# Ulfat Deployment Script
# KITIKKA APPs ☂️

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Ulfat Play Store Deployment" -ForegroundColor Cyan
Write-Host "  KRITTIKA Apps ☂️" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check if icons exist
Write-Host "[1/5] Checking icons..." -ForegroundColor Yellow
if (!(Test-Path "images/icon-192.png") -or !(Test-Path "images/icon-512.png")) {
    Write-Host "❌ Icons not found!" -ForegroundColor Red
    Write-Host "Please create icons first:" -ForegroundColor White
    Write-Host "  1. Visit: https://www.pwabuilder.com/imageGenerator" -ForegroundColor White
    Write-Host "  2. Upload a logo and generate icons" -ForegroundColor White
    Write-Host "  3. Save as icon-192.png and icon-512.png in 'images' folder" -ForegroundColor White
    Write-Host ""
    $createFolder = Read-Host "Create 'images' folder now? (Y/N)"
    if ($createFolder -eq "Y" -or $createFolder -eq "y") {
        New-Item -ItemType Directory -Force -Path "images" | Out-Null
        Write-Host "✅ Created 'images' folder. Please add icons and run script again." -ForegroundColor Green
    }
    exit
} else {
    Write-Host "✅ Icons found!" -ForegroundColor Green
}

# Step 2: Check Git
Write-Host "`n[2/5] Checking Git status..." -ForegroundColor Yellow
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor White
    git init
    git add .
    git commit -m "Initial commit - Ulfat Shayari App by KRITTIKA Apps"
    Write-Host "✅ Git initialized and committed!" -ForegroundColor Green
} else {
    Write-Host "Git repository exists. Checking for changes..." -ForegroundColor White
    git add .
    $changes = git status --porcelain
    if ($changes) {
        git commit -m "Update Ulfat app - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        Write-Host "✅ Changes committed!" -ForegroundColor Green
    } else {
        Write-Host "✅ No new changes to commit" -ForegroundColor Green
    }
}

# Step 3: GitHub Setup
Write-Host "`n[3/5] GitHub Setup" -ForegroundColor Yellow
$hasRemote = git remote -v
if (!$hasRemote) {
    Write-Host "You need to create a GitHub repository:" -ForegroundColor White
    Write-Host "  1. Go to: https://github.com/new" -ForegroundColor Cyan
    Write-Host "  2. Repository name: ulfat" -ForegroundColor White
    Write-Host "  3. Keep it PUBLIC" -ForegroundColor White
    Write-Host "  4. DO NOT initialize with README" -ForegroundColor White
    Write-Host "  5. Click 'Create repository'" -ForegroundColor White
    Write-Host ""
    $githubUsername = Read-Host "Enter your GitHub username"
    Write-Host ""
    Write-Host "Now run these commands:" -ForegroundColor Cyan
    Write-Host "  git remote add origin https://github.com/$githubUsername/ulfat.git" -ForegroundColor White
    Write-Host "  git branch -M main" -ForegroundColor White
    Write-Host "  git push -u origin main" -ForegroundColor White
    Write-Host ""
    Write-Host "After pushing, enable GitHub Pages:" -ForegroundColor Cyan
    Write-Host "  1. Go to: https://github.com/$githubUsername/ulfat/settings/pages" -ForegroundColor White
    Write-Host "  2. Source: Deploy from branch 'main' / (root)" -ForegroundColor White
    Write-Host "  3. Save and wait 2-3 minutes" -ForegroundColor White
    Write-Host ""
    Write-Host "Your app will be live at: https://$githubUsername.github.io/ulfat/" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "✅ GitHub remote configured" -ForegroundColor Green
    $currentRemote = git remote get-url origin
    Write-Host "Remote: $currentRemote" -ForegroundColor White
    
    Write-Host "`nPush changes to GitHub? (Y/N)" -ForegroundColor Cyan
    $pushChoice = Read-Host
    if ($pushChoice -eq "Y" -or $pushChoice -eq "y") {
        git push
        Write-Host "✅ Pushed to GitHub!" -ForegroundColor Green
    }
}

# Step 4: Generate Android Package
Write-Host "`n[4/5] Generate Android Package (.aab)" -ForegroundColor Yellow
Write-Host "To create the Android app package:" -ForegroundColor White
Write-Host "  1. Go to: https://www.pwabuilder.com/" -ForegroundColor Cyan
Write-Host "  2. Enter your URL: https://YOUR_USERNAME.github.io/ulfat/" -ForegroundColor White
Write-Host "  3. Click 'Start' and wait for analysis" -ForegroundColor White
Write-Host "  4. Click 'Package for Stores' → Android" -ForegroundColor White
Write-Host "  5. Configure:" -ForegroundColor White
Write-Host "     - App name: उल्फत - शायरी और ग़ज़ल" -ForegroundColor Gray
Write-Host "     - Package ID: com.kitikkaapps.ulfat" -ForegroundColor Gray
Write-Host "  6. Click 'Generate' and download .aab file" -ForegroundColor White
Write-Host ""

# Step 5: Upload to Play Store
Write-Host "[5/5] Upload to Play Store" -ForegroundColor Yellow
Write-Host "  1. Go to: https://play.google.com/console" -ForegroundColor Cyan
Write-Host "  2. Create account (one-time $25 fee)" -ForegroundColor White
Write-Host "  3. Create new app" -ForegroundColor White
Write-Host "  4. Upload the .aab file" -ForegroundColor White
Write-Host "  5. Complete store listing (see DEPLOY_TO_PLAYSTORE.md)" -ForegroundColor White
Write-Host "  6. Submit for review" -ForegroundColor White
Write-Host ""

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "📖 Complete guide: DEPLOY_TO_PLAYSTORE.md" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Made with ❤️ by KRITTIKA Apps ☂️" -ForegroundColor Magenta
