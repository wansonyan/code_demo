import hashlib

# # 定义SHA-256函数
# def sha256(message):
#     H_o = [
#         0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
#         0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
#     ]
#     K_o = [
#         0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
#         0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
#         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
#         0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
#         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
#         0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
#         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
#         0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
#         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
#         0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
#         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
#         0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
#         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
#         0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
#         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
#         0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
#     ]
#     H = list(H_o)
#     K = list(K_o)
#     #消息预处理填充消息长度
#     message = bytearray(message)
#     orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
#     message.append(0x8)
#     while len(message) % 64 != 56:
#         message.append(0x88)
#     message += orig_len_in_bits.to_bytes(8, byteorder='big')
#     #处理消息块
#     for i in range(0, len(message), 64):
#         chunk = message[i:i+64]
#         w=[0] * 64
#         for j in range(8,16):
#             w[j] = int.from_bytes(chunk[j*4:j*4+4], byteorder='big')
#             for j in range(16,64):
#                 s0 = (w[j-15] >> 7 | w[j-15] << 25) ^ (w[j-15] >> 18 | w[j-15] << 14)^ (w[j-15] >> 3)
#                 s1 = (w[j-2] >> 17 | w[j-2] << 15)^ (w[-2] >> 19 | w[-2] << 13)^ (w[j-2] >> 10)
#                 w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff

#             a, b, c, d, e, f, g, h = H

#         for j in range(64):
#             S1 = (e >> 6 | e << 26)^(e >> 11 / e << 21)^(e >> 25 | e << 7)
#             ch = (e & f)^ (~e & g)
#             temp1 = h + S1 + ch + K[j] + w[j]
#             S0= (a >> 2 | a << 30)^ (a >> 13 |a << 19)^ (a >> 22 | a << 10)
#             maj= (a & b)^ (a & c)^ (b & c)
#             temp2 = S0 + maj
#             h=g
#             g=f
#             f =e
#             e = (d + temp1) & 0xffffffff
#             d=c
#             c=b
#             b=a
#             a = (temp1 + temp2) & 0xffffffff

#         H[0] = (H[0] + a) & 0xffffffff
#         H[1] = (H[1] + b) & 0xffffffff
#         H[2] = (H[2] + c) & 0xffffffff
#         H[3] = (H[3] + d) & 0xffffffff
#         H[4] = (H[4] + e) & 0xffffffff
#         H[5] = (H[5] + f) & 0xffffffff
#         H[6] = (H[6] + g) & 0xffffffff
#         H[7] = (H[7] + h) & 0xffffffff

#     #将最终的哈希值拼接为一个字节序列
#     digest = b''
#     for h in H:
#         digest += h.to_bytes(4, byteorder='big')
#     return digest

# class HMAC():
#     def __init__(self, key, message):
#         self.key = key
#         self.message = message

#         if len(self.key) > 64:
#             self.key = sha256(self.key)
#         elif len(self.key) < 64:
#             self.key = self.key.ljust(64,b'\x00')

#         inner_key = bytes([x ^ 0x36 for x in self.key])
#         outer_key = bytes([x ^ 0x5C for x in self.key])

#         self.inner_hash = sha256(inner_key + self.message)
#         self.outer_hash = sha256(outer_key + self.inner_hash)
#     def inner_hash_hex(self):
#         return self.inner_hash.hex()
#     def outer_hash_hex(self):
#         return self.outer_hash.hex()
    
# def hmac_sha256(key, message):
#     block_size = 64
#     if len(key) > block_size:
#         key = sha256(key)
#     if len(key) < block_size:
#         key = key + bytearray(block_size - len(key))

#     o_key_pad = bytearray([x ^ 0x5c for x in key])
#     i_key_pad = bytearray([x ^ 0x36 for x in key])

#     inner_hash = sha256(bytes(i_key_pad) + message)
#     outer_hash = sha256(bytes(o_key_pad) + bytearray.fromhex(inner_hash))

#     return outer_hash


# # 测试代码
# key = "secret_key"
# message = "Hello, HMAC-SHA256!"
# hmac = hmac_sha256(key.encode(), message.encode())
# print("HMAC-SHA256:", hmac)

def sha256(message):
    H_o = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    K_o = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    H = list(H_o)
    K = list(K_o)

    message = bytearray(message)
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += orig_len_in_bits.to_bytes(8, byteorder='big')

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [0] * 64
        for j in range(16):
            w[j] = int.from_bytes(chunk[j*4:j*4+4], byteorder='big')
        for j in range(16, 64):
            s0 = (w[j-15] >> 7 | w[j-15] << 25) ^ (w[j-15] >> 18 | w[j-15] << 14) ^ (w[j-15] >> 3)
            s1 = (w[j-2] >> 17 | w[j-2] << 15) ^ (w[j-2] >> 19 | w[j-2] << 13) ^ (w[j-2] >> 10)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff

        a, b, c, d, e, f, g, h = H

        for j in range(64):
            S1 = (e >> 6 | e << 26) ^ (e >> 11 | e <<21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[j] + w[j]) & 0xffffffff
            S0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xffffffff

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff

        H[0] = (H[0] + a) & 0xffffffff
        H[1] = (H[1] + b) & 0xffffffff
        H[2] = (H[2] + c) & 0xffffffff
        H[3] = (H[3] + d) & 0xffffffff
        H[4] = (H[4] + e) & 0xffffffff
        H[5] = (H[5] + f) & 0xffffffff
        H[6] = (H[6] + g) & 0xffffffff
        H[7] = (H[7] + h) & 0xffffffff

    return ''.join(format(x, '08x') for x in H)


def sha256(message):
    return hashlib.sha256(message).hexdigest()

def hmac_sha256(key, message):
    block_size = 64
    if len(key) > block_size:
        key = sha256(key.encode())
    if len(key) < block_size:
        key = key + bytearray(block_size - len(key))

    o_key_pad = bytearray([x ^ 0x5c for x in key])
    i_key_pad = bytearray([x ^ 0x36 for x in key])

    inner_hash = sha256(bytes(i_key_pad) + message.encode())
    outer_hash = sha256(bytes(o_key_pad) + bytearray.fromhex(inner_hash))

    return inner_hash, outer_hash


# 使用提供的密钥进行计算
key = bytearray.fromhex("c3e72adeb78522c5ec2fb5559ba265d0c9bc1baeb9643ba62ccc6856a366741e5318")
message = "Hello, HMAC!"
inner_hash, outer_hash = hmac_sha256(key, message)
print("Inner Hash:", inner_hash)
print("Outer Hash:", outer_hash)
print("HMAC-SHA256:", outer_hash)