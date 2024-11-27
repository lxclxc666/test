Fork Test



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract xReentrancy{
    event Transaction(address from, address to, uint256 amount);

    address public owner;
    mapping(address => uint256) balances;
    bool reentrancyGuard;

    constructor() payable{
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(msg.sender == owner, "Nope");
        _;
    }

    function deposit() external payable{
        balances[msg.sender] += msg.value;
    }

    function transfer(address to, uint256 amount) public{
        require(amount <= balances[msg.sender], "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transaction(msg.sender, to, amount);
    }

    function withdraw() public{
        require(!reentrancyGuard, "Re-Entrancy attack detected!");
        uint256 amount = balances[msg.sender];
        reentrancyGuard = true;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transaction failed.");
        balances[msg.sender] = 0;
        reentrancyGuard = false;
        emit Transaction(address(this), msg.sender, amount);
    }

    function getBalances() public view returns(uint256){
        return balances[msg.sender];
    }
}
```

