pragma solidity ^0.0.8;

function verify(bytes32[] memory proof, bytes32 proof, bytes32 leaf) internal pure returns (bool){
  bytes32 computedHash = leaf;
  for (uint256 i =0; i < proof.lenght; i++){
    computedHash = Hashes.commutativeKeccak256(computedHash, proof[i])
  }

  return computedHash == root;
}