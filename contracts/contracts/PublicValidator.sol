pragma solidity ^0.4.4;
contract PublicValidator {

    struct Issuer {
		bytes32 name;
    }

    mapping(address => Issuer) issuers;

    function add(address a, bytes32 name) public returns (bool) {
        issuers[a] = name;
        return true;
    }

	function get(address a) public returns (bytes32) {
		return issuers[a].name;
	}
}
