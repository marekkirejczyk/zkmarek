// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract KZGBlobVerifier {
    address constant POINT_EVALUATION = 0x0A;

    /**
     * @notice Verify KZG proof that p(x) == y where p(x) is the polynomial
     * represented by the KZG commitment. Receives inputs as bytes.
     */
    function verifyBlobKZG(
        uint256 blobIndex,
        bytes48 commitment,
        bytes32 x,
        bytes32 y,
        bytes48 proof
    ) public view returns (bool) {
        bytes32 versionedHash = blobhash(blobIndex);
        if (versionedHash == bytes32(0)) return false;
        
        (bool success,) = POINT_EVALUATION.staticcall(
            abi.encodePacked(commitment, x, y, proof)
        );
        
        return success && verifyVersionedHash(versionedHash, commitment);
    }

    function verifyVersionedHash(bytes32 versionedHash, bytes48 commitment) internal pure returns (bool) {
        if (uint8(uint256(versionedHash) >> 248) != 0x01) return false;
        
        bytes32 commitmentHash = sha256(abi.encodePacked(commitment));
        return uint256(versionedHash) & ((1 << 248) - 1) == uint256(commitmentHash) & ((1 << 248) - 1);
    }
}
