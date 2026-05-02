TestSprite email: zy.gerry@gmail.com
Proof-of-usage: https://github.com/FuturMix/futurmix-ai-quickstart/blob/main/research/testsprite-bugs/dashboard-proof.png

Title: Information disclosure on /health endpoint exposes env and version
Category: Security concern
Steps:
1. From any terminal or browser, run: curl https://api.testsprite.com/health

Expected: Minimal response such as {"status":"ok"} without internal deployment details.
Actual: Returns {"env":"production","version":"v0.2.54"}. The exposed version string allows attackers to fingerprint the exact deployed build and cross-reference known vulnerabilities for that version. The env field confirms production targeting.

Environment: Public internet, any HTTP client (tested Chrome 125 / macOS 15.4, also curl 8.7)
Severity: high

Recommendation: Strip env and version from the production /health response, or gate /health behind authentication. A simple {"status":"ok"} is sufficient for external health checks.
