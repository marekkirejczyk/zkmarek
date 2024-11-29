contract KZGBlobVerifier {
    using KZG for bytes;

    function verifyBlobKZG(
        bytes48 commitment,
        bytes32 x,
        bytes32 y,
        bytes48 proof,
        uint256 blobIndex
    ) public view returns (bool) {
        bytes memory data = abi.encodePacked(commitment, x, y, proof);

        bool success = data.verifyKZGProof();

        bytes32 commitmentHash = blobhash(blobIndex);
        if (commitmentHash == bytes32(0)) return false;
        
        return success && verifyBlobHash(commitmentHash, commitment);
    } 
}
