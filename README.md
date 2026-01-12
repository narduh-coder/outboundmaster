# 🏠 Real Estate Expert - Zoning & Property Analysis Tool

A comprehensive real estate analysis tool that helps investors and developers analyze properties for construction and investment opportunities, with a focus on zoning regulations and market analysis.

## 🎯 Quick Answer: What is RS-9 Zoning?

**RS-9 in Winston-Salem, NC** means:
- ✅ **Single-family homes only** (9,000+ sq ft lots)
- ✅ **~4 homes per acre** maximum density
- ❌ **No apartments or commercial** without special approval
- 💰 **Stable, low-risk residential investment**

**For Miller Rd, Winston Salem, NC 27106:**
- Current market: $231k-$270k median prices
- Good for: Single-family construction or rental investment
- Available: Land lots and existing homes

👉 **See [ZONING_GUIDE.md](ZONING_GUIDE.md) for quick reference**  
👉 **Run the tool below for complete analysis**

## 🚀 Quick Start

### Run the Complete Analysis

```bash
# Run the full analysis for Miller Rd, Winston Salem, NC 27106
python3 real_estate_expert.py
```

This generates:
- 📊 Complete console report with all details
- 💾 JSON file: `real_estate_analysis_report.json`

### Run Usage Examples

```bash
# See focused examples of different features
python3 examples.py
```

### What You Get

The tool analyzes **Miller Rd, Winston Salem, NC 27106 (RS-9 Zoning)** and provides:

1. **Zoning Analysis** - What RS-9 means for construction
2. **Market Data** - Current prices, sales, and trends
3. **Investment Metrics** - Costs, returns, and profitability
4. **Recommendations** - Best strategies for this property

## 📖 Documentation

- **[README.md](README.md)** ← You are here (Main documentation)
- **[ZONING_GUIDE.md](ZONING_GUIDE.md)** ← Quick reference for RS-9 zoning
- **[examples.py](examples.py)** ← Code examples and usage

## Features

### 🏛️ Zoning Analysis
- Detailed zoning code interpretation (currently supports Winston-Salem, NC)
- Permitted and restricted uses
- Investment risk profiles
- Construction considerations
- Required permits and compliance information

### 🏘️ Property Market Analysis
- Local market trends and pricing
- Comparable sales analysis
- Investment metrics calculation
- Development potential assessment
- Neighborhood amenities and schools

## Usage

### Running the Analysis

```bash
python3 real_estate_expert.py
```

This will generate a comprehensive report for the default property:
- **Address:** Miller Rd, Winston Salem, NC 27106
- **Zoning:** RS 9 (Residential Single Family, 9,000 sq ft minimum)

### Output

The tool generates:
1. **Console Report:** Detailed analysis printed to terminal
2. **JSON Report:** Saved as `real_estate_analysis_report.json`

## Example Analysis Output

The tool provides:

### Zoning Details
- Official zoning name and code
- Minimum lot size requirements
- Maximum density allowed
- Permitted and restricted uses
- Investment stability profile
- Construction considerations

### Market Analysis
- Current market prices and trends
- Recent comparable sales
- Days on market statistics
- Price per square foot analysis
- School and amenity information

### Investment Metrics
- Estimated construction costs
- Land acquisition costs
- Total project cost estimates
- Potential profit margins
- ROI calculations

### Recommendations
- Investment suitability rating
- Pros and cons analysis
- Best investment strategies
- Next steps and action items

## Understanding RS-9 Zoning (Winston-Salem, NC)

**RS-9** stands for "Residential Single Family, minimum 9,000 square feet"

### Key Characteristics:
- **Purpose:** Single-family residential development
- **Minimum Lot Size:** 9,000 sq ft per dwelling
- **Density:** Maximum 4 dwelling units per acre
- **Primary Use:** Single-family detached homes

### Permitted Uses:
✅ Single-family detached homes  
✅ Accessory structures (garages, sheds)  
✅ Religious institutions  
✅ Public parks  
✅ Small-scale daycare centers (with permits)

