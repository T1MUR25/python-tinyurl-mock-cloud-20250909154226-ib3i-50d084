import hashlib
s='cloudmax'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
