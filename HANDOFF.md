# PRECISCO FARM VENTURES LTD. — COMPREHENSIVE PROJECT HANDOFF DOCUMENT
**System:** Commercial Layer Farm Management & B2B Corporate Supply Portal  
**Theme:** Donezo Personalized Light & Forest Green UI (`#124e3f`, `#34d399`, `#f2f5f7`)  
**Language:** English (100% Comprehensive)  
**Deliverable Package:** `/home/user/precisco_farm_portal.zip` (117 KB)  
**Date:** August 20, 2026  

---

## 1. Executive Summary & Farm Profile

| Attribute | Specification |
| :--- | :--- |
| **Enterprise Name** | **Precisco Farm Ventures Ltd.** |
| **Farm Location** | Km 12, Asaba-Benin Expressway, Asaba, Delta State, Nigeria |
| **Flock Size & Type** | **6,000 Point-of-Lay (POL) Layer Birds** |
| **Current Active Batch** | `PFV-LAY-001 – 6,000 POL birds – 2026 Batch 1` |
| **Breed / Lineage** | Lohmann Brown Classic (Commercial Layer Strain) |
| **Placement Date & Age** | Placed 10 Feb 2026 at 18 wks (POL); currently **34 Weeks (Peak Laying Stage)** |
| **Current Live Birds** | **5,892 Birds** (Cumulative Mortality: 108 birds; **98.2% Livability**) |
| **Housing Infrastructure** | 1 Main Commercial Unit (Automated 3-Tier Galvanized Battery Cage, 8 Heavy-Duty Exhaust Fans, Automated 2.2 Bar Nipple Drinker Lines, 15,000L Overhead Water Reservoir) |
| **Primary Business Model** | Bulk B2B Egg Supply to Corporate Customers (Hotels, Supermarkets, Bakeries, Caterers) |

---

## 2. Staffing & Role-Based Access Control (RBAC)

The portal features a live **User Role Switcher** in the sidebar/top bar that dynamically adjusts permissions across 6 distinct organizational roles:

| Staff Member | Title & Role | Permissions & Operational Scope |
| :--- | :--- | :--- |
| **Engr. Charles Chukwuma** | **Director / Owner** (`director`) | Executive P&L ledger, corporate receivables, profit margin, strategic reports, high-level audit approvals. |
| **Mr. Adebayo Adeleke** | **Farm Manager** (`manager`) | Full operational control, supervisor sign-offs, feed/egg inventory, B2B waybills, gate passes, staff supervision. |
| **Dr. Emeka Okonkwo, DVM** | **Veterinary Officer** (`veterinarian`) | Health logs, sick bird isolation bays, scheduled vaccines, prescriptions, drug withdrawal safety locks. |
| **Dr. (Mrs.) Ifeoma Nnamdi** | **Poultry Consultant** (`consultant`) | Read-only analytics, Hen-Day efficiency curves, FCR benchmarks, advisory reviews. |
| **Chinedu Obi** | **Attendant (Shift 1 Lead)** (`attendant`) | Morning 6,000 bird inspection, mortality removal, Round 1 egg harvest (08:30 AM), feed distribution. |
| **Blessing Eze** | **Attendant (Shift 2 Lead)** (`attendant`) | Afternoon heat check, sick bird monitoring, Round 2 egg harvest (02:30 PM), cold room tray packing. |
| **Musa Ibrahim** | **Attendant (Shift 3 Lead)** (`attendant`) | Evening health sweep, water reservoir check, lighting shutdown timer, door locks, night security handover. |
| **Sgt. Joshua Garba** | **Security Officer (Gate 1)** (`security`) | Main gate vehicle wheel spray dip logs (Virkon-S 1%), 48h poultry contact screening, visitor registry. |
| **Sunday Alabi** | **Security Officer (Gate 2)** (`security`) | Depot gate, delivery vehicle inspection, dispatch waybill verification, gate pass sign-offs. |

---

## 3. Mathematical Calculations & Performance Engines

### A. Twice-Daily Egg Harvest & 30-Egg Crate Calculator
$$\text{Total Daily Eggs} = \text{Round 1 (Morning: 08:30 AM)} + \text{Round 2 (Afternoon: 02:30 PM)}$$
$$\text{Standard Trays (30-Egg Crates)} = \left\lfloor \frac{\text{Total Harvest}}{30} \right\rfloor + (\text{Total Harvest} \pmod{30}) \text{ loose eggs}$$
$$\text{Grade A Marketable Rate (\%)} = \left( \frac{\text{Grade A Good Eggs}}{\text{Total Harvest}} \right) \times 100 \quad [\text{Baseline: } 98.6\%]$$

