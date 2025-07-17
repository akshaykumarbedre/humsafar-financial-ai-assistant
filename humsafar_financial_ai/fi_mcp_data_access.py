"""
FI-MCP Data Access Module for Humsafar Financial AI Assistant

This module provides modular access to the Financial Intelligence dummy data
organized by user personas. Each function allows AI agents to fetch specific
types of financial data efficiently.

The dummy data represents 25 different user personas with varying financial
profiles, from debt-heavy users to high-net-worth individuals.
"""

import json
import os
from typing import Dict, List, Optional, Union, Any
from pathlib import Path


class FIMCPDataAccess:
    """
    Financial Intelligence MCP Data Access Layer
    
    Provides modular access to dummy financial data for AI agent integration.
    Data is organized by phone number (user persona) and data type.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize the FI-MCP data access layer.
        
        Args:
            data_dir: Path to the test data directory. If None, uses default path.
        """
        if data_dir is None:
            # Default path relative to this file
            current_dir = Path(__file__).parent.parent
            self.data_dir = current_dir / "FI money dummy data" / "test_data_dir"
        else:
            self.data_dir = Path(data_dir)
    
    def _load_data(self, phone_number: str, data_type: str) -> Optional[Dict[str, Any]]:
        """
        Load data for a specific user and data type.
        
        Args:
            phone_number: User identifier (phone number)
            data_type: Type of data to fetch (e.g., 'fetch_net_worth.json')
            
        Returns:
            Dictionary containing the data or None if not found
        """
        try:
            file_path = self.data_dir / phone_number / data_type
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None
        except (json.JSONDecodeError, FileNotFoundError, OSError):
            return None
    
    def get_available_users(self) -> List[str]:
        """
        Get list of all available user personas (phone numbers).
        
        Returns:
            List of phone numbers representing different user personas
        """
        if not self.data_dir.exists():
            return []
        
        return [d.name for d in self.data_dir.iterdir() 
                if d.is_dir() and d.name.isdigit()]
    
    def get_net_worth(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        📊 Fetch net worth and asset breakdown for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing:
                - netWorthResponse: Asset values and total net worth
                - mfSchemeAnalytics: Mutual fund analytics
                - accountDetailsBulkResponse: Account details
                
        Schema:
            netWorthResponse:
                assetValues: List of asset types and values
                    - netWorthAttribute: Asset type (e.g., ASSET_TYPE_SAVINGS_ACCOUNTS)
                    - value: {currencyCode: "INR", units: "amount"}
                totalNetWorthValue: Total net worth {currencyCode, units}
        """
        return self._load_data(phone_number, "fetch_net_worth.json")
    
    def get_bank_transactions(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        🏦 Fetch bank transactions for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing bank transactions data
            
        Schema:
            schemaDescription: Description of transaction schema
            bankTransactions: List of bank accounts with transactions
                bank: Bank name (e.g., "HDFC Bank")
                txns: List of transactions, each containing:
                    [transactionAmount, transactionNarration, transactionDate, 
                     transactionType, transactionMode, currentBalance]
                     
        Transaction Types:
            1: CREDIT, 2: DEBIT, 3: OPENING, 4: INTEREST, 
            5: TDS, 6: INSTALLMENT, 7: CLOSING, 8: OTHERS
        """
        return self._load_data(phone_number, "fetch_bank_transactions.json")
    
    def get_mutual_fund_transactions(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        📈 Fetch mutual fund transactions for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing mutual fund transactions
            
        Schema:
            schemaDescription: Description of transaction schema
            mfTransactions: List of mutual fund investments
                isin: Fund ISIN code
                schemeName: Fund name
                folioId: Folio number
                txns: List of transactions, each containing:
                    [orderType, transactionDate, purchasePrice, purchaseUnits, transactionAmount]
                    
        Order Types:
            1: BUY, 2: SELL
        """
        return self._load_data(phone_number, "fetch_mf_transactions.json")
    
    def get_stock_transactions(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        📊 Fetch stock transactions for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing stock transactions
            
        Schema:
            schemaDescription: Description of transaction schema
            stockTransactions: List of stock investments
                isin: Stock ISIN code
                txns: List of transactions, each containing:
                    [transactionType, transactionDate, quantity, navValue (optional)]
                    
        Transaction Types:
            1: BUY, 2: SELL, 3: BONUS, 4: SPLIT
        """
        return self._load_data(phone_number, "fetch_stock_transactions.json")
    
    def get_epf_details(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        🏛️ Fetch EPF (Employee Provident Fund) details for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing EPF account details
            
        Schema:
            uanAccounts: List of UAN accounts
                phoneNumber: Phone number details
                rawDetails:
                    est_details: List of establishment details
                        est_name: Employer name
                        member_id: Member ID
                        office: EPF office
                        doj_epf: Date of joining EPF
                        doe_epf: Date of exit EPF
                        pf_balance: Balance details
                            net_balance: Total balance
                            employee_share: Employee contribution
                            employer_share: Employer contribution
                    overall_pf_balance: Overall balance summary
        """
        return self._load_data(phone_number, "fetch_epf_details.json")
    
    def get_credit_report(self, phone_number: str) -> Optional[Dict[str, Any]]:
        """
        💳 Fetch credit report and score for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing credit report data
            
        Schema:
            creditReports: List of credit reports
                creditReportData:
                    userMessage: Response status
                    creditProfileHeader: Report metadata (date, time)
                    currentApplication: Current application details
                    creditAccount: Credit account summary and details
                        creditAccountSummary: Account totals and balances
                        creditAccountDetails: List of credit accounts
                            subscriberName: Bank/lender name
                            accountType: Account type code
                            openDate: Account opening date
                            accountStatus: Account status code
                            currentBalance: Current outstanding
                            paymentRating: Payment rating
                    score: Credit score details
                        bureauScore: Credit score
                        bureauScoreConfidenceLevel: Confidence level
                    caps: Credit inquiry details
        """
        return self._load_data(phone_number, "fetch_credit_report.json")
    
    def get_complete_profile(self, phone_number: str) -> Dict[str, Any]:
        """
        📋 Fetch complete financial profile for a user.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing all available financial data for the user
        """
        profile = {
            "user_id": phone_number,
            "net_worth": self.get_net_worth(phone_number),
            "bank_transactions": self.get_bank_transactions(phone_number),
            "mutual_fund_transactions": self.get_mutual_fund_transactions(phone_number),
            "stock_transactions": self.get_stock_transactions(phone_number),
            "epf_details": self.get_epf_details(phone_number),
            "credit_report": self.get_credit_report(phone_number)
        }
        return profile
    
    def get_user_persona_description(self, phone_number: str) -> str:
        """
        📝 Get description of user persona based on phone number.
        
        Args:
            phone_number: User identifier
            
        Returns:
            String description of the user persona
        """
        persona_descriptions = {
            "1111111111": "No assets connected. Only saving account balance present",
            "2222222222": "All assets connected (Banks account, EPF, Indian stocks, US stocks, Credit report). Large mutual fund portfolio with 9 funds",
            "3333333333": "All assets connected (Banks account, EPF, Indian stocks, US stocks, Credit report). Small mutual fund portfolio with only 1 fund",
            "4444444444": "All assets connected (Banks account, EPF, Indian stocks, US stocks). Small mutual fund portfolio with only 1 fund. With 2 UAN account connected. With 3 different bank with multiple account in them. Only have transactions for 2 bank accounts",
            "5555555555": "All assets connected except credit score (Banks account, EPF, Indian stocks, US stocks). Small mutual fund portfolio with only 1 fund. With 3 different bank with multiple account in them. Only have transactions for 2 bank accounts",
            "6666666666": "All assets connected except bank account (EPF, Indian stocks, US stocks). Large mutual fund portfolio with 9 funds. No bank account connected",
            "7777777777": "Debt-Heavy Low Performer. A user with mostly underperforming mutual funds, high liabilities (credit card & personal loans). Poor MF returns (XIRR < 5%). No diversification (all equity, few funds). Credit score < 650. High credit card usage, multiple loans. Negligible net worth or negative.",
            "8888888888": "SIP Samurai. Consistently invests every month in multiple mutual funds via SIP. 3–5 active SIPs in MFs. Moderate returns (XIRR 8–12%).",
            "9999999999": "Fixed Income Fanatic. Strong preference for low-risk investments like debt mutual funds and fixed deposits. 80% of investments in debt MFs. Occasional gold ETF (Optional). Consistent but slow net worth growth (XIRR ~ 8-10%).",
            "1010101010": "Precious Metal Believer. High allocation to gold and fixed deposits, minimal equity exposure. Gold MFs/ETFs ~50% of investment. Conservative SIPs in gold funds. FDs and recurring deposits. Minimal equity exposure.",
            "1212121212": "Dormant EPF Earner. Has EPF account but employer stopped contributing; balance stagnant. EPF balance > ₹2 lakh. Interest not being credited. No private investment.",
            "1414141414": "Salary Sinkhole. User's salary is mostly consumed by EMIs and credit card bills. Salary credit every month. 70% goes to EMIs and credit card dues. Low or zero investment. Credit score ~600–650.",
            "1313131313": "Balanced Growth Tracker. Well-diversified portfolio with EPF, MFs, stocks, and some US exposure. High EPF contribution. SIPs in equity & hybrid MFs. International MFs/ETFs 10–20%. Healthy net worth growth. Good credit score (750+).",
            "2020202020": "Starter Saver. Recently started investing, low ticket sizes, few transactions. Just 1–2 MFs, started < 6 months ago. SIP ₹500–₹1000. Minimal bank balance, no debt.",
            "1515151515": "Ghost Portfolio. Has old investments but hasn't made any changes in years. No MF purchase/redemption in 3 years. EPF stagnant or partially withdrawn. No SIPs or salary inflow. Flat or declining net worth.",
            "1616161616": "Early Retirement Dreamer. Optimizing investments to retire by 40. High savings rate, frugal lifestyle. Aggressive equity exposure (80–90%). Lean monthly expenses. Heavy SIPs + NPS + EPF contributions. No loans, no luxury spending. Targets 30x yearly expenses net worth.",
            "1717171717": "The Swinger. Regularly buys/sells MFs and stocks, seeks short-term gains. Many MF redemptions within 6 months. Equity funds only, high churn. No SIPs. Short holding periods. High txn volume in bank account.",
            "1818181818": "Passive Contributor. No personal income, but has EPF from a past job and joint bank accounts. Old EPF, no current contributions. No active SIPs. Transactions reflect shared household spending. No credit score record (no loans/credit card).",
            "1919191919": "Section 80C Strategist. Uses ELSS, EPF, NPS primarily to optimize taxes. ELSS SIPs in Q4 (Jan–Mar). EPF active. NPS data if available. No non-tax-saving investments. Low-risk debt funds as balance.",
            "2121212121": "Dual Income Dynamo. Has freelance + salary income; cash flow is uneven but investing steadily. Salary + multiple credits from UPI apps. MF investments irregular but increasing. High liquidity in bank accounts. Credit score above 700. Occasional business loans or overdraft.",
            "2222222222": "Sudden Wealth Receiver. Recently inherited wealth, learning how to manage it. Lump sum investments across categories. High idle cash in bank. Recent MF purchases, no SIPs yet. No credit history or debt. EPF missing or dormant.",
            "2323232323": "Overseas Optimizer. NRI who continues to manage Indian EPF, MFs, and bank accounts. Large EPF corpus. No salary inflows, occasional foreign remittances. MF transactions in bulk. Indian address missing or outdated. No credit card usage in India.",
            "2424242424": "Mattress Money Mindset. Doesn't trust the market; everything is in bank savings and FDs. 95% net worth in FDs/savings. No mutual funds or stocks. EPF maybe present. No debt or credit score. Low but consistent net worth growth.",
            "2525252525": "Live-for-Today. High income but spends it all. Investments are negligible or erratic. Salary > ₹2L/month. High food, shopping, travel spends. No SIPs, maybe one-time MF buy. Credit card dues often roll over. Credit score < 700, low or zero net worth."
        }
        return persona_descriptions.get(phone_number, "Unknown persona")
    
    def analyze_user_financial_health(self, phone_number: str) -> Dict[str, Any]:
        """
        🔍 Analyze user's financial health based on all available data.
        
        Args:
            phone_number: User identifier
            
        Returns:
            Dict containing financial health analysis
        """
        profile = self.get_complete_profile(phone_number)
        persona = self.get_user_persona_description(phone_number)
        
        analysis = {
            "user_id": phone_number,
            "persona_description": persona,
            "data_availability": {
                "net_worth": profile["net_worth"] is not None,
                "bank_transactions": profile["bank_transactions"] is not None,
                "mutual_funds": profile["mutual_fund_transactions"] is not None,
                "stocks": profile["stock_transactions"] is not None,
                "epf": profile["epf_details"] is not None,
                "credit_report": profile["credit_report"] is not None
            },
            "profile_completeness": sum(1 for v in profile.values() if v is not None and v != phone_number) / 6 * 100
        }
        
        # Add specific insights based on available data
        if profile["net_worth"]:
            try:
                net_worth_data = profile["net_worth"].get("netWorthResponse", {})
                total_net_worth = net_worth_data.get("totalNetWorthValue", {}).get("units", "0")
                analysis["total_net_worth"] = float(total_net_worth)
            except (ValueError, TypeError):
                analysis["total_net_worth"] = 0
        
        if profile["credit_report"]:
            try:
                credit_data = profile["credit_report"]["creditReports"][0]["creditReportData"]
                credit_score = credit_data.get("score", {}).get("bureauScore", "0")
                analysis["credit_score"] = int(credit_score)
            except (IndexError, KeyError, ValueError, TypeError):
                analysis["credit_score"] = None
        
        return analysis


# Convenience functions for direct access
def get_net_worth(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get net worth data for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_net_worth(phone_number)


def get_bank_transactions(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get bank transactions for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_bank_transactions(phone_number)


def get_mutual_fund_transactions(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get mutual fund transactions for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_mutual_fund_transactions(phone_number)


def get_stock_transactions(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get stock transactions for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_stock_transactions(phone_number)


def get_epf_details(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get EPF details for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_epf_details(phone_number)


def get_credit_report(phone_number: str, data_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get credit report for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_credit_report(phone_number)


def get_complete_profile(phone_number: str, data_dir: Optional[str] = None) -> Dict[str, Any]:
    """Get complete financial profile for a user"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_complete_profile(phone_number)


def analyze_user_financial_health(phone_number: str, data_dir: Optional[str] = None) -> Dict[str, Any]:
    """Analyze user's financial health"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.analyze_user_financial_health(phone_number)


def get_available_users(data_dir: Optional[str] = None) -> List[str]:
    """Get list of available user personas"""
    accessor = FIMCPDataAccess(data_dir)
    return accessor.get_available_users()