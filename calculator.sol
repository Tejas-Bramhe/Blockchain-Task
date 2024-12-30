// SPDX-License-Identifier:MIT
pragma solidity 0.8.26;
contract Calculator{
    uint256 result;
    function add(uint256 num1,uint256 num2) private {
        result=num1+num2;
    }
    function sub(uint256 num1 ,uint256 num2 )private{
        result =num1 -num2; 
    }
    function mul (uint256 num1, uint256 num2) private {
       result=num1 *num2; 
    }
    function divide(uint256 num1,uint256 num2)private{
        if(num2!=0)
        result =num1 /num2;
    }
    function modulo(uint256 num1,uint256 num2)private{
        if(num2!=0)
        result=num1%num2;
    }
    function perform_operation(uint256 num1,uint256 num2,uint8 operation) public {
        if(operation==1)add(num1,num2);
        else if(operation==2)sub(num1 , num2);
        else if(operation==3)mul(num1,num2);
        else if(operation==4)divide(num1,num2); 
        else if (operation==5)modulo(num1,num2);
        else revert("Invalid Operation");
    }
    function get() public view returns (uint256){
        return result;
    }
}