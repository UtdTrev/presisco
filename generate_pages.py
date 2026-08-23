import os

base_dir = "/home/user/precisco-portal"

def get_sidebar(active_page):
    menu_items = [
        ("dashboard.html", "Dashboard", "📊", "dashboard", None),
        ("sales.html", "B2B Sales", "💼", "sales", "12+"),
        ("operations.html", "Shift Tasks", "📋", "operations", None),
        ("eggs.html", "Harvest & Eggs", "🥚", "eggs", None),
        ("flocks.html", "Flocks (6,000)", "🐔", "flocks", None),
        ("houses.html", "House Climate", "🏠", "houses", None),
        ("reports.html", "Analytics", "📈", "reports", None),
        ("pages.html", "All 16 Pages", "✦", "pages", "New")
    ]

    general_items = [
        ("financials.html", "P&L Ledger", "💳", "financials"),
        ("health.html", "Health & Sick", "🩺", "health"),
        ("feed.html", "Feed & Water", "🌾", "feed"),
        ("inventory.html", "Warehouse", "📦", "inventory"),
        ("biosecurity.html", "Gate Security", "🛡️", "biosecurity"),
        ("settings.html", "Settings", "⚙️", "settings")
    ]

    html = """
    <aside class="sidebar">
      <a href="dashboard.html" class="brand-header">
        <div class="brand-logo-icon">🌿</div>
        <div class="brand-title-text">Precisco</div>
      </a>

      <div style="background:#f8fafc; border:1px solid #edf2f7; padding:8px 12px; border-radius:14px;">
        <span style="font-size:0.65rem; color:#64748b; font-family:var(--font-mono); font-weight:700; display:block; margin-bottom:4px;">LOGGED-IN USER ROLE:</span>
        <select id="sidebarRoleSelect" onchange="farmStore.setCurrentUser(this.value);" style="font-size:0.75rem; padding:4px 8px; border-radius:8px;">
          <option value="STF-MGR" selected>Mr. Adebayo (Farm Manager)</option>
          <option value="STF-DIR">Engr. Charles (Director / Owner)</option>
          <option value="STF-VET">Dr. Emeka (Veterinary Officer)</option>
          <option value="STF-CON">Dr. Ifeoma (Consultant)</option>
          <option value="STF-AT1">Chinedu Obi (Attendant Shift 1)</option>
          <option value="STF-AT2">Blessing Eze (Attendant Shift 2)</option>
          <option value="STF-SEC1">Sgt. Joshua (Security Officer)</option>
          <option value="STF-DRV">Kenneth Obi (Logistics Driver)</option>
        </select>
      </div>

      <div class="sidebar-group">
        <div class="sidebar-group-title">MENU</div>
    """

    for url, label, icon, key, badge in menu_items:
        active_cls = "active" if active_page == key else ""
        badge_html = f'<span class="sidebar-count-badge">{badge}</span>' if badge else ""
        html += f"""
        <a href="{url}" class="sidebar-nav-item {active_cls}">
          <div class="nav-left">
            <span>{icon}</span>
            <span>{label}</span>
          </div>
          {badge_html}
        </a>
        """

    html += """
      </div>

      <div class="sidebar-group">
        <div class="sidebar-group-title">GENERAL</div>
    """

    for url, label, icon, key in general_items:
        active_cls = "active" if active_page == key else ""
        html += f"""
        <a href="{url}" class="sidebar-nav-item {active_cls}">
          <div class="nav-left">
            <span>{icon}</span>
            <span>{label}</span>
          </div>
        </a>
        """

    html += """
        <a href="javascript:void(0);" onclick="farmStore.logout();" class="sidebar-nav-item" style="color:#ef4444; margin-top:8px;">
          <div class="nav-left">
            <span>🚪</span>
            <span>Sign Out</span>
          </div>
        </a>
      </div>

      <div class="sidebar-promo-card">
        <div style="width:28px; height:28px; border-radius:50%; background:rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center; margin-bottom:8px; font-size:0.8rem;">📱</div>
        <h4>Precisco Mobile</h4>
        <p>Log egg runs & shift tasks directly on mobile</p>
        <button class="sidebar-promo-btn" onclick="alert('Precisco Farm Attendant PWA is ready for mobile viewing!');">Mobile View</button>
      </div>
    </aside>
    """
    return html

