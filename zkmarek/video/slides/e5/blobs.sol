contract KZGBlobVerifier {
    /**
     * @notice Verify KZG proof that p(x) == y where p(x) is the polynomial
     * represented by the KZG commitment
     */
    function verifyBlobKZG(
        bytes48 commitment,
        bytes32 x,
        bytes32 y,
        bytes48 proof,
        uint256 blobIndex,
    ) public view returns (bool) {

        // Pack the input data
        bytes memory data = abi.encodePacked(commitment, x, y, proof);
        
        // Call KZG precompile using assembly
        bool success;
        assembly {
            // Call precompile at 0x0a
            // gas(), address, value, inputOffset, inputSize, outputOffset, outputSize
            success := staticcall(gas(), 0x0a, add(data, 0x20), mload(data), 0, 0)
        }

        bytes32 commitmentHash = blobhash(blobIndex);
        if (commitmentHash == bytes32(0)) return false;
        return success && verifyBlobHash(commitmentHash, commitment);
    } 
}