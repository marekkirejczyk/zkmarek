// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

    function verify(bytes32[] memory proof, bytes32 root, bytes32 leaf) 
                    internal pure returns (bool) {
        return processProof(proof, leaf) == root;
    }

    function processProof(bytes32[] memory proof, bytes32 leaf) 
                          internal pure returns (bytes32) {
        bytes32 computedHash = leaf;
        for (uint256 i = 0; i < proof.length; i++) {
            computedHash = Hashes.commutativeKeccak256(computedHash, proof[i]);
        }
        return computedHash;
    }