### Restrictions:
❌ Commercial development (without special exception)  
❌ Multi-family dwellings (without variance)  
❌ High-density development  
❌ Mixed-use projects

### Investment Profile:
- **Stability:** High - protected residential character
- **Risk Level:** Low - proven residential use
- **Flexibility:** Low to Moderate - limited to single-family
- **Appreciation:** Moderate to High - suburban stability

## Miller Rd, Winston Salem, NC 27106 - Market Snapshot

### Current Market Data:
- **Median Listing Price:** $269,900
- **Median Sold Price:** $231,500
- **Days on Market:** ~50 days
- **Price per Sq Ft:** $151-$206

### Recent Sales:
- **4728 Miller Rd:** $309,000 (June 2025) - New 3BR/2BA ranch on 1 acre
- **4626 Miller Rd:** ~$266,700 estimated - 3BR/2BA built 1981
- **4982 Miller Rd:** $160,000 (2023) - 2BR/1BA cottage on 3 acres

### Investment Opportunities:
- ✓ Vacant land available (e.g., 3.55 acres for $22,500)
- ✓ New construction potential
- ✓ Renovation opportunities
- ✓ Single-family rental market

## Investment Strategies

### 1. Build-to-Sell
- Purchase vacant land
- Construct single-family home
- Sell at market price
- **Profit Potential:** Moderate to High
- **Timeframe:** 12-18 months

### 2. Buy-and-Hold Rental
- Purchase existing home
- Rent to families
- **Rental Yield:** 6-9% gross
- **Timeframe:** Long-term (5+ years)

### 3. Value-Add Renovation
- Buy older property below market
- Renovate and improve
- Sell or rent at higher value
- **Profit Potential:** High
- **Timeframe:** 6-12 months

### 4. Land Banking
- Purchase vacant lots
- Hold for appreciation
- Develop when market improves
- **Profit Potential:** Moderate
- **Timeframe:** 3-10 years

## Required Permits & Compliance

### City of Winston-Salem Requirements:
1. **Building Permit** - Required for all construction
2. **Site Plan Approval** - Must comply with UDO
3. **Zoning Compliance** - Verify RS-9 requirements met
4. **Environmental Review** - Soil tests, drainage, etc.

### Recommended Professionals:
- Licensed surveyor for lot verification
- Real estate attorney for legal review
- Licensed contractor for cost estimates
- Real estate agent for market insights
- Environmental consultant for site assessment

## Resources

### Winston-Salem Planning Department
- **Website:** https://www.cityofws.org/1551/Zoning-Subdivision
- **UDO Documents:** Available on city website
- **Contact:** Winston-Salem City Hall

### Additional Resources
- Unified Development Ordinance (UDO)
- Zoning maps and overlays
- Building code requirements
- Environmental regulations

## Customization

To analyze a different property, modify the `main()` function in `real_estate_expert.py`:

```python
# Change these values
address = "Your Address Here"
zoning = "Your Zoning Code"
```

To add new zoning codes or market data, update the respective dictionaries in the `ZoningAnalyzer` and `PropertyAnalyzer` classes.

## Technical Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## License

This tool is provided for informational purposes only. Always verify zoning information with local authorities and consult licensed professionals before making investment decisions.

## Disclaimer

This analysis tool provides general information based on publicly available data. It should not be considered:
- Legal advice
- Financial advice
- A substitute for professional real estate consultation
- Guaranteed accurate in all cases

Always:
- Verify zoning with City of Winston-Salem Planning Department
- Conduct thorough due diligence
- Consult with licensed professionals
- Review current market conditions
- Obtain professional property inspections

## Support

For questions about:
- **Zoning:** Contact Winston-Salem Planning & Development Services
- **Property Values:** Consult local real estate agents
- **Legal Matters:** Speak with a real estate attorney
- **Construction:** Engage licensed contractors and engineers

---

**Last Updated:** January 2026  
**Version:** 1.0.0
