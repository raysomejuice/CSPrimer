from luhn import verify

assert verify("17893729974")
assert not verify("17893729975")