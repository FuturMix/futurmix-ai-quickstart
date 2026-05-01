---
name: reddit-karma-grower
version: 1.0.0
description: Action-oriented playbook for growing Reddit post + comment karma safely without triggering shadow bans, suspensions, or sitewide rate limits.
---

# Reddit Karma Grower — skill.md

## Risk Model (3 bullets)

1. **Pattern detection beats velocity detection.** Reddit's anti-spam stack (Crowd Control, Automod, sitewide ML) flags accounts whose behavior clusters with known spam vectors — repeated link domains, copy-paste comment phrasing, low subreddit diversity, post timing in narrow windows. A fast account that varies subreddits, formats, and timing survives where a slow account that hits the same subreddit with similar comments dies.
2. **The first 30 days are probationary.** Accounts under 30 days old with under ~100 comment karma are subject to far stricter rate limits, automod thresholds, and shadow-ban heuristics. Many subreddits silently `removed` posts from new accounts via automod regardless of content quality. Plan the first 30 days as "earning the right to post," not "growing fast."
3. **Shadow bans are silent and survive password resets.** A shadow-banned account sees its own posts and comments; nobody else does. Detection requires an external check (logged-out browser or different account). Recovery requires modmail to /r/help or a fresh account — there is no automated unban for sitewide shadow bans.

---

## One-Line Action for New Accounts

**Comment thoughtfully on 3-5 mid-sized subreddits (10k-200k subscribers) for 14 days before posting any link or self-promotion.**

---

## One-Line Action for Warmed Accounts

**Post 1 high-effort original piece per week per subreddit, comment 5-10x per week per subreddit, never link the same external domain twice in a 7-day window.**

---

## New-Account Playbook (Day 0 to Day 30)

### Day 0-3: Setup and Scout
- Pick a username that does not look bot-generated (avoid `name_1234`, `cool_user_2026`). Two real-word combinations beat numerics.
- Set bio to a single sentence about a hobby. Empty bios are fine; long marketing bios are red flags.
- Subscribe to 15-25 subreddits across 3-4 interest clusters. Diversity itself is a positive signal.
- For each target subreddit, read the rules, sticky posts, and "About" sidebar. Note required post flairs, banned phrases, and karma thresholds.

### Day 3-10: Comment Only
- Comment 3-5 times per day, never more than 10. Each comment 30-150 words.
- Reply to questions in `/r/AskReddit`, `/r/explainlikeimfive`, or topical Q&A subs. These reward thoughtful answers with upvotes.
- Avoid "great post!" and "this." A useful comment either adds information, disagrees with substance, or asks a precise follow-up.
- Never link any external URL until day 14.

### Day 10-14: First Post
- Pick the highest-engagement subreddit you have been commenting in.
- Post a text-only question or experience report — no links, no images requiring approval.
- Title format that wins: `[concrete subject] + [specific question]` (e.g., "I have been running into X when doing Y, has anyone solved this?")
- Engage with every comment in the first 4 hours. Top-of-thread engagement bumps the post in algorithmic ranking.

### Day 14-30: Expand
- Add image and link posts to the rotation, but not in the same subreddit on consecutive days.
- Begin participating in 1-2 niche subreddits where you have specific expertise — these have less competition and higher per-post karma yield.
- Track which post types perform best per subreddit using a simple spreadsheet (subreddit, post type, time of day, karma at 24h, karma at 7d).

---

## Warmed-Account Playbook (Day 30+)

### Cadence
- 1 high-effort original post per week per subreddit. More than this triggers diminishing returns and self-promotion flags.
- 5-10 comments per week per subreddit. Spread across multiple posts, not all in one thread.
- Vary post formats: text post, image post, link to non-self domain, occasional link to your own (only if rule allows + after weeks of contribution).

### Content Angles That Win
- **Process documentation**: "How I X, with steps and screenshots."
- **Failure stories**: "I tried X for 6 months. Here is what did not work and why."
- **Original data**: "I tracked X for 30 days. Here is the chart."
- **Counterintuitive opinions backed by evidence**: "Everyone says X is best. I switched to Y. Six months in, here is the comparison."

