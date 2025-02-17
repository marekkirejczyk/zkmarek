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
        
        require(data.verifyKZGProof(), 'KZG proof verification failed');

        bytes32 blobHash = blobhash(blobIndex);
        require(blobHash != bytes32(0), "Blob not found");
        
        bytes32 commitmentHash = sha256(abi.encodePacked(commitment));
        require(
            uint256(blobHash) & ((1 << 248) - 1) == uint256(commitmentHash) & ((1 << 248) - 1),
            "Blob hash mismatch"
        );
    } 
}