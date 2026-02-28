# Desired Output

A **static HTML site** (`outputs/index.html`) with the following characteristics:

## Structure
1. **Hero section** with title "Unmanned Marine Vehicle (UMV) Market Report" and brief intro
2. **Section 1: Top 15 UMVs by Sales** — card-based layout with:
   - Vehicle name and image (embedded or linked)
   - Manufacturer
   - Largest buyers (nations/organizations)
   - Estimated sales/deployment numbers
   - Primary use cases
   - Brief description
3. **Section 2: 10 Up-and-Coming UUVs** — similar card layout with:
   - Vehicle name and image
   - Manufacturer
   - Development stage
   - Target buyers
   - Intended use cases
   - What makes it notable
4. **Section 3: Honorable Mentions** — compact list/table for both categories with:
   - Same data fields as the relevant section
   - A note on why it didn't make the cut
5. **Sources section** — footnoted references

## Design
- Clean, modern, professional design
- Responsive layout
- All CSS and JS inline (single self-contained HTML file)
- Images embedded as base64 or referenced via URLs from research sources
- Dark/light mode toggle optional but nice-to-have

## Supporting Files
- `outputs/SOURCES.md` — consolidated list of all citations and references
