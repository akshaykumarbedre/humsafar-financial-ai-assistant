#!/usr/bin/env python3
"""
Example MCP Tool Integration for Humsafar Financial AI Assistant

This script demonstrates how the finance calculators can be integrated
as MCP tools for LLM workflows.
"""

import json
import inspect
from typing import Dict, Any, List
from humsafar_financial_ai.finance_calculators import *


def extract_function_metadata(func) -> Dict[str, Any]:
    """Extract metadata from a function for MCP tool definition"""
    signature = inspect.signature(func)
    docstring = func.__doc__ or ""
    
    # Extract icon from docstring
    icon = "📊"  # default icon
    if docstring:
        lines = docstring.split('\n')
        for line in lines:
            if line.strip().startswith(('🚨', '🏦', '🎯', '🏠', '📈', '💸', '💼', '🧾', '💰', '📚', '📊', '📉', '💳', '🩺', '💍', '🔨', '⚖️')):
                icon = line.strip().split()[0]
                break
    
    # Extract parameters
    parameters = {}
    for param_name, param in signature.parameters.items():
        param_type = str(param.annotation) if param.annotation != inspect.Parameter.empty else "Any"
        param_default = param.default if param.default != inspect.Parameter.empty else None
        
        parameters[param_name] = {
            "type": param_type,
            "default": param_default,
            "required": param.default == inspect.Parameter.empty
        }
    
    return {
        "name": func.__name__,
        "icon": icon,
        "description": docstring.split('\n')[1].strip() if docstring else "",
        "parameters": parameters,
        "function": func
    }


def create_mcp_tool_definitions() -> List[Dict[str, Any]]:
    """Create MCP tool definitions for all finance calculators"""
    
    # List of all calculator functions
    calculator_functions = [
        emergency_funds_calculator,
        fixed_deposit_calculator,
        mutual_fund_goal_calculator,
        rent_vs_buy_calculator,
        mutual_fund_sip_calculator,
        ppf_calculator,
        nps_calculator,
        hra_calculator,
        gratuity_calculator,
        epf_calculator,
        cagr_calculator,
        inflation_calculator,
        credit_card_interest_calculator,
        personal_loan_emi_calculator,
        medical_loan_emi_calculator,
        marriage_loan_emi_calculator,
        home_renovation_emi_calculator,
        axis_bank_personal_loan_calculator,
        icici_bank_personal_loan_emi_calculator,
        hdfc_bank_personal_loan_calculator,
        net_worth_calculator
    ]
    
    tools = []
    for func in calculator_functions:
        metadata = extract_function_metadata(func)
        
        # Create MCP tool definition
        tool_def = {
            "type": "function",
            "function": {
                "name": metadata["name"],
                "description": f"{metadata['icon']} {metadata['description']}",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            "handler": metadata["function"]
        }
        
        # Add parameter definitions
        for param_name, param_info in metadata["parameters"].items():
            tool_def["function"]["parameters"]["properties"][param_name] = {
                "type": "number" if "float" in param_info["type"] or "int" in param_info["type"] else "string",
                "description": f"Parameter: {param_name}"
            }
            
            if param_info["required"]:
                tool_def["function"]["parameters"]["required"].append(param_name)
        
        tools.append(tool_def)
    
    return tools


def demonstrate_mcp_integration():
    """Demonstrate MCP tool integration"""
    print("=== MCP Tool Integration Demo ===\n")
    
    # Create tool definitions
    tools = create_mcp_tool_definitions()
    
    print(f"Generated {len(tools)} MCP tool definitions:")
    for i, tool in enumerate(tools, 1):
        print(f"{i:2d}. {tool['function']['description']}")
    
    print("\n=== Sample MCP Tool Definition ===")
    sample_tool = tools[0]  # Emergency funds calculator
    print(json.dumps(sample_tool['function'], indent=2))
    
    print("\n=== Sample Tool Execution ===")
    # Execute the emergency funds calculator
    result = emergency_funds_calculator(monthly_expenses=50000, months_coverage=6, current_savings=100000)
    print("Input: monthly_expenses=50000, months_coverage=6, current_savings=100000")
    print("Output:", json.dumps(result, indent=2))
    
    print("\n=== Tool Categories ===")
    categories = {
        "Investment & Savings": ["emergency_funds", "fixed_deposit", "mutual_fund_goal", "mutual_fund_sip", "ppf", "nps", "cagr", "inflation"],
        "Loans & EMI": ["personal_loan", "medical_loan", "marriage_loan", "home_renovation", "axis_bank", "icici_bank", "hdfc_bank", "credit_card"],
        "Tax & Benefits": ["hra", "gratuity", "epf"],
        "Property & Wealth": ["rent_vs_buy", "net_worth"]
    }
    
    for category, tool_names in categories.items():
        print(f"\n{category}:")
        for tool in tools:
            tool_name = tool['function']['name']
            if any(name in tool_name for name in tool_names):
                print(f"  - {tool['function']['description']}")


def mcp_tool_executor(tool_name: str, **kwargs) -> Dict[str, Any]:
    """Execute an MCP tool by name with given parameters"""
    tools = create_mcp_tool_definitions()
    
    for tool in tools:
        if tool['function']['name'] == tool_name:
            try:
                result = tool['handler'](**kwargs)
                return {
                    "success": True,
                    "result": result,
                    "tool_name": tool_name
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "tool_name": tool_name
                }
    
    return {
        "success": False,
        "error": f"Tool '{tool_name}' not found",
        "tool_name": tool_name
    }


if __name__ == "__main__":
    demonstrate_mcp_integration()
    
    print("\n=== Testing MCP Tool Executor ===")
    # Test the tool executor
    result = mcp_tool_executor("emergency_funds_calculator", monthly_expenses=50000, months_coverage=6, current_savings=100000)
    print("Tool Executor Result:", json.dumps(result, indent=2))