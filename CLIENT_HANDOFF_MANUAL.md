# PRECISCO FARM VENTURES LTD.
## Commercial Layer Farm Management & B2B Operations Portal
### Official Client Handoff, Operational Manual & User Training Guide

**Client:** Precisco Farm Ventures Ltd.  
**Farm Location:** Km 12, Asaba-Benin Expressway, Asaba, Delta State, Nigeria  
**Flock Specification:** 6,000 Point-of-Lay (POL) Layer Birds (`PFV-LAY-001`)  
**Live Portal URL:** [https://presisco.vercel.app/](https://presisco.vercel.app/)  
**Version:** 3.4.0 (Enterprise Commercial Edition)  
**Date of Deployment:** August 2026  

---

## 1. Executive System Overview

The **Precisco Farm Management Portal** is a custom-engineered, multi-role agricultural operating system built specifically for commercial egg production, feed optimization, and corporate B2B egg distribution.

### Core Capabilities:
* **Strict Role-Based Information Segregation:** 7 dedicated portal workspaces tailored for the Director, Farm Manager, Veterinary Officer, Attendants, Security Officers, Delivery Driver, and Consultant.
* **Feed Deduction & Anti-Fraud Engine:** Automated calculation of daily, weekly, and monthly feed requirements based on an **80g – 100g per bird benchmark**, paired with Economic Order Quantity (EOQ), Re-Order Level (ROL), and Minimum Order Quantity (MOQ) optimization.
* **Granular Egg Size Grading Derivatives:** Segregation into **Grade A Large (53–63g+)**, **Medium (45–52g)**, **Small Pullet (<45g)**, and **Hairline Cracked (Bakery Grade)** with commercial B2B pricing.
* **Organic Poultry Manure (Chicken Poo) Tracker:** Tracks wet droppings generated (**778 kg/day**) dried into **24 sacks of 50kg organic fertilizer/day** sold to local cassava and yam plantations (**₦201,600/week revenue stream**).
* **Corporate B2B Dispatch & Invoicing:** Digital waybills, security gate passes, 14-day terms, and accounts receivable tracking for Transcorp Hotels, Grand Delta Supermarkets, and Royal Crown Bakeries.
* **3-Tier Real-Time Data Pipeline:** Works offline inside the poultry house, synchronizes automatically to **Google Sheets** via webhook, and exports to **Microsoft Excel** in one click.

---

## 2. Staff Access Codes & Dedicated Portals Directory

Staff members open **[https://presisco.vercel.app/](https://presisco.vercel.app/)**, enter their assigned staff access code, and are automatically routed into their dedicated workspace:

| Designated Staff User | Official Title | Access Code | Dedicated Portal Link | Allowed Scope | Restricted (Hidden) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Engr. Charles Chukwuma** | **Director / Owner** | `PFV-DIR-2026` | `director.html` | Executive P&L, **Total Revenue (₦2.29M)**, ₦35.3M flock valuation, staff payroll & pensions, WhatsApp briefing generator. | Routine cleaning checklists. |
| **Mr. Adebayo Adeleke** | **Farm Manager** | `PFV-MGR-2026` | `manager.html` | Full operational control, 6,000 birds telemetry, **Physical Stock Reconciler**, ROL/EOQ/MOQ, B2B waybills, Vet emergency link. | None (Full Operational Control). |
| **Dr. Emeka Okonkwo, DVM** | **Veterinary Officer** | `PFV-VET-2026` | `vet.html` | Mortality necropsy logs, **Sick Bay Pen S-1 & S-2 isolation**, vaccine schedules, drug withdrawal safety locks. | ⛔ **Hidden:** Sales revenue, farm expenses, staff salaries. |
| **Chinedu / Blessing / Musa** | **Poultry Attendants (3)** | `PFV-ATT-2026` | `attendant.html` | 3-Shift checklists (Morning, Afternoon, Evening), **Twice-Daily Graded Harvests**, mortality bagging, feeder/drinker routines. | ⛔ **Hidden:** Financial ledgers, sales prices, payroll, stock valuations. |
| **Sgt. Joshua / Sunday / Usman**| **Security Officers (3)** | `PFV-SEC-2026` | `security.html` | Gate 1 & 2 log: **Vehicle Wheel Spray Dip (Virkon-S 1%)**, 48h screening, visitor registry, delivery truck gate passes. | ⛔ **Hidden:** Bird medical files, sales financials. |
| **Kenneth Obi** | **Logistics Driver** | `PFV-DRV-2026` | `driver.html` | Corporate delivery route waybills (Transcorp, Grand Delta, Royal Crown), customer addresses, **digital delivery sign-off**. | ⛔ **Hidden:** Internal farm management and medical logs. |
| **Dr. (Mrs.) Ifeoma Nnamdi** | **Poultry Consultant** | `PFV-CON-2026` | `consultant.html` | Read-only analytics: Hen-Day curves vs 88.5% peak breed standard, FCR efficiency (1.59 kg/doz), advisory notes. | Operational editing controls. |

---

## 3. Step-by-Step User Guides for Each Role

### 👑 3.1. Guide for the Director / Owner (Engr. Charles Chukwuma)
1. **Accessing Executive Dashboards:** Log in with code `PFV-DIR-2026` to open `director.html`.
2. **Reviewing Financial Performance:**
   * **Gross Revenue:** Displays combined revenue from B2B Egg Sales (₦1.99M) + Organic Manure Sales (₦300K).
   * **Operating Margin:** Displays live Gross Margin % (42.5%) and Net Operating Profit after deducting feed, diesel, wages, and veterinary supplies.
3. **Flock Asset Valuation:** Real-time valuation of the 5,892 mature laying hens at market replacement value (**₦35,352,000**).
4. **Spent Hen (Old Layer) Salvage Forecaster:** Displays projected lump-sum cash realization at flock retirement (72–80 weeks): $5,892 \times ₦3,200 = \mathbf{₦18,854,400}$.
5. **1-Click WhatsApp Executive Briefing:** Click the green **"📱 1-Click WhatsApp Report"** button to automatically copy a formatted daily summary to your clipboard, ready to paste on WhatsApp.
6. **Exporting Master Excel:** Click **"📥 Export Master Excel (.csv)"** to download the entire multi-table farm database.

---

### 👔 3.2. Guide for the Farm Manager (Mr. Adebayo Adeleke)
1. **Operational Command:** Log in with code `PFV-MGR-2026` to open `manager.html`.
2. **Daily Feed Stock Taking & Anti-Fraud Reconciler:**
   * Review the daily feed deduction table based on the **80g – 100g benchmark (95g/bird)** for 5,892 birds (559.7 kg/day = 22.4 bags).
   * Check physical closing bag count against recorded issuances to verify zero variance (no feed leakage or theft).
3. **Inventory Re-Order & MOQ Buffer:**
   * The portal automatically alerts you when stock reaches the **Re-Order Level (ROL = 55 bags)**.
   * Prompts ordering the **Minimum Order Quantity (MOQ = 200 bags / 5 tonnes)** or the **Economic Order Quantity (EOQ = 553 bags)**.
4. **Issuing B2B Waybills & Gate Passes:**
   * Click **"+ Issue B2B Waybill"**, select the corporate client (e.g. *Transcorp Hotels*), enter crate breakdown (Large / Medium), and confirm vehicle number.
   * Generates a digital waybill that synchronizes with the Delivery Driver and Security Gate.
5. **Emergency Link to Veterinary Officer:** Click **"🚨 Emergency Call to Vet"** to send an instant priority alert to Dr. Emeka for urgent pen walkthroughs.

---

### 🩺 3.3. Guide for the Veterinary Officer (Dr. Emeka Okonkwo, DVM)
1. **Clinical Welfare Portal:** Log in with code `PFV-VET-2026` to open `vet.html`.
2. **Mortality Logging & Necropsy:**
   * Record dead bird counts, suspected pathology (e.g. *Egg peritonitis*, *Cage fatigue*, *Vent trauma*), and verify on-farm incineration per `SOP-BIO-004`.
   * **6-Bird Threshold Engine:** If daily mortality $\ge 6$ birds, the portal flags an immediate critical health warning.
3. **Sick Bay Isolation Pen (Pen S-1 & S-2):**
   * Track isolated birds, cage row tags, clinical symptoms, and prescribed supportive therapies.
   * Click **"Mark Recovered"** once a bird is ready to return to the laying flock.
4. **Drug Withdrawal Safety Lock:** When pharmaceutical medications are administered, set the withdrawal countdown. The portal automatically locks commercial egg release to guarantee zero chemical residue in table eggs.

---

### 🐔 3.4. Guide for Poultry Attendants (Shift 1, 2, 3 Leads)
1. **Shift Workspace:** Log in with code `PFV-ATT-2026` to open `attendant.html`.
2. **Logging Twice-Daily Harvest with Size Derivatives:**
   * Click **"🥚 Log Graded Harvest"**.
   * Enter egg counts by size:
     - **Large (53–63g+)**
     - **Medium (45–52g)**
     - **Small Pullet (<45g)**
     - **Hairline Cracked**
     - **Broken / Rejects**
   * The portal auto-calculates standard 30-egg pulp trays and updates cold storage stock.
3. **Shift Checklists:** Check off items for Morning (06:30), Afternoon (12:00), and Evening (17:30) walkthroughs, drinker pressure checks (2.2 Bar), and manure conveyor checks.

---

### 🛡️ 3.5. Guide for Security Officers (Sgt. Joshua Garba & Sunday Alabi)
1. **Gate Security Desk:** Log in with code `PFV-SEC-2026` to open `security.html`.
2. **Gate 1 Vehicle Disinfection:** Record every vehicle entering the farm; verify that wheels pass through the **Virkon-S 1% deep spray dip**.
3. **48-Hour Poultry Contact Screening:** Verify and check that visitors have had zero poultry contact within the past 48 hours.
4. **Outbound Delivery Gate Passes:** Verify the driver's waybill crate count before authorizing truck departure.

---

### 🚚 3.6. Guide for the Logistics Delivery Driver (Kenneth Obi)
1. **Logistics Driver Hub:** Log in with code `PFV-DRV-2026` to open `driver.html`.
2. **Delivery Routes:** View active corporate delivery destinations (*Transcorp Hotels Waterfront*, *Grand Delta Supermarket Mall*, *Royal Crown Bakery Layout*).
3. **Delivery Receipts:** Click **"Confirm Delivery & Sign Receipt"** upon client inspection and offloading.

---

### 📊 3.7. Guide for the Poultry Consultant (Dr. (Mrs.) Ifeoma Nnamdi)
1. **Consultant Analytics:** Log in with code `PFV-CON-2026` to open `consultant.html`.
2. **Performance Benchmarking:** Review Hen-Day laying curve vs Lohmann Brown 88.5% peak standard, FCR efficiency (**1.59 kg/doz**), and mortality trends.
3. **Advisory Notes:** Click **"+ Submit Advisory Note"** to send management recommendations directly to the Director and Manager.

---

## 4. Mathematical & Operational Reference Guide

| Metric / Parameter | Mathematical Formula | Precisco Farm Benchmark |
| :--- | :--- | :--- |
| **Hen-Day Laying Rate %** | $(\text{Total Eggs Produced Today} / \text{Live Birds}) \times 100$ | **$87.8\%$** (Target Peak: $88.5\%$) |
| **Standard Crate Packing** | $\lfloor \text{Total Eggs} / 30 \rfloor + (\text{Total Eggs} \pmod{30}) \text{ loose}$ | **172.4 Crates / day** (5,172 eggs) |
| **Daily Feed Requirement** | $(\text{Live Birds} \times 95\text{g}) / 1000$ | **$559.7\text{ kg/day}$** (22.4 bags of 25kg) |
| **Weekly Feed Requirement** | $\text{Daily kg} \times 7$ | **$3,918\text{ kg/week}$** (156.7 bags = ₦2.90M) |
| **Monthly Feed Requirement** | $\text{Daily kg} \times 30$ | **$16,792\text{ kg/month}$** (671.7 bags = ₦12.42M) |
| **Economic Order Quantity** | $\text{EOQ} = \sqrt{(2 \times \text{Annual Demand} \times \text{Order Cost}) / \text{Holding Cost}}$ | **553 Bags** ($\approx 13.8$ tonnes) |
| **Re-Order Level (ROL)** | $(\text{Daily Usage} \times \text{Lead Time}) + \text{Safety Stock}$ | **55 Bags** |
| **Minimum Order Quantity** | Supplier Truckload Minimum | **200 Bags** (5 Tonnes) |
| **Feed Conversion Ratio** | $\text{Total Feed Consumed (kg)} / (\text{Total Eggs} / 12)$ | **$1.59\text{ kg feed / dozen eggs}$** |
| **Water-to-Feed Ratio** | $\text{Daily Water Consumed (L)} / \text{Daily Feed (kg)}$ | **$2.11 : 1$** ($1,180\text{L} : 560\text{kg}$ Normal) |
| **Organic Manure Harvest** | $5,892\text{ birds} \times 0.132\text{kg wet droppings}$ | **778 kg wet droppings/day $\to$ 24 sacks/day** (₦201,600/wk) |
| **Spent Hen Salvage Value** | $5,892\text{ mature layers} \times ₦3,200/\text{hen}$ | **₦18,854,400** lump-sum capital realization |

---

## 5. Google Sheets & Excel Data Integration

### Real-Time Google Sheets Synchronization:
1. Open Google Sheets and create a blank sheet: **`Precisco Farm Ventures - Master Operations Database`**.
2. Go to **Extensions** $\to$ **Apps Script**, paste the included code from **`google-apps-script.js`**, and click **Deploy as Web App** (*Who has access: Anyone*).
3. Paste the generated Web App URL into the **Settings** page of the portal.
4. Every entry (egg harvest, mortality, sales waybill, feed issue, manure sale, expense) will automatically append a new row into its dedicated Google Sheet tab in real-time.

### 1-Click Excel Export:
* Click **"Export Master Excel"** on any management page to instantly download the full `.csv` / `.xlsx` database.

---

## 6. Technical Specifications & Deployment

* **Architecture:** Self-Contained HTML5, CSS3, and Vanilla JavaScript (No Node runtime required, zero build lag).
* **Cross-Device Compatibility:** Fully responsive across mobile smartphones, tablets, laptops, and desktop monitors.
* **Offline Resilience:** Local storage caches all transactions locally so work continues uninterrupted during network outages.
* **Hosting:** Pre-configured for instant zero-config static deployment on **Vercel**, **GitHub Pages**, or local farm servers.

---

*Manual prepared for Engr. Charles Chukwuma, Mr. Adebayo Adeleke, and the staff of Precisco Farm Ventures Ltd.*
