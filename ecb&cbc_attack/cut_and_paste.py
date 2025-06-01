from cipher_modes import encrypt_ecb, decrypt_ecb, encrypt_cbc, decrypt_cbc


def cut_and_paste_ecb(ciphertext, blocks_to_keep=None, blocks_to_remove=None, blocks_to_reorder=None):
    block_size = 8  # DES block size-8 bytes
    blocks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]


    if blocks_to_keep is not None:
        blocks = [blocks[i] for i in blocks_to_keep]
    if blocks_to_remove is not None:
        blocks = [block for i, block in enumerate(blocks) if i not in blocks_to_remove]
    if blocks_to_reorder is not None:
        blocks = [blocks[i] for i in blocks_to_reorder]

    return b''.join(blocks)


def cut_and_paste_cbc(ciphertext, blocks_to_keep=None, blocks_to_remove=None, blocks_to_reorder=None):
    iv = ciphertext[:8]
    ciphertext_blocks = ciphertext[8:]

    block_size = 8
    blocks = [ciphertext_blocks[i:i + block_size] for i in range(0, len(ciphertext_blocks), block_size)]


    if blocks_to_keep is not None:
        blocks = [blocks[i] for i in blocks_to_keep]
    if blocks_to_remove is not None:
        blocks = [block for i, block in enumerate(blocks) if i not in blocks_to_remove]
    if blocks_to_reorder is not None:
        blocks = [blocks[i] for i in blocks_to_reorder]

    return iv + b''.join(blocks)