def get_top_navbar():
    return """
    <div class="top-navbar">
      <div style="display:flex; align-items:center; gap:10px;">
        <button class="mobile-menu-btn" onclick="openMobileDrawer();" title="Open Mobile Navigation">
          ☰
        </button>
        <div class="search-pill-box">
          <span style="color:#94a3b8; font-size:0.85rem;">🔍</span>
          <input type="text" placeholder="Search task or log..." />
          <span class="search-shortcut-badge">⌘F</span>
        </div>
      </div>

      <div class="top-navbar-right">
        <button class="icon-round-btn" title="Emergency Help" onclick="alert('Emergency Hotline: Dr. Emeka (+234 803 555 0192)');">
          📞
        </button>

        <a href="alerts.html" class="icon-round-btn" title="Alerts">
          🔔
          <span style="position:absolute; top:3px; right:3px; width:7px; height:7px; background:#ef4444; border-radius:50%;"></span>
        </a>

        <div class="user-profile-widget" onclick="openMobileDrawer();" title="Click to view staff details">
          <div class="avatar-circle" id="navAvatar">AA</div>
          <div class="user-info">
            <span class="user-name" id="navUserName">Mr. Adebayo Adeleke</span>
            <span class="user-email" id="navUserEmail">manager@preciscofarms.com</span>
          </div>
        </div>

        <button onclick="farmStore.logout();" class="btn-outline-pill" style="padding:6px 12px; font-size:0.75rem; color:#ef4444; border-color:#fecaca;" title="Sign Out">
          <span>Sign Out</span>
        </button>
      </div>
    </div>

    <!-- Slide-Out Mobile Navigation Drawer -->
    <div id="mobileNavDrawer" class="mobile-nav-drawer" onclick="if(event.target === this) closeMobileDrawer();">
      <div class="mobile-nav-content">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:12px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.4rem;">🌿</span>
            <strong style="font-size:1.1rem; color:var(--forest-dark);">Precisco Farms</strong>
          </div>
          <button onclick="closeMobileDrawer();" style="font-size:1.4rem; color:#94a3b8;">&times;</button>
        </div>

        <div style="background:#f8fafc; padding:10px; border-radius:12px; border:1px solid #e2e8f0;">
          <span style="font-size:0.65rem; color:#64748b; font-weight:700; display:block; margin-bottom:4px;">SWITCH PORTAL VIEW:</span>
          <select id="mobileRoleSelect" onchange="farmStore.setCurrentUser(this.value);" style="font-size:0.8rem; padding:6px 10px;">
            <option value="STF-MGR">Mr. Adebayo (Farm Manager)</option>
            <option value="STF-DIR">Engr. Charles (Director / Owner)</option>
            <option value="STF-VET">Dr. Emeka (Veterinary Officer)</option>
            <option value="STF-CON">Dr. Ifeoma (Consultant)</option>
            <option value="STF-AT1">Chinedu Obi (Attendant Shift 1)</option>
            <option value="STF-SEC1">Sgt. Joshua (Security Officer)</option>
            <option value="STF-DRV">Kenneth Obi (Logistics Driver)</option>
          </select>
        </div>

        <div style="display:flex; flex-direction:column; gap:4px; font-size:0.88rem; font-weight:600;">
          <a href="dashboard.html" class="sidebar-nav-item">📊 Dashboard</a>
          <a href="sales.html" class="sidebar-nav-item">💼 B2B Sales & Waybills</a>
          <a href="operations.html" class="sidebar-nav-item">📋 Shift Checklists</a>
          <a href="eggs.html" class="sidebar-nav-item">🥚 Twice-Daily Harvest</a>
          <a href="flocks.html" class="sidebar-nav-item">🐔 Flock PFV-LAY-001</a>
          <a href="houses.html" class="sidebar-nav-item">🏠 House 1 Climate</a>
          <a href="health.html" class="sidebar-nav-item">🩺 Health & Sick Bay</a>
          <a href="feed.html" class="sidebar-nav-item">🌾 Feed & Water Flow</a>
          <a href="inventory.html" class="sidebar-nav-item">📦 Warehouse Stocks</a>
          <a href="financials.html" class="sidebar-nav-item">💳 Operating P&L</a>
          <a href="biosecurity.html" class="sidebar-nav-item">🛡️ Gate Security Log</a>
          <a href="reports.html" class="sidebar-nav-item">📈 Executive Reports</a>
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

def get_dock():
    return """
    <div class="floating-dock-donezo">
      <a href="pages.html" class="btn-forest" style="padding:6px 12px; font-size:0.75rem;">✦ All 16 Pages</a>
      <button onclick="openModal('modalEggHarvest')" class="btn-outline-pill" style="padding:6px 12px; font-size:0.75rem;">🥚 Egg Run</button>
      <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill" style="padding:6px 12px; font-size:0.75rem;">💼 Waybill</button>
      <button onclick="openModal('modalMortality')" class="btn-outline-pill" style="padding:6px 12px; font-size:0.75rem; color:#e11d48;">☠️ Mortality</button>
    </div>
    """

def get_modals():
    return """
    <!-- Modal: Log Egg Harvest -->
    <div id="modalEggHarvest" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title">🥚 Log Harvest (Size Derivatives)</h3>
          <button class="modal-close-btn" onclick="closeModal('modalEggHarvest')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addEggHarvest({
          round: this.round.value,
          large: this.large.value,
          medium: this.medium.value,
          small: this.small.value,
          cracked: this.cracked.value,
          broken: this.broken.value,
          reject: this.reject.value
        }); closeModal('modalEggHarvest'); window.location.reload();">
          <div class="modal-body">
            <div class="form-group">
              <label class="form-label">Harvest Collection Round</label>
              <select name="round">
                <option value="Morning Harvest (Round 1)">Morning Harvest (Round 1 - 08:30 AM)</option>
                <option value="Afternoon Harvest (Round 2)">Afternoon Harvest (Round 2 - 02:30 PM)</option>
              </select>
            </div>
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
        <form onsubmit="event.preventDefault(); farmStore.addMortality({
          count: this.count.value,
          reason: this.reason.value
        }); closeModal('modalMortality'); window.location.reload();">
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
        <form onsubmit="event.preventDefault(); farmStore.addCorporateOrder({
          customer: this.customer.value,
          cratesLarge: this.cratesLarge.value,
          cratesMed: this.cratesMed.value,
          paid: this.paid.value,
          vehicle: this.vehicle.value
        }); closeModal('modalSalesOrder'); window.location.reload();">
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
            <button type="submit" class="btn-forest">Issue Waybill & Gate Pass</button>
          </div>
        </form>
      </div>
    </div>
    """

def wrap_donezo_page(title, active_page, page_content):
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
      {get_sidebar(active_page)}
      <div class="main-panel">
        {get_top_navbar()}
        <div class="page-content-wrapper">
          {page_content}
        </div>
      </div>
      {get_dock()}
      {get_modals()}
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

        const curUser = farmStore.state.currentUser;
        if (document.getElementById("navUserName")) document.getElementById("navUserName").innerText = curUser.name;
        if (document.getElementById("navUserEmail")) document.getElementById("navUserEmail").innerText = (curUser.email || "manager@preciscofarms.com");
        if (document.getElementById("navAvatar")) document.getElementById("navAvatar").innerText = curUser.name.split(" ").map(n => n[0]).slice(0, 2).join("");
        if (document.getElementById("sidebarRoleSelect")) document.getElementById("sidebarRoleSelect").value = curUser.id;
        if (document.getElementById("mobileRoleSelect")) document.getElementById("mobileRoleSelect").value = curUser.id;

        // Digital Time Tracker Clock
        let sec = 5048;
        let timerRunning = true;
        const timeDisplay = document.getElementById("liveTimeTrackerDisplay");

        function updateTimer() {{
          if (!timeDisplay) return;
          let hrs = Math.floor(sec / 3600);
          let mins = Math.floor((sec % 3600) / 60);
          let s = sec % 60;
          timeDisplay.innerText = 
            String(hrs).padStart(2, '0') + ":" + 
            String(mins).padStart(2, '0') + ":" + 
            String(s).padStart(2, '0');
        }}

        setInterval(() => {{
          if (timerRunning) {{
            sec++;
            updateTimer();
          }}
        }}, 1000);

        window.toggleTimer = () => {{
          timerRunning = !timerRunning;
          alert(timerRunning ? 'Shift timer resumed.' : 'Shift timer paused.');
        }};

        window.stopTimer = () => {{
          timerRunning = false;
          alert('Shift duration logged: ' + (timeDisplay ? timeDisplay.innerText : '01:24:08'));
        }};
      }});
    </script>
  </body>
</html>
"""

print("Mobile-first templates compiled.")
