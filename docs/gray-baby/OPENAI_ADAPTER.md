# Gray Baby Generator — OpenAI Server Adapter Contract v0.1

## Why this is separate
The GitHub Pages front end is intentionally static. **Never put `OPENAI_API_KEY` in browser JavaScript, HTML, a public repository, or a client-side environment variable.**

A production render button should call a server-controlled endpoint such as:

`POST /api/gray-baby/render`

The server owns the OpenAI credential and returns only the generated image/result needed by the client.

## Current OpenAI image rail
OpenAI's current image generation documentation uses `gpt-image-2` with the Images API. The adapter should keep the model configurable rather than hard-code product assumptions forever.

Conceptual server flow:

```text
PUBLIC FORM
  ↓
GRAY BABY PROMPT BUILDER
  ↓
POST /api/gray-baby/render
  ↓
SERVER-SIDE VALIDATION + RATE LIMIT
  ↓
OPENAI IMAGES API (gpt-image-2)
  ↓
GENERATED IMAGE
  ↓
RETURN TO USER
```

## Request contract

```json
{
  "prompt": "string",
  "size": "1536x1024",
  "quality": "medium",
  "reference_image": "optional server-uploaded image reference"
}
```

Recommended limits:
- bounded prompt length
- accepted image types only
- upload size cap
- per-IP/session rate limiting
- cost guard / daily budget
- abuse and error logging without storing unnecessary personal content

## Response contract

```json
{
  "ok": true,
  "image": "data-or-short-lived-result-reference",
  "model": "gpt-image-2",
  "request_id": "provider request id when available"
}
```

## Safety and youth-facing design
This project is intended to support family-friendly creative use. Keep clear age-appropriate boundaries, avoid collecting unnecessary child data, do not create hidden behavioral profiles, and provide human/guardian controls when a deployed experience is specifically directed at children.

## Secret boundary

```text
PUBLIC_GITHUB_PAGES = NO_SECRET
OPENAI_API_KEY = SERVER_ONLY
CLIENT_PROMPT = USER_CONTROLLED
ART_OUTPUT != FACT
AUTHORITY_CREATED = FALSE
```
