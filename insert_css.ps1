
$content = Get-Content styles.css -Raw
$content = $content -replace '(?s)(@media \(max-width: 768px\) \{)', '$1
    .container { padding: 0 7vw; }'
Set-Content -Path styles.css -Value $content

