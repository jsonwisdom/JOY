# Apple Blossom Replay — DRY RUN — 2026-09-05

```text
MODE                   = DRY_RUN
SIT_DOWN               = FALSE
CLASS_IN_SESSION       = FALSE
SPECIMEN               = APPLE_BLOSSOM_001
IMAGE                  = ABSENT
IMAGE_CID              = null
PETAL_COUNT            = NOT_RUN
VERDICT                = I_DONT_KNOW
AUTHORITY_CREATED      = FALSE
```

Walked the four replay steps against the template only.

1. Obtain a public photo or a real blossom.  
   Result: no image attached. Stop. Do not invent a CID.

2. Count the petals.  
   Result: cannot count what is not present.

3. Mark MATCH / DIFFERENT / I DON'T KNOW.  
   Result: **I DON'T KNOW**

4. Do not invent an image CID.  
   Result: `cid` remains `null`. PASS.

The claim “An apple blossom typically has five petals” stays a CLASSROOM_CLAIM. Dry-run does not verify botany and does not start class.

What would change the conclusion: a real blossom or a public-domain photo with countable petals.
