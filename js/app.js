/**
 * PRECISCO FARM VENTURES LTD. — MASTER APPLICATION & ADVANCED POULTRY ENGINE
 * Core Features:
 * - 80-100g Feed Deduction Engine, EOQ/ROL/MOQ
 * - Granular Egg Size Derivatives (Large, Medium, Small, Cracked, Broken, Rejects)
 * - Organic Manure Waste & Fertilizer Revenue Tracker
 * - Water-to-Feed Intake Ratio & Leak Detection (1.8 - 2.2 : 1)
 * - Customer Credit Aging (0-7d, 8-14d, 15-30d)
 * - Spent Hen (Old Layers) Salvage Valuation Forecaster
 * - 1-Click WhatsApp Daily Executive Briefing Generator
 */

const STORAGE_KEY = 'precisco_farm_state_v3';
const AUTH_KEY = 'precisco_farm_auth_session_v3';
const GOOGLE_SHEETS_CONFIG_KEY = 'precisco_google_sheets_url';

// 7 Distinct Staff Access Roles Directory
const ACCESS_ROLES = {
  "PFV-MGR-2026": {
    id: "STF-MGR",
    name: "Mr. Adebayo Adeleke",
    role: "Farm Manager",
    roleKey: "manager",
    email: "manager@preciscofarms.com",
    badge: "FARM MANAGER",
    portalUrl: "manager.html"
  },
  "PFV-DIR-2026": {
    id: "STF-DIR",
    name: "Engr. Charles Chukwuma",
    role: "Director / Owner",
    roleKey: "director",
    email: "charles@preciscofarms.com",
    badge: "DIRECTOR / OWNER",
    portalUrl: "director.html"
  },
  "PFV-VET-2026": {
    id: "STF-VET",
    name: "Dr. Emeka Okonkwo, DVM",
    role: "Veterinary Officer",
    roleKey: "veterinarian",
    email: "vet@preciscofarms.com",
    badge: "VETERINARY OFFICER",
    portalUrl: "vet.html"
  },
  "PFV-ATT-2026": {
    id: "STF-AT1",
    name: "Chinedu Obi",
    role: "Poultry Attendant (Shift 1 Lead)",
    roleKey: "attendant",
    email: "chinedu@preciscofarms.com",
    badge: "POULTRY ATTENDANT",
    portalUrl: "attendant.html"
  },
  "PFV-SEC-2026": {
    id: "STF-SEC1",
    name: "Sgt. Joshua Garba",
    role: "Security Officer (Gate 1 Lead)",
    roleKey: "security",
    email: "security@preciscofarms.com",
    badge: "GATE SECURITY",
    portalUrl: "security.html"
  },
  "PFV-DRV-2026": {
    id: "STF-DRV",
    name: "Kenneth Obi",
    role: "Corporate Logistics Driver",
    roleKey: "driver",
    email: "logistics@preciscofarms.com",
    badge: "LOGISTICS DRIVER",
    portalUrl: "driver.html"
  },
  "PFV-CON-2026": {
    id: "STF-CON",
    name: "Dr. (Mrs.) Ifeoma Nnamdi",
    role: "Poultry Consultant",
    roleKey: "consultant",
    email: "consultant@preciscofarms.com",
    badge: "POULTRY CONSULTANT",
    portalUrl: "consultant.html"
  }
};

