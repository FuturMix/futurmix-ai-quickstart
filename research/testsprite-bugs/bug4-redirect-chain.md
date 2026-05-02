TestSprite email: zy.gerry@gmail.com
Proof-of-usage: https://github.com/FuturMix/futurmix-ai-quickstart/blob/main/research/testsprite-bugs/dashboard-proof.png

Title: Double redirect chain on root domain with incorrect 302 (should be 301)
Category: Performance issue / Functional bug
Steps:
1. curl -I http://testsprite.com → 301 → https://testsprite.com/
2. curl -I https://testsprite.com → 302 → https://www.testsprite.com/
3. curl -I http://www.testsprite.com → 301 → https://www.testsprite.com/

Expected: Single redirect from any non-canonical form to https://www.testsprite.com/, all using 301 (permanent).
Actual: Visiting http://testsprite.com requires two hops. The apex-to-www step uses 302 (temporary) instead of 301 (permanent). This prevents browser and CDN caching of the redirect, adding ~100-200ms latency for every new visitor who types the bare domain. Search engines also treat 302 differently from 301 for link equity.

Environment: Public internet, tested with curl 8.7
Severity: medium

Recommendation: Collapse to a single 301 from any variant directly to https://www.testsprite.com/. Change the apex 302 to 301.
