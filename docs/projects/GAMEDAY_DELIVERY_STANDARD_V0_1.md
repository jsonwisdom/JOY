# Game Day Delivery Standard v0.1 — Computer Wisdom / JOY

**Status: DRAFT CONCEPT ONLY · merchant relationship UNKNOWN · ordering NOT ACTIVE · no payment or dispatch · no public customer photo feed.**

## Purpose

America's game-day standard for stadiums and sports bars should extend to food delivered to a fan's door. The aim is a **nationally reusable verification contract**, fulfilled by **locally authorized independent restaurants** with city-specific safety rules, prices, capacity and service radii. It does not imply national shipping of hot prepared food by one Alabama restaurant.

## Grounded Alabama research

**Coaches Corner Sports Bar & Grill**, 203 Orline St, Wetumpka, AL, is a named **reference business**, not an enrolled merchant. Its [official contact page](https://coachescornersportsbarandgrill.com/contact-us/) and [lunch menu](https://coachescornersportsbarandgrill.com/lunch-menu/) are publicly locatable. [Official specials](https://coachescornersportsbarandgrill.com/specials/) explicitly designate several offers **dine-in only**. Structured business discovery returned **takeout available** and **delivery not listed** on 2026-11-10. Neither observation authorizes an app to take orders.

The existing JOY [Coaches Corner Menu Hash Packet](../../FAMILY/receipts/COACHES_CORNER_MENU_HASH_PACKET_V0_1.md) is **WITNESS_GREEN_PACKET_STRUCTURE_ONLY**, with its **content hash pending**. That is meaningful evidence of earlier recordkeeping, **not** an independently verified menu or prices. Preserve the historical packet; do not rewrite it to imply current verification.

## The proposed 12-control standard

| Gate | Business rule |
| --- | --- |
| 01 Consent | Written merchant agreement for logos, menu, orders, service area and fulfillment |
| 02 Local food law | Jurisdiction-specific permits, health rules and enforcement |
| 03 Time/temperature | Document correct handling of time-temperature controlled foods |
| 04 Allergens | Verified ingredient/allergen information; don't invent allergy guarantees |
| 05 Accuracy | Count every food item/modifier; reject dine-in-only specials as delivery items |
| 06 Packaging | Tamper evidence, leak resistance, separation of temperature classes |
| 07 Handoff | Document pickup, delivery and exception events without public customer addresses |
| 08 Geography | Local radius and hours per authorized restaurant; not overnight coast-to-coast meals |
| 09 Fees/refunds | Itemized prices, tax, tip, fees, cancellation and chargeback rules |
| 10 Photos | Customer-controlled opt-in and moderation; no default sharing, minors or geotags |
| 11 Regulated items | **No alcohol ordering in this prototype**, irrespective of restaurant bar menu |
| 12 Receipts | Provenance + local CI-first PASS/FAIL/UNKNOWN; hash verifies bytes, not sanitary safety |

FDA's [Food Code](https://www.fda.gov/food/fda-food-code/food-code-2022) is a **model**, not automatically identical to each state's law; its standard hot holding reference is at least 135°F for TCS food and cold 41°F or below when temperature control is used. Alabama's [Department of Public Health rules](https://www.alabamapublichealth.gov/foodsafety/food-and-lodging.html) govern the Alabama analysis. Applicable time-as-a-public-health-control exceptions and procedures must be considered before a temperature alert can be classified. FDA also identifies [third-party delivery hazards and best practices](https://www.fda.gov/food/hfp-constituent-updates/fda-highlights-best-practices-food-safety-online-delivery-services) such as packaging and allergen control.

The [Alabama ABC Board](https://alabcboard.gov/licensing-compliance/how-to-apply) requires a separate licensed and trained process for alcohol deliveries. **Do not enable alcoholic beverages here**.

## Local game-day math demo

For an **entirely fictional** restaurant and orders, a customer picks two non-alcoholic foods, a kitchen packs, a courier transports and a recipient verifies. The exercise is to check `items_ordered == items_packed == items_delivered`, pickup and delivery sequence, and what evidence is still unavailable. Students can make a private illustrated food card, not publish any person's photo.

For a proposed partner pilot: merchant chooses approved items, packaging tests, game-day capacity, delivery territory and cancellation policy; trained adults conduct a consented pilot under required permits. A lawyer/food-safety professional reviews local compliance. Publication of images must be independently consented and rights-cleared.

## National cooperative model

**Common standard, local fulfillment**: each participating independent restaurant controls its own menu, timing, margins and permission to share customer-created art. ZIP codes are routing inputs, **not** permission to expose or profile customers. A "Game Day Verified" indicator would require evidence checks and a legitimate third-party/merchant audit process; it cannot be self-awarded because GitHub Actions passed.

## CI-FIRST

The machine-readable specification is [GAMEDAY_DELIVERY_STANDARD_V0_1.json](GAMEDAY_DELIVERY_STANDARD_V0_1.json) and the static validation test is [gameday-delivery-standard.test.mjs](gameday-delivery-standard.test.mjs). No customer data, payments, contract authority, brand approval, live dispatch or account integration exists. **PR draft only. Do not merge or deploy without human authorization and merchant permission.**

*This is Computer Wisdom independent research, not a Coaches Corner-operated app, health certificate, or partnership.*