// Master Initial State
const DEFAULT_STATE = {
  currentUser: ACCESS_ROLES["PFV-MGR-2026"],
  farm: {
    name: "Precisco Farm Ventures Ltd.",
    location: "Km 12, Asaba-Benin Expressway, Asaba, Delta State",
    capacity: 6000,
    pricePerTrayLarge: 4500,
    pricePerTrayMedium: 4300,
    pricePerTraySmall: 3800,
    pricePerTrayCracked: 3200,
    manurePricePerBag: 1200,
    feedPricePerBag: 18500,
    spentHenPrice: 3200,
    feedGramPerBirdTarget: 95
  },
  batch: {
    id: "PFV-LAY-001",
    name: "PFV-LAY-001 – 6,000 POL birds – 2026 Batch 1",
    breed: "Lohmann Brown Classic",
    initialBirds: 6000,
    currentBirds: 5892,
    ageWeeks: 34,
    stage: "Peak Laying Stage (34 Wks)",
    feedType: "Layers Mash Phase 1 (17.5% CP)",
    targetHenDay: 88.5,
    cumulativeEggs: 412500,
    totalMortality: 108,
    withdrawalUntil: null
  },
  house: {
    id: "PEN-01",
    name: "Main Production House 1",
    type: "Automated 3-Tier Galvanized Battery Cage",
    currentTemp: 29.6,
    humidity: 72,
    fansActive: 7,
    fanCount: 8,
    waterPressure: 2.2,
    waterLitersConsumed: 1180, // ~2.1 : 1 ratio vs 560kg feed
    waterStatus: "Normal (2.2 Bar) • Automated Header Tank Active",
    lighting: "05:30 - 21:30 (16-Hour Photoperiod Active)"
  },
  // Granular Egg Harvest with Size Derivatives
  eggs: [
    {
      id: "EGG-01",
      date: "2026-08-19",
      time: "08:30 AM",
      round: "Morning Harvest (Round 1)",
      large: 1850,
      medium: 1120,
      small: 150,
      cracked: 22,
      broken: 8,
      reject: 14,
      totalGood: 3120,
      total: 3164,
      trays: 105.4,
      henDay: 53.7,
      staff: "Chinedu Obi"
    },
    {
      id: "EGG-02",
      date: "2026-08-19",
      time: "02:30 PM",
      round: "Afternoon Harvest (Round 2)",
      large: 1180,
      medium: 710,
      small: 90,
      cracked: 15,
      broken: 4,
      reject: 9,
      totalGood: 1980,
      total: 2008,
      trays: 66.9,
      henDay: 87.8,
      staff: "Blessing Eze"
    }
  ],
  mortality: [
    { id: "MORT-01", date: "2026-08-19", time: "07:15 AM", count: 3, reason: "Egg peritonitis / cage fatigue", action: "Incinerated per SOP-BIO-004", staff: "Chinedu Obi", status: "Verified by Manager" },
    { id: "MORT-02", date: "2026-08-18", time: "07:20 AM", count: 2, reason: "Vent pecking trauma", action: "Incinerated per SOP-BIO-004", staff: "Blessing Eze", status: "Verified by Manager" }
  ],
  sickBirds: [
    { id: "SCK-01", date: "2026-08-19", tag: "Cage Tier 2-A4", symptoms: "Dullness, pale comb, reduced water intake", diagnosis: "Respiratory stress / fatigue", isolation: "Sick Bay Pen S-1", treatment: "Oral Multivitamins + Electrolytes", status: "Active Isolation", staff: "Chinedu Obi" },
    { id: "SCK-02", date: "2026-08-18", tag: "Cage Tier 3-B12", symptoms: "Vent abrasion from pecking", diagnosis: "Vent trauma", isolation: "Sick Bay Pen S-2", treatment: "Gentian Violet spray + Vitamin K", status: "Recovered", staff: "Blessing Eze" }
  ],
  feed: [
    {
      id: "FEED-01",
      date: "2026-08-19",
      type: "Layers Mash Phase 1",
      openingBags: 185,
      issuedKg: 575,
      remainingKg: 15,
      consumedKg: 560,
      live: 5892,
      expectedGrams: 95,
      actualGrams: 95.04,
      waterConsumedLiters: 1180,
      waterFeedRatio: "2.11 : 1",
      status: "Optimal Precision",
      staff: "Adebayo Adeleke"
    }
  ],
  manureLogs: [
    {
      id: "MNR-2026-0819",
      date: "2026-08-19",
      wetWeightKg: 780,
      bagsHarvested: 24,
      moistureStatus: "Conveyor Belt Dry",
      storedBagsTotal: 240,
      disposalAction: "Bagged in 50kg bags for Cassava & Yam Farmers",
      staff: "Musa Ibrahim"
    }
  ],
  manureSales: [
    { id: "MAN-01", date: "2026-08-16", buyer: "Asaba Green Farmers Cooperative", bags: 150, unitPrice: 1200, total: 180000, status: "Paid in Cash", staff: "Adebayo Adeleke" },
    { id: "MAN-02", date: "2026-08-09", buyer: "Oshimili Cassava & Yam Plantations", bags: 100, unitPrice: 1200, total: 120000, status: "Paid via Transfer", staff: "Adebayo Adeleke" }
  ],
  inventoryItems: [
    { id: "INV-FD-01", category: "Feed", name: "Layers Mash Phase 1 (25kg Bags)", inStock: 157, reorderPoint: 55, moq: 200, eoq: 553, unit: "Bags", cost: 18500, supplier: "Vital Feeds Ltd", dailyUsage: 22.4, daysLeft: 7.0, status: "Safe Buffer" },
    { id: "INV-FD-02", category: "Feed", name: "Coarse Oyster Shell Grit (50kg)", inStock: 30, reorderPoint: 15, moq: 50, eoq: 80, unit: "Bags", cost: 8500, supplier: "Delta Minerals", dailyUsage: 1.2, daysLeft: 25, status: "Adequate" },
    { id: "INV-EG-01", category: "Eggs", name: "Grade A Large Stored Crates (53-63g)", inStock: 290, reorderPoint: 60, moq: 150, eoq: 200, unit: "Crates", cost: 4500, supplier: "Main House 1", dailyUsage: 100, daysLeft: 2.9, status: "Ready for Dispatch" },
    { id: "INV-EG-02", category: "Eggs", name: "Grade A Medium Stored Crates (45-52g)", inStock: 165, reorderPoint: 40, moq: 100, eoq: 150, unit: "Crates", cost: 4300, supplier: "Main House 1", dailyUsage: 50, daysLeft: 3.3, status: "Ready for Dispatch" },
    { id: "INV-EG-03", category: "Eggs", name: "Grade A Small / Pullet Crates (<45g)", inStock: 30, reorderPoint: 10, moq: 30, eoq: 50, unit: "Crates", cost: 3800, supplier: "Main House 1", dailyUsage: 10, daysLeft: 3.0, status: "Ready for Dispatch" },
    { id: "INV-EG-04", category: "Eggs", name: "Hairline Cracked Bakery Crates", inStock: 18, reorderPoint: 5, moq: 20, eoq: 30, unit: "Crates", cost: 3200, supplier: "Main House 1", dailyUsage: 8, daysLeft: 2.2, status: "Bakery Grade" },
    { id: "INV-MN-01", category: "Manure", name: "Dry Organic Poultry Manure (50kg Bags)", inStock: 240, reorderPoint: 50, moq: 100, eoq: 200, unit: "Bags", cost: 1200, supplier: "Manure Scraper", dailyUsage: 0, daysLeft: 0, status: "Ready for Sale" },
    { id: "INV-VT-01", category: "Veterinary", name: "Lasota ND Vaccine (1000 doses)", inStock: 12, reorderPoint: 6, moq: 20, eoq: 25, unit: "Vials", cost: 3500, supplier: "NVRI Vom", dailyUsage: 0, daysLeft: 32, status: "Cold Chain 4°C" },
    { id: "INV-SP-01", category: "Packaging", name: "30-Egg Pulp Trays (100-pack bundles)", inStock: 120, reorderPoint: 40, moq: 100, eoq: 120, unit: "Bundles", cost: 9500, supplier: "Onitsha Packaging", dailyUsage: 1.7, daysLeft: 70, status: "Adequate" }
  ],
  sales: [
    { id: "ORD-01", waybill: "WB-PFV-2026-104", date: "2026-08-18", customer: "Transcorp Hotels & Suites Ltd", address: "Plot 4 Asaba Waterfront District", contact: "Chef Gabriel Alonge (+234 803 112 8899)", cratesLarge: 80, cratesMed: 40, cratesTotal: 120, unitPrice: 4300, total: 516000, paid: 0, balance: 516000, status: "Outstanding (14-Day Term)", agingBracket: "0-7 Days", driver: "Kenneth Obi", vehicle: "Toyota Dyna (DLT-892-XA)", gatePass: "PASS-0818-01" },
    { id: "ORD-02", waybill: "WB-PFV-2026-103", date: "2026-08-17", customer: "Grand Delta Supermarkets Ltd", address: "Okpanam Road Commercial Mall, Asaba", contact: "Mrs. Nneka Umeh (+234 802 445 9900)", cratesLarge: 100, cratesMed: 100, cratesTotal: 200, unitPrice: 4250, total: 850000, paid: 850000, balance: 0, status: "Paid in Full", agingBracket: "Cleared", driver: "Kenneth Obi", vehicle: "Isuzu Truck (ASB-441-XX)", gatePass: "PASS-0817-02" },
    { id: "ORD-03", waybill: "WB-PFV-2026-102", date: "2026-08-15", customer: "Royal Crown Confectioneries", address: "Benin-Asaba Expressway Industrial Area", contact: "Mr. Tunde Bakare (+234 813 778 2211)", cratesLarge: 50, cratesMed: 100, cratesTotal: 150, unitPrice: 4200, total: 630000, paid: 630000, balance: 0, status: "Paid in Full", agingBracket: "Cleared", driver: "Kenneth Obi", vehicle: "Ford Transit (BEN-119-AA)", gatePass: "PASS-0815-03" }
  ],
  expenses: [
    { id: "EXP-01", date: "2026-08-15", category: "Feed Purchases", desc: "Purchase of 200 bags Layers Mash Phase 1 (Vital Feeds)", amount: 3700000, payee: "Vital Feeds Distributor Ltd", authorizedBy: "Engr. Charles Chukwuma" },
    { id: "EXP-02", date: "2026-08-12", category: "Veterinary Supplies", desc: "Lasota ND vaccines + Electrolyte stress packs", amount: 145000, payee: "NVRI Vom / Vet Planet", authorizedBy: "Mr. Adebayo Adeleke" },
    { id: "EXP-03", date: "2026-08-10", category: "Logistics & Diesel Fuel", desc: "1,000L Diesel for farm backup generator & ventilation", amount: 1250000, payee: "Rainoil Depot Asaba", authorizedBy: "Engr. Charles Chukwuma" },
    { id: "EXP-04", date: "2026-08-08", category: "Cleaning & Disinfectants", desc: "5 Tubs Virkon-S 5kg + Disinfectant wheel spray", amount: 225000, payee: "Animal Care Asaba", authorizedBy: "Mr. Adebayo Adeleke" },
    { id: "EXP-05", date: "2026-08-05", category: "Pest Control & Fumigation", desc: "Rodent bait stations & monthly pen fumigation", amount: 85000, payee: "Delta Agro Chemicals", authorizedBy: "Mr. Adebayo Adeleke" },
    { id: "EXP-06", date: "2026-08-03", category: "Data, Calls & Logistics", desc: "Monthly farm internet data + staff communication allowance", amount: 45000, payee: "MTN Nigeria / Airtel", authorizedBy: "Mr. Adebayo Adeleke" },
    { id: "EXP-07", date: "2026-08-01", category: "Salaries & Payroll", desc: "Staff Monthly Net Salaries (9 Personnel)", amount: 1650000, payee: "Precisco Staff Payroll", authorizedBy: "Engr. Charles Chukwuma" }
  ],
  payroll: [
    { id: "PAY-01", name: "Mr. Adebayo Adeleke", role: "Farm Manager", basicSalary: 350000, overtime: 25000, bonus: 35000, pensionEmployer: 35000, pensionEmployee: 28000, netPay: 382000, status: "Paid" },
    { id: "PAY-02", name: "Dr. Emeka Okonkwo", role: "Veterinary Officer", basicSalary: 300000, overtime: 0, bonus: 30000, pensionEmployer: 30000, pensionEmployee: 24000, netPay: 306000, status: "Paid" },
    { id: "PAY-03", name: "Chinedu Obi", role: "Attendant (Shift 1 Lead)", basicSalary: 120000, overtime: 15000, bonus: 12000, pensionEmployer: 12000, pensionEmployee: 9600, netPay: 137400, status: "Paid" },
    { id: "PAY-04", name: "Blessing Eze", role: "Attendant (Shift 2 Lead)", basicSalary: 120000, overtime: 15000, bonus: 12000, pensionEmployer: 12000, pensionEmployee: 9600, netPay: 137400, status: "Paid" },
    { id: "PAY-05", name: "Musa Ibrahim", role: "Attendant (Shift 3 & Maint)", basicSalary: 120000, overtime: 18000, bonus: 12000, pensionEmployer: 12000, pensionEmployee: 9600, netPay: 140400, status: "Paid" },
    { id: "PAY-06", name: "Kenneth Obi", role: "Logistics Driver", basicSalary: 110000, overtime: 20000, bonus: 10000, pensionEmployer: 11000, pensionEmployee: 8800, netPay: 131200, status: "Paid" },
    { id: "PAY-07", name: "Sgt. Joshua Garba", role: "Security Officer (Day Gate 1)", basicSalary: 90000, overtime: 10000, bonus: 5000, pensionEmployer: 9000, pensionEmployee: 7200, netPay: 97800, status: "Paid" },
    { id: "PAY-08", name: "Sunday Alabi", role: "Security Officer (Day Gate 2)", basicSalary: 90000, overtime: 10000, bonus: 5000, pensionEmployer: 9000, pensionEmployee: 7200, netPay: 97800, status: "Paid" },
    { id: "PAY-09", name: "Usman Danjuma", role: "Security Officer (Night Patrol)", basicSalary: 95000, overtime: 15000, bonus: 5000, pensionEmployer: 9500, pensionEmployee: 7600, netPay: 107400, status: "Paid" }
  ],
  visitors: [
    { id: "VIS-01", date: "2026-08-18", time: "09:30 AM", name: "Engr. Patrick Agbo", org: "Delta State Ministry of Agriculture", purpose: "Biosecurity Compliance Audit", result: "Passed Grade A (Virkon-S Wheel Dip Verified)", guard: "Sgt. Joshua Garba" },
    { id: "VIS-02", date: "2026-08-17", time: "02:00 PM", name: "Gabriel Alonge (Procurement)", org: "Transcorp Hotels Ltd", purpose: "B2B Egg Inspection & Dispatch", result: "Waybill WB-104 Signed & Gate Pass Issued", guard: "Sunday Alabi" }
  ]
};

