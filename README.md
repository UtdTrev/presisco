# Precisco Farm Ventures Ltd. — Commercial Layer Poultry Management Portal
### Personalized Executive Dashboard & Multi-Page Farm Management Portal (Donezo Theme)

**Enterprise:** Precisco Farm Ventures Ltd.  
**Location:** Km 12, Asaba-Benin Expressway, Asaba, Delta State, Nigeria  
**Flock:** 6,000 Point-of-Lay (POL) Layer Birds (`PFV-LAY-001`)  
**Design System:** Donezo Clean Light & Forest Green Palette (`#124e3f`, `#34d399`, `#f4f6f9`)

---

## 🌟 Features & Highlights

- **Pure HTML, CSS & Vanilla JavaScript**: Zero build steps, zero node dependencies, zero bundler errors. Runs natively in any browser or static hosting environment.
- **Personalized Header**: Dynamic greeting, search bar with keyboard shortcut (`⌘F`), user profile indicator (`Mr. Adebayo Adeleke / manager@preciscofarms.com`), and role switcher.
- **Master Donezo Operations Dashboard**:
  - **Forest Green Highlight Card**: `5,892 Live Birds` (98.2% Livability)
  - **White Key Cards**: `5,172 Harvest Today (172.4 Crates)`, `87.8% Hen-Day Laying`, `6 Days of Feed Left`
  - **Laying Analytics**: 7-day capsule bar chart with hatched, mint green, and solid forest green bars
  - **Reminders**: Dark green action card with walkthrough and climate alerts
  - **Corporate Orders**: B2B order list with micro-icons (Transcorp Hotels, Grand Delta Supermarkets, Royal Crown Bakeries)
  - **Team Collaboration**: Attendant attendance and task status pills (`Completed`, `In Progress`, `Pending`)
  - **Flock Progress Gauge**: Semi-circular donut meter showing `87.8% Hen-Day Laying`
  - **Shift Time Tracker**: Interactive running digital timer (`01:24:08`) with Pause and Stop controls
- **Cross-Page Data Sync (`js/app.js`)**: All 16 pages share live state, calculations, and active roles using `localStorage`.

---

## 📁 File Structure

```text
precisco-portal/
 ├── index.html            # Brand Landing & Enterprise Overview
 ├── dashboard.html        # Master Donezo Personalized Dashboard
 ├── sales.html            # Corporate B2B Sales, Invoices & Waybills
 ├── financials.html       # Operating Expenses & P&L Ledger
 ├── operations.html       # 3-Shift Attendant SOP Checklists
 ├── eggs.html             # Twice-Daily Harvest & Crate Grading
 ├── flocks.html           # Flock PFV-LAY-001 (6,000 POL) Lifecycle
 ├── houses.html           # Main House 1 & 8 Fans Climate Telemetry
 ├── health.html           # Veterinary Health, Mortality & Sick Bay
 ├── feed.html             # Feed Intake (118g) & 15,000L Reservoir
 ├── inventory.html        # Warehouse Stocks & Supplies
 ├── tasks.html            # Tasks & SOP 5-Question Rule Manual
 ├── biosecurity.html      # Gate 1 Wheel Spray Dip & Visitor Log
 ├── reports.html          # Executive Performance Reports (Print/CSV)
 ├── alerts.html           # Alert Engine & Escalation Center
 ├── settings.html         # Farm Settings, Thresholds & RBAC
 ├── pages.html            # All 16 Pages Visual Directory / Sitemap
 ├── css/
 │    └── styles.css       # Clean, modern Donezo stylesheet
 ├── js/
 │    └── app.js          # Native JS state store & calculation engine
 ├── vercel.json           # Static deployment configuration
 └── README.md             # Documentation
```

---

## 🚀 How to Run & Deploy

### Option 1: Run Locally (Instant)
Double-click `dashboard.html` or `index.html` in any browser, or run:
```bash
cd precisco-portal
python3 -m http.server 5173
# Open http://localhost:5173/dashboard.html in your browser!
```

### Option 2: Deploy to GitHub & Vercel
```bash
cd precisco-portal
git init
git add .
git commit -m "feat: complete Precisco Farm Ventures Donezo portal"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/precisco-portal.git
git push -u origin main
```
Import the repository on **[vercel.com](https://vercel.com)** to deploy as a static site in 10 seconds.
