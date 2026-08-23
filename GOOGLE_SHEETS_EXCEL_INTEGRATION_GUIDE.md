# PRECISCO FARM VENTURES LTD. — GOOGLE SHEETS & EXCEL DATA INTEGRATION MANUAL

This guide explains how data is captured, stored, synchronized in real-time to **Google Sheets**, and exported to **Microsoft Excel**.

---

## 1. Data Storage Architecture Overview

The system operates a **3-tier hybrid data pipeline**:

```
[Attendants / Vet / Manager on Farm Devices]
                     │
                     ▼
  Tier 1: Local Device & Offline Storage (`localStorage`)
  • Instant, zero-latency record creation
  • 100% functional even when pen Wi-Fi / cellular connectivity drops
                     │
                     ▼
  Tier 2: Real-Time Google Sheets Webhook Sync (`Google Apps Script`)
  • Automatically appends rows into separate Google Spreadsheet tabs
  • Accessible 24/7 by Director, Consultant, and Accountant anywhere
                     │
                     ▼
  Tier 3: 1-Click Master Excel / CSV Export (`.xlsx` / `.csv`)
  • Download the entire multi-table farm database in 1 click
```

---

## 2. Setting Up Live Real-Time Google Sheets Sync (2 Minutes)

You do **not** need complex database servers or monthly SaaS fees. You can use Google Sheets as your cloud database.

### Step-by-Step Instructions:

#### Step 1: Create a Google Spreadsheet
1. Open [Google Sheets](https://sheets.google.com) and create a **Blank spreadsheet**.
2. Name the spreadsheet: **`Precisco Farm Ventures - Master Operations Database`**.

#### Step 2: Open Google Apps Script
1. In your Google Spreadsheet menu, click **Extensions** $\to$ **Apps Script**.
2. Delete any existing code in the script editor.
3. Open the file **`google-apps-script.js`** (included in your portal repository) and copy the entire code.
4. Paste the code into the Google Apps Script editor.
5. Click the 💾 **Save** icon.

#### Step 3: Deploy as Web App
1. At the top right of Apps Script, click the blue **Deploy** button $\to$ **New deployment**.
2. Click the gear icon next to "Select type" and choose **Web app**.
3. Fill in the deployment details:
   - **Description:** `Precisco Farm Portal Webhook`
   - **Execute as:** `Me (your email)`
   - **Who has access:** `Anyone` *(Allows your farm portal to securely post entries without complex OAuth popups)*
4. Click **Deploy**.
5. Grant permissions if prompted by Google.
6. Copy the generated **Web App URL** (looks like `https://script.google.com/macros/s/AKfycbx.../exec`).

#### Step 4: Connect URL to Your Farm Portal
1. Open your Precisco Farm Portal in your browser.
2. Go to **Settings** (`settings.html`) or the **Google Sheets Sync** card.
3. Paste your Web App URL into the **Google Sheets Webhook URL** input box.
4. Click **Save Webhook URL**.

---

## 3. Automated Google Spreadsheet Tabs

Once connected, every action taken in the portal automatically creates and populates dedicated tabs in your Google Sheet:

| Google Sheet Tab Name | Auto-Populated Columns | Trigger Action |
| :--- | :--- | :--- |
| **`Egg_Harvest_Log`** | Log ID, Date, Time, Harvest Round, Grade A Good, Cracked, Broken, Rejects, Total Eggs, Trays (30-Egg), Hen-Day %, Staff Name, Recorded At | When attendant logs Morning or Afternoon egg run |
| **`Mortality_Records`** | Mortality ID, Date, Time, Dead Birds Count, Suspected Cause, Biosecurity Disposal Action, Reported By, Review Status, Recorded At | When mortality is recorded |
| **`Feed_Records`** | Feed ID, Date, Formulation, Issued (kg), Remaining (kg), Consumed (kg), Live Birds, g/bird/day, Intake Status, Staff Name | When daily feed ration is issued |
| **`Corporate_Sales_Orders`** | Order ID, Waybill #, Date, Corporate Client, Crates, Unit Price ₦, Total ₦, Paid ₦, Balance Due ₦, Status, Vehicle | When B2B order & waybill is created |
| **`Farm_Expenses_PL`** | Voucher ID, Date, Category, Description, Amount ₦, Payee / Vendor, Authorized By | When farm expense voucher is posted |
| **`Sick_Bay_Isolation`** | Case ID, Date, Cage Location, Observed Symptoms, Diagnosis, Isolation Bay, Prescribed Therapy, Attendant, Status | When sick bird is isolated in Pen S-1 |
| **`Gate_Biosecurity_Visitors`** | Visitor ID, Date, Time In, Visitor Name & Organization, Purpose of Visit, Checks Passed, Security Officer | When visitor or vehicle logs entry at Gate 1 |

---

## 4. Microsoft Excel Direct Download & Backup

You can download your entire database into Excel without configuring Google Sheets:

1. In the portal navigation dock or reports page, click **"Export Master Excel"**.
2. The portal instantly compiles and downloads a formatted CSV spreadsheet containing all tables:
   - Egg Collection & Grading History
   - B2B Corporate Sales & Waybill Registers
   - Daily Mortality Logs
   - Operating Cost Ledger
3. Double-click the downloaded file to open in **Microsoft Excel**, **Apple Numbers**, or **Google Sheets**.
