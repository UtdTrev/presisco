/**
 * PRECISCO FARM VENTURES LTD. — CORE APPLICATION CONTROLLER
 * Self-Contained Native JS State Store, Calculators, Modals & RBAC
 */

const STORAGE_KEY = 'precisco_farm_state_v1';

// Baseline State (Precisco 6,000 POL Layers)
const DEFAULT_STATE = {
  currentUser: { id: "STF-MGR", name: "Mr. Adebayo Adeleke", role: "Farm Manager", roleKey: "manager" },
  farm: {
    name: "Precisco Farm Ventures Ltd.",
    location: "Km 12, Asaba-Benin Expressway, Asaba, Delta State",
    capacity: 6000,
    pricePerTray: 4300,
    feedPricePerBag: 18500
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
    type: "Automated 3-Tier Battery Cage",
    currentTemp: 29.6,
    humidity: 72,
    fansActive: 7,
    fanCount: 8,
    waterPressure: 2.2,
    waterStatus: "Normal Pressure (2.2 Bar) • Automated Header Tank Active",
    lighting: "05:30 - 21:30 (16-Hour Photoperiod Active)"
  },
  eggs: [
    { id: "EGG-01", date: "2026-08-19", time: "08:30 AM", round: "Morning Harvest (Round 1)", good: 3120, cracked: 22, broken: 8, reject: 14, total: 3164, trays: 105.4, henDay: 53.7, staff: "Chinedu Obi" },
    { id: "EGG-02", date: "2026-08-19", time: "02:30 PM", round: "Afternoon Harvest (Round 2)", good: 1980, cracked: 15, broken: 4, reject: 9, total: 2008, trays: 66.9, henDay: 87.8, staff: "Blessing Eze" }
  ],
  mortality: [
    { id: "MORT-01", date: "2026-08-19", time: "07:15 AM", count: 3, reason: "Egg peritonitis / cage fatigue", action: "Incinerated per SOP-BIO-004", staff: "Chinedu Obi", status: "Verified by Manager" },
    { id: "MORT-02", date: "2026-08-18", time: "07:20 AM", count: 2, reason: "Vent pecking trauma", action: "Incinerated per SOP-BIO-004", staff: "Blessing Eze", status: "Verified by Manager" }
  ],
  sickBirds: [
    { id: "SCK-01", date: "2026-08-19", tag: "Cage Tier 2-A4", symptoms: "Dullness, pale comb, lethargy", diagnosis: "Early respiratory fatigue", isolation: "Sick Bay Pen S-1", treatment: "Oral Multivitamins + Electrolytes", status: "Active Isolation", staff: "Chinedu Obi" }
  ],
  feed: [
    { id: "FEED-01", date: "2026-08-19", type: "Layers Mash Phase 1", issuedKg: 700, remainingKg: 15, consumedKg: 685, live: 5892, gramsPerBird: 116.3, status: "Optimal Range", staff: "Adebayo Adeleke" }
  ],
  sales: [
    { id: "ORD-01", waybill: "WB-PFV-2026-104", date: "2026-08-18", customer: "Transcorp Hotels & Suites Ltd", crates: 120, unitPrice: 4300, total: 516000, paid: 0, balance: 516000, status: "Outstanding (14-Day Term)", vehicle: "Toyota Dyna (DLT-892-XA)" },
    { id: "ORD-02", waybill: "WB-PFV-2026-103", date: "2026-08-17", customer: "Grand Delta Supermarkets Ltd", crates: 200, unitPrice: 4250, total: 850000, paid: 850000, balance: 0, status: "Paid in Full", vehicle: "Isuzu Truck (ASB-441-XX)" },
    { id: "ORD-03", waybill: "WB-PFV-2026-102", date: "2026-08-15", customer: "Royal Crown Confectioneries", crates: 150, unitPrice: 4200, total: 630000, paid: 630000, balance: 0, status: "Paid in Full", vehicle: "Ford Transit (BEN-119-AA)" }
  ],
  expenses: [
    { id: "EXP-01", date: "2026-08-15", category: "Feed Purchases", desc: "Purchase of 200 bags Layers Mash Phase 1 (Vital Feeds)", amount: 3700000, payee: "Vital Feeds Ltd" },
    { id: "EXP-02", date: "2026-08-12", category: "Veterinary Supplies", desc: "Lasota ND vaccines + Electrolyte packs", amount: 145000, payee: "NVRI Vom / Vet Planet" },
    { id: "EXP-03", date: "2026-08-10", category: "Utilities & Generator", desc: "1,000L Diesel fuel for farm backup generator", amount: 1250000, payee: "Rainoil Depot Asaba" },
    { id: "EXP-04", date: "2026-08-01", category: "Salaries & Payroll", desc: "Monthly Farm Staff Payroll (7 Staff)", amount: 1650000, payee: "Precisco Staff Payroll" }
  ],
  inventory: [
    { id: "INV-FD-01", category: "Feed", name: "Layers Mash Phase 1 (25kg)", inStock: 157, min: 45, unit: "Bags", cost: 18500 },
    { id: "INV-EG-01", category: "Eggs", name: "Grade A Marketable Stored Crates", inStock: 485, min: 100, unit: "Crates (30-Egg)", cost: 4300 },
    { id: "INV-VT-01", category: "Veterinary", name: "Lasota ND Vaccine (1000 doses)", inStock: 12, min: 6, unit: "Vials", cost: 3500 },
    { id: "INV-SP-01", category: "Packaging", name: "30-Egg Pulp Trays (100-pack)", inStock: 120, min: 40, unit: "Bundles", cost: 9500 }
  ],
  visitors: [
    { id: "VIS-01", date: "2026-08-18", name: "Engr. Patrick Agbo", org: "Delta State Ministry of Agriculture", purpose: "Biosecurity Compliance Audit", result: "Passed Grade A", guard: "Sgt. Joshua Garba" },
    { id: "VIS-02", date: "2026-08-17", name: "Gabriel Alonge (Procurement)", org: "Transcorp Hotels Ltd", purpose: "B2B Egg Inspection & Dispatch", result: "Waybill WB-104 Signed", guard: "Sunday Alabi" }
  ],
  staff: [
    { id: "STF-DIR", name: "Engr. Charles Chukwuma", role: "Director / Owner", roleKey: "director" },
    { id: "STF-MGR", name: "Mr. Adebayo Adeleke", role: "Farm Manager", roleKey: "manager" },
    { id: "STF-VET", name: "Dr. Emeka Okonkwo, DVM", role: "Veterinary Officer", roleKey: "veterinarian" },
    { id: "STF-CON", name: "Dr. (Mrs.) Ifeoma Nnamdi", role: "Poultry Consultant", roleKey: "consultant" },
    { id: "STF-AT1", name: "Chinedu Obi", role: "Poultry Attendant (Shift 1)", roleKey: "attendant" },
    { id: "STF-AT2", name: "Blessing Eze", role: "Poultry Attendant (Shift 2)", roleKey: "attendant" },
    { id: "STF-AT3", name: "Musa Ibrahim", role: "Poultry Attendant (Shift 3)", roleKey: "attendant" },
    { id: "STF-SEC1", name: "Sgt. Joshua Garba", role: "Security Officer (Gate 1)", roleKey: "security" },
    { id: "STF-SEC2", name: "Sunday Alabi", role: "Security Officer (Gate 2)", roleKey: "security" }
  ]
};

