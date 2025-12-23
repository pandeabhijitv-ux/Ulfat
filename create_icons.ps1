# Simple script to create placeholder icons
Add-Type -AssemblyName System.Drawing

# Create images directory
New-Item -ItemType Directory -Force -Path "images" | Out-Null

# Function to create icon
function Create-Icon {
    param($size, $filename)
    
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $graphics = [System.Drawing.Graphics]::FromImage($bmp)
    
    # Purple gradient background
    $brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
        (New-Object System.Drawing.Point(0, 0)),
        (New-Object System.Drawing.Point($size, $size)),
        [System.Drawing.Color]::FromArgb(102, 126, 234),
        [System.Drawing.Color]::FromArgb(139, 71, 137)
    )
    $graphics.FillRectangle($brush, 0, 0, $size, $size)
    
    # Add text
    $font = New-Object System.Drawing.Font("Arial", ($size/4), [System.Drawing.FontStyle]::Bold)
    $textBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $text = "उल्फत"
    $textSize = $graphics.MeasureString($text, $font)
    $x = ($size - $textSize.Width) / 2
    $y = ($size - $textSize.Height) / 2
    $graphics.DrawString($text, $font, $textBrush, $x, $y)
    
    # Save
    $bmp.Save("images\$filename", [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    $graphics.Dispose()
}

Write-Host "Creating icons..." -ForegroundColor Cyan
Create-Icon 192 "icon-192.png"
Create-Icon 512 "icon-512.png"
Write-Host "✅ Icons created successfully!" -ForegroundColor Green
Write-Host "Location: C:\Ulfat\images\" -ForegroundColor White
