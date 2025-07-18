#!/usr/bin/env python3
"""
Test script for FI-MCP Data Access functionality.
Tests all modular functions and validates data access.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humsafar_financial_ai import (
    FIMCPDataAccess,
    get_net_worth,
    get_bank_transactions,
    get_mutual_fund_transactions,
    get_stock_transactions,
    get_epf_details,
    get_credit_report,
    get_complete_profile,
    analyze_user_financial_health,
    get_available_users
)


def test_fi_mcp_data_access():
    """Test FI-MCP Data Access functionality"""
    print("=== FI-MCP Data Access Tests ===\n")
    
    # Test getting available users
    print("📋 Testing get_available_users...")
    users = get_available_users()
    print(f"  Available users: {len(users)}")
    print(f"  Sample users: {users[:5]}")
    print()
    
    # Test with different user personas
    test_users = ["1111111111", "2222222222", "7777777777", "1313131313"]
    
    for user_id in test_users:
        print(f"👤 Testing User: {user_id}")
        
        # Test individual data access functions
        print("📊 Testing get_net_worth...")
        net_worth = get_net_worth(user_id)
        if net_worth:
            try:
                total_worth = net_worth["netWorthResponse"]["totalNetWorthValue"]["units"]
                print(f"  ✅ Net Worth: ₹{total_worth}")
            except KeyError:
                print("  ⚠️  Net worth data structure different")
        else:
            print("  ❌ No net worth data")
        
        print("🏦 Testing get_bank_transactions...")
        bank_txns = get_bank_transactions(user_id)
        if bank_txns:
            txn_count = sum(len(bank.get("txns", [])) for bank in bank_txns.get("bankTransactions", []))
            print(f"  ✅ Bank transactions: {txn_count} transactions")
        else:
            print("  ❌ No bank transaction data")
        
        print("📈 Testing get_mutual_fund_transactions...")
        mf_txns = get_mutual_fund_transactions(user_id)
        if mf_txns:
            fund_count = len(mf_txns.get("mfTransactions", []))
            print(f"  ✅ MF transactions: {fund_count} funds")
        else:
            print("  ❌ No MF transaction data")
        
        print("📊 Testing get_stock_transactions...")
        stock_txns = get_stock_transactions(user_id)
        if stock_txns:
            stock_count = len(stock_txns.get("stockTransactions", []))
            print(f"  ✅ Stock transactions: {stock_count} stocks")
        else:
            print("  ❌ No stock transaction data")
        
        print("🏛️ Testing get_epf_details...")
        epf_data = get_epf_details(user_id)
        if epf_data:
            uan_count = len(epf_data.get("uanAccounts", []))
            print(f"  ✅ EPF data: {uan_count} UAN accounts")
        else:
            print("  ❌ No EPF data")
        
        print("💳 Testing get_credit_report...")
        credit_data = get_credit_report(user_id)
        if credit_data:
            try:
                score = credit_data["creditReports"][0]["creditReportData"]["score"]["bureauScore"]
                print(f"  ✅ Credit score: {score}")
            except (KeyError, IndexError):
                print("  ⚠️  Credit data available but score not accessible")
        else:
            print("  ❌ No credit data")
        
        print("🔍 Testing analyze_user_financial_health...")
        analysis = analyze_user_financial_health(user_id)
        print(f"  📊 Profile completeness: {analysis['profile_completeness']:.1f}%")
        print(f"  📝 Persona: {analysis['persona_description'][:50]}...")
        if 'total_net_worth' in analysis:
            print(f"  💰 Total Net Worth: ₹{analysis['total_net_worth']:,.2f}")
        if 'credit_score' in analysis and analysis['credit_score']:
            print(f"  💳 Credit Score: {analysis['credit_score']}")
        
        print("-" * 50)
        print()


def test_class_based_access():
    """Test class-based data access"""
    print("=== Class-Based FI-MCP Access Tests ===\n")
    
    # Initialize data access
    fi_data = FIMCPDataAccess()
    
    print("📋 Testing FIMCPDataAccess class...")
    users = fi_data.get_available_users()
    print(f"  Available users: {len(users)}")
    
    # Test with a few users
    test_users = users[:3] if len(users) >= 3 else users
    
    for user_id in test_users:
        print(f"\n👤 Testing User: {user_id}")
        
        # Get complete profile
        profile = fi_data.get_complete_profile(user_id)
        data_types = [k for k, v in profile.items() if v is not None and k != 'user_id']
        print(f"  📋 Available data types: {', '.join(data_types)}")
        
        # Get persona description
        persona = fi_data.get_user_persona_description(user_id)
        print(f"  📝 Persona: {persona[:60]}...")
        
        # Analyze financial health
        health = fi_data.analyze_user_financial_health(user_id)
        print(f"  🏥 Health score: {health['profile_completeness']:.1f}%")


def test_integration_example():
    """Test integration with finance calculators"""
    print("=== Integration Example ===\n")
    
    print("🔗 Testing integration with finance calculators...")
    
    # Get a user with good data
    users = get_available_users()
    test_user = "2222222222"  # Wealthy investor
    
    if test_user in users:
        print(f"👤 Analyzing user: {test_user}")
        
        # Get financial data
        analysis = analyze_user_financial_health(test_user)
        net_worth_data = get_net_worth(test_user)
        
        print(f"  📊 Data completeness: {analysis['profile_completeness']:.1f}%")
        print(f"  📝 Persona: {analysis['persona_description'][:50]}...")
        
        if net_worth_data:
            print("  ✅ Net worth data available for calculator integration")
        
        # Example: Combine with finance calculators
        from humsafar_financial_ai import retirement_corpus_calculator, net_worth_calculator
        
        # Example calculation using dummy values based on persona
        if "wealthy" in analysis['persona_description'].lower():
            retirement_calc = retirement_corpus_calculator(
                current_age=35,
                retirement_age=60,
                monthly_expenses=100000,
                inflation_rate=6.0,
                expected_return=12.0,
                current_savings=analysis.get('total_net_worth', 1000000)
            )
            print(f"  🎯 Retirement corpus needed: ₹{retirement_calc['retirement_corpus_needed']:,.2f}")
        
    else:
        print(f"  ❌ Test user {test_user} not available")


def main():
    """Run all tests"""
    print("🧪 Starting FI-MCP Data Access Tests...\n")
    
    try:
        test_fi_mcp_data_access()
        test_class_based_access()
        test_integration_example()
        
        print("✅ All FI-MCP tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()