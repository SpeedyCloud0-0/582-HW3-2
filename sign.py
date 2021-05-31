from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256


def sign(m):
	#generate public key
	#Generate a private key
	private_key, public_key = keys.gen_keypair(curve.P256)

	#generate signature
	#Your code here
	r, s = ecdsa.sign(m, private_key)
	# valid = ecdsa.verify((r, s), m, public_key)

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )


