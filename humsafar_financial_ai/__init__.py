"""
Humsafar Financial AI Assistant

A comprehensive suite of financial calculators and tools designed for 
AI-powered financial decision making and MCP tool integration.
"""

__version__ = "1.0.0"
__author__ = "Akshay Kumar Bedre"
__email__ = "your.email@example.com"

from .finance_calculators import *
from .fi_mcp_data_access import *

__all__ = [
    # Finance Calculators
    "emergency_funds_calculator",
    "fixed_deposit_calculator", 
    "mutual_fund_goal_calculator",
    "rent_vs_buy_calculator",
    "mutual_fund_sip_calculator",
    "ppf_calculator",
    "nps_calculator",
    "hra_calculator",
    "gratuity_calculator",
    "epf_calculator",
    "cagr_calculator",
    "inflation_calculator",
    "credit_card_interest_calculator",
    "personal_loan_emi_calculator",
    "medical_loan_emi_calculator",
    "marriage_loan_emi_calculator",
    "home_renovation_emi_calculator",
    "axis_bank_personal_loan_calculator",
    "icici_bank_personal_loan_emi_calculator",
    "hdfc_bank_personal_loan_calculator",
    "net_worth_calculator",
    "retirement_corpus_calculator",
    "child_education_goal_calculator",
    "home_loan_affordability_calculator",
    "loan_prepayment_calculator",
    "income_tax_calculator",
    "lump_sum_investment_calculator",
    "goal_based_multi_investment_planner",
    "debt_to_income_ratio_calculator",
    "asset_allocation_rebalancer",
    "capital_gains_tax_calculator",
    
    # FI-MCP Data Access
    "FIMCPDataAccess",
    "get_net_worth",
    "get_bank_transactions",
    "get_mutual_fund_transactions",
    "get_stock_transactions",
    "get_epf_details",
    "get_credit_report",
    "get_complete_profile",
    "analyze_user_financial_health",
    "get_available_users"
]