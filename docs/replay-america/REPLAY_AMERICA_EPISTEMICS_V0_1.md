# Replay America Epistemics V0.1

Status: DRAFT_REPLAYABLE  
Authority: false  
No Fake Green: true  
Append Only: true  
Render Authority: none  
Evidence Direction: SOURCE -> RECEIPT -> CHECK -> STATUS -> RENDER

## 0. Purpose

This file is the math / epistemics layer for Replay America.

It explains why repeated logos are not automatically independent observations, propagation can amplify a claim without adding evidence, presentation layers must not mutate evidentiary state, correlation/dependence/coordination/intent must remain separate, and receipts are required for evidentiary promotion.

The "Miscounted Kid" is a mnemonic. The mathematics is the actual constraint.

## 1. Effective sample size — the Miscounted Kid invariant

When observations are exchangeable and approximately equicorrelated with pairwise correlation rho, a common effective-sample-size approximation is:

~~~text
n_eff = n / (1 + (n - 1) * rho)
~~~

This is a model, not a universal law. It is useful when repeated signals share strong common dependence.

Examples for n = 500:

~~~text
rho = 0.90
n_eff = 500 / (1 + 499 * 0.90)
      = 500 / 450.1
      ≈ 1.111

rho = 0.50
n_eff = 500 / (1 + 499 * 0.50)
      = 500 / 250.5
      ≈ 1.996

rho = 0.99
n_eff = 500 / (1 + 499 * 0.99)
      = 500 / 495.01
      ≈ 1.010
~~~

Therefore:

~~~text
500 LOGOS != 500 INDEPENDENT OBSERVATIONS
REPETITION != INDEPENDENT CORROBORATION
SYNDICATION != NEW ROOT
SHARED UPSTREAM SOURCE != MULTIPLE ROOT SOURCES
~~~

Important boundary:

~~~text
CORRELATION != COORDINATION
DEPENDENCE != INTENT
COMMON SOURCE != CONSPIRACY
~~~

Dependence may arise from syndication, a common upstream report, shared public data, simultaneous events, common incentives, common tooling, or many other mechanisms.

This is the mathematical justification for:

~~~text
NO_FAKE_GREEN
APPEND_ONLY
INDEPENDENT_ROOT_COUNTING
PROVENANCE_DAG_ANALYSIS
~~~

## 2. Root-counting before logo-counting

Let a provenance graph be:

~~~text
G = (V, E, tau)
~~~

where:

~~~text
V   = source / publisher / artifact nodes
E   = directed provenance or dependency edges
tau = typed edge relation
~~~

A publisher count is not a root count.

Define:

~~~text
ROOT(v) = node v has no admissible upstream evidence parent in the bounded graph
~~~

Then:

~~~text
N_publishers = count(publisher nodes)
N_roots      = count(independent admissible roots)

N_publishers >= N_roots
~~~

A larger publisher count does not itself increase evidentiary independence.

## 3. Propagation matrix — cascade physics

For a two-type linearized branching approximation, define:

~~~text
R = [ R_II  R_AI
      R_IA  R_AA ]
~~~

where:

~~~text
R_II = institution -> institution propagation
R_AA = audience    -> audience propagation
R_IA = institution -> audience propagation
R_AI = audience    -> institution propagation
~~~

Let:

~~~text
rho(R) = spectral radius of R
~~~

In a linear branching approximation:

~~~text
rho(R) > 1
~~~

means the local propagation process is supercritical: a small perturbation may grow rather than die out.

This is a model condition, not a guarantee of indefinite real-world growth. Saturation, finite audiences, damping, competing narratives, platform intervention, time decay, and nonlinear behavior can stop a cascade.

The important epistemic rule is:

~~~text
PROPAGATION_STRENGTH != EVIDENCE_STRENGTH
~~~

A claim can propagate strongly without gaining a new independent root.

Therefore:

~~~text
AMPLIFICATION != CORROBORATION
VIRALITY != VERIFICATION
REPETITION != PROOF
~~~

## 4. Sidecar constraint — presentation != evidence

Replay America keeps two state families separate:

~~~text
X_E(t) = evidentiary state
X_P(t) = presentation / pedagogy state
~~~

