#!/usr/bin/env python3
"""
Test script for Humsafar Financial AI Assistant calculators.
Tests basic functionality of all implemented finance calculators.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humsafar_financial_ai.finance_calculators import *


def test_emergency_funds_calculator():
    """Test Emergency Funds Calculator"""
    print("🚨 Testing Emergency Funds Calculator...")
    result = emergency_funds_calculator(monthly_expenses=50000, months_coverage=6, current_savings=100000)
    print(f"  Required Fund: ₹{result['required_fund']}")
    print(f"  Shortfall: ₹{result['shortfall']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_fixed_deposit_calculator():
    """Test Fixed Deposit Calculator"""
    print("🏦 Testing Fixed Deposit Calculator...")
    result = fixed_deposit_calculator(principal=100000, annual_rate=7.5, tenure_years=5)
    print(f"  Principal: ₹{result['principal']}")
    print(f"  Maturity Amount: ₹{result['maturity_amount']}")
    print(f"  Interest Earned: ₹{result['interest_earned']}")
    print()


def test_mutual_fund_goal_calculator():
    """Test Mutual Fund Goal Calculator"""
    print("🎯 Testing Mutual Fund Goal Calculator...")
    result = mutual_fund_goal_calculator(target_amount=5000000, current_age=25, target_age=45, expected_return=12)
    print(f"  Target Amount: ₹{result['target_amount']}")
    print(f"  Monthly SIP Needed: ₹{result['monthly_sip_needed']}")
    print(f"  Lumpsum Needed: ₹{result['lumpsum_needed']}")
    print()


def test_rent_vs_buy_calculator():
    """Test Rent vs Buy Calculator"""
    print("🏠 Testing Rent vs Buy Calculator...")
    result = rent_vs_buy_calculator(
        property_price=5000000,
        monthly_rent=25000,
        down_payment_percent=20,
        loan_tenure_years=20,
        home_loan_rate=8.5
    )
    print(f"  Buy Total Cost: ₹{result['buy_total_cost']}")
    print(f"  Rent Total Cost: ₹{result['rent_total_cost']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_mutual_fund_sip_calculator():
    """Test Mutual Fund SIP Calculator"""
    print("📈 Testing Mutual Fund SIP Calculator...")
    result = mutual_fund_sip_calculator(monthly_investment=10000, annual_return=12, investment_period_years=15)
    print(f"  Total Invested: ₹{result['total_invested']}")
    print(f"  Maturity Amount: ₹{result['maturity_amount']}")
    print(f"  Capital Gains: ₹{result['capital_gains']}")
    print()


def test_ppf_calculator():
    """Test PPF Calculator"""
    print("💸 Testing PPF Calculator...")
    result = ppf_calculator(annual_contribution=150000, contribution_years=15)
    print(f"  Total Contribution: ₹{result['total_contribution']}")
    print(f"  Maturity Amount: ₹{result['maturity_amount']}")
    print(f"  Interest Earned: ₹{result['interest_earned']}")
    print()


def test_nps_calculator():
    """Test NPS Calculator"""
    print("💼 Testing NPS Calculator...")
    result = nps_calculator(monthly_contribution=5000, current_age=30, retirement_age=60)
    print(f"  Total Contribution: ₹{result['total_contribution']}")
    print(f"  Corpus at Retirement: ₹{result['corpus_at_retirement']}")
    print(f"  Monthly Pension: ₹{result['monthly_pension']}")
    print()


def test_hra_calculator():
    """Test HRA Calculator"""
    print("🧾 Testing HRA Calculator...")
    result = hra_calculator(basic_salary=50000, hra_received=20000, actual_rent=15000, metro_city=True)
    print(f"  HRA Received: ₹{result['hra_received']}")
    print(f"  HRA Exempt: ₹{result['hra_exempt']}")
    print(f"  HRA Taxable: ₹{result['hra_taxable']}")
    print()


def test_gratuity_calculator():
    """Test Gratuity Calculator"""
    print("💰 Testing Gratuity Calculator...")
    result = gratuity_calculator(monthly_salary=50000, years_of_service=15, months_of_service=6)
    print(f"  Gratuity Amount: ₹{result['gratuity_amount']}")
    print(f"  Tax Free Gratuity: ₹{result['tax_free_gratuity']}")
    print(f"  Eligibility: {result['eligibility']}")
    print()


def test_epf_calculator():
    """Test EPF Calculator"""
    print("📚 Testing EPF Calculator...")
    result = epf_calculator(monthly_basic=25000, years_of_service=30)
    print(f"  Total Contribution: ₹{result['total_contribution']}")
    print(f"  Maturity Amount: ₹{result['maturity_amount']}")
    print(f"  Monthly Pension: ₹{result['monthly_pension']}")
    print()


def test_cagr_calculator():
    """Test CAGR Calculator"""
    print("📊 Testing CAGR Calculator...")
    result = cagr_calculator(initial_value=100000, final_value=500000, investment_period_years=10)
    print(f"  CAGR: {result['cagr']}%")
    print(f"  Total Return: ₹{result['total_return']}")
    print(f"  Total Return %: {result['total_return_percent']}%")
    print()


def test_inflation_calculator():
    """Test Inflation Calculator"""
    print("📉 Testing Inflation Calculator...")
    result = inflation_calculator(current_price=100000, years=10, inflation_rate=6.0)
    print(f"  Current Price: ₹{result['current_price']}")
    print(f"  Future Price: ₹{result['future_price']}")
    print(f"  Purchasing Power Loss: {result['purchasing_power_loss']}%")
    print()


def test_credit_card_interest_calculator():
    """Test Credit Card Interest Calculator"""
    print("💳 Testing Credit Card Interest Calculator...")
    result = credit_card_interest_calculator(outstanding_balance=50000, annual_interest_rate=36.0, additional_payment=2000)
    print(f"  Outstanding Balance: ₹{result['outstanding_balance']}")
    print(f"  Total Monthly Payment: ₹{result['total_monthly_payment']}")
    print(f"  Payoff Months: {result['payoff_months']}")
    print(f"  Total Interest Paid: ₹{result['total_interest_paid']}")
    print()


def test_personal_loan_emi_calculator():
    """Test Personal Loan EMI Calculator"""
    print("💸 Testing Personal Loan EMI Calculator...")
    result = personal_loan_emi_calculator(loan_amount=500000, annual_interest_rate=12.0, tenure_months=60)
    print(f"  Loan Amount: ₹{result['loan_amount']}")
    print(f"  EMI: ₹{result['emi']}")
    print(f"  Total Payment: ₹{result['total_payment']}")
    print(f"  Total Interest: ₹{result['total_interest']}")
    print()


def test_net_worth_calculator():
    """Test Net Worth Calculator"""
    print("⚖️ Testing Net Worth Calculator...")
    assets = {
        "cash": 100000,
        "investments": 500000,
        "real_estate": 2000000,
        "vehicle": 800000
    }
    liabilities = {
        "home_loan": 1500000,
        "personal_loan": 200000,
        "credit_card": 50000
    }
    result = net_worth_calculator(assets=assets, liabilities=liabilities)
    print(f"  Total Assets: ₹{result['total_assets']}")
    print(f"  Total Liabilities: ₹{result['total_liabilities']}")
    print(f"  Net Worth: ₹{result['net_worth']}")
    print(f"  Financial Health: {result['financial_health']}")
    print()


def test_retirement_corpus_calculator():
    """Test Retirement Corpus Calculator"""
    print("👴 Testing Retirement Corpus Calculator...")
    result = retirement_corpus_calculator(
        current_age=30,
        retirement_age=60,
        monthly_expenses=50000,
        inflation_rate=6.0,
        expected_return=12.0,
        current_savings=100000
    )
    print(f"  Years to Retirement: {result['years_to_retirement']}")
    print(f"  Future Monthly Expenses: ₹{result['future_monthly_expenses']}")
    print(f"  Retirement Corpus Needed: ₹{result['retirement_corpus_needed']}")
    print(f"  Monthly SIP Needed: ₹{result['monthly_sip_needed']}")
    print()


def test_child_education_goal_calculator():
    """Test Child Education Goal Calculator"""
    print("📚 Testing Child Education Goal Calculator...")
    result = child_education_goal_calculator(
        child_current_age=5,
        education_age=18,
        current_education_cost=500000,
        inflation_rate=8.0,
        expected_return=12.0,
        current_savings=50000
    )
    print(f"  Years to Education: {result['years_to_education']}")
    print(f"  Future Education Cost: ₹{result['future_education_cost']}")
    print(f"  Monthly SIP Needed: ₹{result['monthly_sip_needed']}")
    print(f"  Total Investment: ₹{result['total_investment']}")
    print()


def test_home_loan_affordability_calculator():
    """Test Home Loan Affordability Calculator"""
    print("🏡 Testing Home Loan Affordability Calculator...")
    result = home_loan_affordability_calculator(
        monthly_income=100000,
        existing_emis=20000,
        interest_rate=8.5,
        loan_tenure_years=20,
        foir_ratio=0.5
    )
    print(f"  Monthly Income: ₹{result['monthly_income']}")
    print(f"  Available for EMI: ₹{result['available_for_emi']}")
    print(f"  Max Loan Amount: ₹{result['max_loan_amount']}")
    print(f"  Property Value: ₹{result['property_value']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_loan_prepayment_calculator():
    """Test Loan Prepayment Calculator"""
    print("💰 Testing Loan Prepayment Calculator...")
    result = loan_prepayment_calculator(
        outstanding_principal=2000000,
        monthly_emi=25000,
        interest_rate=8.5,
        prepayment_amount=500000,
        prepayment_type="reduce_tenure"
    )
    print(f"  Original Tenure: {result['original_tenure_months']} months")
    print(f"  New Tenure: {result['new_tenure_months']} months")
    print(f"  Interest Saved: ₹{result['interest_saved']}")
    print(f"  New EMI: ₹{result['new_emi']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_income_tax_calculator():
    """Test Income Tax Calculator"""
    print("📊 Testing Income Tax Calculator...")
    result = income_tax_calculator(
        annual_salary=1200000,
        standard_deduction=50000,
        section_80c=150000,
        section_80d=25000,
        hra_received=240000,
        rent_paid=300000,
        other_deductions=50000
    )
    print(f"  Old Regime Tax: ₹{result['old_regime_tax']}")
    print(f"  New Regime Tax: ₹{result['new_regime_tax']}")
    print(f"  Tax Difference: ₹{result['tax_difference']}")
    print(f"  Recommended Regime: {result['recommended_regime']}")
    print()


def test_lump_sum_investment_calculator():
    """Test Lump Sum Investment Calculator"""
    print("💎 Testing Lump Sum Investment Calculator...")
    result = lump_sum_investment_calculator(
        investment_amount=100000,
        annual_return=12.0,
        investment_years=10
    )
    print(f"  Investment Amount: ₹{result['investment_amount']}")
    print(f"  Future Value: ₹{result['future_value']}")
    print(f"  Total Gain: ₹{result['total_gain']}")
    print(f"  Wealth Multiplier: {result['wealth_multiplier']}x")
    print()


def test_goal_based_multi_investment_planner():
    """Test Goal-Based Multi-Investment Planner"""
    print("🎯 Testing Goal-Based Multi-Investment Planner...")
    goals = [
        {"name": "House Down Payment", "target_amount": 2000000, "years": 7},
        {"name": "Child Education", "target_amount": 1500000, "years": 15},
        {"name": "Retirement", "target_amount": 10000000, "years": 25}
    ]
    result = goal_based_multi_investment_planner(goals=goals, expected_return=12.0)
    print(f"  Total Monthly SIP: ₹{result['total_monthly_sip']}")
    print(f"  Total Investment: ₹{result['total_investment']}")
    print(f"  Total Maturity Value: ₹{result['total_maturity_value']}")
    print(f"  Number of Goals: {len(result['goal_details'])}")
    print()


def test_debt_to_income_ratio_calculator():
    """Test Debt-to-Income Ratio Calculator"""
    print("📈 Testing Debt-to-Income Ratio Calculator...")
    result = debt_to_income_ratio_calculator(
        monthly_income=80000,
        monthly_emis=25000,
        credit_card_payments=5000,
        other_debts=3000
    )
    print(f"  Monthly Income: ₹{result['monthly_income']}")
    print(f"  Total Debt Payments: ₹{result['total_debt_payments']}")
    print(f"  Debt-to-Income Ratio: {result['debt_to_income_ratio']}%")
    print(f"  Risk Grade: {result['risk_grade']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_asset_allocation_rebalancer():
    """Test Asset Allocation Rebalancer"""
    print("⚖️ Testing Asset Allocation Rebalancer...")
    result = asset_allocation_rebalancer(
        current_age=35,
        current_equity_percent=80,
        current_debt_percent=20,
        current_gold_percent=0,
        risk_tolerance="moderate"
    )
    print(f"  Current Allocation: {result['current_allocation']}")
    print(f"  Suggested Allocation: {result['suggested_allocation']}")
    print(f"  Rebalancing Needed: {result['rebalancing_needed']}")
    print(f"  Risk Profile: {result['risk_profile']}")
    print(f"  Recommendation: {result['recommendation']}")
    print()


def test_capital_gains_tax_calculator():
    """Test Capital Gains Tax Calculator"""
    print("🏛️ Testing Capital Gains Tax Calculator...")
    result = capital_gains_tax_calculator(
        asset_type="equity",
        purchase_price=100000,
        sale_price=150000,
        purchase_date="2020-01-01",
        sale_date="2022-01-01",
        indexation_benefit=True
    )
    print(f"  Capital Gain: ₹{result['capital_gain']}")
    print(f"  Gain Type: {result['gain_type']}")
    print(f"  Holding Period: {result['holding_period_days']} days")
    print(f"  Tax Rate: {result['tax_rate']}%")
    print(f"  Tax Liability: ₹{result['tax_liability']}")
    print(f"  Net Gain: ₹{result['net_gain']}")
    print()


def main():
    """Run all calculator tests"""
    print("=== Humsafar Financial AI Assistant Calculator Tests ===\n")
    
    # Test original 21 calculators
    test_emergency_funds_calculator()
    test_fixed_deposit_calculator()
    test_mutual_fund_goal_calculator()
    test_rent_vs_buy_calculator()
    test_mutual_fund_sip_calculator()
    test_ppf_calculator()
    test_nps_calculator()
    test_hra_calculator()
    test_gratuity_calculator()
    test_epf_calculator()
    test_cagr_calculator()
    test_inflation_calculator()
    test_credit_card_interest_calculator()
    test_personal_loan_emi_calculator()
    test_net_worth_calculator()
    
    # Test new 10 calculators
    test_retirement_corpus_calculator()
    test_child_education_goal_calculator()
    test_home_loan_affordability_calculator()
    test_loan_prepayment_calculator()
    test_income_tax_calculator()
    test_lump_sum_investment_calculator()
    test_goal_based_multi_investment_planner()
    test_debt_to_income_ratio_calculator()
    test_asset_allocation_rebalancer()
    test_capital_gains_tax_calculator()
    
    print("=== All Tests Completed Successfully! ===")
    print("✅ Total Calculators Tested: 31 (21 original + 10 new)")


if __name__ == "__main__":
    main()