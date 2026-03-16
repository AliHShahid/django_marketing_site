$p='website/templates/services_social_media.html'
$c=Get-Content -Raw -Path $p
$c=$c.Replace('<title>AEO Services | ROI-Focused Answer Engine Optimization Agency</title>','<title>Social Media Marketing Services | ROI-Focused Social Media Agency</title>')
$c=$c.Replace('content="Adryze AEO services deliver ROI-focused answer engine optimization with disciplined execution, transparent reporting, and continuous growth.">','content="Adryze social media marketing services deliver ROI-focused growth with disciplined creative strategy, transparent reporting, and continuous optimization.">')
$start=$c.IndexOf('<main><!--/$-->')
$end=$c.IndexOf('</main>')
if($start -ge 0 -and $end -gt $start){
  $pre=$c.Substring(0,$start)
  $m=$c.Substring($start,$end-$start)
  $post=$c.Substring($end)
  $pairs=@(
    @('AEO Management Services','Social Media Marketing Services'),
    @('AEO Growth Agency','Social Media Growth Agency'),
    @('AEO Growth Partner','Social Media Growth Partner'),
    @('AEO Performance','Social Media Performance'),
    @('Why AEO?','Why Social Media Marketing?'),
    @('What is AEO?','What is Social Media Marketing?'),
    @('Common AEO Mistakes','Common Social Media Mistakes'),
    @('AEO Services','Social Media Services'),
    @('AEO Case Studies','Social Media Case Studies'),
    @('AEO strategy','social media strategy'),
    @('AEO specialists','social media specialists'),
    @('AEO-certified experts','social media experts'),
    @('AEO-certified','social media'),
    @('AEO tools','social media tools'),
    @('AEO budget','social media budget'),
    @('Get Free AEO Audit','Get Free Social Media Audit'),
    @('Get A Free AEO Audit','Get A Free Social Media Audit'),
    @('Get Your Free AEO Audit','Get Your Free Social Media Audit'),
    @('Ready to dominate AEO?','Ready to dominate social media?'),
    @('Ready to Scale Your AEO?','Ready to Scale Your Social Media?'),
    @('AEO+','Social+Media+'),
    @('AEO','Social Media')
  )
  foreach($pair in $pairs){
    $m=$m.Replace($pair[0],$pair[1])
  }
  $c=$pre+$m+$post
}
Set-Content -Path $p -Value $c -NoNewline
Write-Output 'done'