// State Manager
class FarmStore {
  constructor() {
    this.state = this.load();
  }

  load() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn("Could not load from localStorage, using default", e);
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

  reset() {
    localStorage.removeItem(STORAGE_KEY);
    this.state = JSON.parse(JSON.stringify(DEFAULT_STATE));
    this.save();
    window.location.reload();
  }

  // Aggregate Calculations
  getAggregates() {
    const liveBirds = this.state.batch.currentBirds;
    const todayEggs = this.state.eggs.filter(e => e.date === "2026-08-19");
    const totalHarvestToday = todayEggs.reduce((s, e) => s + e.total, 0);
    const goodEggsToday = todayEggs.reduce((s, e) => s + e.good, 0);
    const totalTraysToday = Math.floor(totalHarvestToday / 30);
    const henDayPct = liveBirds > 0 ? ((totalHarvestToday / liveBirds) * 100).toFixed(1) : "0.0";
    
    const todayMort = this.state.mortality.filter(m => m.date === "2026-08-19").reduce((s, m) => s + m.count, 0);
    
    const todayFeed = this.state.feed.find(f => f.date === "2026-08-19") || { consumedKg: 685, gramsPerBird: 116.3 };
    const feedStockItem = this.state.inventory.find(i => i.id === "INV-FD-01") || { inStock: 157 };
    const dailyBagsUsed = (todayFeed.consumedKg / 25) || 27.5;
    const daysOfFeedRemaining = Math.floor(feedStockItem.inStock / dailyBagsUsed);

    const totalB2BRevenue = this.state.sales.reduce((s, o) => s + o.total, 0);
    const totalCashCollected = this.state.sales.reduce((s, o) => s + o.paid, 0);
    const totalReceivables = this.state.sales.reduce((s, o) => s + o.balance, 0);
    const totalExpenses = this.state.expenses.reduce((s, e) => s + e.amount, 0);
    const netProfit = totalB2BRevenue - totalExpenses;

    return {
      liveBirds,
      totalHarvestToday,
      goodEggsToday,
      totalTraysToday,
      henDayPct,
      todayMort,
      consumedKg: todayFeed.consumedKg,
      gramsPerBird: todayFeed.gramsPerBird,
      feedBagsInStock: feedStockItem.inStock,
      daysOfFeedRemaining,
      totalB2BRevenue,
      totalCashCollected,
      totalReceivables,
      totalExpenses,
      netProfit
    };
  }

