export function getProof(tree: BytesLike[], index: number): HexString[] {
    checkLeafNode(tree, index);
  
    const proof: HexString[] = [];
    while (index > 0) {
      proof.push(toHex(tree[siblingIndex(index)]!)); 
      index = parentIndex(index); 
    }
    return proof;
  }
  
