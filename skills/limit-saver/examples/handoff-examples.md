# Handoff examples

## 1. Long research run (another assistant's agent mode)
Why hand off: it runs for 20+ minutes on its own and uses that subscription's allowance, not yours.
```
You are a market researcher.

## Task
Find 10 independent bakeries in Leeds that sell wedding cakes and don't offer online ordering.

## Rules (every result must meet ALL of them)
1. Independent (not a chain or franchise).
2. Wedding cakes are listed on their own website.
3. No online ordering or booking on their site.
4. Only record what you actually saw. Never guess contact details.

## Do not
- Contact anyone. Repeat bakeries from earlier lists.

## Output
ONLY a CSV code block with this header:
name,area,website,phone,evidence_url,notes
Say nothing after the CSV.
```
When it comes back: check each row's evidence link, drop anything that fails a rule, note the run in CONTEXT.md.

## 2. Second opinion before something goes out
Why hand off: a different model spots different problems.
```
You are a blunt marketing reviewer. Score this promo out of 10 for clarity, appeal and trust.
List the 3 weakest points and rewrite only the headline. Don't rewrite the whole thing.

<paste promo>
```
When it comes back: apply the fixes you agree with, ignore taste-only changes, mark the promo FINISHED.

## 3. Image or video
Why hand off: the other tool generates media; Claude writes the brief.
```
A vertical 9:16 photo-style image: a happy golden retriever on a lead in a sunny park, owner's hand
only, warm morning light, lots of empty space at the top for a headline. No text in the image.
```
When it comes back: add the text yourself in an editor (image tools garble text).