  // Mutations
  addEggHarvest(data) {
    const total = Number(data.good || 0) + Number(data.cracked || 0) + Number(data.broken || 0) + Number(data.reject || 0);
    const live = this.state.batch.currentBirds;
    const henDay = live > 0 ? ((total / live) * 100).toFixed(1) : 0;
    const trays = (total / 30).toFixed(1);

    const newRecord = {
      id: "EGG-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      time: data.time || "08:30 AM",
      round: data.round || "Morning Harvest (Round 1)",
      good: Number(data.good || 0),
      cracked: Number(data.cracked || 0),
      broken: Number(data.broken || 0),
      reject: Number(data.reject || 0),
      total: total,
      trays: Number(trays),
      henDay: Number(henDay),
      staff: data.staff || this.state.currentUser.name
    };

    this.state.eggs.unshift(newRecord);
    this.state.batch.cumulativeEggs += total;

    // Update stored crates
    const goodCrates = Math.floor(newRecord.good / 30);
    const eggStock = this.state.inventory.find(i => i.id === "INV-EG-01");
    if (eggStock) eggStock.inStock += goodCrates;

    this.save();
  }

  addMortality(data) {
    const count = Number(data.count || 1);
    const newRecord = {
      id: "MORT-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      time: data.time || "07:15 AM",
      count: count,
      reason: data.reason || "Natural cage fatigue",
      action: data.action || "Incinerated per SOP-BIO-004",
      staff: data.staff || this.state.currentUser.name,
      status: count > 6 ? "Flagged for Vet Necropsy" : "Verified by Manager"
    };

    this.state.mortality.unshift(newRecord);
    this.state.batch.currentBirds = Math.max(0, this.state.batch.currentBirds - count);
    this.state.batch.totalMortality += count;
    this.save();
  }

  addCorporateOrder(data) {
    const crates = Number(data.crates || 100);
    const price = Number(data.unitPrice || 4300);
    const total = crates * price;
    const paid = Number(data.paid || 0);
    const balance = Math.max(0, total - paid);

    const newOrder = {
      id: "ORD-" + Date.now().toString().slice(-4),
      waybill: "WB-PFV-2026-" + Date.now().toString().slice(-3),
      date: data.date || "2026-08-19",
      customer: data.customer || "Corporate Client",
      crates: crates,
      unitPrice: price,
      total: total,
      paid: paid,
      balance: balance,
      status: balance === 0 ? "Paid in Full" : "Outstanding (14-Day Term)",
      vehicle: data.vehicle || "Corporate Delivery Van"
    };

    this.state.sales.unshift(newOrder);

    // Deduct crates
    const eggStock = this.state.inventory.find(i => i.id === "INV-EG-01");
    if (eggStock) eggStock.inStock = Math.max(0, eggStock.inStock - crates);

    this.save();
  }

  addExpense(data) {
    const newExp = {
      id: "EXP-" + Date.now().toString().slice(-4),
      date: data.date || "2026-08-19",
      category: data.category || "Feed Purchases",
      desc: data.desc || "Farm operating expense",
      amount: Number(data.amount || 0),
      payee: data.payee || "Vendor"
    };

    this.state.expenses.unshift(newExp);
    this.save();
  }

  setCurrentUser(staffId) {
    const stf = this.state.staff.find(s => s.id === staffId);
    if (stf) {
      this.state.currentUser = stf;
      this.save();
      window.location.reload();
    }
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

// Close on backdrop click
window.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-backdrop')) {
    e.target.classList.remove('open');
  }
});

// CSV Exporter Helper
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
