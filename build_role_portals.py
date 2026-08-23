import os

base_dir = "/home/user/precisco-portal"

def get_role_nav(user_role_name, user_email, user_avatar):
    return f"""
    <header class="top-navbar">
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="mobile-menu-btn" onclick="openMobileDrawer();" title="Open Mobile Navigation">
          ☰
        </button>
        <a href="dashboard.html" style="display:flex; align-items:center; gap:8px; text-decoration:none;">
          <div style="width:34px; height:34px; border-radius:10px; background:#e6f4ea; border:2px solid #124e3f; display:flex; align-items:center; justify-content:center; color:#124e3f; font-size:1.1rem; font-weight:800;">🌿</div>
          <span style="font-size:1.1rem; font-weight:800; color:#111827; letter-spacing:-0.03em;">Precisco</span>
        </a>
      </div>

      <div class="top-navbar-right">
        <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:4px 10px; border-radius:9999px; font-size:0.72rem; font-family:ui-monospace, monospace;" class="font-mono">
          <span style="color:#d97706; font-weight:700;">☀️ 29.6°C</span>
          <span style="color:#94a3b8; margin:0 2px;">|</span>
          <span style="color:#15803d; font-weight:700;">Fans 7/8</span>
        </div>

        <div class="user-profile-widget" onclick="openMobileDrawer();" title="Click to view staff details">
          <div class="avatar-circle">{user_avatar}</div>
          <div class="user-info">
            <span class="user-name">{user_role_name}</span>
            <span class="user-email">{user_email}</span>
          </div>
        </div>

        <button onclick="farmStore.logout();" class="btn-outline-pill" style="padding:5px 10px; font-size:0.72rem; color:#e11d48; border-color:#fecaca;" title="Sign out of portal">
          <span>Sign Out</span>
        </button>
      </div>
    </header>

    <!-- Slide-Out Mobile Navigation Drawer -->
    <div id="mobileNavDrawer" class="mobile-nav-drawer" onclick="if(event.target === this) closeMobileDrawer();">
      <div class="mobile-nav-content">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:12px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.3rem;">🌿</span>
            <strong style="font-size:1.05rem; color:var(--forest-dark);">Precisco Farms</strong>
          </div>
          <button onclick="closeMobileDrawer();" style="font-size:1.4rem; color:#94a3b8;">&times;</button>
        </div>

        <div style="background:#f8fafc; padding:10px; border-radius:12px; border:1px solid #e2e8f0;">
          <span style="font-size:0.65rem; color:#64748b; font-weight:700; display:block; margin-bottom:4px;">SWITCH PORTAL VIEW:</span>
          <select id="mobileRoleSelect" onchange="farmStore.setCurrentUser(this.value);" style="font-size:0.8rem; padding:6px 10px;">
            <option value="STF-DIR">Engr. Charles (Director / Owner)</option>
            <option value="STF-MGR">Mr. Adebayo (Farm Manager)</option>
            <option value="STF-VET">Dr. Emeka (Veterinary Officer)</option>
            <option value="STF-CON">Dr. Ifeoma (Consultant)</option>
            <option value="STF-AT1">Chinedu Obi (Attendant Shift 1)</option>
            <option value="STF-SEC1">Sgt. Joshua (Security Officer)</option>
            <option value="STF-DRV">Kenneth Obi (Logistics Driver)</option>
          </select>
        </div>

        <div style="display:flex; flex-direction:column; gap:4px; font-size:0.88rem; font-weight:600;">
          <a href="dashboard.html" class="sidebar-nav-item">📊 Dashboard</a>
          <a href="director.html" class="sidebar-nav-item">👑 Director Portal</a>
          <a href="manager.html" class="sidebar-nav-item">👔 Manager Portal</a>
          <a href="vet.html" class="sidebar-nav-item">🩺 Vet Officer Portal</a>
          <a href="attendant.html" class="sidebar-nav-item">🐔 Attendant Portal</a>
          <a href="security.html" class="sidebar-nav-item">🛡️ Security Gate Portal</a>
          <a href="driver.html" class="sidebar-nav-item">🚚 Delivery Driver Hub</a>
          <a href="consultant.html" class="sidebar-nav-item">📊 Consultant Portal</a>
          <a href="sales.html" class="sidebar-nav-item">💼 B2B Sales & Waybills</a>
          <a href="operations.html" class="sidebar-nav-item">📋 Shift Checklists</a>
          <a href="eggs.html" class="sidebar-nav-item">🥚 Twice-Daily Harvest</a>
          <a href="pages.html" class="sidebar-nav-item" style="color:var(--forest-dark); font-weight:800;">✦ All 16 Pages Sitemap</a>
        </div>

        <div style="margin-top:auto; padding-top:12px; border-top:1px solid #edf2f7;">
          <button onclick="farmStore.logout();" class="btn-forest" style="width:100%; background:#ef4444; justify-content:center;">
            Sign Out of Portal
          </button>
        </div>
      </div>
    </div>
    """

