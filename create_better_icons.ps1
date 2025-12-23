# Create better app icons with heart emoji for Ulfat
Add-Type -AssemblyName System.Drawing

# Create images directory
New-Item -ItemType Directory -Force -Path "images" | Out-Null

# Function to create icon with heart emoji
function Create-BetterIcon {
    param($size, $filename)
    
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $graphics = [System.Drawing.Graphics]::FromImage($bmp)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAlias
    
    # Purple gradient background
    $brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
        (New-Object System.Drawing.Point(0, 0)),
        (New-Object System.Drawing.Point($size, $size)),
        [System.Drawing.Color]::FromArgb(139, 71, 137),
        [System.Drawing.Color]::FromArgb(102, 126, 234)
    )
    $graphics.FillRectangle($brush, 0, 0, $size, $size)
    
    # Add rounded corners effect with white circle
    $circleBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(40, 255, 255, 255))
    $graphics.FillEllipse($circleBrush, ($size * 0.1), ($size * 0.1), ($size * 0.8), ($size * 0.8))
    
    # Add large heart emoji
    $emojiFont = New-Object System.Drawing.Font("Segoe UI Emoji", ($size/2.5), [System.Drawing.FontStyle]::Regular)
    $emojiBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $emoji = "💕"
    $emojiSize = $graphics.MeasureString($emoji, $emojiFont)
    $x = ($size - $emojiSize.Width) / 2
    $y = ($size - $emojiSize.Height) / 2
    $graphics.DrawString($emoji, $emojiFont, $emojiBrush, $x, $y)
    
    # Save
    $bmp.Save("images\$filename", [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    $graphics.Dispose()
}

Write-Host "Creating better icons with heart emoji..." -ForegroundColor Cyan
Create-BetterIcon 192 "icon-192.png"
Create-BetterIcon 512 "icon-512.png"
Write-Host "✅ Better icons created successfully!" -ForegroundColor Green
Write-Host "Location: C:\Ulfat\images\" -ForegroundColor White
