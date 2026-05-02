TestSprite email: zy.gerry@gmail.com
Proof-of-usage: https://github.com/FuturMix/futurmix-ai-quickstart/blob/main/research/testsprite-bugs/dashboard-proof.png

Title: Frontend changelog version (v2.x.x) vs API health version (v0.2.54) mismatch — confuses bug reporters
Category: Documentation mismatch
Steps:
1. Visit https://www.testsprite.com/changelog — observe latest versions listed: 2.1.1, 2.1.0, 2.0.19.
2. Run curl https://api.testsprite.com/health — observe version: "v0.2.54".
3. No documentation explains the relationship between these two version schemes.

Expected: Either consistent version numbering across all surfaces, or clear labeling explaining the relationship (e.g., "API v0.2.54 powers platform v2.1.1").
Actual: Frontend changelog shows v2.x.x while API reports v0.x.x. Customers reporting issues cannot reliably state which version they encountered a bug on. Support teams receiving reports with "version 2.1.1" vs "version 0.2.54" would not know if these refer to the same build.

Environment: Public web + public API
Severity: high

Recommendation: Document the version-numbering relationship on the changelog page, or unify the schemes. At minimum, add a mapping table or note like "Platform v2.1.1 runs on API v0.2.54."
