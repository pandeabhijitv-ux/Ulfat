# Build Android App using Bubblewrap
# This script helps you create a Play Store ready Android app

Write-Host "🚀 Ulfat - Android App Builder" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Check if Bubblewrap is installed
Write-Host "📦 Checking for Bubblewrap CLI..." -ForegroundColor Yellow
$bubblewrap = Get-Command bubblewrap -ErrorAction SilentlyContinue

if (-not $bubblewrap) {
    Write-Host "❌ Bubblewrap not found. Installing..." -ForegroundColor Red
    Write-Host "   Run: npm install -g @bubblewrap/cli" -ForegroundColor Yellow
    Write-Host ""
    $install = Read-Host "Install Bubblewrap now? (y/n)"
    if ($install -eq 'y') {
        npm install -g @bubblewrap/cli
    } else {
        Write-Host "⚠️  Please install Bubblewrap first: npm install -g @bubblewrap/cli" -ForegroundColor Yellow
        exit
    }
}

Write-Host "✅ Bubblewrap is installed`n" -ForegroundColor Green

# Check if app is deployed online
Write-Host "🌐 DEPLOYMENT CHECK" -ForegroundColor Cyan
Write-Host "For TWA to work, your app must be hosted online.`n"

Write-Host "Options:" -ForegroundColor Yellow
Write-Host "  1. GitHub Pages (Free, Recommended)"
Write-Host "  2. Netlify (Free)"
Write-Host "  3. Vercel (Free)"
Write-Host "  4. Firebase Hosting (Free)"
Write-Host ""

$deployed = Read-Host "Is your app already deployed online? (y/n)"

if ($deployed -ne 'y') {
    Write-Host "`n📘 DEPLOYMENT GUIDE:" -ForegroundColor Cyan
    Write-Host "================================`n"
    Write-Host "QUICK DEPLOY TO GITHUB PAGES:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Create GitHub repository:"
    Write-Host "   git init"
    Write-Host "   git add ."
    Write-Host "   git commit -m 'Ulfat Shayari App'"
    Write-Host ""
    Write-Host "2. Push to GitHub:"
    Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/ulfat.git"
    Write-Host "   git push -u origin main"
    Write-Host ""
    Write-Host "3. Enable GitHub Pages in repository settings"
    Write-Host ""
    Write-Host "4. Your app URL will be: https://YOUR_USERNAME.github.io/ulfat/"
    Write-Host ""
    Write-Host "Then run this script again!`n" -ForegroundColor Green
    
    $openGuide = Read-Host "Open deployment guide? (y/n)"
    if ($openGuide -eq 'y') {
        Start-Process "PLAYSTORE_DEPLOYMENT.md"
    }
    exit
}

# Get app URL
Write-Host "`n🔗 Enter your deployed app URL:" -ForegroundColor Cyan
$appUrl = Read-Host "URL (e.g., https://username.github.io/ulfat)"

if (-not $appUrl) {
    Write-Host "❌ URL is required!" -ForegroundColor Red
    exit
}

Write-Host "`n✨ Building Android App..." -ForegroundColor Green
Write-Host "================================`n"

# Initialize Bubblewrap project
Write-Host "📱 Initializing TWA project..." -ForegroundColor Yellow

$initCommand = "bubblewrap init --manifest=$appUrl/manifest.json"
Write-Host "Running: $initCommand`n"

# Note: This is interactive, so we'll provide guidance
Write-Host "🔔 Bubblewrap will ask you questions:" -ForegroundColor Cyan
Write-Host "================================`n"
Write-Host "Suggested answers:"
Write-Host "  App Name: उल्फत - Shayari"
Write-Host "  Package Name: com.ulfat.shayari"
Write-Host "  Host: Your domain (e.g., username.github.io)"
Write-Host "  Start URL: /ulfat/index.html"
Write-Host "  Theme Color: #8B4789"
Write-Host "  Background Color: #667eea"
Write-Host "  Navigation Color: #8B4789"
Write-Host "  Display: standalone"
Write-Host "  Orientation: portrait"
Write-Host ""

$proceed = Read-Host "Ready to initialize? (y/n)"
if ($proceed -eq 'y') {
    Invoke-Expression $initCommand
    
    Write-Host "`n✅ Project initialized!" -ForegroundColor Green
    Write-Host "`n📦 Building APK/AAB..." -ForegroundColor Yellow
    
    bubblewrap build
    
    Write-Host "`n🎉 BUILD COMPLETE!" -ForegroundColor Green
    Write-Host "================================`n"
    Write-Host "Your Android app is ready in the 'app-release-bundle.aab' file!"
    Write-Host ""
    Write-Host "📤 NEXT STEPS:" -ForegroundColor Cyan
    Write-Host "  1. Go to: https://play.google.com/console"
    Write-Host "  2. Create new app"
    Write-Host "  3. Upload the .aab file"
    Write-Host "  4. Complete store listing"
    Write-Host "  5. Submit for review!"
    Write-Host ""
    Write-Host "📖 See PLAYSTORE_DEPLOYMENT.md for detailed instructions`n"
    
    $openConsole = Read-Host "Open Play Console? (y/n)"
    if ($openConsole -eq 'y') {
        Start-Process "https://play.google.com/console"
    }
}

Write-Host "`n✨ Done! Good luck with your app launch! 🚀`n" -ForegroundColor Green
