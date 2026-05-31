import json
import sys

print('ALMS replay lock scaffold')
print('Authority remains false')
print('Dual-environment execution required before replay_proven may become true')

if len(sys.argv) > 1:
    print('commit_sha=', sys.argv[1])
