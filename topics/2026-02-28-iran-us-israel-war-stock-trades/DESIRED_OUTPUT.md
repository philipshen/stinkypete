# Desired Output: Iran-US/Israel War Stock Trades

## Format
A single interactive static HTML file (no build step, no dependencies beyond CDN-loaded libraries).

## Structure

### Header
- Title: "Iran-US/Israel Conflict: Stock Trade Ideas"
- Subtitle with date and brief context
- Disclaimer: "For informational purposes only. Not financial advice."

### Filter Bar
- Filter by sector (Defense, Energy, Cybersecurity, Gold/Precious Metals, Shipping, Shorts/Hedges, Nuclear, Israeli Defense)
- Filter by trade direction (Long, Short, Hedge)
- Filter by risk level (Low, Medium, High)
- Filter by conviction (High, Medium, Speculative)
- Sort by: sector, risk, conviction

### Trade Cards (main content)
Each card displays:
- **Ticker symbol** (prominent)
- **Company name**
- **Sector tag** (color-coded)
- **Direction**: Long / Short / Hedge
- **Thesis**: 2-4 sentence investment thesis with citations [^1]
- **Risk level**: Low / Medium / High (with visual indicator)
- **Conviction**: High / Medium / Speculative
- **Risk/Reward chart**: Visual bar or gauge showing downside risk vs upside potential (approximate price targets or percentage moves)
- **Key risks**: Bullet points of what could go wrong
- **Historical precedent**: Brief note on how this stock/sector performed in past conflicts
- **Citations**: Footnote references to research sources

### Sectors to Cover
1. **Defense/Aerospace** — Lockheed Martin, Raytheon (RTX), Northrop Grumman, General Dynamics, L3Harris, etc.
2. **Energy/Oil** — Exxon, Chevron, ConocoPhillips, Halliburton, Schlumberger, etc.
3. **Cybersecurity** — CrowdStrike, Palo Alto Networks, Fortinet, etc.
4. **Gold/Precious Metals** — Newmont, Barrick Gold, gold ETFs
5. **Shipping/Logistics** — Companies affected by Strait of Hormuz / Red Sea disruptions
6. **Israeli Defense** — Elbit Systems, etc.
7. **Nuclear/Uranium** — Cameco, uranium ETFs
8. **Shorts/Hedges** — Airlines, travel stocks, emerging market exposures that would be hurt

### Risk/Reward Visualization
For each trade card, include a horizontal bar chart or gauge showing:
- Current price (or recent level)
- Downside target (bear case)
- Upside target (bull case)
- Visual representation of risk/reward ratio

### Sources Section
- Full list of all citations with URLs
- Organized by topic area
- Every factual claim in a thesis must have a citation

## Technical Requirements
- Single HTML file, self-contained
- Use Tailwind CSS via CDN for styling
- Use vanilla JavaScript for interactivity (filtering, sorting)
- Dark theme with accent colors for sectors
- Responsive — works on mobile and desktop
- Charts rendered with inline SVG or simple CSS (no heavy chart library needed)