def wrap_portal_page(title, role_name, email, avatar, content):
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Precisco Farm Ventures — {title}</title>
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <div class="dashboard-wrapper">
      <div class="main-panel">
        {get_role_nav(role_name, email, avatar)}
        <div class="page-content-wrapper">
          {content}
        </div>
      </div>
    </div>

    <!-- Reusable Modals & Scripts -->
    <div id="modalEggHarvest" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title">🥚 Log Harvest (Size Derivatives)</h3>
          <button class="modal-close-btn" onclick="closeModal('modalEggHarvest')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addEggHarvest({{
          round: this.round.value,
          large: this.large.value,
          medium: this.medium.value,
          small: this.small.value,
          cracked: this.cracked.value,
          broken: this.broken.value,
          reject: this.reject.value
        }}); closeModal('modalEggHarvest'); window.location.reload();">
          <div class="modal-body">
            <div class="form-group">
              <label class="form-label">Harvest Collection Round</label>
              <select name="round">
                <option value="Morning Harvest (Round 1)">Morning Harvest (Round 1 - 08:30 AM)</option>
                <option value="Afternoon Harvest (Round 2)">Afternoon Harvest (Round 2 - 02:30 PM)</option>
              </select>
            </div>
            
            <span style="font-size:0.75rem; font-weight:700; color:var(--forest-dark); text-transform:uppercase;">1. Grade A Good Eggs</span>
            <div class="form-row-3">
              <div class="form-group">
                <label class="form-label" style="color:var(--forest-dark);">Large (53-63g+)</label>
                <input type="number" name="large" placeholder="1850" required>
              </div>
              <div class="form-group">
                <label class="form-label" style="color:var(--forest-dark);">Medium (45-52g)</label>
                <input type="number" name="medium" placeholder="1120" required>
              </div>
              <div class="form-group">
                <label class="form-label" style="color:var(--forest-dark);">Small (&lt;45g)</label>
                <input type="number" name="small" placeholder="150" value="0">
              </div>
            </div>

            <span style="font-size:0.75rem; font-weight:700; color:var(--amber-dark); text-transform:uppercase; margin-top:6px;">2. Damaged & Defects</span>
            <div class="form-row-3">
              <div class="form-group">
                <label class="form-label" style="color:var(--amber-dark);">Cracked</label>
                <input type="number" name="cracked" placeholder="22" value="0">
              </div>
              <div class="form-group">
                <label class="form-label" style="color:var(--rose-dark);">Broken</label>
                <input type="number" name="broken" placeholder="8" value="0">
              </div>
              <div class="form-group">
                <label class="form-label">Dirty</label>
                <input type="number" name="reject" placeholder="14" value="0">
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn-outline-pill" onclick="closeModal('modalEggHarvest')">Cancel</button>
            <button type="submit" class="btn-forest">Save Harvest</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal: Record Mortality -->
    <div id="modalMortality" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title" style="color:var(--rose-dark);">☠️ Record Daily Mortality</h3>
          <button class="modal-close-btn" onclick="closeModal('modalMortality')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addMortality({{
          count: this.count.value,
          reason: this.reason.value
        }}); closeModal('modalMortality'); window.location.reload();">
          <div class="modal-body">
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">Dead Birds Count</label>
                <input type="number" name="count" min="1" placeholder="e.g. 2" required>
              </div>
              <div class="form-group">
                <label class="form-label">Suspected Cause</label>
                <select name="reason">
                  <option value="Natural cage fatigue">Natural cage fatigue</option>
                  <option value="Egg peritonitis">Egg peritonitis</option>
                  <option value="Vent pecking trauma">Vent pecking trauma</option>
                  <option value="Asaba heat exhaustion">Asaba heat exhaustion</option>
                </select>
              </div>
            </div>
            <div style="background:#fee2e2; padding:10px; border-radius:10px; font-size:0.72rem; color:#991b1b;">
              <strong>SOP-BIO-004:</strong> Carcasses must be bagged immediately and incinerated on-farm.
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn-outline-pill" onclick="closeModal('modalMortality')">Cancel</button>
            <button type="submit" class="btn-forest" style="background:var(--rose-dark);">Confirm</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal: Corporate Sales Order -->
    <div id="modalSalesOrder" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title">💼 Create Corporate B2B Order</h3>
          <button class="modal-close-btn" onclick="closeModal('modalSalesOrder')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addCorporateOrder({{
          customer: this.customer.value,
          cratesLarge: this.cratesLarge.value,
          cratesMed: this.cratesMed.value,
          paid: this.paid.value,
          vehicle: this.vehicle.value
        }}); closeModal('modalSalesOrder'); window.location.reload();">
          <div class="modal-body">
            <div class="form-group">
              <label class="form-label">Corporate Client</label>
              <select name="customer">
                <option value="Transcorp Hotels & Suites Ltd">Transcorp Hotels & Suites Ltd (Large @ ₦4,500)</option>
                <option value="Grand Delta Supermarkets Ltd">Grand Delta Supermarkets Ltd (Medium @ ₦4,300)</option>
                <option value="Royal Crown Confectioneries">Royal Crown Confectioneries (Mixed @ ₦4,200)</option>
              </select>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">Large Crates (53-63g+)</label>
                <input type="number" name="cratesLarge" value="80">
              </div>
              <div class="form-group">
                <label class="form-label">Medium Crates (45-52g)</label>
                <input type="number" name="cratesMed" value="40">
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">Immediate Payment (₦)</label>
                <input type="number" name="paid" value="0" placeholder="0 if 14-day invoice">
              </div>
              <div class="form-group">
                <label class="form-label">Delivery Vehicle Reg #</label>
                <input type="text" name="vehicle" value="Toyota Dyna (DLT-892-XA)" required>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn-outline-pill" onclick="closeModal('modalSalesOrder')">Cancel</button>
            <button type="submit" class="btn-forest">Issue Waybill</button>
          </div>
        </form>
      </div>
    </div>

    <script src="js/app.js"></script>
    <script>
      function openMobileDrawer() {{
        const el = document.getElementById("mobileNavDrawer");
        if (el) el.classList.add("open");
      }}
      function closeMobileDrawer() {{
        const el = document.getElementById("mobileNavDrawer");
        if (el) el.classList.remove("open");
      }}

      document.addEventListener("DOMContentLoaded", () => {{
        farmStore.checkAuthGuard();
        if (document.getElementById("mobileRoleSelect")) {{
          const curUser = farmStore.state.currentUser;
          if (curUser && curUser.id) document.getElementById("mobileRoleSelect").value = curUser.id;
        }}
      }});
    </script>
  </body>