### B. Hen-Day Laying Productivity (Flock Efficiency)
$$\text{Hen-Day Laying Rate (\%)} = \left( \frac{\text{Total Eggs Harvested Today}}{\text{Current Live Birds (5,892)}} \right) \times 100$$
*Baseline Current:* **$87.8\%$** (Peak target: **$88.5\%$**).

### C. Daily Feed Intake & Predictive Buffer Forecast
$$\text{Daily Feed Consumed (kg)} = \text{Feed Issued (kg)} - \text{Trough Balance Remaining (kg)}$$
$$\text{Intake per Bird (g/day)} = \left( \frac{\text{Feed Consumed (kg)} \times 1000}{\text{Live Birds (5,892)}} \right) \quad [\text{Optimal: } 115\text{g} - 125\text{g}, \text{ Current: } 116.3\text{g}]$$
$$\text{Days of Feed Remaining} = \left\lfloor \frac{\text{Warehouse Bags} \times 25\text{kg}}{\text{Daily Feed Consumed (kg)}} \right\rfloor \quad [\text{Current: } 6\text{ Days left}]$$
*Automatic Alert:* If $\text{Days of Feed Remaining} \le 5\text{ days}$, auto-notification is sent to the Manager to order 200 bags.

### D. Feed Conversion Ratio (FCR) per Dozen Eggs
$$\text{FCR}_{\text{dozen}} = \frac{\text{Total Feed Consumed (kg)}}{\text{Total Eggs Produced} / 12} \quad [\text{Baseline: } 1.59\text{ kg feed / dozen}]$$

### E. Financial Profitability & Corporate Invoicing
$$\text{Total B2B Revenue} = \sum (\text{Crates Dispatched} \times \text{Agreed Corporate Rate})$$
$$\text{Operating Profit} = \text{B2B Revenue} - (\text{Feed} + \text{Veterinary} + \text{Diesel/Power} + \text{Packaging} + \text{Salaries})$$
$$\text{Corporate Receivables} = \sum (\text{Total Invoiced} - \text{Cash/Transfer Paid})$$

---

## 4. Complete Directory of All 17 Pages

All 17 pages are self-contained `.html` files in `/home/user/precisco-portal/` with zero build dependencies:

| # | File Name | Route / Title | Purpose & Content |
| :--- | :--- | :--- | :--- |
| **1** | `index.html` | `/#/showcase` | Brand Landing Page with Donezo telemetry mockup & feature highlights. |
| **2** | `dashboard.html` | `/#/dashboard` | **Master Control Room**: 4 KPI cards (1 Forest green + 3 White), capsule bar chart, reminders, orders widget, team list, semi-circle donut meter, and running digital shift timer. |
| **3** | `sales.html` | `/#/sales` | **Corporate B2B Sales**: Client accounts (Transcorp Hotels, Grand Delta Supermarkets), delivery waybills, invoices, and accounts receivable tracker. |
| **4** | `financials.html` | `/#/financials` | **P&L Ledger**: General ledger, operating expenses by category, gross margin %, and cost per crate. |
| **5** | `operations.html` | `/#/operations` | **3-Shift SOP Checklists**: Morning (06:30), Afternoon (12:00), and Evening (17:30) checklists with supervisor approvals. |
| **6** | `eggs.html` | `/#/eggs` | **Twice-Daily Harvest**: Morning & afternoon logs, 30-egg crate converter, hairline crack sorting, and CSV exporter. |
| **7** | `flocks.html` | `/#/flocks` | **Flock PFV-LAY-001**: 6,000 POL layer records, age 34 wks peak, Lohmann Brown lineage, and cumulative eggs. |
| **8** | `houses.html` | `/#/houses` | **Main House 1**: 3-tier cage telemetry, 8 exhaust fans, 2.2 Bar drinker pressure, and Asaba heat check. |
| **9** | `health.html` | `/#/health` | **Veterinary Welfare**: Mortality logging (incineration SOP-BIO-004), Sick Bay Pen S-1 isolation, and drug withdrawal hold. |
| **10** | `feed.html` | `/#/feed` | **Feed & Water**: 118g/bird benchmark, Days of Feed remaining forecast, and 15,000L reservoir monitor. |
| **11** | `inventory.html` | `/#/inventory` | **Warehouse Inventory**: Feed bags, cold room egg crates, vaccine cold chain, and packaging trays. |
| **12** | `tasks.html` | `/#/tasks` | **SOP Manual**: Standard operating procedures implementing the 5-Question Framework (*What → When → By Whom → Record → Abnormal*). |
| **13** | `biosecurity.html` | `/#/biosecurity` | **Gate Biosecurity**: Gate 1 vehicle wheel spray dip logs, 48h screening, and visitor registry. |
| **14** | `reports.html` | `/#/reports` | **Executive Reports**: Hen-Day curve, FCR per dozen, egg sales revenue, with Print & CSV exports. |
| **15** | `alerts.html` | `/#/alerts` | **Alert Engine**: Automated rule engine for mortality spikes, heat stress, feed shortages, and food safety holds. |
| **16** | `settings.html` | `/#/settings` | **Settings & RBAC**: Configurable thresholds, ₦ pricing, 6 staff role directories, and demo data reset. |
| **17** | `pages.html` | `/#/pages` | **Visual Sitemap**: 16 clickable cards to jump directly to any page. |

