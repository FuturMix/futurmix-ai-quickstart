TestSprite email: zy.gerry@gmail.com
Proof-of-usage: https://github.com/FuturMix/futurmix-ai-quickstart/blob/main/research/testsprite-bugs/dashboard-proof.png

Title: All standard authentication paths return 404 — no discoverable sign-in route
Category: Functional bug
Steps:
1. Open https://www.testsprite.com in a browser.
2. Manually navigate to /login, /signup, /register, /signin, or /auth.
3. All five paths return 404 Not Found.

Expected: Either a working auth page at one of these standard paths, or a clear redirect to wherever authentication actually lives.
Actual: All five paths return 404 Not Found. A new visitor who types testsprite.com/login (as most SaaS users would expect) hits a dead end. The only entry point is the "Get Started" CTA button, which is not discoverable from a typed URL.

Environment: Chrome 125 / macOS 15.4, also tested Safari 18 and Firefox 126
Severity: high

Recommendation: Implement /login and /signup as 301 redirects to the actual auth flow. Even if auth is handled by a third-party provider, users expect these standard paths to work.
