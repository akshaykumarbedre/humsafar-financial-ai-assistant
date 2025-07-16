# Humsafar Financial AI Assistant

A comprehensive suite of financial calculators designed for AI-powered financial decision making and MCP (Model Context Protocol) tool integration. This package provides 31 specialized financial calculators, each optimized for LLM workflows and structured data exchange.

## 🚀 Features

### Core Financial Calculators (21 Original)

1. **🚨 Emergency Funds Calculator** - Calculate required emergency fund coverage
2. **🏦 Fixed Deposit Calculator** - Compute FD maturity and interest
3. **🎯 Mutual Fund Goal Calculator** - Plan investments for financial goals
4. **🏠 Rent vs Buy Calculator** - Compare renting vs buying property
5. **📈 Mutual Fund SIP Calculator** - Estimate SIP returns
6. **💸 PPF Calculator** - Calculate PPF maturity and benefits
7. **💼 NPS Calculator** - Estimate NPS corpus and pension
8. **🧾 HRA Calculator** - Compute HRA tax exemption
9. **💰 Gratuity Calculator** - Calculate gratuity benefits
10. **📚 EPF Calculator** - Compute EPF maturity and pension
11. **📊 CAGR Calculator** - Calculate compound annual growth rate
12. **📉 Inflation Calculator** - Assess inflation impact on savings
13. **💳 Credit Card Interest Calculator** - Calculate credit card payoff scenarios
14. **💸 Personal Loan EMI Calculator** - Compute personal loan EMI
15. **🩺 Medical Loan EMI Calculator** - Calculate medical loan EMI with moratorium
16. **💍 Marriage Loan EMI Calculator** - Estimate marriage loan EMI
17. **🔨 Home Renovation EMI Calculator** - Calculate home renovation loan EMI
18. **🏦 Axis Bank Personal Loan Calculator** - Axis Bank specific loan calculator
19. **🏦 ICICI Bank Personal Loan Calculator** - ICICI Bank specific loan calculator
20. **🏦 HDFC Bank Personal Loan Calculator** - HDFC Bank specific loan calculator
21. **⚖️ Net Worth Calculator** - Calculate net worth and financial health

### Enhanced Financial Calculators (10 New)

22. **👴 Retirement Corpus Calculator** - Plan retirement savings based on current age, expenses, inflation
23. **📚 Child Education Goal Calculator** - Estimate future education costs & plan SIP
24. **🏡 Home Loan Affordability Calculator** - Estimate how much home loan user can afford
25. **💰 Loan Prepayment Calculator** - Calculate interest saved or tenure reduced
26. **📊 Income Tax Calculator (Old vs New)** - Compare tax liability under both regimes
27. **💎 Lump Sum Investment Calculator** - Project value of one-time investment
28. **🎯 Goal-Based Multi-Investment Planner** - Track multiple financial goals via SIPs
29. **📈 Debt-to-Income Ratio Calculator** - Check financial leverage
30. **⚖️ Asset Allocation Rebalancer** - Recommend mix of equity/debt/gold
31. **🏛️ Capital Gains Tax Calculator** - Calculate STCG or LTCG based on asset type

## 🛠️ Installation

```bash
git clone https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant.git
cd humsafar-financial-ai-assistant
pip install -e .
```

## 📖 Usage

### Basic Usage

```python
from humsafar_financial_ai.finance_calculators import (
    emergency_funds_calculator,
    fixed_deposit_calculator,
    mutual_fund_sip_calculator,
    net_worth_calculator,
    retirement_corpus_calculator,
    child_education_goal_calculator,
    home_loan_affordability_calculator,
    income_tax_calculator,
    capital_gains_tax_calculator
)

# Calculate emergency fund requirement
emergency_result = emergency_funds_calculator(
    monthly_expenses=50000,
    months_coverage=6,
    current_savings=100000
)
print(f"Emergency Fund Required: ₹{emergency_result['required_fund']}")

# Calculate FD maturity
fd_result = fixed_deposit_calculator(
    principal=100000,
    annual_rate=7.5,
    tenure_years=5
)
print(f"FD Maturity Amount: ₹{fd_result['maturity_amount']}")

# Calculate SIP returns
sip_result = mutual_fund_sip_calculator(
    monthly_investment=10000,
    annual_return=12,
    investment_period_years=15
)
print(f"SIP Maturity Amount: ₹{sip_result['maturity_amount']}")

# Calculate net worth
assets = {
    "cash": 100000,
    "investments": 500000,
    "real_estate": 2000000
}
liabilities = {
    "home_loan": 1500000,
    "personal_loan": 200000
}
net_worth_result = net_worth_calculator(assets=assets, liabilities=liabilities)
print(f"Net Worth: ₹{net_worth_result['net_worth']}")
```

### Enhanced Calculators Usage