</html>
"""

# ==============================================================================
# 1. DIRECTOR PORTAL (director.html)
# ==============================================================================
director_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <!-- Welcome Banner -->
  <div style="background:linear-gradient(135deg, #0d382d, #124e3f); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.15); color:#a7f3d0; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px; text-transform:uppercase;">
        👑 DIRECTOR & OWNER EXECUTIVE DESK
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Welcome, Engr. Charles Chukwuma
      </h1>
      <p style="color:#d1fae5; font-size:0.85rem;">Executive Financial Dashboard • 80-100g Feed Engine • Egg Size Streams • Spent Hen Valuation</p>
    </div>

    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <button onclick="farmStore.generateWhatsAppBriefing()" class="btn-forest" style="background:#25D366; color:#ffffff; font-weight:800;">
        📱 1-Click WhatsApp Report
      </button>
      <button onclick="farmStore.exportMasterExcel()" class="btn-outline-pill" style="background:rgba(255,255,255,0.1); color:#ffffff; border-color:rgba(255,255,255,0.3);">
        📥 Export Master Excel (.csv)
      </button>
    </div>
  </div>

  <!-- 4 Executive Financial & Valuation Cards -->
  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Total Farm Revenue</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">₦2.29M</div>
      <div class="m-footer-badge">Eggs: ₦1.99M • Manure: ₦300K</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Operating Expenses</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b91c1c;">₦6.74M</div>
      <div class="m-footer-badge" style="background:#fee2e2; color:#b91c1c;">Feed, Power, Wages & Drugs</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Receivables Outstanding</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b45309;">₦516,000</div>
      <div class="m-footer-badge" style="background:#fef3c7; color:#b45309;">Transcorp Hotels (14d Term)</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Flock Asset Valuation</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">₦35.3M</div>
      <div class="m-footer-badge green-tag">5,892 Mature Layers @ ₦6,000</div>
    </div>
  </div>

  <!-- 80-100g Feed Consumption Projection Grid -->
  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Feed Intake Deduction Engine (80g - 100g Benchmark for 5,892 Birds)</h3>
      <span class="status-pill completed">Configured @ 95g / Bird</span>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-top:6px;">
      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.72rem; color:#64748b; display:block;">Daily Consumption (95g)</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">559.7 kg</strong>
        <span style="font-size:0.68rem; color:#64748b;">22.4 Bags of 25kg</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.72rem; color:#64748b; display:block;">Weekly Requirement</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">3,918 kg</strong>
        <span style="font-size:0.68rem; color:#64748b;">156.7 Bags (₦2.90M)</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.72rem; color:#64748b; display:block;">Monthly Requirement</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">16,792 kg</strong>
        <span style="font-size:0.68rem; color:#64748b;">671.7 Bags (₦12.42M)</span>
      </div>

      <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; border-radius:12px;">
        <span style="font-size:0.72rem; color:#166534; display:block;">Inventory Optimization (EOQ)</span>
        <strong style="font-size:1.3rem; color:#15803d; display:block;">553 Bags</strong>
        <span style="font-size:0.68rem; color:#166534;">ROL: <strong>55 Bags</strong> • MOQ: <strong>200 Bags</strong></span>
      </div>
    </div>
  </div>

  <!-- Egg Derivatives & Spent Hen Meat Salvage Valuation -->
  <div style="display:grid; grid-template-columns: 1.2fr 1fr; gap:20px;" class="dashboard-middle-grid">
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Egg Harvest Derivatives & Revenue Streams</h3>
        <span class="status-pill completed">5,172 Eggs Today</span>
      </div>

      <div class="table-responsive">
        <table class="data-table-custom">
          <thead>
            <tr>
              <th>Egg Grade / Classification</th>
              <th>Today's Harvest</th>
              <th>Crates</th>
              <th>Rate (₦)</th>
              <th>Daily Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Grade A Large (53-63g+)</strong></td>
              <td>3,030 eggs</td>
              <td>101.0 Cr</td>
              <td style="color:#15803d; font-weight:700;">₦4,500</td>
              <td style="font-weight:700;">₦454,500</td>
            </tr>
            <tr>
              <td><strong>Grade A Medium (45-52g)</strong></td>
              <td>1,830 eggs</td>
              <td>61.0 Cr</td>
              <td style="color:#15803d; font-weight:700;">₦4,300</td>
              <td style="font-weight:700;">₦262,300</td>
            </tr>
            <tr>
              <td><strong>Grade A Small Pullet (&lt;45g)</strong></td>
              <td>240 eggs</td>
              <td>8.0 Cr</td>
              <td style="color:#d97706; font-weight:700;">₦3,800</td>
              <td style="font-weight:700;">₦30,400</td>
            </tr>
            <tr>
              <td><strong>Hairline Cracked</strong></td>
              <td>37 eggs</td>
              <td>1.2 Cr</td>
              <td style="color:#d97706; font-weight:700;">₦3,200</td>
              <td style="font-weight:700;">₦3,840</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Spent Hen Salvage Forecaster -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Spent Hen Salvage Forecaster</h3>
        <span class="status-pill completed">72-80 Wks</span>
      </div>

      <div style="display:flex; flex-direction:column; gap:10px; margin-top:6px;">
        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #f1f5f9; font-size:0.82rem;">
          <span>Current Mature Birds</span>
          <strong>5,892 Live Birds</strong>
        </div>
        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #f1f5f9; font-size:0.82rem;">
          <span>Spent Hen Meat Price</span>
          <strong style="color:#15803d;">₦3,200 / Bird</strong>
        </div>
        <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; border-radius:12px; text-align:center;">
          <span style="font-size:0.7rem; color:#166534; font-weight:700; text-transform:uppercase;">Flock Meat Salvage Value</span>
          <div style="font-size:1.6rem; font-weight:800; color:#15803d; margin-top:2px;">₦18,854,400</div>
          <small style="color:#166534; font-size:0.68rem;">Lump-sum capital recovery at flock retirement</small>
        </div>
      </div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/director.html", "w") as f:
    f.write(wrap_portal_page("Director & Owner Executive Portal", "Engr. Charles Chukwuma (Director / Owner)", "charles@preciscofarms.com", "CC", director_content))

# ==============================================================================
# 2. FARM MANAGER PORTAL (manager.html)
# ==============================================================================
manager_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <!-- Welcome Banner -->
  <div style="background:linear-gradient(135deg, #124e3f, #1e705b); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:#F2B705; color:#0a0a0a; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px; text-transform:uppercase;">
        ✦ FARM MANAGER COMMAND
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Welcome, Mr. Adebayo Adeleke
      </h1>
      <p style="color:#d1fae5; font-size:0.85rem;">6,000 POL Layers • Water:Feed Ratio (2.11:1) • Stock Reconciler • Egg Size Derivatives</p>
    </div>

    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <button onclick="farmStore.generateWhatsAppBriefing()" class="btn-forest" style="background:#25D366; color:#ffffff; font-weight:800;">📱 WhatsApp Daily Report</button>
      <button onclick="openModal('modalEggHarvest')" class="btn-forest" style="background:#34d399; color:#0d382d;">+ Log Graded Harvest</button>
      <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill" style="background:rgba(255,255,255,0.15); color:#ffffff; border-color:rgba(255,255,255,0.3);">+ Issue B2B Waybill</button>
    </div>
  </div>

  <!-- 4 Manager Operational KPI Cards -->
  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Live Birds</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">5,892</div>
      <div class="m-footer-badge">Initial: 6,000 • 98.2% Livability</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Today's Harvest</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#d97706;">5,172</div>
      <div class="m-footer-badge green-tag">172.4 Crates (101 Large, 61 Med)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Water:Feed Ratio</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#0891b2;">2.11 : 1</div>
      <div class="m-footer-badge green-tag">1,180L Water : 560kg Feed (Normal)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Days of Feed Left</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">7.0 Days</div>
      <div class="m-footer-badge green-tag">157 Bags Warehouse Buffer</div>
    </div>
  </div>

  <!-- Feed Calculation Engine -->
  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Feed Deduction Engine (80g - 100g Daily Requirement per Bird)</h3>
      <span class="status-pill completed">Live Flock: 5,892 Birds</span>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:10px; margin-top:6px;">
      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:10px; border-radius:10px;">
        <span style="font-size:0.7rem; color:#64748b; display:block;">Daily Consumption (95g)</span>
        <strong style="font-size:1.2rem; color:#124e3f; display:block;">559.7 kg</strong>
        <span style="font-size:0.65rem; color:#64748b;">22.4 Bags of 25kg</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:10px; border-radius:10px;">
        <span style="font-size:0.7rem; color:#64748b; display:block;">Weekly Requirement</span>
        <strong style="font-size:1.2rem; color:#124e3f; display:block;">3,918 kg</strong>
        <span style="font-size:0.65rem; color:#64748b;">156.7 Bags (₦2.90M)</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:10px; border-radius:10px;">
        <span style="font-size:0.7rem; color:#64748b; display:block;">Monthly Requirement</span>
        <strong style="font-size:1.2rem; color:#124e3f; display:block;">16,792 kg</strong>
        <span style="font-size:0.65rem; color:#64748b;">671.7 Bags (₦12.42M)</span>
      </div>

      <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:10px; border-radius:10px;">
        <span style="font-size:0.7rem; color:#166534; display:block;">Re-Order Level (ROL)</span>
        <strong style="font-size:1.2rem; color:#15803d; display:block;">55 Bags</strong>
        <span style="font-size:0.65rem; color:#166534;">MOQ: <strong>200 Bags</strong> • EOQ: <strong>553 Bags</strong></span>
      </div>
    </div>
  </div>

  <!-- Physical Stock Taking & Reconciler -->
  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Daily Stock Taking & Anti-Fraud Reconciler</h3>
      <span class="status-pill completed">Audit Trail Active</span>
    </div>

    <div class="table-responsive">
      <table class="data-table-custom">
        <thead>
          <tr>
            <th>Stock Item</th>
            <th>Opening</th>
            <th>Issued</th>
            <th>Physical Closing</th>
            <th>Variance</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Layers Mash (25kg Bags)</strong></td>
            <td>185 Bags</td>
            <td>28 Bags (700 kg)</td>
            <td><strong>157 Bags</strong></td>
            <td style="color:#15803d; font-weight:700;">0 (No Leakage)</td>
            <td><span class="status-pill-green">✓ Balanced</span></td>
          </tr>
          <tr>
            <td><strong>Grade A Large Stored Crates</strong></td>
            <td>189 Crates</td>
            <td>+ 101 Crates</td>
            <td><strong>290 Crates</strong></td>
            <td style="color:#15803d; font-weight:700;">0 (Accurate)</td>
            <td><span class="status-pill-green">✓ Balanced</span></td>
          </tr>
          <tr>
            <td><strong>Grade A Medium Stored Crates</strong></td>
            <td>104 Crates</td>
            <td>+ 61 Crates</td>
            <td><strong>165 Crates</strong></td>
            <td style="color:#15803d; font-weight:700;">0 (Accurate)</td>
            <td><span class="status-pill-green">✓ Balanced</span></td>
          </tr>
          <tr>
            <td><strong>Dry Manure 50kg Sacks</strong></td>
            <td>216 Bags</td>
            <td>+ 24 Bags</td>
            <td><strong>240 Bags</strong></td>
            <td style="color:#15803d; font-weight:700;">0 (Accurate)</td>
            <td><span class="status-pill-green">✓ Balanced</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/manager.html", "w") as f:
    f.write(wrap_portal_page("Farm Manager Command Portal", "Mr. Adebayo Adeleke (Farm Manager)", "manager@preciscofarms.com", "AA", manager_content))

# ==============================================================================
# 3. VETERINARY OFFICER PORTAL (vet.html)
# ==============================================================================
vet_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <div style="background:linear-gradient(135deg, #4a1d96, #2e1065); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.2); color:#e9d5ff; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px; text-transform:uppercase;">
        🩺 VETERINARY & CLINICAL WELFARE PORTAL
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Welcome, Dr. Emeka Okonkwo, DVM
      </h1>
      <p style="color:#e9d5ff; font-size:0.85rem;">Flock Welfare • Sick Bay Isolation (Pen S-1/S-2) • Mortality Necropsy • Drug Withdrawal Hold</p>
    </div>

    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <button onclick="openModal('modalMortality')" class="btn-forest" style="background:#e11d48; color:#ffffff;">☠️ Record Necropsy</button>
      <button onclick="farmStore.triggerVetEmergency()" class="btn-outline-pill" style="background:rgba(255,255,255,0.15); color:#ffffff; border-color:rgba(255,255,255,0.3);">
        📞 Link Farm Manager
      </button>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest" style="background:#581c87; border-color:#581c87;">
      <div class="m-header-flex"><span class="m-title" style="color:#e9d5ff;">Flock Livability</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">98.2%</div>
      <div class="m-footer-badge">5,892 Live Birds</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Daily Mortality</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b91c1c;">3 Birds</div>
      <div class="m-footer-badge" style="background:#fee2e2; color:#b91c1c;">Threshold: 6 Birds Max</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Sick Bay Isolation</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b45309;">1 in Care</div>
      <div class="m-footer-badge" style="background:#fef3c7; color:#b45309;">Pen S-1 Active Care</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Drug Withdrawal</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">0 Days</div>
      <div class="m-footer-badge green-tag">✓ Food Safety Clear</div>
    </div>
  </div>

  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Sick Bay Isolation Pen Tracker (Pen S-1 & S-2)</h3>
      <span class="status-pill in-progress">Active Isolation</span>
    </div>

    <div class="table-responsive">
      <table class="data-table-custom">
        <thead>
          <tr>
            <th>Date</th>
            <th>Cage Tag</th>
            <th>Symptoms</th>
            <th>Diagnosis</th>
            <th>Isolation Bay</th>
            <th>Therapy</th>
            <th>Attendant</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>2026-08-19</td>
            <td><strong>Cage Tier 2-A4</strong></td>
            <td>Dullness, pale comb, reduced water intake</td>
            <td>Respiratory stress / fatigue</td>
            <td><span class="status-pill-amber">Sick Bay Pen S-1</span></td>
            <td>Oral Multivitamins + Electrolytes in header tank</td>
            <td>Chinedu Obi</td>
            <td><button onclick="farmStore.resolveSickBird('SCK-01'); alert('Bird recovered and returned to Tier 2.'); window.location.reload();" class="btn-forest" style="padding:4px 10px; font-size:0.75rem;">Mark Recovered</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/vet.html", "w") as f:
    f.write(wrap_portal_page("Veterinary Officer Portal", "Dr. Emeka Okonkwo, DVM (Veterinary Officer)", "vet@preciscofarms.com", "EO", vet_content))

# ==============================================================================
# 4. ATTENDANT PORTAL (attendant.html)
# ==============================================================================
attendant_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <div style="background:linear-gradient(135deg, #124e3f, #15803d); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.2); color:#d1fae5; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px;">
        🐔 ATTENDANT SHIFT WORKSPACE
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Attendant Shift Duties (Shift 1, 2, 3)
      </h1>
      <p style="color:#d1fae5; font-size:0.85rem;">Egg Harvest with Size Derivatives • Dead Bird Disposal • Manure Scraper & Water Check</p>
    </div>

    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <button onclick="openModal('modalEggHarvest')" class="btn-forest" style="background:#F2B705; color:#000; font-weight:800;">🥚 Log Graded Harvest</button>
      <button onclick="openModal('modalMortality')" class="btn-forest" style="background:#e11d48; color:#fff;">☠️ Log Dead Bird</button>
    </div>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:10px;">
        <h3 style="font-size:0.95rem;">Morning Shift (06:30 - 12:00)</h3>
        <span class="status-pill completed">Chinedu Obi</span>
      </div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>1. Walkthrough inspection across 3 tiers</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>2. Remove dead birds to incinerator bin</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>3. Drinker pressure check (2.2 Bar)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>4. Round 1 Harvest (3,164 eggs graded)</span></div>
    </div>

    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:10px;">
        <h3 style="font-size:0.95rem;">Afternoon Shift (12:00 - 17:30)</h3>
        <span class="status-pill completed">Blessing Eze</span>
      </div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>1. Asaba ambient heat check (29.6°C)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>2. Feed top-up & Sick Bay S-1 check</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>3. Round 2 Harvest (2,008 eggs graded)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>4. Stack Large/Medium trays in cold store</span></div>
    </div>

    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:10px;">
        <h3 style="font-size:0.95rem;">Evening Shift (17:30 - 20:30)</h3>
        <span class="status-pill in-progress">Musa Ibrahim</span>
      </div>
      <div class="checklist-item done"><input type="checkbox" checked> <span>1. Final health sweep</span></div>
      <div class="checklist-item done"><input type="checkbox" checked> <span>2. Check 15,000L header reservoir</span></div>
      <div class="checklist-item"><input type="checkbox"> <span>3. Manure scraper conveyor belt check</span></div>
      <div class="checklist-item"><input type="checkbox"> <span>4. Lock and padlock pen doors</span></div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/attendant.html", "w") as f:
    f.write(wrap_portal_page("Attendant Shift Portal", "Chinedu Obi (Poultry Attendant)", "chinedu@preciscofarms.com", "CO", attendant_content))

# ==============================================================================
# 5. SECURITY PORTAL (security.html)
# ==============================================================================
security_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <div style="background:linear-gradient(135deg, #1e293b, #0f172a); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.15); color:#94a3b8; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px;">
        🛡️ GATE 1 & GATE 2 SECURITY DESK
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Security Gate Registry & Disinfection
      </h1>
      <p style="color:#94a3b8; font-size:0.85rem;">Truck Wheel Spray Dip • 48-Hour Contact Screening • Outbound Delivery Gate Passes</p>
    </div>

    <button onclick="alert('New visitor entry recorded at Gate 1.');" class="btn-forest" style="background:#15803d; color:#fff;">+ Register Entry</button>
  </div>

  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Gate 1 Vehicle Wheel Dip & Visitor Entry Registry</h3>
      <span class="status-pill completed">Virkon-S 1% Active</span>
    </div>

    <div class="table-responsive">
      <table class="data-table-custom">
        <thead>
          <tr>
            <th>Time In</th>
            <th>Visitor Name & Org</th>
            <th>Vehicle Reg #</th>
            <th>Purpose of Entry</th>
            <th>Biosecurity Disinfection Passed</th>
            <th>Security Guard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>09:30 AM</td>
            <td><strong>Engr. Patrick Agbo (Delta Ministry of Ag)</strong></td>
            <td>Gov Prado (DT-01-AGR)</td>
            <td>Biosecurity Audit</td>
            <td><span class="status-pill-green">✓ Wheel Spray • Boots • 48h Clear</span></td>
            <td>Sgt. Joshua Garba</td>
          </tr>
          <tr>
            <td>02:00 PM</td>
            <td><strong>Kenneth Obi (Corporate Logistics)</strong></td>
            <td>Toyota Dyna (DLT-892-XA)</td>
            <td>B2B Egg Dispatch (120 Crates)</td>
            <td><span class="status-pill-green">✓ Gate Pass #PASS-0818-01 Verified</span></td>
            <td>Sunday Alabi</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/security.html", "w") as f:
    f.write(wrap_portal_page("Security Officers Portal", "Sgt. Joshua Garba (Security Officer)", "security@preciscofarms.com", "JG", security_content))

# ==============================================================================
# 6. DRIVER PORTAL (driver.html)
# ==============================================================================
driver_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <div style="background:linear-gradient(135deg, #0369a1, #075985); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.2); color:#bae6fd; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px;">
        🚚 LOGISTICS & DELIVERY DRIVER HUB
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Welcome, Kenneth Obi
      </h1>
      <p style="color:#bae6fd; font-size:0.85rem;">Vehicle: Toyota Dyna Van (DLT-892-XA) • Active Corporate Delivery Waybills</p>
    </div>
  </div>

  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Active Delivery Route Waybills</h3>
      <span class="status-pill in-progress">3 Routes Active</span>
    </div>

    <div class="table-responsive">
      <table class="data-table-custom">
        <thead>
          <tr>
            <th>Waybill #</th>
            <th>Destination Client</th>
            <th>Delivery Address</th>
            <th>Contact Person</th>
            <th>Crates Breakdown</th>
            <th>Delivery Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>WB-PFV-2026-104</strong></td>
            <td><strong>Transcorp Hotels & Suites</strong></td>
            <td>Plot 4 Asaba Waterfront District</td>
            <td>Chef Gabriel (+234 803 112 8899)</td>
            <td><strong>120 Crates</strong> (80 Large, 40 Med)</td>
            <td><button onclick="alert('Delivery confirmed! Client receipt signed.');" class="btn-forest" style="padding:4px 10px; font-size:0.75rem;">Confirm Delivery & Sign Receipt</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/driver.html", "w") as f:
    f.write(wrap_portal_page("Logistics Driver Portal", "Kenneth Obi (Logistics Driver)", "logistics@preciscofarms.com", "KO", driver_content))

# ==============================================================================
# 7. CONSULTANT PORTAL (consultant.html)
# ==============================================================================
consultant_content = """
<div style="display:flex; flex-direction:column; gap:20px;">
  <div style="background:linear-gradient(135deg, #0f766e, #115e59); border-radius:20px; padding:22px 24px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
    <div>
      <span style="background:rgba(255,255,255,0.2); color:#ccfbf1; font-size:0.7rem; font-family:ui-monospace, monospace; font-weight:800; padding:3px 10px; border-radius:9999px;">
        📊 POULTRY MANAGEMENT CONSULTANT
      </span>
      <h1 style="color:#ffffff; font-size:1.8rem; font-weight:800; margin:6px 0 2px; font-family:var(--font-display);">
        Welcome, Dr. (Mrs.) Ifeoma Nnamdi
      </h1>
      <p style="color:#ccfbf1; font-size:0.85rem;">Flock Performance Analytics • FCR Efficiency • 80-100g Feed Benchmarks • EOQ Review</p>
    </div>

    <button onclick="alert('Consultant recommendations submitted to Director.');" class="btn-forest" style="background:#F2B705; color:#000;">+ Submit Advisory Note</button>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest" style="background:#115e59; border-color:#115e59;">
      <div class="m-header-flex"><span class="m-title">Hen-Day Rate</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">87.8%</div>
      <div class="m-footer-badge">Peak Target: 88.5%</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">FCR Efficiency</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">1.59</div>
      <div class="m-footer-badge green-tag">kg feed per dozen eggs</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Feed Intake</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#0891b2;">95.04g</div>
      <div class="m-footer-badge green-tag">Within 80-100g Target</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Mortality Rate</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">0.051%</div>
      <div class="m-footer-badge green-tag">Well below 0.12% limit</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/consultant.html", "w") as f:
    f.write(wrap_portal_page("Poultry Consultant Portal", "Dr. (Mrs.) Ifeoma Nnamdi (Consultant)", "consultant@preciscofarms.com", "IN", consultant_content))

print("All role portals regenerated with clean universal responsive layouts!")
