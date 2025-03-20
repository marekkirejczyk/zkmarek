    function verify(bytes32[] memory proof, bytes32 root, bytes32 leaf) internal pure returns (bool) {
        bytes32 computedHash = leaf;
        
        for (uint256 i = 0; i < proof.length; i++) { 
            computedHash = commutativeKeccak256(computedHash, proof[i]); 
        }

        return computedHash == root;
    }