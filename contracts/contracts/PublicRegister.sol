pragma solidity ^0.4.4;
contract PublicRegister {

    struct Entry {
		bytes32 hash;
        address issuer;
		address owner;
    }

    mapping(bytes32 => Entry) entries;

    function add(bytes32 key, bytes32 hash) public returns (bool) {
		if (entries[key].hash == '') {
			entries[key].hash = hash;
			entries[key].owner = msg.sender;
			entries[key].issuer = msg.sender;
			return true;
		}
		else {
			require (entries[key].owner == msg.sender);
			entries[key].hash = hash;
			return true;
		}
		return false;
    }

	function get(bytes32 key) public returns (bytes32) {
		return entries[key].hash;
	}
}
