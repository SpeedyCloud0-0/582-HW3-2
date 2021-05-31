from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256


def sign(m):
	#generate public key
	private_key, public_key = keys.gen_keypair(curve.secp256k1)

	#generate signature
	r, s = ecdsa.sign(m, private_key, curve=secp256k1, hashfunc=sha256)
	valid = ecdsa.verify((r, s), m, public_key, curve=secp256k1, hashfunc=sha256)
	# print(valid)

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )

	return public_key, [r, s]