The sidecar may update:

~~~text
X_P(t+1) = Sidecar(X_E(t), E(t), C(t))
~~~

where:

~~~text
E(t) = emotional / affective context
C(t) = audience / teaching context
~~~

But:

~~~text
SIDECAR MAY TRANSFORM PRESENTATION
SIDECAR MAY NOT TRANSFORM EVIDENTIARY STATE
~~~

Therefore:

~~~text
SuperSecretSisterSideCar
= PRESENTATION / CONTINUITY / PEDAGOGY

SuperSecretSisterSideCar
!= RECEIPT
!= VERIFIER
!= AUTHORITY
~~~

Feelings matter for communication:

~~~text
RESONANCE = g(emotion, clarity, relevance, repetition, context)
~~~

But:

~~~text
HIGH_EMOTION != TRUE
HIGH_RESONANCE != PROOF
LOW_RESONANCE != FALSE
~~~

## 5. Conservation law

The core conservation law is:

~~~text
FACTS stay facts.
FEELINGS stay feelings.
NAMES stay names.
RECEIPTS decide evidentiary state.
~~~

For evidentiary state:

~~~text
X_E(t+1) = F(X_E(t), event, admissible_receipt)
~~~

If there is no admissible new receipt:

~~~text
NO_NEW_RECEIPT
-> NO_EVIDENTIARY_STATE_ADVANCE
~~~

This does not mean nothing in the system may change.

Presentation, teaching language, UI state, jokes, navigation, or audience context may change while the evidentiary state remains fixed.

Therefore:

~~~text
NO_FAKE_GREEN
NO_FAKE_RED
NO_FAKE_UPDATES
NO_FAKE_AUTHORITY
~~~

## 6. Coordination and intent boundary

The math may establish or estimate:

~~~text
correlation
dependence
shared upstream roots
temporal clustering
propagation
amplification
structural similarity
~~~

It does not by itself establish:

~~~text
coordination
intent
motive
malice
conspiracy
editorial direction
~~~

A coordination or intent rail requires evidence specific to that proposition, such as:

~~~text
directives
communications
contracts
funding relationships
editorial instructions
other admissible actor-to-action evidence
~~~

Therefore:

~~~text
CORRELATION != COORDINATION
COORDINATION != INTENT
INTENT != LEGAL LIABILITY
~~~

Each promotion needs its own receipt.

## 7. Media / infrastructure role separation

For any media + infrastructure investigation:

~~~text
PUBLISHER
DNS PROVIDER
CDN / EDGE PROVIDER
CERTIFICATE AUTHORITY
UPSTREAM SOURCE
CONTENT AUTHOR
LEGAL AUTHORITY
~~~

must remain separate typed roles.

Hard rules:

~~~text
DNS != EDITORIAL CONTROL
CDN != AUTHORSHIP
CERTIFICATE != CONTENT AUTHORITY
RADAR / RESOLVER OBSERVATION != HOSTING RELATIONSHIP
PUBLISHER != PRIMARY SOURCE
SAME SCREEN != SAME OWNER
~~~

## 8. FoxFartCloudFlareDust — bounded infrastructure replay

FOXFARTCLOUDFLAREDUST is a satire/render label only.

~~~text
FOXFARTCLOUDFLAREDUST
= SATIRE / MEDIA-LITERACY RENDER

FOXFARTCLOUDFLAREDUST
!= TECHNICAL FINDING
!= LEGAL FINDING
!= CLAIM OF COORDINATION
~~~

### Current public-source snapshot — 2026-09-30

Public WHOIS surfaces for foxnews.com currently list authoritative nameservers under:

~~~text
ns01.dns.fox
ns02.dns.fox
ns03.dns.fox
ns04.dns.fox

ns01.foxdoua.com
ns02.foxdoua.com
ns03.foxdoua.com
ns04.foxdoua.com
~~~

Source locators:

~~~text
https://who.is/whois/foxnews.com
https://www.whois.com/whois/foxnews.com
~~~

Public network-observation services currently associate multiple foxnews.com hostnames with Akamai CDN infrastructure.

Examples:

