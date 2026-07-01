# Guideline: YouTube Content Strategy for B2B SaaS — Research Project

Topic chosen: **YouTube content strategy for B2B SaaS**

This is a working plan for how to execute HundredHires' 2nd assignment. Follow it step by step, but adapt as you actually work — the goal is genuine research, not ticking boxes.

---

## 0. What's actually being graded (keep this in view)

- **Quality of experts**, not quantity. 10 people who genuinely run B2B YouTube channels (their own or clients') beat 10 SEO-blog authors who write *about* B2B video strategy.
- **Repo structure** — clean, matches the spec exactly.
- **Ability to work with APIs/tools** — YouTube transcript pulls, structured folders, real commits.
- **Whether the material could support a real playbook** — i.e. is there enough substance (tactics, numbers, mistakes) in what you collected, not just fluff.

A heads-up from my own research: this topic actually has better signal than most — B2B YouTube strategy is a live, active niche right now with real, named practitioners producing recent content (2025-2026), not just recycled agency listicles. I found and verified 6 strong candidates below. That said, some generic "best of" agency roundups still show up in search — skip those.

---

## 1. Vetting checklist — how to tell a genuine practitioner from a content mill

A candidate is a **strong pick** if most of these are true:

- [ ] They have a **real, checkable YouTube channel** (their own, or one they visibly run/produce for a named client) — not just a claim of "I do YouTube strategy."
- [ ] They talk in **specifics**: view counts, subscriber growth, watch time, what flopped, actual video titles — not just "YouTube drives brand awareness."
- [ ] They've **built or grown something themselves** or for a named client (a channel, an agency with named results) rather than only writing listicle advice.
- [ ] Their content is **recent** (last 6-12 months) — YouTube's algorithm and B2B content norms shift fast.
- [ ] You can find them across **at least two formats** (e.g. their own YouTube channel + a podcast appearance, or LinkedIn posts + a case study) — suggests a consistent public track record, not a one-off blog post.

**Red flags — skip these:**
- Agency "best of" roundup articles (rank agencies, not practitioners)
- Anonymized/unverifiable case studies ("Company X's channel grew 500%...")
- Generic marketing influencers with no YouTube-specific, checkable track record
- Content that's clearly AI-generated SEO filler with no personal voice or verifiable claims

---

## 2. Where to actually look

- **YouTube itself** — search "B2B SaaS YouTube strategy," "how to grow a B2B YouTube channel," filter by upload date (last year). Check the channel's own upload history and whether they practice this on their own channel, not just talk about it.
- **LinkedIn search** — search posts (not profiles) for "B2B YouTube" — see who's cited by name in case studies from other creators (a strong signal, since practitioners reference each other).
- **Podcasts** — B2B marketing/GTM podcasts (Breaking B2B, Growth Activated, The ChangeOver, GTM Podcast) often host YouTube-specific guests — search episode titles for "YouTube."
- **The channels themselves** — once you find one strong practitioner, check who they've worked with or namedropped as clients/collaborators; this tends to surface more real names fast (this is how several of the candidates below were found).

---

## 3. Verified candidates found so far (start here, verify yourself before finalizing)

| Name | Role / Channel | Why credible | Link(s) |
|---|---|---|---|
| **Samu Kovács** | Founder, KS Media (YouTube-first B2B agency) | Runs YouTube strategy for 40+ B2B clients incl. Adam Robinson (RB2B), Breaking B2B, The B2B Playbook; speaks in specifics (3 content pillars framework, real client numbers) across multiple podcasts | ks-media.co, LinkedIn: samu-kovacs, guest on Growth Activated podcast ep. #47, Breaking B2B podcast |
| **Sam Dunning** | CEO, Breaking B2B | Runs his own YouTube channel as part of bootstrapping Breaking B2B to $200k/mo; a named, long-running case study of B2B YouTube working in practice, not just theory | breakingb2b.com, Breaking B2B YouTube channel |
| **Adam Robinson** | Founder, RB2B | Documented, named case study: grew from 100-300 views/video to 100k+ views and hundreds of signups in 5 months via a restructured YouTube strategy | Referenced via KS Media/LinkedIn case study — verify his own channel directly |
| **Kyle Denhoff** | Senior Director of Marketing, HubSpot | Manages 12+ YouTube channels for HubSpot (a major SaaS company); gives structural, specific advice (channel architecture, format definition) rather than generic tips | Interviewed on The ChangeOver podcast (Weidert), HubSpot |
| **A. Lee Judge** | Founder, Content Monsta | 20+ years in B2B marketing, runs his own YouTube channel (Content Monsta Marketing) plus a podcast, video-production practitioner with a long public track record | aleejudge.com, YouTube: Content Monsta Marketing, Forbes Agency Council |

Note: I found a 6th lead (a cold-email-space creator referenced in a KS Media case study, name spelled inconsistently as "Taylor Heron"/"Taylor Haren" across sources) that needs direct verification before you trust it — treat any name you can't pin down to one consistent, checkable identity as unconfirmed.

You need **5 more** to reach 10. Use section 2's tactics — checking who these five have worked with or referenced is often the fastest route to the next names.

---

## 4. Repo structure (build this exactly)

```
your-repo/
├── README.md
├── research/
    ├── sources.md
    ├── linkedin-posts/
    │   └── <author-name>/
    │       └── post-01.md, post-02.md, ...
    ├── youtube-transcripts/
    │   └── <author-name>/
    │       └── video-title.md (or .txt)
    └── other/
        └── (podcast notes, newsletter excerpts, case studies, etc.)
```

`sources.md` format for each expert:

```markdown
## [Name]
- Platform(s): YouTube / LinkedIn / Podcast
- Link: [channel or profile URL]
- Why they're credible: [1-2 sentences — what have they actually built/run?]
- Content collected: [list what you pulled — e.g. "5 YouTube transcripts, 3 LinkedIn posts"]
- Date reviewed: [date]
```

---

## 5. Collecting the content

**YouTube transcripts:**
This is a good technical task to hand to Claude Code or Codex inside Cursor, since it's a real coding task. A clean approach:
- Use the `youtube-transcript-api` Python package (pulls public transcripts, no API key needed) or the Supadata API if you want a hosted option.
- Ask Claude Code (in Cursor) something like: *"Write a Python script that takes a list of YouTube video URLs and saves each transcript as a markdown file into research/youtube-transcripts/<author-name>/."*
- Run it, review the output for garbled auto-captions, and clean up before committing.

**LinkedIn posts:**
LinkedIn's terms of service prohibit automated scraping, and tools that do this risk getting your account restricted — I'd stay away from building a scraper for it. The safe approach:
- Manually copy each post's text into a markdown file (`research/linkedin-posts/<author>/post-01.md`), including the post date and a link back to the original.
- This is slower but it's what "manually collect their latest posts" in the instructions is pointing you toward anyway.

**Other (podcasts, case studies, client-result posts):**
- For podcasts: note timestamp + key quotes/tactics in a markdown file, link to the episode.
- For case studies (e.g. Adam Robinson's / Kyle Denhoff's specific numbers and frameworks): save as markdown with a link and date, and note exactly which numbers/claims are attributable to which source.

---

## 6. Commit cadence

Commit as you go, not all at once at the end — this is explicitly called out as something they check:

- Commit after `sources.md` has your first 3-4 experts drafted
- Commit after each author's folder is populated
- Commit after the README update
- Aim for commit messages that describe real progress, e.g. `"Add sources.md with first 5 experts"`, `"Add YouTube transcripts for Samu Kovács"`, `"Add LinkedIn posts for A. Lee Judge"`

## 7. README.md update (add this section once research is done)

```markdown
## Research: YouTube Content Strategy for B2B SaaS

Chose this topic because [your real reason — e.g. relevance to your own agency's content strategy, genuine interest, etc.]

Found and reviewed 10 practitioners who actively build or run B2B YouTube channels (not just people writing about it). See `/research/sources.md` for the full list with links and annotations.

Collected [X] YouTube transcripts and [X] LinkedIn posts, organized by author in `/research/youtube-transcripts/` and `/research/linkedin-posts/`.

Key patterns I noticed across sources: [1-3 real takeaways once you've actually gone through the material]
```

---

## Next step for you

Verify the 5 candidates in section 3 yourself (check their actual channels/profiles), then find 5 more using the "who have they worked with" tactic in section 2. Share what you find and I'll help you sanity-check each before you commit time to collecting their content, and I can help write the transcript-pulling script whenever you're ready.
