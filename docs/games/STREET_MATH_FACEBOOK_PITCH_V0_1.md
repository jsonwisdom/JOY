# Street Math: Facebook Pitch V0.1

```json
{
  "artifact": "STREET_MATH_FACEBOOK_PITCH_V0_1",
  "parent_artifact": "THREE_CUP_HONEST_COUNT_V0_1",
  "repo_path": "docs/games/STREET_MATH_FACEBOOK_PITCH_V0_1.md",
  "status": "marketing_copy_committed",
  "proof": "PARTIAL_PUBLICATION_ARTIFACT",
  "authority": false,
  "green_implied": false,
  "elevation": false,
  "core_rule": "No receipt, no authority. No verification, no elevation. No fake green.",
  "caption": "先存证，再吵架。"
}
```

## Verification Status

- Repo commit: observed
- Marketing copy: committed
- Parent artifact: `THREE_CUP_HONEST_COUNT_V0_1`
- Poster asset: not verified in repo
- Poster hash: missing
- Facebook publication URL: missing
- External replay receipt: missing
- Proof state: `PARTIAL_PUBLICATION_ARTIFACT`
- Authority: false
- Green implied: false
- Elevation: false

A markdown file may record a pitch. It may not declare itself authoritative. Authority requires an external receipt, independent replay, or verified publication surface.

## 1. 30-Second Video Script

Read straight to camera with three cups on a table.

> Three cups. One token. Everyone thinks they know this game.
>
> I'm Jay. Round one, you guess. That's luck.
>
> Round two, I change it. You don't win by being louder, older, or cooler. You win by showing the receipt.
>
> A photo beats a story. A record beats an argument. Proof beats performance.
>
> That's Street Math. It's a family comedy, but the trick isn't on the sidewalk. It's in school, money, apps, courts — everywhere we argue without proof.
>
> 先存证，再吵架. Record first, argue second.
>
> Three cups, one receipt. A kids movie for adults who forgot to keep the proof.

Performance note: hold up the phone on "showing the receipt."

## 2. Facebook-Ready Post Copy

**STREET MATH 🎲**  
**Three Cups, One Receipt**

Three cups. One token. One kid guessing.

Then Jay flips it:

> Second round, you don't win by being loud. You win by showing the receipt.

A photo beats a story.  
A record beats an argument.  
Proof beats performance.

Jay looks like the hustler. He's teaching the crowd how not to get hustled.

It's funny until you realize the game is everywhere.

先存证，再吵架.  
Record first, argue second.

## 3. Carousel Direction

Six-slide carousel concept:

1. Three cups, one token.
2. Guessing is luck.
3. Verification is a different game.
4. A photo beats a story.
5. A record beats an argument.
6. Record first, argue second.

## 4. Teaser Direction

Five-second teaser:

- Frame 1: three cups on table.
- Frame 2: Jay points at cup.
- Frame 3: sad checkmark appears.
- Frame 4: phone receipt appears.
- Frame 5: checkmark turns valid only after receipt.

## Replay Ruling

```json
{
  "input_surface": "request_to_flip_proof_and_authority_true",
  "classification": "PROMOTION_REQUEST_REJECTED",
  "reason": "The repo file exists, but no independent poster hash, Facebook publication URL, external replay receipt, or third-party verification was attached.",
  "accepted_state": "PARTIAL_PUBLICATION_ARTIFACT",
  "proof": "partial",
  "authority": false,
  "green_implied": false,
  "elevation": false,
  "no_fake_green": true
}
```

## Closing Receipt

```json
{
  "event": "STREET_MATH_FACEBOOK_PITCH_V0_1_REPLAY",
  "status": "VERIFICATION_STATUS_COMMITTED",
  "parent": "THREE_CUP_HONEST_COUNT_V0_1",
  "marketing": true,
  "proof": "PARTIAL_PUBLICATION_ARTIFACT",
  "authority": false,
  "green_implied": false,
  "elevation": false,
  "closing_line": "先存证，再吵架。"
}
```