~~~text
https://www.netify.ai/resources/hostnames/247preview.foxnews.com
https://www.netify.ai/resources/hostnames/press.foxnews.com
https://www.netify.ai/resources/hostnames/nation.foxnews.com
https://www.netify.ai/resources/hostnames/my.foxnews.com
~~~

Cloudflare Radar has a page for foxnews.com, but Cloudflare Radar observes domains through public Internet measurement surfaces, including 1.1.1.1 resolver data. The existence of a Cloudflare Radar page is not evidence that Cloudflare is Fox News's authoritative DNS provider, publisher, editor, or primary CDN.

Locator:

~~~text
https://radar.cloudflare.com/domains/domain/foxnews.com
~~~

A technology survey reports Cloudflare-operated CDNJS on a subdomain. That is a third-party asset/library relationship and does not establish that the primary foxnews.com publishing stack is Cloudflare-controlled.

Locator:

~~~text
https://w3techs.com/sites/info/foxnews.com
~~~

### Bounded status

~~~text
FOXNEWS_DOMAIN_EXISTS                 = PASS
FOXNEWS_PUBLIC_WHOIS_NS_OBSERVED      = PASS
AKAMAI_ASSOCIATED_SUBDOMAINS          = OBSERVED
CLOUDFLARE_RADAR_OBSERVATION          = OBSERVED

CLOUDFLARE_AUTHORITATIVE_DNS_BIND     = NOT_ESTABLISHED
CLOUDFLARE_PRIMARY_CDN_BIND           = NOT_ESTABLISHED
CLOUDFLARE_EDITORIAL_CONTROL          = NOT_ESTABLISHED
FOX_CLOUDFLARE_COORDINATION           = NOT_ESTABLISHED
~~~

Therefore:

~~~text
CLOUDFLARE_RADAR_PAGE != CLOUDFLARE_HOSTING_PROOF
THIRD_PARTY_CLOUDFLARE_ASSET != PUBLISHER_CONTROL
AKAMAI_OBSERVATION != EXCLUSIVE_INFRASTRUCTURE_PROOF
~~~

This is exactly why role fission must happen before narrative fusion.

## 9. America.gov bridge

Replay America is a civic replay system, not a government authority surface.

The current federal America.gov announcement describes America.gov as an AI-enhanced gateway/front door drawing from information across more than 29,000 government websites.

That makes it a discovery / navigation surface.

It does not collapse:

~~~text
AMERICA.GOV_RESULT
into
UNDERLYING_AGENCY_FINDING
~~~

Replay path:

~~~text
AMERICA.GOV RESULT
-> UNDERLYING AGENCY SOURCE
-> SOURCE BYTES / LOCATOR
-> CLAIM FISSION
-> RECEIPT
-> CHECKER
-> STATUS
-> PUBLIC EXPLANATION
~~~

## 10. Miscounted Kid -> Replay America bridge

The mnemonic teaches:

~~~text
500 logos != 500 independent observations
~~~

Replay America operationalizes it:

~~~text
LOGOS
-> PROVENANCE DAG
-> ROOT DECOMPOSITION
-> DEPENDENCY MODEL
-> RECEIPT SET
-> CHECKER
-> STATUS
~~~

The art makes the error memorable.

The math specifies the error.

The receipt architecture prevents the error from silently changing system state.

## 11. Canonical invariants

~~~text
SATIRE != RECEIPT
RENDER != SOURCE
NAME != IDENTITY
ATTESTATION != UNIVERSAL_TRUTH
REPETITION != CORROBORATION
CORRELATION != COORDINATION
COORDINATION != INTENT
PROPAGATION != EVIDENCE
PRESENTATION != EVIDENTIARY STATE
DNS != EDITORIAL AUTHORITY
CDN != AUTHORSHIP
AMERICA.GOV_RESULT != AGENCY FINDING
NO_NEW_RECEIPT -> NO_EVIDENTIARY_STATE_ADVANCE
~~~

## 12. Lock line

~~~text
Count roots, not logos.
Measure dependence before consensus.
Separate propagation from proof.
Separate correlation from coordination.
Let the sidecar explain.
Never let the sidecar promote.
Preserve the receipt.
Replay the method.
~~~

AUTHORITY_CREATED = FALSE  
NO_FAKE_GREEN = TRUE
