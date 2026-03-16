$p = 'website/templates/services_landing_pages.html'
$c = Get-Content -Raw -Path $p

$pairs = @(
  @('Web Development Services','Landing Page Services'),
  @('Web Development Agency','Landing Page Agency'),
  @('Web Development Partner','Landing Page Partner'),
  @('Web Development Performance','Landing Page Performance'),
  @('Web Development Case Studies','Landing Page Case Studies'),
  @('What is Web Development?','What are Landing Pages?'),
  @('Common Website Mistakes','Common Landing Page Mistakes'),
  @('Get Free Website Audit','Get Free Landing Page Audit'),
  @('Get A Free Website Audit','Get A Free Landing Page Audit'),
  @('Get Your Free Website Audit','Get Your Free Landing Page Audit'),
  @('Web+Development+','Landing+Pages+'),
  @('Web Development','Landing Pages'),
  @('Web development','Landing pages'),
  @('Websites','Landing Pages'),
  @('Website','Landing Page'),
  @('website','landing page')
)

foreach ($pair in $pairs) {
  $c = $c.Replace($pair[0], $pair[1])
}

Set-Content -Path $p -Value $c -NoNewline
Write-Output 'done'