```python
# Plan retirement corpus
retirement_result = retirement_corpus_calculator(
    current_age=30,
    retirement_age=60,
    monthly_expenses=50000,
    inflation_rate=6.0,
    expected_return=12.0,
    current_savings=100000
)
print(f"Retirement Corpus Needed: ₹{retirement_result['retirement_corpus_needed']}")
print(f"Monthly SIP Required: ₹{retirement_result['monthly_sip_needed']}")

# Calculate child education goal
education_result = child_education_goal_calculator(
    child_current_age=5,
    education_age=18,
    current_education_cost=500000,
    inflation_rate=8.0,
    expected_return=12.0,
    current_savings=50000
)
print(f"Future Education Cost: ₹{education_result['future_education_cost']}")
print(f"Monthly SIP Needed: ₹{education_result['monthly_sip_needed']}")

# Check home loan affordability
affordability_result = home_loan_affordability_calculator(
    monthly_income=100000,
    existing_emis=20000,
    interest_rate=8.5,
    loan_tenure_years=20
)
print(f"Max Loan Amount: ₹{affordability_result['max_loan_amount']}")
print(f"Property Value: ₹{affordability_result['property_value']}")

# Compare tax regimes
tax_result = income_tax_calculator(
    annual_salary=1200000,
    section_80c=150000,
    hra_received=240000,
    rent_paid=300000
)
print(f"Old Regime Tax: ₹{tax_result['old_regime_tax']}")
print(f"New Regime Tax: ₹{tax_result['new_regime_tax']}")
print(f"Recommended: {tax_result['recommended_regime']}")

# Calculate capital gains tax
capital_gains_result = capital_gains_tax_calculator(
    asset_type="equity",
    purchase_price=100000,
    sale_price=150000,
    purchase_date="2020-01-01",
    sale_date="2022-01-01"
)
print(f"Capital Gain: ₹{capital_gains_result['capital_gain']}")
print(f"Tax Liability: ₹{capital_gains_result['tax_liability']}")
print(f"Net Gain: ₹{capital_gains_result['net_gain']}")
```

### Testing the Calculators

```bash
python test_calculators.py
```

## 🔧 MCP Tool Integration

All calculators are designed to be MCP tool-ready with:

- **Structured Input/Output**: All functions accept parameters and return structured dictionaries
- **JSON Serializable**: All return values are JSON serializable for easy API integration
- **Comprehensive Docstrings**: Each function has detailed documentation for parameter types and return values
- **Error Handling**: Robust error handling with informative error messages
- **Category Icons**: Each calculator has a unique emoji icon for UI/UX clarity

### Example MCP Tool Definition

```python
def create_mcp_tool_definition(calculator_func):
    """Convert calculator function to MCP tool definition"""
    return {
        "name": calculator_func.__name__,
        "description": calculator_func.__doc__.split('\n')[1].strip(),
        "parameters": extract_parameters(calculator_func),
        "returns": "Dict[str, Union[float, str]]"
    }
```

## 📊 Function Categories

### Investment & Savings
- Emergency Funds Calculator
- Fixed Deposit Calculator
- Mutual Fund Goal Calculator
- Mutual Fund SIP Calculator
- PPF Calculator
- NPS Calculator
- CAGR Calculator
- Inflation Calculator

### Loans & EMI
- Personal Loan EMI Calculator
- Medical Loan EMI Calculator
- Marriage Loan EMI Calculator
- Home Renovation EMI Calculator
- Axis Bank Personal Loan Calculator
- ICICI Bank Personal Loan Calculator
- HDFC Bank Personal Loan Calculator
- Credit Card Interest Calculator

### Tax & Benefits
- HRA Calculator
- Gratuity Calculator
- EPF Calculator

### Property & Wealth
- Rent vs Buy Calculator
- Net Worth Calculator

## 🧮 Calculator Details

### Emergency Funds Calculator 🚨
Calculates required emergency fund based on monthly expenses and desired coverage period.

**Parameters:**
- `monthly_expenses`: Monthly household expenses
- `months_coverage`: Number of months of coverage (default: 6)
- `current_savings`: Current emergency fund savings

**Returns:**
- Required fund amount
- Current coverage in months
- Shortfall amount
- Personalized recommendation

### Fixed Deposit Calculator 🏦
Computes maturity amount and interest for fixed deposits with compound interest.

**Parameters:**
- `principal`: Initial deposit amount
- `annual_rate`: Annual interest rate (percentage)
- `tenure_years`: Investment tenure in years
- `compounding_frequency`: Compounding frequency per year

**Returns:**
- Maturity amount
- Interest earned
- Effective annual rate
- Monthly interest

### Mutual Fund SIP Calculator 📈
Estimates returns from systematic investment plans with optional step-up.

**Parameters:**
- `monthly_investment`: Monthly SIP amount
- `annual_return`: Expected annual return (percentage)
- `investment_period_years`: Investment period in years
- `step_up_percent`: Annual step-up percentage (optional)

**Returns:**
- Total invested amount
- Maturity amount
- Capital gains
- Average monthly return

### Net Worth Calculator ⚖️
Computes comprehensive net worth analysis with financial health assessment.

**Parameters:**
- `assets`: Dictionary of asset categories and values
- `liabilities`: Dictionary of liability categories and values

**Returns:**
- Total assets and liabilities
- Net worth
- Asset and liability breakdown
- Debt-to-asset ratio
- Financial health assessment

## 🔍 Error Handling

All calculators include comprehensive error handling:

```python
result = mutual_fund_goal_calculator(
    target_amount=5000000,
    current_age=45,
    target_age=25,  # Invalid: target age < current age
    expected_return=12
)
# Returns: {"error": "Target age must be greater than current age"}
```

## 📚 API Documentation

Each function returns a structured dictionary with:
- `icon`: Category emoji for UI display
- Calculated values (all rounded to 2 decimal places)
- Additional metadata and recommendations
- Error messages when applicable

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Designed for integration with AI/LLM systems
- Follows Indian financial regulations and tax structures
- Optimized for MCP (Model Context Protocol) tool integration
- Built with Python standard library for maximum compatibility

## 🔗 Links

- [GitHub Repository](https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant)
- [Issue Tracker](https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant/issues)
- [Documentation](https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant/blob/main/README.md)

---

Built with ❤️ for the AI and Financial Technology community.