### Cross-Subreddit Strategy
- Identify 2-3 "hub" subreddits where your content fits and 5-7 "spoke" subreddits with overlapping audiences but different cultures.
- Tailor the post format to each subreddit's culture — tech subs reward markdown formatting; lifestyle subs reward narrative.
- Never cross-post identically; always rewrite the title and intro for each target subreddit.

### Self-Promotion Discipline
- Reddit's general guideline: 9:1 ratio (9 non-self contributions per 1 self-promotion).
- Define "self-promotion" broadly: anything linking to a domain you control, anything mentioning a product you sell, anything driving traffic to your accounts.
- In subreddits without explicit self-promotion rules, default to 1 self-promotion per 30 contributions.

---

## Anti-Patterns (Explicit Don'ts)

| Anti-pattern | Why it kills accounts |
|--------------|----------------------|
| Posting the same link in 5+ subreddits within 24h | Triggers domain-spam ML model |
| Copy-paste comment text across multiple threads | Triggers comment-similarity detection (cosine similarity > 0.85) |
| Account creation → first post within 1 hour | Strong new-account spam signal |
| Voting only on your own content | Vote-manipulation detection via vote-ratio analysis |
| Account warmth via bot-purchased karma | Detected via vote-pattern anomalies; immediate sitewide ban |
| Asking friends to upvote in DMs | Discord vote-trading rings get caught quarterly |
| Creating multiple accounts on same IP | Account-linking via fingerprint; mass-ban risk |
| Posting during 02:00-06:00 your local time consistently | Pattern matches automated bot behavior |
| Replying to your own posts to bump them | Visible in modmail analytics; automod flags |
| Editing posts to add links after upvoting | "Bait-and-switch" pattern; many subs auto-remove edits |

---

## Shadow-Ban Detection

### Indicators
- Your post karma stops growing despite continued posting.
- Comment count on your posts is zero or near-zero.
- DMs to active users go unanswered for weeks (they may not see your messages).

### Verification (run weekly)
1. Open your profile in a logged-out incognito browser. If your posts and comments are visible: not shadow-banned at sitewide level.
2. Check a specific recent post via direct URL while logged out. If it 404s or shows "no posts": shadow-banned.
3. Use https://reddit.com/user/YOURUSERNAME without login. Profile loading but posts missing = shadow-banned.
4. Subreddit-specific shadow ban: post in `/r/ShadowBan` and follow their automated check bot instructions.

### Recovery
- For sitewide shadow-bans: message `/r/ModSupport` (sometimes responsive) or `/r/help`.
- Acknowledge the behavior that triggered the ban; do not argue.
- If no response in 14 days: account is effectively dead. Start a new one with lessons learned, never on the same IP without a clean VPN session.

---

## Automod Survival

- Read the `/r/{subreddit}/about/rules` and `/r/{subreddit}/wiki/index` for every subreddit before first post.
- Many subs require minimum karma (often 10-50 comment karma) and account age (often 7-30 days). Do not waste content on subs you cannot post in yet.
- Words that frequently trigger removal: "free," "click," "discount," external URL shorteners (bit.ly, tinyurl).
- Edits within 5 minutes of posting often re-trigger automod review. Get the post right before submitting.

---

## Measurement

Track weekly:
- Post karma delta
- Comment karma delta
- Number of comments received on your posts
- Number of comments per top-level post (engagement quality > raw karma)
- Subreddit diversity index (number of unique subreddits posted/commented in)

A healthy growth curve: +50-200 comment karma per week from week 4 onward, +100-500 post karma per week from week 6 onward, with engagement-per-post ratio (comments / upvotes) staying above 0.05.

---

## Final Note on Ethics and Sustainability

The single biggest predictor of long-term Reddit account health is **whether you would still post the same content if karma did not exist**. Accounts grown by genuine participation accumulate trust that compounds across years. Accounts grown by gaming velocity die in waves whenever Reddit ships an anti-spam update.

Treat karma as a side effect of being useful in communities you actually care about, not as the goal.