// Core Farm Store Engine
class FarmStore {
  constructor() {
    this.state = this.load();
    this.googleSheetsUrl = localStorage.getItem(GOOGLE_SHEETS_CONFIG_KEY) || "";
  }

  load() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn("Could not load from localStorage", e);
    }
    return JSON.parse(JSON.stringify(DEFAULT_STATE));
  }

  save() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.state));
    } catch (e) {
      console.warn("Could not save to localStorage", e);
    }
  }

  isAuthenticated() {
    return localStorage.getItem(AUTH_KEY) === 'true';
  }

  loginWithCode(code) {
    const cleanCode = (code || '').trim().toUpperCase();
    const userRole = ACCESS_ROLES[cleanCode] || ACCESS_ROLES["PFV-MGR-2026"];

    this.state.currentUser = userRole;
    this.save();
    localStorage.setItem(AUTH_KEY, 'true');
    return { success: true, user: userRole, redirectUrl: userRole.portalUrl };
  }

  logout() {
    localStorage.removeItem(AUTH_KEY);
    window.location.href = 'index.html';
  }

  checkAuthGuard() {
    const isLogin = window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('login.html') || window.location.pathname === '/' || window.location.pathname === '';
    if (!this.isAuthenticated() && !isLogin) {
      window.location.href = 'index.html';
    }
  }

  reset() {
    localStorage.removeItem(STORAGE_KEY);
    localStorage.removeItem(AUTH_KEY);
    this.state = JSON.parse(JSON.stringify(DEFAULT_STATE));
    this.save();
    window.location.href = 'index.html';
  }

  // Google Sheets Webhook Connector
  setGoogleSheetsUrl(url) {
    this.googleSheetsUrl = url.trim();
    localStorage.setItem(GOOGLE_SHEETS_CONFIG_KEY, this.googleSheetsUrl);
    alert("Google Sheets Webhook URL saved successfully!");
  }

  async syncToGoogleSheets(sheetName, data) {
    if (!this.googleSheetsUrl) return;

    try {
      fetch(this.googleSheetsUrl, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "append_row", sheetName: sheetName, data: data })
      });
    } catch (err) {
      console.warn("Google Sheets sync error:", err);
    }
  }

  // ==========================================
  // MATHEMATICAL CALCULATION ENGINES
  // ==========================================

  // 1. Feed Requirements Calculation (80g - 100g Benchmark)
  calculateFeedRequirements(gramsPerBird = 95) {
    const live = this.state.batch.currentBirds; // 5,892 birds
    const dailyKg = (live * gramsPerBird) / 1000;
    const weeklyKg = dailyKg * 7;
    const monthlyKg = dailyKg * 30;

    const dailyBags = (dailyKg / 25).toFixed(1);
    const weeklyBags = Math.ceil(weeklyKg / 25);
    const monthlyBags = Math.ceil(monthlyKg / 25);

    const pricePerBag = this.state.farm.feedPricePerBag || 18500;
    const dailyCost = dailyBags * pricePerBag;
    const weeklyCost = weeklyBags * pricePerBag;
    const monthlyCost = monthlyBags * pricePerBag;

    return {
      gramsPerBird,
      liveBirds: live,
      dailyKg: dailyKg.toFixed(1),
      dailyBags,
      dailyCost,
      weeklyKg: weeklyKg.toFixed(1),
      weeklyBags,
      weeklyCost,
      monthlyKg: monthlyKg.toFixed(1),
      monthlyBags,
      monthlyCost
    };
  }

  // 2. Inventory Optimization: EOQ, ROL & MOQ
  calculateInventoryOptimization() {
    const feedCalc = this.calculateFeedRequirements(95);
    const annualDemandBags = Number(feedCalc.monthlyBags) * 12; // ~8,160 bags
    const orderingCostPerOrder = 15000; // Logistics per truck order
    const holdingCostPerBagPerYear = 800; // Storage, warehouse insurance, spoilage

    // EOQ = Sqrt((2 * D * S) / H)
    const eoqBags = Math.round(Math.sqrt((2 * annualDemandBags * orderingCostPerOrder) / holdingCostPerBagPerYear)); // ~553 bags (~13.8 tonnes)

    const leadTimeDays = 2; // 2 days delivery
    const safetyBufferBags = 10;
    const reorderLevelBags = Math.ceil((Number(feedCalc.dailyBags) * leadTimeDays) + safetyBufferBags); // ~55 bags

    const moqBags = 200; // Supplier minimum order quantity (5 tonnes)

    return {
      annualDemandBags,
      eoqBags,
      reorderLevelBags,
      moqBags,
      leadTimeDays,
      currentWarehouseBags: 157,
      daysLeft: (157 / Number(feedCalc.dailyBags)).toFixed(1)
    };
  }

  // 3. Manure Waste Generation Engine (Chicken Poo Tracking)
  calculateManureGeneration() {
    const live = this.state.batch.currentBirds;
    const kgWetDroppingsPerBird = 0.132;
    const dailyWetDroppingsKg = Math.round(live * kgWetDroppingsPerBird); // ~778 kg wet poo/day
    const weeklyWetDroppingsKg = dailyWetDroppingsKg * 7;
    const dryBagConversionPerDay = Math.round(dailyWetDroppingsKg / 32); // ~24 bags/day

    const pricePerBag = this.state.farm.manurePricePerBag || 1200;
    const weeklyManureRevenuePotential = dryBagConversionPerDay * 7 * pricePerBag; // ~₦201,600/week

    return {
      dailyWetDroppingsKg,
      weeklyWetDroppingsKg,
      dryBagConversionPerDay,
      weeklyManureRevenuePotential,
      pricePerBag
    };
  }

  // 4. Water-to-Feed Intake Ratio Telemetry
  getWaterFeedRatio() {
    const feedKg = 560; // 560 kg consumed
    const waterLiters = 1180; // 1,180 Liters consumed
    const ratio = (waterLiters / feedKg).toFixed(2); // ~2.11 : 1
    const status = (ratio >= 1.8 && ratio <= 2.3) ? "Normal Optimal" : (ratio > 2.3) ? "High (Heat / Leak Warning)" : "Low (Dehydration Warning)";
    return { feedKg, waterLiters, ratio: `${ratio} : 1`, status };
  }

  // 5. Spent Hen (Old Layer) Meat Salvage Valuation Forecaster
  calculateSpentHenSalvage() {
    const live = this.state.batch.currentBirds;
    const pricePerHen = this.state.farm.spentHenPrice || 3200;
    const totalSalvageValue = live * pricePerHen; // ~₦18.85M
    return { liveHens: live, pricePerHen, totalSalvageValue };
  }

  // 6. Generate 1-Click WhatsApp Executive Briefing
  generateWhatsAppBriefing() {
    const aggs = this.getAggregates();
    const water = this.getWaterFeedRatio();

    const text = `🌿 *PRECISCO FARM VENTURES LTD. — DAILY BRIEFING*
📅 *Date:* 19 Aug 2026 | *Flock:* PFV-LAY-001 (34 Wks Peak)
━━━━━━━━━━━━━━━━━━━
🐔 *Live Birds:* ${aggs.liveBirds.toLocaleString()} (98.2% Livability)
🥚 *Harvest Today:* ${aggs.totalHarvestToday.toLocaleString()} Eggs (${aggs.totalTraysToday} Crates)
   • Large (53-63g): 101.0 Crates (₦4,500/cr)
   • Medium (45-52g): 61.0 Crates (₦4,300/cr)
   • Small/Cracked: 10.4 Crates
📈 *Hen-Day Laying:* ${aggs.henDayPct}% (Target: 88.5%)
🌾 *Feed Consumed:* ${aggs.consumedKg} kg (${aggs.actualGrams}g/bird)
💧 *Water-to-Feed:* ${water.waterLiters}L (${water.ratio}) - ${water.status}
📦 *Warehouse Buffer:* ${aggs.feedBagsInStock} Bags (${aggs.daysOfFeedRemaining} Days Left)
💩 *Manure Harvested:* ${aggs.dryBagsManurePerDay} Bags (₦${(aggs.dryBagsManurePerDay * 1200).toLocaleString()})
💰 *B2B Revenue:* ₦${aggs.totalGrossRevenue.toLocaleString()}
━━━━━━━━━━━━━━━━━━━
🛡️ *Biosecurity:* Level A Passed | Asaba Temp: 29.6°C Normal`;

    navigator.clipboard.writeText(text).then(() => {
      alert("✅ WhatsApp Executive Briefing copied to clipboard! Ready to paste to Mr. Tony on WhatsApp.");
    }).catch(() => {
      prompt("Copy your WhatsApp Daily Briefing below:", text);
    });
  }

  // Aggregate Calculations
  getAggregates() {
    const liveBirds = this.state.batch.currentBirds;
    const todayEggs = this.state.eggs.filter(e => e.date === "2026-08-19");
    const totalHarvestToday = todayEggs.reduce((s, e) => s + e.total, 0);
    const goodEggsToday = todayEggs.reduce((s, e) => s + e.totalGood, 0);
    const totalTraysToday = Math.floor(totalHarvestToday / 30);
    const henDayPct = liveBirds > 0 ? ((totalHarvestToday / liveBirds) * 100).toFixed(1) : "0.0";
    
    const todayMort = this.state.mortality.filter(m => m.date === "2026-08-19").reduce((s, m) => s + m.count, 0);
    const todayFeed = this.state.feed[0] || { consumedKg: 560, actualGrams: 95.04 };
    const feedStockItem = this.state.inventoryItems.find(i => i.id === "INV-FD-01") || { inStock: 157, daysLeft: 7.0 };

    const totalEggRevenue = this.state.sales.reduce((s, o) => s + o.total, 0);
    const totalManureRevenue = this.state.manureSales.reduce((s, m) => s + m.total, 0);
    const totalGrossRevenue = totalEggRevenue + totalManureRevenue;
    
    const totalCashCollected = this.state.sales.reduce((s, o) => s + o.paid, 0) + totalManureRevenue;
    const totalReceivables = this.state.sales.reduce((s, o) => s + o.balance, 0);
    
    const totalOperatingExpenses = this.state.expenses.reduce((s, e) => s + e.amount, 0);
    const totalPayroll = this.state.payroll.reduce((s, p) => s + p.netPay, 0);
    const netProfit = totalGrossRevenue - totalOperatingExpenses;
    const grossMarginPct = totalGrossRevenue > 0 ? (((totalGrossRevenue - (totalOperatingExpenses * 0.65)) / totalGrossRevenue) * 100).toFixed(1) : "42.5";

    const feedOpt = this.calculateInventoryOptimization();
    const manureOpt = this.calculateManureGeneration();

    return {
      liveBirds,
      totalHarvestToday,
      goodEggsToday,
      totalTraysToday,
      henDayPct,
      todayMort,
      consumedKg: todayFeed.consumedKg,
      actualGrams: todayFeed.actualGrams,
      feedBagsInStock: feedStockItem.inStock,
      daysOfFeedRemaining: feedOpt.daysLeft,
      reorderLevelBags: feedOpt.reorderLevelBags,
      eoqBags: feedOpt.eoqBags,
      moqBags: feedOpt.moqBags,
      dailyManureKg: manureOpt.dailyWetDroppingsKg,
      dryBagsManurePerDay: manureOpt.dryBagConversionPerDay,
      totalEggRevenue,
      totalManureRevenue,
      totalGrossRevenue,
      totalCashCollected,
      totalReceivables,
      totalOperatingExpenses,
      totalPayroll,
      netProfit,
      grossMarginPct
    };
  }

  // Mutations
  addEggHarvest(data) {
    const large = Number(data.large || 0);
    const medium = Number(data.medium || 0);
    const small = Number(data.small || 0);
    const cracked = Number(data.cracked || 0);
    const broken = Number(data.broken || 0);
    const reject = Number(data.reject || 0);

    const totalGood = large + medium + small;
    const total = totalGood + cracked + broken + reject;
    const live = this.state.batch.currentBirds;
    const henDay = live > 0 ? ((total / live) * 100).toFixed(1) : 0;
    const trays = (total / 30).toFixed(1);

    const newRecord = {
      id: "EGG-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      time: data.time || "08:30 AM",
      round: data.round || "Morning Harvest (Round 1)",
      large: large,
      medium: medium,
      small: small,
      cracked: cracked,
      broken: broken,
      reject: reject,
      totalGood: totalGood,
      total: total,
      trays: Number(trays),
      henDay: Number(henDay),
      staff: data.staff || this.state.currentUser.name
    };

    this.state.eggs.unshift(newRecord);
    this.state.batch.cumulativeEggs += total;

    const largeCrates = Math.floor(large / 30);
    const medCrates = Math.floor(medium / 30);
    const smallCrates = Math.floor(small / 30);
    const crackedCrates = Math.floor(cracked / 30);

    const itemL = this.state.inventoryItems.find(i => i.id === "INV-EG-01");
    if (itemL) itemL.inStock += largeCrates;
    const itemM = this.state.inventoryItems.find(i => i.id === "INV-EG-02");
    if (itemM) itemM.inStock += medCrates;
    const itemS = this.state.inventoryItems.find(i => i.id === "INV-EG-03");
    if (itemS) itemS.inStock += smallCrates;
    const itemC = this.state.inventoryItems.find(i => i.id === "INV-EG-04");
    if (itemC) itemC.inStock += crackedCrates;

    this.save();
    this.syncToGoogleSheets("Egg_Harvest_Log", newRecord);
  }

  addMortality(data) {
    const count = Number(data.count || 1);
    const newRecord = {
      id: "MORT-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      time: data.time || "07:15 AM",
      count: count,
      reason: data.reason || "Natural cage fatigue",
      action: data.action || "Incinerated on-farm per SOP-BIO-004",
      staff: data.staff || this.state.currentUser.name,
      status: count > 6 ? "Flagged for Vet Necropsy" : "Verified by Manager"
    };

    this.state.mortality.unshift(newRecord);
    this.state.batch.currentBirds = Math.max(0, this.state.batch.currentBirds - count);
    this.state.batch.totalMortality += count;
    
    this.save();
    this.syncToGoogleSheets("Mortality_Records", newRecord);
  }

  addCorporateOrder(data) {
    const cratesLarge = Number(data.cratesLarge || 0);
    const cratesMed = Number(data.cratesMed || 0);
    const cratesTotal = cratesLarge + cratesMed + Number(data.crates || 0);
    
    const priceLarge = 4500;
    const priceMed = 4300;
    const total = (cratesLarge * priceLarge) + (cratesMed * priceMed) || (cratesTotal * (Number(data.unitPrice) || 4300));
    
    const paid = Number(data.paid || 0);
    const balance = Math.max(0, total - paid);

    const newOrder = {
      id: "ORD-" + Date.now().toString().slice(-4),
      waybill: "WB-PFV-2026-" + Date.now().toString().slice(-3),
      date: data.date || "2026-08-19",
      customer: data.customer || "Corporate Client",
      address: data.address || "Asaba, Delta State",
      contact: data.contact || "Procurement Manager",
      cratesLarge: cratesLarge,
      cratesMed: cratesMed,
      cratesTotal: cratesTotal,
      unitPrice: Math.round(total / (cratesTotal || 1)),
      total: total,
      paid: paid,
      balance: balance,
      status: balance === 0 ? "Paid in Full" : "Outstanding (14-Day Term)",
      agingBracket: "0-7 Days",
      driver: "Kenneth Obi",
      vehicle: data.vehicle || "Toyota Dyna (DLT-892-XA)",
      gatePass: "PASS-" + Date.now().toString().slice(-4)
    };

    this.state.sales.unshift(newOrder);

    const itemL = this.state.inventoryItems.find(i => i.id === "INV-EG-01");
    if (itemL) itemL.inStock = Math.max(0, itemL.inStock - cratesLarge);
    const itemM = this.state.inventoryItems.find(i => i.id === "INV-EG-02");
    if (itemM) itemM.inStock = Math.max(0, itemM.inStock - cratesMed);

    this.save();
    this.syncToGoogleSheets("Corporate_Sales_Orders", newOrder);
  }

  addManureLog(data) {
    const bags = Number(data.bags || 24);
    const newLog = {
      id: "MNR-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      wetWeightKg: Math.round(this.state.batch.currentBirds * 0.132),
      bagsHarvested: bags,
      moistureStatus: data.moisture || "Conveyor Belt Dry",
      storedBagsTotal: 240 + bags,
      disposalAction: "Bagged in 50kg sacks for cassava/yam farmers",
      staff: this.state.currentUser.name
    };

    this.state.manureLogs.unshift(newLog);
    const manureStock = this.state.inventoryItems.find(i => i.id === "INV-MN-01");
    if (manureStock) manureStock.inStock += bags;

    this.save();
    this.syncToGoogleSheets("Manure_Organic_Waste", newLog);
  }

  addExpense(data) {
    const newExp = {
      id: "EXP-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      category: data.category || "Feed Purchases",
      desc: data.desc || "Farm operating expense",
      amount: Number(data.amount || 0),
      payee: data.payee || "Vendor",
      authorizedBy: this.state.currentUser.name
    };

    this.state.expenses.unshift(newExp);
    this.save();
    this.syncToGoogleSheets("Farm_Expenses_PL", newExp);
  }

  setCurrentUser(staffId) {
    const roleKey = Object.keys(ACCESS_ROLES).find(k => ACCESS_ROLES[k].id === staffId);
    if (roleKey) {
      this.state.currentUser = ACCESS_ROLES[roleKey];
      this.save();
      window.location.href = ACCESS_ROLES[roleKey].portalUrl;
    }
  }

  triggerVetEmergency() {
    alert("EMERGENCY ALERT SENT TO VET (Dr. Emeka): Urgent inspection requested for Pen 1!");
  }

  exportMasterExcel() {
    const aggs = this.getAggregates();
    const exportData = [
      ["=== PRECISCO FARM VENTURES LTD. MASTER ENTERPRISE SPREADSHEET ==="],
      ["Exported Date:", new Date().toLocaleString()],
      ["Flock Designation:", this.state.batch.name],
      ["Current Live Birds:", aggs.liveBirds],
      ["Today's Egg Harvest:", aggs.totalHarvestToday + " Eggs (" + aggs.totalTraysToday + " Crates)"],
      ["Hen-Day Laying Rate:", aggs.henDayPct + "%"],
      ["Days of Feed Buffer:", aggs.daysOfFeedRemaining + " Days (157 Bags)"],
      ["Total B2B Revenue:", "NGN " + aggs.totalGrossRevenue.toLocaleString()],
      ["Net Operating Profit:", "NGN " + aggs.netProfit.toLocaleString()],
      [],
      ["--- 1. EGG HARVEST & SIZE DERIVATIVES ---"],
      ["Log ID", "Date", "Round", "Large (53-63g+)", "Medium (45-52g)", "Small (<45g)", "Cracked", "Broken", "Rejects", "Total Eggs", "Trays", "Hen-Day %", "Staff"],
      ...this.state.eggs.map(e => [e.id, e.date, e.round, e.large, e.medium, e.small, e.cracked, e.broken, e.reject, e.total, e.trays, e.henDay + "%", e.staff]),
      [],
      ["--- 2. B2B CORPORATE SALES & WAYBILLS ---"],
      ["Order ID", "Waybill #", "Date", "Corporate Client", "Large Crates", "Medium Crates", "Total Crates", "Total (NGN)", "Paid (NGN)", "Balance (NGN)", "Status", "Driver"],
      ...this.state.sales.map(s => [s.id, s.waybill, s.date, s.customer, s.cratesLarge, s.cratesMed, s.cratesTotal, s.total, s.paid, s.balance, s.status, s.driver]),
      [],
      ["--- 3. DAILY MORTALITY RECORDS ---"],
      ["Mortality ID", "Date", "Time", "Count", "Reason", "Action Taken", "Reported By", "Status"],
      ...this.state.mortality.map(m => [m.id, m.date, m.time, m.count, m.reason, m.action, m.staff, m.status]),
      [],
      ["--- 4. ORGANIC POULTRY MANURE SALES ---"],
      ["Sale ID", "Date", "Buyer / Plantation", "50kg Bags", "Rate (NGN)", "Total (NGN)", "Status"],
      ...this.state.manureSales.map(mn => [mn.id, mn.date, mn.buyer, mn.bags, mn.unitPrice, mn.total, mn.status])
    ];

    exportTableToCSV("Precisco_Master_Farm_Database.csv", exportData);
  }
}

// Global Store Instance
const farmStore = new FarmStore();

// Modal Functions
function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('open');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('open');
}

window.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-backdrop')) {
    e.target.classList.remove('open');
  }
});

function exportTableToCSV(filename, rows) {
  const processRow = (row) => row.map(val => `"${String(val).replace(/"/g, '""')}"`).join(',');
  const csvContent = "data:text/csv;charset=utf-8," + rows.map(processRow).join("\n");
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", filename);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
