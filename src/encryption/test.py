
from cocks.cocks import CocksPKG, Cocks

cocks_pkg = CocksPKG()   # Optional param.: bit size (default = 2048)


r, a = cocks_pkg.extract("User1")

cocks = Cocks(cocks_pkg.n)  # Must use same public modulus, n, from cocks_pkg


c = cocks.encrypt(b"asHaving a single PKG issue private keys for all the users could be burdensome, especially for large organisations that may spread all over the world. This is because the private key generation is computationally expensive, and the authentication of the users and the delivery of the keys require secure channels between the PKG and the corresponding users. Hierarchical identity-based crypto (HIBC) is a generalisation of IBC that reflects an organisational hierarchy and eases the hierarchical administrative issues in large international companies or government. HIBC enables a root PKG to delegate the key generation and delivery to lower-level ", a)
print(c)
msg = cocks.decrypt(c, r, a)  # => b"test"

print(msg)


