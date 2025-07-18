#!/usr/bin/env python3
"""
Complete Integration Example: FI-MCP Data + Finance Calculators

This example demonstrates how to use FI-MCP dummy data with the finance
calculators to create comprehensive financial analysis for different user personas.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humsafar_financial_ai import (
    # FI-MCP Data Access
    FIMCPDataAccess,
    analyze_user_financial_health,
    get_complete_profile,
    get_net_worth,
    get_credit_report,
    get_epf_details,
    
    # Finance Calculators
    emergency_funds_calculator,
    retirement_corpus_calculator,
    net_worth_calculator,
    debt_to_income_ratio_calculator,
    asset_allocation_rebalancer,
    home_loan_affordability_calculator,
    income_tax_calculator
)


def comprehensive_financial_analysis(user_id: str):
    """
    Perform comprehensive financial analysis using FI-MCP data and calculators.
    
    Args:
        user_id: Phone number representing user persona
        
    Returns:
        Dict containing complete financial analysis
    """
    print(f"🔍 Comprehensive Financial Analysis for User: {user_id}")
    print("=" * 60)
    
    # Initialize data access
    fi_data = FIMCPDataAccess()
    
    # Get user profile and analysis
    profile = fi_data.get_complete_profile(user_id)
    health_analysis = fi_data.analyze_user_financial_health(user_id)
    persona = fi_data.get_user_persona_description(user_id)
    
    print(f"👤 User Persona: {persona}")
    print(f"📊 Profile Completeness: {health_analysis['profile_completeness']:.1f}%")
    print()
    
    analysis_results = {
        "user_id": user_id,
        "persona": persona,
        "data_completeness": health_analysis['profile_completeness'],
        "recommendations": []
    }
    
    # 1. Net Worth Analysis
    print("💰 NET WORTH ANALYSIS")
    print("-" * 30)
    
    if profile["net_worth"]:
        try:
            net_worth_raw = float(profile["net_worth"]["netWorthResponse"]["totalNetWorthValue"]["units"])
            print(f"Current Net Worth: ₹{net_worth_raw:,.2f}")
            
            # Simulate asset/liability breakdown for calculator
            if net_worth_raw > 0:
                # Positive net worth - estimate assets and liabilities
                estimated_assets = {"investments": net_worth_raw * 0.8, "cash": net_worth_raw * 0.2}
                estimated_liabilities = {"loans": max(0, net_worth_raw * 0.1)}
            else:
                # Negative net worth - high liabilities
                estimated_assets = {"investments": 100000, "cash": 50000}
                estimated_liabilities = {"loans": abs(net_worth_raw) + 150000}
            
            nw_analysis = net_worth_calculator(estimated_assets, estimated_liabilities)
            print(f"Financial Health: {nw_analysis.get('financial_health', 'Unknown')}")
            
            analysis_results["net_worth"] = {
                "current": net_worth_raw,
                "health_status": nw_analysis.get('financial_health', 'Unknown')
            }
            
            if net_worth_raw < 500000:
                analysis_results["recommendations"].append("💡 Focus on wealth building - Net worth below ₹5L")
                
        except (KeyError, ValueError, TypeError):
            print("Net worth data not accessible")
    else:
        print("No net worth data available")
    
    print()
    
    # 2. Credit Score Analysis
    print("💳 CREDIT ANALYSIS")
    print("-" * 20)
    
    if profile["credit_report"]:
        try:
            credit_data = profile["credit_report"]["creditReports"][0]["creditReportData"]
            credit_score = int(credit_data["score"]["bureauScore"])
            print(f"Credit Score: {credit_score}")
            
            # Credit score recommendations
            if credit_score < 650:
                analysis_results["recommendations"].append("🚨 Urgent: Improve credit score (currently < 650)")
            elif credit_score < 750:
                analysis_results["recommendations"].append("⚠️ Work on improving credit score to 750+")
            else:
                analysis_results["recommendations"].append("✅ Excellent credit score maintained")
            
            analysis_results["credit_score"] = credit_score
            
            # Analyze outstanding balances
            total_outstanding = int(credit_data["creditAccount"]["creditAccountSummary"]["totalOutstandingBalance"]["outstandingBalanceAll"])
            print(f"Total Outstanding: ₹{total_outstanding:,}")
            
            if total_outstanding > 100000:
                analysis_results["recommendations"].append("💸 High credit utilization - consider debt consolidation")
                
        except (KeyError, ValueError, IndexError):
            print("Credit score not accessible")
    else:
        print("No credit report available")
    
    print()
    
    # 3. Emergency Fund Analysis
    print("🚨 EMERGENCY FUND ANALYSIS")
    print("-" * 30)
    
    # Estimate monthly expenses based on persona
    monthly_expenses = estimate_monthly_expenses(persona, profile)
    current_savings = estimate_liquid_savings(profile)
    
    emergency_analysis = emergency_funds_calculator(
        monthly_expenses=monthly_expenses,
        months_coverage=6,
        current_savings=current_savings
    )
    
    print(f"Estimated Monthly Expenses: ₹{monthly_expenses:,}")
    print(f"Emergency Fund Required: ₹{emergency_analysis['required_fund']:,}")
    print(f"Current Coverage: {emergency_analysis['months_covered']:.1f} months")
    print(f"Recommendation: {emergency_analysis['recommendation']}")
    
    analysis_results["emergency_fund"] = emergency_analysis
    
    if emergency_analysis['shortfall'] > 0:
        analysis_results["recommendations"].append(f"🚨 Build emergency fund: ₹{emergency_analysis['shortfall']:,} needed")
    
    print()
    
    # 4. Retirement Planning
    print("👴 RETIREMENT PLANNING")
    print("-" * 25)
    
    # Estimate age based on persona
    current_age = estimate_age_from_persona(persona)
    
    retirement_analysis = retirement_corpus_calculator(
        current_age=current_age,
        retirement_age=60,
        monthly_expenses=monthly_expenses,
        inflation_rate=6.0,
        expected_return=12.0,
        current_savings=health_analysis.get('total_net_worth', 0)
    )
    
    print(f"Estimated Current Age: {current_age}")
    print(f"Retirement Corpus Needed: ₹{retirement_analysis['retirement_corpus_needed']:,.2f}")
    print(f"Monthly SIP Required: ₹{retirement_analysis['monthly_sip_needed']:,.2f}")
    
    analysis_results["retirement"] = retirement_analysis
    
    if retirement_analysis['monthly_sip_needed'] > monthly_expenses * 0.3:
        analysis_results["recommendations"].append("⚠️ Retirement planning requires significant investment - consider longer timeline")
    
    print()
    
    # 5. Investment Pattern Analysis
    print("📈 INVESTMENT ANALYSIS")
    print("-" * 25)
    
    mf_count = len(profile.get("mutual_fund_transactions", {}).get("mfTransactions", []))
    stock_count = len(profile.get("stock_transactions", {}).get("stockTransactions", []))
    
    print(f"Mutual Funds: {mf_count}")
    print(f"Stocks: {stock_count}")
    
    # Asset allocation analysis
    asset_allocation = asset_allocation_rebalancer(
        current_age=current_age,
        current_equity_percent=60,
        current_debt_percent=30,
        current_gold_percent=10,
        risk_tolerance="moderate"
    )
    
    print(f"Recommended Asset Allocation: {asset_allocation['suggested_allocation']}")
    print(f"Recommendation: {asset_allocation['recommendation']}")
    
    analysis_results["investment"] = {
        "mf_funds": mf_count,
        "stocks": stock_count,
        "asset_allocation": asset_allocation
    }
    
    if mf_count < 3:
        analysis_results["recommendations"].append("📈 Consider diversifying mutual fund portfolio")
    
    print()
    
    # 6. Home Loan Affordability (if applicable)
    if "salary" in persona.lower() or "income" in persona.lower():
        print("🏠 HOME LOAN AFFORDABILITY")
        print("-" * 30)
        
        estimated_income = estimate_monthly_income(persona)
        affordability = home_loan_affordability_calculator(
            monthly_income=estimated_income,
            existing_emis=monthly_expenses * 0.2,  # Assume 20% of expenses are EMIs
            interest_rate=8.5,
            loan_tenure_years=20
        )
        
        print(f"Estimated Monthly Income: ₹{estimated_income:,}")
        print(f"Max Loan Amount: ₹{affordability['max_loan_amount']:,.2f}")
        print(f"Property Value Affordable: ₹{affordability['property_value']:,.2f}")
        print(f"Recommendation: {affordability['recommendation']}")
        
        analysis_results["home_loan"] = affordability
    
    print()
    print("📋 SUMMARY RECOMMENDATIONS:")
    print("-" * 30)
    for i, rec in enumerate(analysis_results["recommendations"], 1):
        print(f"{i}. {rec}")
    
    print()
    print("=" * 60)
    
    return analysis_results


def estimate_monthly_expenses(persona: str, profile: dict) -> float:
    """Estimate monthly expenses based on persona"""
    if "high income" in persona.lower() or "salary > ₹2l" in persona:
        return 80000
    elif "live-for-today" in persona.lower():
        return 150000
    elif "early retirement" in persona.lower() or "frugal" in persona.lower():
        return 30000
    elif "starter" in persona.lower() or "minimal" in persona.lower():
        return 25000
    elif "wealthy" in persona.lower() or "inheritance" in persona.lower():
        return 60000
    else:
        return 40000


def estimate_liquid_savings(profile: dict) -> float:
    """Estimate liquid savings from net worth"""
    if profile.get("net_worth"):
        try:
            net_worth = float(profile["net_worth"]["netWorthResponse"]["totalNetWorthValue"]["units"])
            # Assume 20% of net worth is liquid
            return max(0, net_worth * 0.2)
        except (KeyError, ValueError):
            pass
    return 50000  # Default


def estimate_age_from_persona(persona: str) -> int:
    """Estimate age based on persona description"""
    if "early retirement" in persona.lower():
        return 28
    elif "starter" in persona.lower() or "recently" in persona.lower():
        return 25
    elif "old" in persona.lower() or "stagnant" in persona.lower():
        return 45
    elif "experienced" in persona.lower():
        return 35
    else:
        return 30


def estimate_monthly_income(persona: str) -> float:
    """Estimate monthly income based on persona"""
    if "high income" in persona.lower() or "salary > ₹2l" in persona:
        return 250000
    elif "dual income" in persona.lower():
        return 120000
    elif "starter" in persona.lower():
        return 50000
    elif "salary sinkhole" in persona.lower():
        return 80000
    else:
        return 75000


def main():
    """Run comprehensive analysis for different user personas"""
    print("🏦 Humsafar Financial AI - Complete Integration Demo")
    print("=" * 60)
    print()
    
    # Test different personas
    test_users = [
        "2222222222",  # Wealthy Investor
        "7777777777",  # Debt-Heavy Low Performer  
        "1313131313",  # Balanced Growth Tracker
        "2020202020",  # Starter Saver
    ]
    
    for user_id in test_users:
        try:
            result = comprehensive_financial_analysis(user_id)
            print(f"✅ Analysis completed for {user_id}")
            print()
        except Exception as e:
            print(f"❌ Analysis failed for {user_id}: {e}")
            print()
    
    print("🎉 Complete integration demo finished!")


if __name__ == "__main__":
    main()