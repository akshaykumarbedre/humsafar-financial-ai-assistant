"""
Finance Decision Performance Functions for MCP Tool Integration

This module contains a comprehensive suite of financial calculators designed
for AI-powered financial decision making and MCP tool integration.
Each function is well-documented and returns structured data for easy
integration with LLM workflows.
"""

import math
from typing import Dict, List, Optional, Union


def emergency_funds_calculator(
    monthly_expenses: float,
    months_coverage: int = 6,
    current_savings: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    🚨 Emergency Funds Calculator
    
    Calculates the required emergency fund based on monthly expenses and
    desired coverage period.
    
    Args:
        monthly_expenses: Monthly household expenses in currency units
        months_coverage: Number of months of coverage desired (default: 6)
        current_savings: Current emergency fund savings (default: 0.0)
        
    Returns:
        Dict containing:
            - required_fund: Total emergency fund needed
            - current_savings: Current emergency fund amount
            - shortfall: Additional amount needed
            - months_covered: Current months covered by existing savings
            - recommendation: Personalized advice
    """
    required_fund = monthly_expenses * months_coverage
    shortfall = max(0, required_fund - current_savings)
    months_covered = current_savings / monthly_expenses if monthly_expenses > 0 else 0
    
    if shortfall == 0:
        recommendation = "✅ You have adequate emergency funds!"
    elif months_covered >= 3:
        recommendation = "⚠️ You have partial coverage. Consider building up to full coverage."
    else:
        recommendation = "🚨 Critical: Build emergency fund immediately!"
    
    return {
        "icon": "🚨",
        "required_fund": round(required_fund, 2),
        "current_savings": round(current_savings, 2),
        "shortfall": round(shortfall, 2),
        "months_covered": round(months_covered, 1),
        "recommendation": recommendation
    }


def fixed_deposit_calculator(
    principal: float,
    annual_rate: float,
    tenure_years: float,
    compounding_frequency: int = 4
) -> Dict[str, Union[float, str]]:
    """
    🏦 Fixed Deposit Calculator
    
    Computes maturity amount and interest earned for fixed deposits.
    
    Args:
        principal: Initial deposit amount
        annual_rate: Annual interest rate (as percentage, e.g., 7.5 for 7.5%)
        tenure_years: Investment tenure in years
        compounding_frequency: Compounding frequency per year (default: 4 for quarterly)
        
    Returns:
        Dict containing:
            - principal: Initial investment
            - maturity_amount: Final amount after tenure
            - interest_earned: Total interest earned
            - effective_rate: Effective annual rate
            - monthly_interest: Average monthly interest
    """
    rate_decimal = annual_rate / 100
    maturity_amount = principal * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * tenure_years)
    interest_earned = maturity_amount - principal
    effective_rate = ((maturity_amount / principal) ** (1 / tenure_years) - 1) * 100
    monthly_interest = interest_earned / (tenure_years * 12)
    
    return {
        "icon": "🏦",
        "principal": round(principal, 2),
        "maturity_amount": round(maturity_amount, 2),
        "interest_earned": round(interest_earned, 2),
        "effective_rate": round(effective_rate, 2),
        "monthly_interest": round(monthly_interest, 2)
    }


def mutual_fund_goal_calculator(
    target_amount: float,
    current_age: int,
    target_age: int,
    expected_return: float,
    current_investment: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    🎯 Mutual Fund Goal Calculator
    
    Determines investment required to reach a future financial goal via mutual funds.
    
    Args:
        target_amount: Target corpus amount
        current_age: Current age
        target_age: Age when target is needed
        expected_return: Expected annual return (as percentage)
        current_investment: Current mutual fund investment value (default: 0.0)
        
    Returns:
        Dict containing:
            - target_amount: Goal amount
            - years_to_goal: Time remaining
            - monthly_sip_needed: Required monthly SIP
            - lumpsum_needed: Required lumpsum investment today
            - current_investment: Current investment value
            - projected_current_value: Future value of current investment
    """
    years_to_goal = target_age - current_age
    if years_to_goal <= 0:
        return {
            "icon": "🎯",
            "error": "Target age must be greater than current age"
        }
    
    monthly_rate = expected_return / 100 / 12
    months = years_to_goal * 12
    
    # Future value of current investment
    projected_current_value = current_investment * (1 + expected_return / 100) ** years_to_goal
    
    # Remaining amount needed
    remaining_amount = target_amount - projected_current_value
    
    # Monthly SIP calculation
    if remaining_amount > 0:
        monthly_sip_needed = remaining_amount * monthly_rate / ((1 + monthly_rate) ** months - 1)
    else:
        monthly_sip_needed = 0
    
    # Lumpsum needed today
    lumpsum_needed = remaining_amount / (1 + expected_return / 100) ** years_to_goal
    
    return {
        "icon": "🎯",
        "target_amount": round(target_amount, 2),
        "years_to_goal": years_to_goal,
        "monthly_sip_needed": round(monthly_sip_needed, 2),
        "lumpsum_needed": round(max(0, lumpsum_needed), 2),
        "current_investment": round(current_investment, 2),
        "projected_current_value": round(projected_current_value, 2)
    }


def rent_vs_buy_calculator(
    property_price: float,
    monthly_rent: float,
    down_payment_percent: float,
    loan_tenure_years: int,
    home_loan_rate: float,
    annual_rent_increase: float = 3.0,
    annual_property_appreciation: float = 5.0,
    maintenance_percent: float = 1.0
) -> Dict[str, Union[float, str]]:
    """
    🏠 Rent vs Buy Calculator
    
    Compares the long-term financial impact of renting vs buying a property.
    
    Args:
        property_price: Current property price
        monthly_rent: Current monthly rent
        down_payment_percent: Down payment as percentage of property price
        loan_tenure_years: Home loan tenure in years
        home_loan_rate: Home loan interest rate (as percentage)
        annual_rent_increase: Annual rent increase rate (default: 3.0%)
        annual_property_appreciation: Annual property appreciation rate (default: 5.0%)
        maintenance_percent: Annual maintenance cost as % of property value (default: 1.0%)
        
    Returns:
        Dict containing:
            - buy_total_cost: Total cost of buying over loan tenure
            - rent_total_cost: Total cost of renting over same period
            - property_value_after_tenure: Property value after loan tenure
            - net_buying_cost: Net cost after considering property appreciation
            - recommendation: Buy vs Rent recommendation
    """
    down_payment = property_price * down_payment_percent / 100
    loan_amount = property_price - down_payment
    
    # EMI calculation
    monthly_rate = home_loan_rate / 100 / 12
    months = loan_tenure_years * 12
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    
    # Total buying costs
    total_emi_paid = emi * months
    annual_maintenance = property_price * maintenance_percent / 100
    total_maintenance = annual_maintenance * loan_tenure_years
    buy_total_cost = down_payment + total_emi_paid + total_maintenance
    
    # Total renting costs
    total_rent = 0
    current_rent = monthly_rent
    for year in range(loan_tenure_years):
        total_rent += current_rent * 12
        current_rent *= (1 + annual_rent_increase / 100)
    
    # Property value after tenure
    property_value_after_tenure = property_price * (1 + annual_property_appreciation / 100) ** loan_tenure_years
    
    # Net cost considering property appreciation
    net_buying_cost = buy_total_cost - property_value_after_tenure
    
    if net_buying_cost < total_rent:
        recommendation = "🏠 Buying is more advantageous"
    else:
        recommendation = "🏠 Renting is more cost-effective"
    
    return {
        "icon": "🏠",
        "buy_total_cost": round(buy_total_cost, 2),
        "rent_total_cost": round(total_rent, 2),
        "property_value_after_tenure": round(property_value_after_tenure, 2),
        "net_buying_cost": round(net_buying_cost, 2),
        "monthly_emi": round(emi, 2),
        "down_payment": round(down_payment, 2),
        "recommendation": recommendation
    }


def mutual_fund_sip_calculator(
    monthly_investment: float,
    annual_return: float,
    investment_period_years: int,
    step_up_percent: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    📈 Mutual Fund SIP Calculator
    
    Estimates returns from systematic investment plans in mutual funds.
    
    Args:
        monthly_investment: Monthly SIP amount
        annual_return: Expected annual return (as percentage)
        investment_period_years: Investment period in years
        step_up_percent: Annual step-up percentage (default: 0.0)
        
    Returns:
        Dict containing:
            - total_invested: Total amount invested
            - maturity_amount: Final corpus value
            - capital_gains: Total capital gains
            - monthly_return: Average monthly return
            - annual_return_rate: Effective annual return rate
    """
    monthly_rate = annual_return / 100 / 12
    total_invested = 0
    maturity_amount = 0
    current_sip = monthly_investment
    
    for year in range(investment_period_years):
        for month in range(12):
            total_invested += current_sip
            # Calculate future value of this SIP payment
            remaining_months = (investment_period_years - year) * 12 - month
            maturity_amount += current_sip * (1 + monthly_rate) ** remaining_months
        
        # Step up SIP amount for next year
        current_sip *= (1 + step_up_percent / 100)
    
    capital_gains = maturity_amount - total_invested
    monthly_return = capital_gains / (investment_period_years * 12)
    
    return {
        "icon": "📈",
        "total_invested": round(total_invested, 2),
        "maturity_amount": round(maturity_amount, 2),
        "capital_gains": round(capital_gains, 2),
        "monthly_return": round(monthly_return, 2),
        "annual_return_rate": annual_return
    }


def ppf_calculator(
    annual_contribution: float,
    contribution_years: int = 15,
    interest_rate: float = 7.1,
    extend_years: int = 0
) -> Dict[str, Union[float, str]]:
    """
    💸 PPF Calculator
    
    Calculates projected returns and maturity from Public Provident Fund contributions.
    
    Args:
        annual_contribution: Annual PPF contribution (max 1.5 lakh)
        contribution_years: Years of contribution (default: 15)
        interest_rate: PPF interest rate (default: 7.1%)
        extend_years: Years to extend after maturity (default: 0)
        
    Returns:
        Dict containing:
            - total_contribution: Total amount contributed
            - maturity_amount: Amount at maturity
            - interest_earned: Total interest earned
            - extended_amount: Amount after extension (if applicable)
            - tax_benefit: Tax benefit under 80C
    """
    # Ensure contribution is within limits
    annual_contribution = min(annual_contribution, 150000)
    
    # Calculate maturity amount
    rate = interest_rate / 100
    maturity_amount = annual_contribution * (((1 + rate) ** contribution_years - 1) / rate)
    total_contribution = annual_contribution * contribution_years
    interest_earned = maturity_amount - total_contribution
    
    # Calculate extended amount if applicable
    extended_amount = maturity_amount
    if extend_years > 0:
        extended_amount = maturity_amount * (1 + rate) ** extend_years
    
    # Tax benefit (80C deduction)
    tax_benefit = annual_contribution * 0.3  # Assuming 30% tax bracket
    
    return {
        "icon": "💸",
        "total_contribution": round(total_contribution, 2),
        "maturity_amount": round(maturity_amount, 2),
        "interest_earned": round(interest_earned, 2),
        "extended_amount": round(extended_amount, 2),
        "tax_benefit": round(tax_benefit, 2),
        "contribution_years": contribution_years
    }


def nps_calculator(
    monthly_contribution: float,
    current_age: int,
    retirement_age: int = 60,
    expected_return: float = 10.0,
    annuity_rate: float = 6.0
) -> Dict[str, Union[float, str]]:
    """
    💼 NPS Calculator
    
    Estimates corpus and pension from National Pension Scheme investments.
    
    Args:
        monthly_contribution: Monthly NPS contribution
        current_age: Current age
        retirement_age: Retirement age (default: 60)
        expected_return: Expected annual return (default: 10.0%)
        annuity_rate: Annuity rate for pension calculation (default: 6.0%)
        
    Returns:
        Dict containing:
            - total_contribution: Total amount contributed
            - corpus_at_retirement: Total corpus at retirement
            - lumpsum_withdrawal: 60% lumpsum withdrawal amount
            - annuity_amount: 40% amount used for annuity
            - monthly_pension: Estimated monthly pension
            - tax_benefit: Annual tax benefit
    """
    investment_years = retirement_age - current_age
    if investment_years <= 0:
        return {
            "icon": "💼",
            "error": "Retirement age must be greater than current age"
        }
    
    monthly_rate = expected_return / 100 / 12
    months = investment_years * 12
    
    # Future value of monthly contributions
    corpus_at_retirement = monthly_contribution * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    total_contribution = monthly_contribution * months
    
    # At retirement, 60% can be withdrawn, 40% must be used for annuity
    lumpsum_withdrawal = corpus_at_retirement * 0.6
    annuity_amount = corpus_at_retirement * 0.4
    
    # Monthly pension calculation
    monthly_pension = annuity_amount * (annuity_rate / 100) / 12
    
    # Tax benefit (80CCD(1) + 80CCD(1B))
    annual_contribution = monthly_contribution * 12
    tax_benefit = min(annual_contribution * 0.3, 46800)  # 30% tax bracket, max benefit
    
    return {
        "icon": "💼",
        "total_contribution": round(total_contribution, 2),
        "corpus_at_retirement": round(corpus_at_retirement, 2),
        "lumpsum_withdrawal": round(lumpsum_withdrawal, 2),
        "annuity_amount": round(annuity_amount, 2),
        "monthly_pension": round(monthly_pension, 2),
        "tax_benefit": round(tax_benefit, 2),
        "investment_years": investment_years
    }


def hra_calculator(
    basic_salary: float,
    hra_received: float,
    actual_rent: float,
    metro_city: bool = False
) -> Dict[str, Union[float, str]]:
    """
    🧾 HRA Calculator
    
    Computes House Rent Allowance tax exemption as per Indian tax laws.
    
    Args:
        basic_salary: Basic salary per month
        hra_received: HRA received per month
        actual_rent: Actual rent paid per month
        metro_city: Whether residing in metro city (default: False)
        
    Returns:
        Dict containing:
            - hra_received: HRA received annually
            - hra_exempt: HRA exempt from tax
            - hra_taxable: HRA taxable amount
            - rent_excess: Rent exceeding 10% of basic salary
            - metro_exemption: Metro city exemption rate
    """
    annual_basic = basic_salary * 12
    annual_hra = hra_received * 12
    annual_rent = actual_rent * 12
    
    # HRA exemption calculation as per Income Tax Act
    # Minimum of:
    # 1. Actual HRA received
    # 2. 50% of basic salary (metro) or 40% of basic salary (non-metro)
    # 3. Actual rent paid minus 10% of basic salary
    
    metro_percent = 50 if metro_city else 40
    exemption_by_city = annual_basic * metro_percent / 100
    rent_excess = max(0, annual_rent - annual_basic * 0.1)
    
    hra_exempt = min(annual_hra, exemption_by_city, rent_excess)
    hra_taxable = annual_hra - hra_exempt
    
    return {
        "icon": "🧾",
        "hra_received": round(annual_hra, 2),
        "hra_exempt": round(hra_exempt, 2),
        "hra_taxable": round(hra_taxable, 2),
        "rent_excess": round(rent_excess, 2),
        "metro_exemption": metro_percent,
        "annual_tax_saving": round(hra_exempt * 0.3, 2)  # Assuming 30% tax bracket
    }


def gratuity_calculator(
    monthly_salary: float,
    years_of_service: int,
    months_of_service: int = 0
) -> Dict[str, Union[float, str]]:
    """
    💰 Gratuity Calculator
    
    Calculates gratuity amount based on tenure and last drawn salary.
    
    Args:
        monthly_salary: Last drawn basic salary per month
        years_of_service: Complete years of service
        months_of_service: Additional months of service (default: 0)
        
    Returns:
        Dict containing:
            - gratuity_amount: Calculated gratuity amount
            - taxable_gratuity: Taxable portion of gratuity
            - tax_free_gratuity: Tax-free portion of gratuity
            - service_period: Total service period
    """
    # Convert months to years for calculation
    total_years = years_of_service + months_of_service / 12
    
    # Gratuity formula: (Basic Salary × 15 × Years of Service) / 26
    gratuity_amount = (monthly_salary * 15 * total_years) / 26
    
    # Tax exemption limit (as per current rules)
    tax_free_limit = 2000000  # 20 lakh
    tax_free_gratuity = min(gratuity_amount, tax_free_limit)
    taxable_gratuity = max(0, gratuity_amount - tax_free_limit)
    
    return {
        "icon": "💰",
        "gratuity_amount": round(gratuity_amount, 2),
        "taxable_gratuity": round(taxable_gratuity, 2),
        "tax_free_gratuity": round(tax_free_gratuity, 2),
        "service_period": f"{years_of_service} years {months_of_service} months",
        "eligibility": "Eligible" if total_years >= 5 else "Not eligible (minimum 5 years required)"
    }


def epf_calculator(
    monthly_basic: float,
    employee_contribution_percent: float = 12.0,
    employer_contribution_percent: float = 12.0,
    years_of_service: int = 30,
    annual_increment: float = 8.0,
    epf_interest_rate: float = 8.5
) -> Dict[str, Union[float, str]]:
    """
    📚 EPF Calculator
    
    Computes maturity value and contributions for Employee Provident Fund.
    
    Args:
        monthly_basic: Monthly basic salary
        employee_contribution_percent: Employee EPF contribution percentage (default: 12%)
        employer_contribution_percent: Employer EPF contribution percentage (default: 12%)
        years_of_service: Years of service (default: 30)
        annual_increment: Annual salary increment percentage (default: 8%)
        epf_interest_rate: EPF interest rate (default: 8.5%)
        
    Returns:
        Dict containing:
            - total_employee_contribution: Total employee contribution
            - total_employer_contribution: Total employer contribution
            - total_contribution: Combined total contribution
            - maturity_amount: EPF maturity amount with interest
            - monthly_pension: Estimated monthly pension (EPS)
    """
    monthly_rate = epf_interest_rate / 100 / 12
    total_employee_contribution = 0
    total_employer_contribution = 0
    maturity_amount = 0
    current_basic = monthly_basic
    
    for year in range(years_of_service):
        # Monthly contributions for this year
        monthly_employee_contribution = current_basic * employee_contribution_percent / 100
        monthly_employer_contribution = current_basic * employer_contribution_percent / 100
        
        # Add contributions for 12 months
        for month in range(12):
            total_employee_contribution += monthly_employee_contribution
            total_employer_contribution += monthly_employer_contribution
            
            # Calculate future value of this month's contribution
            remaining_months = (years_of_service - year) * 12 - month
            contribution_fv = (monthly_employee_contribution + monthly_employer_contribution) * (1 + monthly_rate) ** remaining_months
            maturity_amount += contribution_fv
        
        # Annual salary increment
        current_basic *= (1 + annual_increment / 100)
    
    total_contribution = total_employee_contribution + total_employer_contribution
    
    # EPS pension calculation (simplified)
    pensionable_salary = min(monthly_basic, 15000)  # EPS ceiling
    monthly_pension = pensionable_salary * years_of_service / 70  # Simplified formula
    
    return {
        "icon": "📚",
        "total_employee_contribution": round(total_employee_contribution, 2),
        "total_employer_contribution": round(total_employer_contribution, 2),
        "total_contribution": round(total_contribution, 2),
        "maturity_amount": round(maturity_amount, 2),
        "monthly_pension": round(monthly_pension, 2),
        "years_of_service": years_of_service
    }


def cagr_calculator(
    initial_value: float,
    final_value: float,
    investment_period_years: float
) -> Dict[str, Union[float, str]]:
    """
    📊 CAGR Calculator
    
    Calculates Compound Annual Growth Rate for investments.
    
    Args:
        initial_value: Initial investment value
        final_value: Final investment value
        investment_period_years: Investment period in years
        
    Returns:
        Dict containing:
            - cagr: Compound Annual Growth Rate as percentage
            - initial_value: Starting investment value
            - final_value: Ending investment value
            - total_return: Total return amount
            - total_return_percent: Total return as percentage
    """
    if initial_value <= 0 or investment_period_years <= 0:
        return {
            "icon": "📊",
            "error": "Initial value and investment period must be positive"
        }
    
    cagr = ((final_value / initial_value) ** (1 / investment_period_years) - 1) * 100
    total_return = final_value - initial_value
    total_return_percent = (total_return / initial_value) * 100
    
    return {
        "icon": "📊",
        "cagr": round(cagr, 2),
        "initial_value": round(initial_value, 2),
        "final_value": round(final_value, 2),
        "total_return": round(total_return, 2),
        "total_return_percent": round(total_return_percent, 2),
        "investment_period_years": investment_period_years
    }


def inflation_calculator(
    current_price: float,
    years: int,
    inflation_rate: float = 6.0,
    current_savings: float = 0.0,
    savings_growth_rate: float = 8.0
) -> Dict[str, Union[float, str]]:
    """
    📉 Inflation Calculator
    
    Evaluates impact of inflation on purchasing power and savings.
    
    Args:
        current_price: Current price of item/service
        years: Number of years to project
        inflation_rate: Expected inflation rate (default: 6.0%)
        current_savings: Current savings amount (default: 0.0)
        savings_growth_rate: Expected savings growth rate (default: 8.0%)
        
    Returns:
        Dict containing:
            - future_price: Price after inflation
            - price_increase: Absolute price increase
            - purchasing_power_loss: Loss in purchasing power
            - required_savings: Required savings to maintain purchasing power
            - savings_shortfall: Shortfall in savings
    """
    future_price = current_price * (1 + inflation_rate / 100) ** years
    price_increase = future_price - current_price
    purchasing_power_loss = (price_increase / current_price) * 100
    
    # Future value of current savings
    future_savings = current_savings * (1 + savings_growth_rate / 100) ** years
    
    # Required savings to maintain purchasing power
    required_savings = future_price
    savings_shortfall = max(0, required_savings - future_savings)
    
    return {
        "icon": "📉",
        "current_price": round(current_price, 2),
        "future_price": round(future_price, 2),
        "price_increase": round(price_increase, 2),
        "purchasing_power_loss": round(purchasing_power_loss, 2),
        "future_savings": round(future_savings, 2),
        "required_savings": round(required_savings, 2),
        "savings_shortfall": round(savings_shortfall, 2),
        "years": years
    }


def credit_card_interest_calculator(
    outstanding_balance: float,
    annual_interest_rate: float,
    minimum_payment_percent: float = 5.0,
    additional_payment: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    💳 Credit Card Interest Calculator
    
    Computes interest payable on outstanding credit card bills.
    
    Args:
        outstanding_balance: Current outstanding balance
        annual_interest_rate: Annual interest rate (as percentage)
        minimum_payment_percent: Minimum payment as percentage of balance (default: 5%)
        additional_payment: Additional payment beyond minimum (default: 0.0)
        
    Returns:
        Dict containing:
            - monthly_interest_rate: Monthly interest rate
            - minimum_payment: Minimum payment amount
            - total_monthly_payment: Total monthly payment
            - payoff_months: Months to pay off balance
            - total_interest_paid: Total interest paid
            - total_amount_paid: Total amount paid
    """
    monthly_rate = annual_interest_rate / 100 / 12
    minimum_payment = outstanding_balance * minimum_payment_percent / 100
    total_monthly_payment = minimum_payment + additional_payment
    
    # Calculate payoff time and total interest
    balance = outstanding_balance
    months = 0
    total_interest_paid = 0
    
    while balance > 0 and months < 600:  # Max 50 years to avoid infinite loop
        interest_payment = balance * monthly_rate
        principal_payment = min(total_monthly_payment - interest_payment, balance)
        
        if principal_payment <= 0:
            return {
                "icon": "💳",
                "error": "Monthly payment is less than interest. Balance will never be paid off!"
            }
        
        balance -= principal_payment
        total_interest_paid += interest_payment
        months += 1
    
    total_amount_paid = outstanding_balance + total_interest_paid
    
    return {
        "icon": "💳",
        "monthly_interest_rate": round(monthly_rate * 100, 2),
        "minimum_payment": round(minimum_payment, 2),
        "total_monthly_payment": round(total_monthly_payment, 2),
        "payoff_months": months,
        "total_interest_paid": round(total_interest_paid, 2),
        "total_amount_paid": round(total_amount_paid, 2),
        "outstanding_balance": round(outstanding_balance, 2)
    }


def personal_loan_emi_calculator(
    loan_amount: float,
    annual_interest_rate: float,
    tenure_months: int,
    processing_fee_percent: float = 1.0
) -> Dict[str, Union[float, str]]:
    """
    💸 Personal Loan EMI Calculator
    
    Estimates EMI and total repayment for personal loans.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (as percentage)
        tenure_months: Loan tenure in months
        processing_fee_percent: Processing fee as percentage of loan amount (default: 1.0%)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - total_cost: Total cost including processing fee
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    
    # EMI calculation using formula: P * r * (1+r)^n / [(1+r)^n - 1]
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    total_cost = total_payment + processing_fee
    
    return {
        "icon": "💸",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "total_cost": round(total_cost, 2),
        "tenure_months": tenure_months
    }


def medical_loan_emi_calculator(
    loan_amount: float,
    annual_interest_rate: float,
    tenure_months: int,
    moratorium_months: int = 6,
    processing_fee_percent: float = 0.5
) -> Dict[str, Union[float, str]]:
    """
    🩺 Medical Loan EMI Calculator
    
    Calculates EMI for medical professional loans with moratorium period.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (as percentage)
        tenure_months: Loan tenure in months
        moratorium_months: Moratorium period in months (default: 6)
        processing_fee_percent: Processing fee as percentage (default: 0.5%)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount (after moratorium)
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - moratorium_interest: Interest during moratorium
            - processing_fee: Processing fee amount
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    
    # Interest accumulation during moratorium
    moratorium_interest = loan_amount * monthly_rate * moratorium_months
    effective_loan_amount = loan_amount + moratorium_interest
    
    # EMI calculation for remaining tenure
    remaining_months = tenure_months - moratorium_months
    emi = effective_loan_amount * monthly_rate * (1 + monthly_rate) ** remaining_months / ((1 + monthly_rate) ** remaining_months - 1)
    
    total_payment = emi * remaining_months
    total_interest = total_payment - loan_amount
    
    return {
        "icon": "🩺",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "moratorium_interest": round(moratorium_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "moratorium_months": moratorium_months,
        "repayment_months": remaining_months
    }


def marriage_loan_emi_calculator(
    loan_amount: float,
    annual_interest_rate: float,
    tenure_months: int,
    processing_fee_percent: float = 1.0,
    prepayment_charges_percent: float = 2.0
) -> Dict[str, Union[float, str]]:
    """
    💍 Marriage Loan EMI Calculator
    
    Estimates EMI and total repayment for marriage loans.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (as percentage)
        tenure_months: Loan tenure in months
        processing_fee_percent: Processing fee as percentage (default: 1.0%)
        prepayment_charges_percent: Prepayment charges as percentage (default: 2.0%)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - prepayment_charges: Prepayment charges (if applicable)
            - total_cost: Total cost including fees
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    prepayment_charges = loan_amount * prepayment_charges_percent / 100
    
    # EMI calculation
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    total_cost = total_payment + processing_fee
    
    return {
        "icon": "💍",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "prepayment_charges": round(prepayment_charges, 2),
        "total_cost": round(total_cost, 2),
        "tenure_months": tenure_months
    }


def home_renovation_emi_calculator(
    loan_amount: float,
    annual_interest_rate: float,
    tenure_months: int,
    property_value: float,
    processing_fee_percent: float = 0.5
) -> Dict[str, Union[float, str]]:
    """
    🔨 Home Renovation EMI Calculator
    
    Computes EMI for home renovation loans.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (as percentage)
        tenure_months: Loan tenure in months
        property_value: Current property value
        processing_fee_percent: Processing fee as percentage (default: 0.5%)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - loan_to_value_ratio: Loan to value ratio
            - eligibility_status: Eligibility status
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    
    # Calculate loan-to-value ratio
    ltv_ratio = (loan_amount / property_value) * 100
    
    # Eligibility check (typically max 80% LTV for renovation loans)
    eligibility_status = "Eligible" if ltv_ratio <= 80 else "Not eligible - LTV exceeds 80%"
    
    # EMI calculation
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    
    return {
        "icon": "🔨",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "loan_to_value_ratio": round(ltv_ratio, 2),
        "eligibility_status": eligibility_status,
        "property_value": round(property_value, 2)
    }


def axis_bank_personal_loan_calculator(
    loan_amount: float,
    annual_interest_rate: float = 10.5,
    tenure_months: int = 60,
    processing_fee_percent: float = 2.0,
    insurance_premium_percent: float = 0.5
) -> Dict[str, Union[float, str]]:
    """
    🏦 Axis Bank Personal Loan Calculator
    
    Calculates EMI for Axis Bank personal loans with specific terms.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (default: 10.5%)
        tenure_months: Loan tenure in months (default: 60)
        processing_fee_percent: Processing fee as percentage (default: 2.0%)
        insurance_premium_percent: Insurance premium as percentage (default: 0.5%)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - insurance_premium: Insurance premium amount
            - total_cost: Total cost including all fees
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    insurance_premium = loan_amount * insurance_premium_percent / 100
    
    # EMI calculation
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    total_cost = total_payment + processing_fee + insurance_premium
    
    return {
        "icon": "🏦",
        "bank": "Axis Bank",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "insurance_premium": round(insurance_premium, 2),
        "total_cost": round(total_cost, 2),
        "tenure_months": tenure_months
    }


def icici_bank_personal_loan_emi_calculator(
    loan_amount: float,
    annual_interest_rate: float = 10.75,
    tenure_months: int = 60,
    processing_fee_percent: float = 2.5,
    documentation_charges: float = 5000
) -> Dict[str, Union[float, str]]:
    """
    🏦 ICICI Bank Personal Loan EMI Calculator
    
    Computes EMI for ICICI Bank personal loans with specific terms.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (default: 10.75%)
        tenure_months: Loan tenure in months (default: 60)
        processing_fee_percent: Processing fee as percentage (default: 2.5%)
        documentation_charges: Documentation charges (default: 5000)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - documentation_charges: Documentation charges
            - total_cost: Total cost including all fees
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    
    # EMI calculation
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    total_cost = total_payment + processing_fee + documentation_charges
    
    return {
        "icon": "🏦",
        "bank": "ICICI Bank",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "documentation_charges": round(documentation_charges, 2),
        "total_cost": round(total_cost, 2),
        "tenure_months": tenure_months
    }


def hdfc_bank_personal_loan_calculator(
    loan_amount: float,
    annual_interest_rate: float = 10.85,
    tenure_months: int = 60,
    processing_fee_percent: float = 2.5,
    salary_requirement: float = 25000
) -> Dict[str, Union[float, str]]:
    """
    🏦 HDFC Bank Personal Loan Calculator
    
    Calculates EMI, eligibility, and rates for HDFC Bank personal loans.
    
    Args:
        loan_amount: Loan principal amount
        annual_interest_rate: Annual interest rate (default: 10.85%)
        tenure_months: Loan tenure in months (default: 60)
        processing_fee_percent: Processing fee as percentage (default: 2.5%)
        salary_requirement: Minimum salary requirement (default: 25000)
        
    Returns:
        Dict containing:
            - emi: Monthly EMI amount
            - total_payment: Total amount to be paid
            - total_interest: Total interest paid
            - processing_fee: Processing fee amount
            - eligibility_status: Eligibility status
            - max_loan_amount: Maximum loan amount based on salary
    """
    monthly_rate = annual_interest_rate / 100 / 12
    processing_fee = loan_amount * processing_fee_percent / 100
    
    # Eligibility calculation (typically 10-15x monthly salary)
    max_loan_amount = salary_requirement * 12
    eligibility_status = "Eligible" if loan_amount <= max_loan_amount else "Not eligible - Exceeds income criteria"
    
    # EMI calculation
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount
    
    return {
        "icon": "🏦",
        "bank": "HDFC Bank",
        "loan_amount": round(loan_amount, 2),
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "processing_fee": round(processing_fee, 2),
        "eligibility_status": eligibility_status,
        "max_loan_amount": round(max_loan_amount, 2),
        "salary_requirement": round(salary_requirement, 2)
    }


def net_worth_calculator(
    assets: Dict[str, float],
    liabilities: Dict[str, float]
) -> Dict[str, Union[float, str, Dict]]:
    """
    ⚖️ Net Worth Calculator
    
    Computes net worth by calculating the difference between total assets and liabilities.
    
    Args:
        assets: Dictionary of asset categories and their values
                Example: {"cash": 50000, "investments": 200000, "real_estate": 1000000}
        liabilities: Dictionary of liability categories and their values
                    Example: {"home_loan": 800000, "personal_loan": 100000, "credit_card": 25000}
        
    Returns:
        Dict containing:
            - total_assets: Sum of all assets
            - total_liabilities: Sum of all liabilities
            - net_worth: Net worth (assets - liabilities)
            - asset_breakdown: Detailed breakdown of assets
            - liability_breakdown: Detailed breakdown of liabilities
            - debt_to_asset_ratio: Debt to asset ratio as percentage
            - financial_health: Financial health assessment
    """
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())
    net_worth = total_assets - total_liabilities
    
    # Calculate debt-to-asset ratio
    debt_to_asset_ratio = (total_liabilities / total_assets * 100) if total_assets > 0 else 0
    
    # Financial health assessment
    if debt_to_asset_ratio <= 30:
        financial_health = "Excellent - Low debt burden"
    elif debt_to_asset_ratio <= 50:
        financial_health = "Good - Moderate debt burden"
    elif debt_to_asset_ratio <= 70:
        financial_health = "Average - High debt burden"
    else:
        financial_health = "Poor - Very high debt burden"
    
    return {
        "icon": "⚖️",
        "total_assets": round(total_assets, 2),
        "total_liabilities": round(total_liabilities, 2),
        "net_worth": round(net_worth, 2),
        "asset_breakdown": {k: round(v, 2) for k, v in assets.items()},
        "liability_breakdown": {k: round(v, 2) for k, v in liabilities.items()},
        "debt_to_asset_ratio": round(debt_to_asset_ratio, 2),
        "financial_health": financial_health
    }


# Export all functions for easy import
__all__ = [
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
    "net_worth_calculator"
]