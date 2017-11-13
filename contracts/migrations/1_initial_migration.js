var Migrations = artifacts.require("./Migrations.sol");
var PublicRegister = artifacts.require("./PublicRegister.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(PublicRegister); 
};
