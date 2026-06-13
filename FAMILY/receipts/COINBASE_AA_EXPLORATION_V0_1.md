# COINBASE_AA_EXPLORATION_V0_1

## STATUS: AA_STACK_MAP_DRAFT
## AUTHORITY: FALSE
## NO_FAKE_GREEN: TRUE

## Stack

UserOperation -> Bundler -> EntryPoint -> Smart Account -> Optional Paymaster

## Boundary

This artifact describes the Coinbase Account Abstraction path conceptually.
It does not prove a specific transfer, mint, deploy, sponsorship, or authority claim.

## Claimed Related Transaction

0x8a642cb0e2129fb7b386aee865e421dc9c60a4a1f20120a9cb6feefd9322474b

## Required Before Promotion

- Base receipt read-back
- EntryPoint handleOps confirmation
- sender/recipient confirmation
- token contract confirmation
- decoded transfer amount confirmation
