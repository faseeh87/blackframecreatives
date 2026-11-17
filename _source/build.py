# Builds the preview page (blackfilms-site.html, for the claude.ai artifact) and the live site (site/index.html for Vercel) from src.html.
import shutil,os
D='/mnt/project-files/blackfilms/'
SITE='https://www.bfcreatives.com'
FORM='https://formsubmit.co/ajax/mohammed.zia@bfcreatives.com'
s=open(D+'src.html').read().replace('{{LOGO_LIGHT}}','assets/logo-light.png').replace('{{LOGO_RED}}','assets/logo-red.png')
open(D+'blackfilms-site.html','w').write(s.replace('{{FORM_ENDPOINT}}',''))
web=s.replace('{{FORM_ENDPOINT}}',FORM)
web=web.replace('<title>Black Frame Creatives</title>','<title>Black Frame Creatives | Marketing &amp; Photography in Mangalore</title>')
head,rest=web.split('</style>',1)
meta=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0A0A0A">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="canonical" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Black Frame Creatives">
<meta property="og:title" content="Black Frame Creatives | Marketing &amp; Photography, Mangalore">
<meta property="og:description" content="A Mangalore marketing and photography crew. We plan the campaign, shoot it, and get it in front of the people who buy.">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:url" content="{SITE}/">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Black Frame Creatives","url":"{SITE}/","logo":"{SITE}/assets/logo-red.png","image":"{SITE}/assets/og-image.jpg","email":"mohammed.zia@bfcreatives.com","telephone":"+91 78295 98055","address":{{"@type":"PostalAddress","addressLocality":"Mangalore","addressRegion":"Karnataka","addressCountry":"IN"}},"sameAs":["https://www.instagram.com/blackframecreatives/"]}}</script>
'''
out=D+'site/'
shutil.rmtree(out,ignore_errors=True);os.makedirs(out)
open(out+'index.html','w').write(meta+head+'</style>\n</head>\n<body>\n'+rest+'\n</body>\n</html>\n')
shutil.copytree(D+'assets',out+'assets',ignore=shutil.ignore_patterns('logo-original.png'))
open(out+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
open(out+'sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}/</loc></url></urlset>\n')
print('built')
