# Definition
Transport Layer Security is a cryptographic protocol designed to provide secure communications between systems.

TLS is the successor of SSL and there are different TLS versions. The most common ones nowadays being:
- TLSv1.3
- TLSv1.2

Previous TLS versions are known to be vulnerable and shall no longer be used. TLSv1.3 also fixes several security vulnerabilities and performs a faster cypher negotiation.

All cyphers in TLSv1.3 support [Perfect Forward Secrecy(PFS)](https://www.perfectforwardsecrecy.com), which is not the case in TLSv1.2. The usage of RSA has also been removed, as it is incompatible with PFS.


# TLS handshake
![TLSv1.2_3 handshakes](/Security/TLS/TLS_handshakes.jpeg)

The handshake of TLSv1.3 has less round trips than TLS1.2 and is hence faster.

In TLSv1.3 [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange) is used instead of RSA which allows PFS and avoids vulnerabilities like [POODLE](https://www.entrust.com/knowledgebase/ssl/poodle-vulnerability-tls).

# AEAD encryption
TLSv1.3 uses stream cyphers instead of bulk cyphers. The deprecated bulk cyphers have fixed length blocks which require padding when the data for some block is not sufficient. This is not optimal and opens a door for exploitation.

In TLS 1.3 encryption and authentication have been combined into one.
There are several types of AEAD, the most common is the **Encrypt-then-MAC (EtM)**
![AEAD encryption](/Security/TLS/EtM.png)


# TLSv1.3 recommended cypher suits:
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256
- TLS_AES_128_GCM_SHA256
- TLS_AES_128_CCM_8_SHA256
- TLS_AES_128_CCM_SHA256


# How to check web server TLS security
A good tool to do this is [testssl](https://github.com/drwetter/testssl.sh). It is free and open source. Testssl automatically tests the TLS versions and cyphers offered by a server, against several user agents, including the ones of mobile phones.

Another simpler option is to user a vulnerability scanner such as nmap:
```
nmap --script ssl-enum-ciphers -p <port_number> <server>
```


# References
- [How secure can HTTPS be? Demystifying TLS Cipher Suites!](https://www.youtube.com/watch?v=XwrfZLKsuhE)
- [Breaking Down the TLS Handshake](https://www.youtube.com/watch?v=cuR05y_2Gxc)
- [Cipher suite info](https://ciphersuite.info)
- [TLS 1.2 vs TLS 1.3: What are the Main Differences?](https://www.linkedin.com/pulse/tls-12-vs-13-what-main-differences-farid-jabari/)
- [TLS 1.3: Everything you need to know](https://www.thesslstore.com/blog/tls-1-3-everything-possibly-needed-know/)
- [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange)
- [Galois/Counter Mode (GCM)](https://en.wikipedia.org/wiki/Galois/Counter_Mode)