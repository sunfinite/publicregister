### Problem
Fake marks cards continue to be a recurring problem. A recent  case (https://goo.gl/CTuvN2) found 400+ people who secured jobs using such certificates and marks cards and the total beneficiaries of this scam are estimated to be in the thousands. Various universities have proposed solutions such as NFC chips on cards linked to a cloud server (Mangalore Univeristy news report from October 20, 2017: https://goo.gl/GdAEhW). NFC chips require physical changes in the printing process and are costly and moreover cannot be used for existing marks cards. Verifying the validity of these cards publicly is also not simple if each university has its own setup. If we were to overcome adoption difficulties and make all universities use a single secure cloud service, setting up and maintaining such a service would involve significant costs. And even in this scenario, we cannot guarantee that the records on this central server have not been tampered.

### Solution
* We can verify a marks card just by taking a picture of it (directly from a custom app or by uploading to a web service). This is possible because we compute a unique signature for the document and store it on a public blockchain.
* Documents can uploaded in the form of CSV or excel files too (for bulk additions)
* Anyone can verify the validity of a document by recomputing the signature and confirming its presence on the blockchain.
* Adding and modifying signatures to the blockchain can be done only by a known _Issuer_ .
* We have two smart contracts:
	* __PublicRegister.sol__: Implements the actual lookup table for documents and their signatures.	
	* __PublicValidator.sol__: Called by the `PublicRegister` contract to verify if an _Issuer_ is known. This contract can be updated only by a single entity (eg. Department of Education)
* __Partial Proofs__:
	* For marks cards, we extract tabular information and unique ID and compute the signature using a data structure known as the [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree).
	* This enables us to verify a single subject's marks or grade without knowing other grades.


### Demo

* Website: https://sunfinite.tech/publicregister
* Video: 


### Libraries used/Dependencies

* Google Cloud Vision API
* Django
* Ethereum/Solidity
* web3.py
* Testrpc
* Truffle
* Etherparty block explorer
* Android Studio

