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

      <!-- Role Switcher -->
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
        <!-- Sign Out Link in Sidebar -->
        <a href="javascript:void(0);" onclick="farmStore.logout();" class="sidebar-nav-item" style="color:#ef4444; margin-top:8px;">
          <div class="nav-left">
            <span>🚪</span>
            <span>Sign Out</span>
          </div>
        </a>
      </div>

      <!-- Mobile App Promo Card -->
      <div class="sidebar-promo-card">
        <div style="width:28px; height:28px; border-radius:50%; background:rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center; margin-bottom:8px; font-size:0.8rem;">📱</div>
        <h4>Precisco Mobile</h4>
        <p>Log egg runs & shift tasks directly on mobile</p>
        <button class="sidebar-promo-btn" onclick="alert('Precisco Farm Attendant PWA Ready for Mobile install!');">Download App</button>
      </div>
    </aside>
    """
    return html

def get_top_navbar():
    return """
    <div class="top-navbar">
      <!-- Search Task Pill (Donezo Style) -->
      <div class="search-pill-box">
        <span style="color:#94a3b8; font-size:0.9rem;">🔍</span>
        <input type="text" placeholder="Search task, bird tag or order..." />
        <span class="search-shortcut-badge">⌘F</span>
      </div>

      <!-- Right Profile, Sign Out & Notifications -->
      <div class="top-navbar-right">
        <button class="icon-round-btn" title="Messages" onclick="alert('No new shift handover messages.');">
          ✉️
        </button>

        <a href="alerts.html" class="icon-round-btn" title="Notifications">
          🔔
          <span style="position:absolute; top:4px; right:4px; width:8px; height:8px; background:#ef4444; border-radius:50%;"></span>
        </a>

        <div class="user-profile-widget" onclick="openModal('modalRoleSwitcher');" title="Click to Switch User Role">
          <div class="avatar-circle" id="navAvatar">AA</div>
          <div class="user-info">
            <span class="user-name" id="navUserName">Mr. Adebayo Adeleke</span>
            <span class="user-email" id="navUserEmail">manager@preciscofarms.com</span>
          </div>
        </div>

        <button onclick="farmStore.logout();" class="btn-outline-pill" style="padding:6px 14px; font-size:0.75rem; color:#ef4444; border-color:#fecaca;" title="Sign Out of Portal">
          <span>Sign Out</span>
        </button>
      </div>
    </div>
    """

def get_dock():
    return """
    <div class="floating-dock-donezo">
      <a href="pages.html" class="btn-forest" style="padding:6px 14px; font-size:0.75rem;">✦ All 16 Pages</a>
      <button onclick="openModal('modalEggHarvest')" class="btn-outline-pill" style="padding:6px 14px; font-size:0.75rem;">🥚 Egg Run</button>
      <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill" style="padding:6px 14px; font-size:0.75rem;">💼 B2B Waybill</button>
      <button onclick="openModal('modalMortality')" class="btn-outline-pill" style="padding:6px 14px; font-size:0.75rem; color:#e11d48;">☠️ Mortality</button>
      <a href="operations.html" class="btn-outline-pill" style="padding:6px 14px; font-size:0.75rem;">📋 Checklists</a>
    </div>
    """

def get_modals():
    return """
    <!-- Modal: Log Egg Harvest -->
    <div id="modalEggHarvest" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title">🥚 Log Twice-Daily Egg Harvest</h3>
          <button class="modal-close-btn" onclick="closeModal('modalEggHarvest')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addEggHarvest({
          round: this.round.value,
          good: this.good.value,
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
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label" style="color:var(--forest-dark);">✓ Grade A Marketable Eggs</label>
                <input type="number" name="good" placeholder="e.g. 3100" required>
              </div>
              <div class="form-group">
                <label class="form-label" style="color:var(--amber-dark);">⚠️ Hairline Cracked Eggs</label>
                <input type="number" name="cracked" placeholder="e.g. 20" value="0">
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label" style="color:var(--rose-dark);">✕ Broken / Leaking Eggs</label>
                <input type="number" name="broken" placeholder="e.g. 5" value="0">
              </div>
              <div class="form-group">
                <label class="form-label">🪶 Dirty / Rejects</label>
                <input type="number" name="reject" placeholder="e.g. 10" value="0">
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn-outline-pill" onclick="closeModal('modalEggHarvest')">Cancel</button>
            <button type="submit" class="btn-forest">Save Harvest Record</button>
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
                  <option value="Undetermined (Awaiting Vet)">Undetermined (Awaiting Vet)</option>
                </select>
              </div>
            </div>
            <div style="background:#fee2e2; padding:12px; border-radius:12px; font-size:0.75rem; color:#991b1b;">
              <strong>SOP-BIO-004:</strong> Carcasses must be bagged immediately in biohazard polythene and incinerated.
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn-outline-pill" onclick="closeModal('modalMortality')">Cancel</button>
            <button type="submit" class="btn-forest" style="background:var(--rose-dark);">Confirm Mortality</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal: Corporate Sales Order -->
    <div id="modalSalesOrder" class="modal-backdrop">
      <div class="modal-box">
        <div class="modal-header">
          <h3 class="modal-title">💼 Create Corporate B2B Order & Waybill</h3>
          <button class="modal-close-btn" onclick="closeModal('modalSalesOrder')">&times;</button>
        </div>
        <form onsubmit="event.preventDefault(); farmStore.addCorporateOrder({
          customer: this.customer.value,
          crates: this.crates.value,
          unitPrice: this.unitPrice.value,
          paid: this.paid.value,
          vehicle: this.vehicle.value
        }); closeModal('modalSalesOrder'); window.location.reload();">
          <div class="modal-body">
            <div class="form-group">
              <label class="form-label">Corporate Client</label>
              <select name="customer">
                <option value="Transcorp Hotels & Suites Ltd">Transcorp Hotels & Suites Ltd</option>
                <option value="Grand Delta Supermarkets Ltd">Grand Delta Supermarkets Ltd</option>
                <option value="Royal Crown Confectioneries">Royal Crown Confectioneries</option>
                <option value="Prime Catering & Offshore Services">Prime Catering & Offshore Services</option>
              </select>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label class="form-label">Crates (30-Egg Trays)</label>
                <input type="number" name="crates" placeholder="e.g. 100" required>
              </div>
              <div class="form-group">
                <label class="form-label">Rate per Crate (₦)</label>
                <input type="number" name="unitPrice" value="4300" required>
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
            <button type="submit" class="btn-forest">Generate Waybill & Issue Gate Pass</button>
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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
      // Auth Guard & User Data Hydration
      document.addEventListener("DOMContentLoaded", () => {{
        // Enforce Login Guard
        farmStore.checkAuthGuard();

        const curUser = farmStore.state.currentUser;
        if (document.getElementById("navUserName")) document.getElementById("navUserName").innerText = curUser.name;
        if (document.getElementById("navUserEmail")) document.getElementById("navUserEmail").innerText = (curUser.email || (curUser.name.toLowerCase().split(" ")[0] + "@preciscofarms.com"));
        if (document.getElementById("navAvatar")) document.getElementById("navAvatar").innerText = curUser.name.split(" ").map(n => n[0]).slice(0, 2).join("");
        if (document.getElementById("sidebarRoleSelect")) document.getElementById("sidebarRoleSelect").value = curUser.id;

        // Digital Time Tracker Clock
        let sec = 5048; // 01:24:08 baseline
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

print("Donezo template generator updated with Auth Guard.")
