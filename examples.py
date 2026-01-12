#!/usr/bin/env python3
"""
Example usage of the Real Estate Expert tool
"""

from real_estate_expert import ZoningAnalyzer, PropertyAnalyzer


def example_1_basic_zoning_analysis():
    """Example 1: Basic zoning analysis"""
    print("=" * 80)
    print("EXAMPLE 1: Basic Zoning Analysis")
    print("=" * 80)
    print()
    
    analyzer = ZoningAnalyzer()
    result = analyzer.analyze_address(
        "Miller Rd, Winston Salem, NC 27106",
        "RS 9"
    )
    
    print(f"Address: {result['address']}")
    print(f"Zoning: {result['zoning_code']}")
    
    if 'zoning_details' in result:
        details = result['zoning_details']
        print(f"\nZoning Type: {details['name']}")
        print(f"Minimum Lot Size: {details['minimum_lot_size']:,} sq ft")
        print(f"Primary Use: {details['primary_use']}")
        
        print("\nInvestment Profile:")
        for key, value in details['investment_profile'].items():
            print(f"  • {key.replace('_', ' ').title()}: {value}")
    
    print()


def example_2_property_market_analysis():
    """Example 2: Property market analysis"""
    print("=" * 80)
    print("EXAMPLE 2: Property Market Analysis")
    print("=" * 80)
    print()
    
    analyzer = PropertyAnalyzer()
    result = analyzer.analyze_property("Miller Rd, Winston Salem, NC 27106")
    
    if 'market_analysis' in result:
        market = result['market_analysis']
        print(f"Area: {market['area']}")
        print(f"Median Listing Price: ${market['median_listing_price']:,}")
        print(f"Median Sold Price: ${market['median_sold_price']:,}")
        print(f"Days on Market: {market['days_on_market']} days")
        
        print("\nRecent Sales:")
        for sale in market['recent_sales'][:2]:  # Show first 2
            print(f"  • {sale['address']}")
            if 'sale_price' in sale:
                print(f"    Price: ${sale['sale_price']:,}")
            print(f"    Type: {sale['type']}")
    
    print()


def example_3_investment_metrics():
    """Example 3: Investment metrics calculation"""
    print("=" * 80)
    print("EXAMPLE 3: Investment Metrics")
    print("=" * 80)
    print()
    
    analyzer = PropertyAnalyzer()
    result = analyzer.analyze_property("Miller Rd, Winston Salem, NC 27106")
    
    if 'investment_metrics' in result:
        metrics = result['investment_metrics']
        
        print("New Construction Project Analysis:")
        print(f"\nConstruction Cost (1,500 sq ft home):")
        print(f"  Low Estimate: ${metrics['estimated_construction_cost_new_home']['low']:,.0f}")
        print(f"  High Estimate: ${metrics['estimated_construction_cost_new_home']['high']:,.0f}")
        
        print(f"\nLand Cost: ${metrics['estimated_land_cost']:,}")
        
        print(f"\nTotal Project Cost:")
        print(f"  Low: ${metrics['total_project_cost_estimate']['low']:,.0f}")
        print(f"  High: ${metrics['total_project_cost_estimate']['high']:,.0f}")
        
        print(f"\nPotential Sale Price: ${metrics['potential_sale_price']:,.0f}")
        print(f"Time to Sale: {metrics['time_to_sale']}")
    
    print()


def example_4_investment_recommendation():
    """Example 4: Get investment recommendations"""
    print("=" * 80)
    print("EXAMPLE 4: Investment Recommendations")
    print("=" * 80)
    print()
    
    # Get zoning analysis
    zoning_analyzer = ZoningAnalyzer()
    zoning_result = zoning_analyzer.analyze_address(
        "Miller Rd, Winston Salem, NC 27106",
        "RS 9"
    )
    
    if 'summary' in zoning_result:
        rec = zoning_result['summary']['investment_recommendation']
        
        print(f"Suitability: {rec['suitability']}\n")
        
        print("Pros:")
        for pro in rec['pros']:
            print(f"  ✓ {pro}")
        
        print("\nCons:")
        for con in rec['cons']:
            print(f"  ✗ {con}")
        
        print(f"\nIdeal For: {rec['ideal_investor_profile']}")
    
    # Get property analysis
    property_analyzer = PropertyAnalyzer()
    property_result = property_analyzer.analyze_property("Miller Rd, Winston Salem, NC 27106")
    
    if 'recommendation' in property_result:
        rec = property_result['recommendation']
        
        print(f"\n\nOverall Rating: {rec['overall_rating']}\n")
        
        print("Best Investment Strategies:")
        for i, strategy in enumerate(rec['best_strategy'], 1):
            print(f"  {i}. {strategy}")
    
    print()


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("REAL ESTATE EXPERT - USAGE EXAMPLES")
    print("=" * 80)
    print()
    
    # Run all examples
    example_1_basic_zoning_analysis()
    example_2_property_market_analysis()
    example_3_investment_metrics()
    example_4_investment_recommendation()
    
    print("=" * 80)
    print("For complete analysis, run: python3 real_estate_expert.py")
    print("=" * 80)
    print()
