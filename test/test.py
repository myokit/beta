#!/usr/bin/env python3
print('GOING TO IMPORT')

import myokit_beta

print('GOING TO SAY HI')

print(myokit_beta.hi())

print('GOING TO DO SUM')

print(myokit_beta.sum())

assert myokit_beta.sum() == 12.345

myokit_beta.sim(False)