---

## 5. Technology Stack & File Map

```text
/home/user/precisco-portal/
 ├── index.html                  # Brand Landing Page
 ├── dashboard.html              # Master Donezo Personalized Dashboard
 ├── sales.html                  # Corporate B2B Sales & Invoicing
 ├── financials.html             # Operating Expenses & P&L Ledger
 ├── operations.html             # 3-Shift Attendant SOP Checklists
 ├── eggs.html                   # Twice-Daily Harvest & Crate Grading
 ├── flocks.html                 # Flock PFV-LAY-001 (6,000 POL) Lifecycle
 ├── houses.html                 # Main House 1, 8 Fans & Climate
 ├── health.html                 # Veterinary Health, Mortality & Sick Bay
 ├── feed.html                   # Feed Intake (118g) & Days-of-Feed Forecast
 ├── inventory.html              # Warehouse Stocks & Packaging
 ├── tasks.html                  # Tasks & SOP 5-Question Rule Manual
 ├── biosecurity.html            # Gate 1 Wheel Spray Dip & Visitor Log
 ├── reports.html                # Executive Performance Reports (Print/CSV)
 ├── alerts.html                 # Alert Engine & Incident Center
 ├── settings.html               # Farm Settings, Thresholds & RBAC
 ├── pages.html                  # All 16 Pages Directory / Sitemap
 │
 ├── css/
 │    └── styles.css             # Donezo Light & Forest Green Stylesheet
 ├── js/
 │    └── app.js                # State Store, localStorage Sync, Calculators & Modals
 ├── generate_pages.py           # Multi-page HTML generator engine
 ├── build_all_html.py           # Automated page builder script
 ├── vercel.json                 # Vercel static hosting routing configuration
 └── README.md                   # Complete Deployment Manual
```

---

## 6. How to Deploy to GitHub & Vercel (10 Seconds)

### Step 1: Push to GitHub
```bash
cd /home/user/precisco-portal
git init
git add .
git commit -m "feat: Precisco Farm Ventures complete Donezo 6,000 POL layer portal"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/precisco-farm-portal.git
git push -u origin main
```

### Step 2: Deploy to Vercel
1. Go to **[vercel.com](https://vercel.com)** and log in.
2. Click **"Add New..."** $\to$ **"Project"** $\to$ Import your GitHub repository.
3. Vercel automatically deploys static HTML/CSS/JS repositories without any build commands.
4. Click **"Deploy"**. The site will be live instantly with SSL on `https://precisco-farm-portal.vercel.app`.

---

## 7. How to Continue Development in Future Sessions

If extending this project with a backend (Node.js/Express, Python/FastAPI, or Supabase):
1. **API Integration:** Replace the `FarmStore` class methods in `js/app.js` with `fetch('/api/...')` REST endpoints or Supabase client queries.
2. **Database Schema:** Use the PostgreSQL schema provided in `Layer_Poultry_Management_Framework_Asaba.md`.
3. **Authentication:** Connect OAuth / JWT authentication to the existing `currentUser` role switcher state.
