TestSprite email: zy.gerry@gmail.com
Proof-of-usage: https://github.com/FuturMix/futurmix-ai-quickstart/blob/main/research/testsprite-bugs/dashboard-proof.png

Title: Case-insensitive routing creates SEO duplicate content across URL variants
Category: Functional bug / SEO
Steps:
1. curl -I https://www.testsprite.com/pricing → 200 OK
2. curl -I https://www.testsprite.com/PRICING → 200 OK (same page content)
3. curl -I https://www.testsprite.com/Pricing → 200 OK (same page content)

Expected: One canonical URL (lowercase) serves the page; other casings 301-redirect to the canonical form.
Actual: All three URL casings return HTTP 200 with identical content. Search engines may index /pricing, /PRICING, and /Pricing as three separate pages, splitting page authority and potentially triggering duplicate-content penalties in Google Search Console.

Environment: Public internet, tested with curl 8.7 and Chrome 125
Severity: medium

Recommendation: Canonicalize all URLs to lowercase via 301 redirect at the server/CDN level. Alternatively, add <link rel="canonical" href="https://www.testsprite.com/pricing"> to every page.
