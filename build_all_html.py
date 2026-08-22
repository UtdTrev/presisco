import os
from generate_pages import wrap_donezo_page

base_dir = "/home/user/precisco-portal"

# 1. dashboard.html (Exact Donezo Light/Forest-Green Personalized Dashboard)
dashboard_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <!-- Dashboard Header Row -->
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Dashboard</h1>
      <p>Plan, prioritize, and accomplish your layer farm tasks with ease.</p>
    </div>

    <div class="dashboard-action-buttons">
      <button onclick="openModal('modalEggHarvest')" class="btn-forest">
        <span>+ Log Harvest</span>
      </button>
      <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill">
        <span>+ B2B Order</span>
      </button>
      <button onclick="window.print()" class="btn-outline-pill">
        <span>Export Data</span>
      </button>
    </div>
  </div>

  <!-- 4 Metric Cards (1 Forest Green Solid Highlight + 3 White Cards) -->
  <div class="metrics-row-4">
    <!-- 1. Total Live Birds (Forest Green Highlight) -->
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex">
        <span class="m-title">Total POL Birds</span>
        <div class="m-arrow-btn">↗</div>
      </div>
      <div class="m-number">5,892</div>
      <div class="m-footer-badge">
        <span>↑</span> 98.2% Livability from arrival
      </div>
    </div>

    <!-- 2. Harvest Today (White Card) -->
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex">
        <span class="m-title">Harvest Today</span>
        <div class="m-arrow-btn">↗</div>
      </div>
      <div class="m-number">5,172</div>
      <div class="m-footer-badge green-tag">
        <span>↑</span> 172.4 Crates produced
      </div>
    </div>

    <!-- 3. Hen-Day Rate (White Card) -->
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex">
        <span class="m-title">Hen-Day Laying</span>
        <div class="m-arrow-btn">↗</div>
      </div>
      <div class="m-number">87.8%</div>
      <div class="m-footer-badge green-tag">
        <span>↑</span> Peak Target 88.5%
      </div>
    </div>

    <!-- 4. Days of Feed (White Card) -->
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex">
        <span class="m-title">Days of Feed</span>
        <div class="m-arrow-btn">↗</div>
      </div>
      <div class="m-number">6 Days</div>
      <div class="m-footer-badge green-tag" style="background:#f1f5f9; color:#64748b;">
        157 Bags Warehouse Buffer
      </div>
    </div>
  </div>

  <!-- Middle 3-Column Grid (Donezo Layout) -->
  <div class="dashboard-middle-grid">
    <!-- Card 1: Project / Laying Analytics Capsule Bar Chart -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Laying Analytics</h3>
      </div>

      <div class="pill-chart-container">
        <!-- Sun (Hatched) -->
        <div class="pill-bar-col">
          <div class="pill-bar hatched" style="height: 65px;"></div>
          <span class="pill-bar-day">S</span>
        </div>

        <!-- Mon (Solid Green) -->
        <div class="pill-bar-col">
          <div class="pill-bar solid-green" style="height: 95px;"></div>
          <span class="pill-bar-day">M</span>
        </div>

        <!-- Tue (Mint Green with Tooltip) -->
        <div class="pill-bar-col">
          <div class="pill-bar mint-green" style="height: 75px;">
            <div class="pill-bar-tooltip">87.8%</div>
          </div>
          <span class="pill-bar-day">T</span>
        </div>

        <!-- Wed (Solid Green High) -->
        <div class="pill-bar-col">
          <div class="pill-bar solid-green" style="height: 105px;"></div>
          <span class="pill-bar-day">W</span>
        </div>

        <!-- Thu (Hatched) -->
        <div class="pill-bar-col">
          <div class="pill-bar hatched" style="height: 60px;"></div>
          <span class="pill-bar-day">T</span>
        </div>

        <!-- Fri (Hatched) -->
        <div class="pill-bar-col">
          <div class="pill-bar hatched" style="height: 70px;"></div>
          <span class="pill-bar-day">F</span>
        </div>

        <!-- Sat (Hatched) -->
        <div class="pill-bar-col">
          <div class="pill-bar hatched" style="height: 80px;"></div>
          <span class="pill-bar-day">S</span>
        </div>
      </div>
    </div>

    <!-- Card 2: Reminders (Dark Green Banner) -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Reminders</h3>
      </div>

      <div style="display:flex; flex-direction:column; gap:8px;">
        <h4 style="font-size:1.05rem; color:var(--text-main); font-weight:700; line-height:1.2;">
          Morning Walkthrough & Heat Check
        </h4>
        <span style="font-size:0.75rem; color:var(--text-muted);">Time: 02.00 pm - 04.00 pm • Main House 1</span>
      </div>

      <a href="operations.html" class="reminders-meeting-card">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:1.2rem;">📋</span>
          <div>
            <h4 style="font-size:0.88rem; margin:0;">Check 8 Exhaust Fans</h4>
            <p style="margin:0; font-size:0.72rem;">Asaba 29.6°C • Drinker 2.2 Bar</p>
          </div>
        </div>
        <span style="font-size:0.8rem; font-weight:700; background:rgba(255,255,255,0.2); padding:4px 10px; border-radius:var(--radius-full);">Open &rarr;</span>
      </a>
    </div>

    <!-- Card 3: Corporate Orders List -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Corporate Orders</h3>
        <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill" style="padding:4px 12px; font-size:0.75rem;">+ New</button>
      </div>

      <div class="project-list-widget">
        <div class="project-item-row">
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="project-icon-box" style="background:#e0f2fe; color:#0284c7;">🏨</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Transcorp Hotels (120 Crates)</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Due date: Aug 20, 2026</span>
            </div>
          </div>
          <span class="status-pill pending" style="font-size:0.65rem;">14d Term</span>
        </div>

        <div class="project-item-row">
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="project-icon-box" style="background:#dcfce7; color:#16a34a;">🛒</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Grand Delta Supermarkets (200 Crates)</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Due date: Aug 22, 2026</span>
            </div>
          </div>
          <span class="status-pill completed" style="font-size:0.65rem;">Paid</span>
        </div>

        <div class="project-item-row">
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="project-icon-box" style="background:#fef3c7; color:#d97706;">🍞</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Royal Crown Bakeries (150 Crates)</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Due date: Aug 25, 2026</span>
            </div>
          </div>
          <span class="status-pill completed" style="font-size:0.65rem;">Paid</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom 3-Column Grid (Donezo Layout) -->
  <div class="dashboard-bottom-grid">
    <!-- Card 1: Team Collaboration -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Team Collaboration</h3>
        <button onclick="alert('Staff Duty Schedule active.');" class="btn-outline-pill" style="padding:4px 12px; font-size:0.75rem;">+ Add Member</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:4px;">
        <div class="team-member-row">
          <div class="team-user-flex">
            <div class="team-user-avatar" style="background:#fee2e2; color:#b91c1c;">CO</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Chinedu Obi</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Shift 1: Morning 6,000 Layer Harvest</span>
            </div>
          </div>
          <span class="status-pill completed">Completed</span>
        </div>

        <div class="team-member-row">
          <div class="team-user-flex">
            <div class="team-user-avatar" style="background:#dcfce7; color:#15803d;">BE</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Blessing Eze</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Shift 2: Afternoon Egg Grading & Cold Room</span>
            </div>
          </div>
          <span class="status-pill in-progress">In Progress</span>
        </div>

        <div class="team-member-row">
          <div class="team-user-flex">
            <div class="team-user-avatar" style="background:#e0e7ff; color:#4338ca;">MI</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Musa Ibrahim</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Shift 3: Drinker Flushing & Evening Lock</span>
            </div>
          </div>
          <span class="status-pill pending">Pending</span>
        </div>

        <div class="team-member-row">
          <div class="team-user-flex">
            <div class="team-user-avatar" style="background:#fef3c7; color:#b45309;">EO</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Dr. Emeka Okonkwo</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Lead Vet: Sick Bay Pen S-1 Isolation</span>
            </div>
          </div>
          <span class="status-pill in-progress">In Progress</span>
        </div>
      </div>
    </div>

    <!-- Card 2: Flock Production Progress (Semi-Circular Donut Meter) -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Production Target</h3>
      </div>

      <div class="semi-circle-chart-box">
        <!-- SVG Semi Circle Donut Gauge -->
        <svg width="220" height="120" viewBox="0 0 220 120">
          <!-- Background Arc (Hatched/Gray) -->
          <path d="M 20 110 A 90 90 0 0 1 200 110" fill="none" stroke="#e2e8f0" stroke-width="24" stroke-linecap="round" />
          <!-- Mint Arc Segment -->
          <path d="M 20 110 A 90 90 0 0 1 180 60" fill="none" stroke="#34d399" stroke-width="24" stroke-linecap="round" stroke-dasharray="280" stroke-dashoffset="60" />
          <!-- Dark Green Completed Segment -->
          <path d="M 20 110 A 90 90 0 0 1 120 20" fill="none" stroke="#124e3f" stroke-width="24" stroke-linecap="round" />
        </svg>

        <div class="semi-circle-inner-value">
          <div class="big-val">87.8%</div>
          <div class="sub-val">Hen-Day Laying</div>
        </div>
      </div>

      <div class="chart-legend-row">
        <span><span class="legend-dot" style="background:#124e3f;"></span> Completed</span>
        <span><span class="legend-dot" style="background:#34d399;"></span> In Progress</span>
        <span><span class="legend-dot" style="background:#cbd5e1;"></span> Pending</span>
      </div>
    </div>

    <!-- Card 3: Shift Time Tracker (Dark Forest Green Wave Widget) -->
    <div class="time-tracker-card">
      <div class="card-title">Shift Time Tracker</div>
      
      <div class="digital-time-display" id="liveTimeTrackerDisplay">
        01:24:08
      </div>

      <div class="timer-controls-row">
        <button class="timer-control-btn pause" onclick="window.toggleTimer();" title="Pause / Resume Shift Timer">
          ⏸
        </button>
        <button class="timer-control-btn stop" onclick="window.stopTimer();" title="Stop & Log Shift Duration">
          ⏹
        </button>
      </div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/dashboard.html", "w") as f:
    f.write(wrap_donezo_page("Dashboard", "dashboard", dashboard_content))

# 2. index.html (Showcase Landing)
index_content = """
<div style="display:flex; flex-direction:column; gap:32px;">
  <div style="background:linear-gradient(135deg, #091f19, #0d382d); border-radius:24px; padding:36px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
    <div style="max-width:600px; display:flex; flex-direction:column; gap:12px;">
      <span style="font-size:0.75rem; font-family:var(--font-mono); color:#a7f3d0; text-transform:uppercase; font-weight:700;">✦ Commercial Layer Enterprise</span>
      <h1 style="color:#ffffff; font-size:2.4rem; font-family:var(--font-display); line-height:1.15;">Precisco Farm Ventures Ltd.</h1>
      <p style="color:#e2e8f0; font-size:0.95rem; line-height:1.5;">Personalized management dashboard for 6,000 Point-of-Lay birds, automated drinker systems, daily harvest sorting, and B2B corporate supply.</p>
      
      <div style="display:flex; gap:12px; margin-top:8px;">
        <a href="dashboard.html" class="btn-forest" style="background:#34d399; color:#06261d;">Open Personalized Dashboard &rarr;</a>
        <a href="sales.html" class="btn-outline-pill" style="background:transparent; color:#ffffff; border-color:rgba(255,255,255,0.3);">View Corporate Orders</a>
      </div>
    </div>

    <div class="glass-card" style="background:rgba(255,255,255,0.08); border-color:rgba(255,255,255,0.15); width:280px; padding:20px; border-radius:20px;">
      <span style="font-size:0.75rem; color:#a7f3d0; font-family:var(--font-mono);">FLOCK SUMMARY</span>
      <div style="font-size:2rem; font-weight:800; color:#fff; margin:6px 0;">5,892 Birds</div>
      <div style="font-size:0.75rem; color:#e2e8f0;">Laying Rate: <strong>87.8% Hen-Day</strong></div>
      <div style="font-size:0.75rem; color:#e2e8f0; margin-top:4px;">Today: <strong>172.4 Crates Produced</strong></div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:18px;">
    <a href="dashboard.html" class="donezo-card" style="text-decoration:none;">
      <span style="font-size:1.8rem;">📊</span>
      <h3 style="font-size:1.1rem; color:var(--text-main);">Personalized Dashboard</h3>
      <p style="font-size:0.8rem; color:var(--text-muted);">Master control room with key KPIs, laying analytics and shift timer.</p>
    </a>

    <a href="sales.html" class="donezo-card" style="text-decoration:none;">
      <span style="font-size:1.8rem;">💼</span>
      <h3 style="font-size:1.1rem; color:var(--text-main);">Corporate B2B Sales</h3>
      <p style="font-size:0.8rem; color:var(--text-muted);">Transcorp Hotels, Grand Delta Supermarket waybills & invoicing.</p>
    </a>

    <a href="operations.html" class="donezo-card" style="text-decoration:none;">
      <span style="font-size:1.8rem;">📋</span>
      <h3 style="font-size:1.1rem; color:var(--text-main);">3-Shift Checklists</h3>
      <p style="font-size:0.8rem; color:var(--text-muted);">Morning, Afternoon and Evening attendant SOP routines with sign-off.</p>
    </a>

    <a href="health.html" class="donezo-card" style="text-decoration:none;">
      <span style="font-size:1.8rem;">🩺</span>
      <h3 style="font-size:1.1rem; color:var(--text-main);">Health & Sick Bay</h3>
      <p style="font-size:0.8rem; color:var(--text-muted);">Daily mortality incineration and Sick Bay Pen S-1 isolation tracking.</p>
    </a>
  </div>
</div>
"""

with open(f"{base_dir}/index.html", "w") as f:
    f.write(wrap_donezo_page("Showcase", "showcase", index_content))

# 3. sales.html (Corporate B2B Sales)
sales_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Corporate B2B Sales & Invoicing</h1>
      <p>Manage bulk egg supply contracts, delivery waybills, and corporate receivables.</p>
    </div>

    <div class="dashboard-action-buttons">
      <button onclick="openModal('modalSalesOrder')" class="btn-forest">+ Create B2B Order</button>
      <button onclick="exportTableToCSV('Precisco_Sales.csv', [['Waybill','Customer','Crates','Total','Status'],['WB-104','Transcorp',120,516000,'14d Term']])" class="btn-outline-pill">Export CSV</button>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Total Invoiced</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">₦1.99M</div>
      <div class="m-footer-badge">470 Crates Dispatched</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Cash Collected</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">₦1.48M</div>
      <div class="m-footer-badge green-tag">Direct Bank Transfers</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Receivables Due</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b45309;">₦516,000</div>
      <div class="m-footer-badge" style="background:#fef3c7; color:#b45309;">Transcorp Hotels (14d)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Avg Crate Price</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">₦4,246</div>
      <div class="m-footer-badge green-tag">30-Egg Pulp Tray</div>
    </div>
  </div>

  <div class="data-table-container">
    <div class="data-table-header">
      <h3 style="font-size:1rem; font-weight:700;">Corporate Waybills & Delivery Ledger</h3>
      <span class="status-pill completed">B2B Traceability Active</span>
    </div>
    <table>
      <thead>
        <tr>
          <th>Waybill #</th>
          <th>Date</th>
          <th>Corporate Client</th>
          <th>Crates</th>
          <th>Total (₦)</th>
          <th>Paid (₦)</th>
          <th>Balance Due</th>
          <th>Status</th>
          <th>Delivery Vehicle</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:var(--forest-dark);">WB-PFV-2026-104</strong></td>
          <td>2026-08-18</td>
          <td><strong>Transcorp Hotels & Suites Ltd</strong></td>
          <td><strong>120 Crates</strong> (3,600 eggs)</td>
          <td>₦516,000</td>
          <td style="color:#15803d;">₦0</td>
          <td style="color:#b45309; font-weight:700;">₦516,000</td>
          <td><span class="status-pill pending">14-Day Term</span></td>
          <td>Toyota Dyna (DLT-892-XA)</td>
        </tr>
        <tr>
          <td><strong style="color:var(--forest-dark);">WB-PFV-2026-103</strong></td>
          <td>2026-08-17</td>
          <td><strong>Grand Delta Supermarkets Ltd</strong></td>
          <td><strong>200 Crates</strong> (6,000 eggs)</td>
          <td>₦850,000</td>
          <td style="color:#15803d; font-weight:700;">₦850,000</td>
          <td>₦0</td>
          <td><span class="status-pill completed">✓ Paid in Full</span></td>
          <td>Isuzu Truck (ASB-441-XX)</td>
        </tr>
        <tr>
          <td><strong style="color:var(--forest-dark);">WB-PFV-2026-102</strong></td>
          <td>2026-08-15</td>
          <td><strong>Royal Crown Confectioneries</strong></td>
          <td><strong>150 Crates</strong> (4,500 eggs)</td>
          <td>₦630,000</td>
          <td style="color:#15803d; font-weight:700;">₦630,000</td>
          <td>₦0</td>
          <td><span class="status-pill completed">✓ Paid in Full</span></td>
          <td>Ford Transit (BEN-119-AA)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

with open(f"{base_dir}/sales.html", "w") as f:
    f.write(wrap_donezo_page("Corporate B2B Sales", "sales", sales_content))

# 4. operations.html (3-Shift Checklists)
operations_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>3-Shift SOP Checklists & Handover</h1>
      <p>Morning (06:30), Afternoon (12:00), and Evening (17:30) operational routines.</p>
    </div>

    <button onclick="alert('Shift Checklists verified and locked by Farm Manager.');" class="btn-forest">✓ Supervisor Sign-Off</button>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
    <!-- Shift 1 -->
    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:12px;">
        <div>
          <h3 style="font-size:1.05rem;">Morning Shift (06:30 - 12:00)</h3>
          <span style="font-size:0.75rem; color:var(--text-muted);">Attendant: Chinedu Obi</span>
        </div>
        <span class="status-pill completed">10/10 Done</span>
      </div>

      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>1. Walkthrough inspection of 6,000 birds</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>2. Check mortality, remove to biohazard bin</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>3. Check drinker line pressure (2.2 Bar)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>4. Distribute morning feed (700 kg issued)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>5. Round 1 Harvest (08:30 AM - 3,164 eggs)</span></div>
    </div>

    <!-- Shift 2 -->
    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:12px;">
        <div>
          <h3 style="font-size:1.05rem;">Afternoon Shift (12:00 - 17:30)</h3>
          <span style="font-size:0.75rem; color:var(--text-muted);">Attendant: Blessing Eze</span>
        </div>
        <span class="status-pill completed">8/8 Done</span>
      </div>

      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>1. Asaba ambient heat stress check (29.6°C)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>2. Monitor Sick Bay Pen S-1 isolation</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>3. Round 2 Harvest (02:30 PM - 2,008 eggs)</span></div>
      <div class="checklist-item done"><input type="checkbox" checked disabled> <span>4. Grade & stack pulp trays in cold store</span></div>
    </div>

    <!-- Shift 3 -->
    <div class="donezo-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #edf2f7; padding-bottom:12px;">
        <div>
          <h3 style="font-size:1.05rem;">Evening Shift (17:30 - 20:30)</h3>
          <span style="font-size:0.75rem; color:var(--text-muted);">Attendant: Musa Ibrahim</span>
        </div>
        <span class="status-pill in-progress">In Progress</span>
      </div>

      <div class="checklist-item done"><input type="checkbox" checked> <span>1. Final flock demeanor check</span></div>
      <div class="checklist-item done"><input type="checkbox" checked> <span>2. Check 15,000L header tank valves</span></div>
      <div class="checklist-item"><input type="checkbox"> <span>3. Verify lighting timer (shutdown at 21:30)</span></div>
      <div class="checklist-item"><input type="checkbox"> <span>4. Lock and padlock pen doors</span></div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/operations.html", "w") as f:
    f.write(wrap_donezo_page("Shift Tasks", "operations", operations_content))

# 5. eggs.html (Twice-Daily Harvest)
eggs_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Twice-Daily Harvest & Crate Grading</h1>
      <p>Morning (08:30 AM) and Afternoon (02:30 PM) collections and 30-egg crate conversion.</p>
    </div>

    <div class="dashboard-action-buttons">
      <button onclick="openModal('modalEggHarvest')" class="btn-forest">+ Log Harvest Run</button>
      <button onclick="exportTableToCSV('Egg_Harvest.csv', [['Date','Round','Good','Cracked','Total','Trays'],['2026-08-19','Round 1',3120,22,3164,105.4]])" class="btn-outline-pill">Export CSV</button>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Total Today</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">5,172</div>
      <div class="m-footer-badge">172.4 Crates Produced</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Grade A Marketable</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">5,100</div>
      <div class="m-footer-badge green-tag">98.6% Marketability</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Hen-Day Laying</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">87.8%</div>
      <div class="m-footer-badge green-tag">5,892 Live Hens</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Cracked / Rejects</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b91c1c;">72</div>
      <div class="m-footer-badge" style="background:#fee2e2; color:#b91c1c;">Cracked: 37 • Broken: 12</div>
    </div>
  </div>

  <div class="data-table-container">
    <div class="data-table-header">
      <h3 style="font-size:1rem; font-weight:700;">Harvest Collection Logs</h3>
    </div>
    <table>
      <thead>
        <tr>
          <th>Date & Time</th>
          <th>Harvest Round</th>
          <th>Grade A Good</th>
          <th>Cracked</th>
          <th>Broken</th>
          <th>Rejects</th>
          <th>Total Eggs</th>
          <th>Trays (30-Egg)</th>
          <th>Hen-Day %</th>
          <th>Collector</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2026-08-19 • 08:30 AM</td>
          <td><strong>Morning Harvest (Round 1)</strong></td>
          <td style="color:#15803d; font-weight:700;">3,120</td>
          <td>22</td>
          <td>8</td>
          <td>14</td>
          <td><strong>3,164</strong></td>
          <td>105.4 Trays</td>
          <td style="color:#15803d; font-weight:700;">53.7%</td>
          <td>Chinedu Obi</td>
        </tr>
        <tr>
          <td>2026-08-19 • 02:30 PM</td>
          <td><strong>Afternoon Harvest (Round 2)</strong></td>
          <td style="color:#15803d; font-weight:700;">1,980</td>
          <td>15</td>
          <td>4</td>
          <td>9</td>
          <td><strong>2,008</strong></td>
          <td>66.9 Trays</td>
          <td style="color:#15803d; font-weight:700;">87.8% (Comb)</td>
          <td>Blessing Eze</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

with open(f"{base_dir}/eggs.html", "w") as f:
    f.write(wrap_donezo_page("Twice-Daily Harvest", "eggs", eggs_content))

# 6. flocks.html (Flocks)
flocks_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Flock PFV-LAY-001 Lifecycle</h1>
      <p>6,000 POL Layer Birds • Lohmann Brown Classic • 2026 Batch 1</p>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Live Birds</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">5,892</div>
      <div class="m-footer-badge">Initial: 6,000 POL</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Flock Age</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">34 Wks</div>
      <div class="m-footer-badge green-tag">Peak Laying Stage</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Cumulative Eggs</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">412,500</div>
      <div class="m-footer-badge green-tag">13,750 Crates Total</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Livability %</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">98.2%</div>
      <div class="m-footer-badge green-tag">Mortality: 108 birds</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/flocks.html", "w") as f:
    f.write(wrap_donezo_page("Flock Lifecycle", "flocks", flocks_content))

# 7. houses.html (House Climate)
houses_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Main House 1 & Climate Telemetry</h1>
      <p>Automated 3-tier battery cage system, 8 exhaust fans, 2.2 Bar drinker pressure.</p>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Temperature</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">29.6°C</div>
      <div class="m-footer-badge">Optimal (&lt;32.5°C)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Humidity</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">72%</div>
      <div class="m-footer-badge green-tag">Comfort Zone 65-80%</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Fans Active</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">7 / 8</div>
      <div class="m-footer-badge green-tag">Tunnel Flow Active</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Drinker Pressure</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">2.2 Bar</div>
      <div class="m-footer-badge green-tag">Automated Header Tank</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/houses.html", "w") as f:
    f.write(wrap_donezo_page("House Climate", "houses", houses_content))

# 8. financials.html (P&L Ledger)
financials_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Operating Expenses & P&L Ledger</h1>
      <p>Operating cost tracking, supplier purchase vouchers, and enterprise profitability (₦ Naira).</p>
    </div>

    <button onclick="window.print()" class="btn-forest">Print P&L Statement</button>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">B2B Revenue</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">₦1.99M</div>
      <div class="m-footer-badge">470 Crates Sold</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Operating Expenses</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b91c1c;">₦6.74M</div>
      <div class="m-footer-badge" style="background:#fee2e2; color:#b91c1c;">Feed, Power, Wages</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Gross Margin</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">42.5%</div>
      <div class="m-footer-badge green-tag">Egg Sales Margin</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Feed Cost Share</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">68.5%</div>
      <div class="m-footer-badge green-tag">Dominant Cost Factor</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/financials.html", "w") as f:
    f.write(wrap_donezo_page("P&L Ledger", "financials", financials_content))

# 9. health.html (Health & Sick Bay)
health_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Health, Mortality & Sick Bay Isolation</h1>
      <p>Daily mortality logs, Sick Bay Pen S-1 isolation, and drug withdrawal safety locks.</p>
    </div>

    <button onclick="openModal('modalMortality')" class="btn-forest" style="background:var(--rose-dark);">☠️ Record Mortality</button>
  </div>

  <div class="data-table-container">
    <div class="data-table-header">
      <h3 style="font-size:1rem; font-weight:700;">Sick Bay Isolation Pen (Active Care)</h3>
      <span class="status-pill in-progress">1 Bird in Isolation</span>
    </div>
    <table>
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
          <td>Respiratory stress</td>
          <td>Sick Bay Pen S-1</td>
          <td>Oral Multivitamins + Electrolytes</td>
          <td>Chinedu Obi</td>
          <td><button onclick="alert('Bird tagged recovered and returned to Tier 2.');" class="btn-forest" style="padding:4px 10px; font-size:0.75rem;">Mark Recovered</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

with open(f"{base_dir}/health.html", "w") as f:
    f.write(wrap_donezo_page("Health & Sick Bay", "health", health_content))

# 10. feed.html (Feed Intake)
feed_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Feed Intake & Water Line System</h1>
      <p>Daily feed consumption vs 118g benchmark for 6,000 birds and Days-of-Feed forecast.</p>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Consumed Today</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">685 kg</div>
      <div class="m-footer-badge">Issued 700 kg • Left 15 kg</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Actual Intake</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">116.3 g</div>
      <div class="m-footer-badge green-tag">Target: 118g Optimal</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Warehouse Stock</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">157 Bags</div>
      <div class="m-footer-badge green-tag">25kg Layers Mash</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Days Remaining</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">6 Days</div>
      <div class="m-footer-badge green-tag">Safe Buffer (>5d)</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/feed.html", "w") as f:
    f.write(wrap_donezo_page("Feed & Water", "feed", feed_content))

# 11. inventory.html
inventory_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Warehouse Inventory & Supplies</h1>
      <p>Feed bags, 30-egg stored crates, veterinary vaccines and packaging inventory.</p>
    </div>
  </div>

  <div class="data-table-container">
    <div class="data-table-header">
      <h3 style="font-size:1rem; font-weight:700;">Inventory Ledger</h3>
    </div>
    <table>
      <thead>
        <tr>
          <th>Category</th>
          <th>Item</th>
          <th>In Stock</th>
          <th>Min Buffer</th>
          <th>Unit Cost</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="status-pill completed">Feed</span></td>
          <td><strong>Layers Mash Phase 1 (25kg Bags)</strong></td>
          <td><strong>157 Bags</strong></td>
          <td>45 Bags</td>
          <td>₦18,500</td>
          <td>Warehouse Bay 1</td>
        </tr>
        <tr>
          <td><span class="status-pill in-progress">Eggs</span></td>
          <td><strong>Grade A Marketable Stored Crates</strong></td>
          <td><strong>485 Crates</strong></td>
          <td>100 Crates</td>
          <td>₦4,300</td>
          <td>Egg Cold Room (18°C)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

with open(f"{base_dir}/inventory.html", "w") as f:
    f.write(wrap_donezo_page("Warehouse", "inventory", inventory_content))

# 12. tasks.html
tasks_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Tasks & SOP Operational Manual</h1>
      <p>Standard operating procedure library implementing the 5-Question Framework.</p>
    </div>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:18px;">
    <div class="donezo-card">
      <span class="status-pill completed">Daily Task</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">Morning 6,000 Bird Walkthrough & Harvest</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Responsible: Chinedu Obi • Evidence: Shift 1 Checklist</p>
    </div>
    <div class="donezo-card">
      <span class="status-pill in-progress">Weekly Task</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">Drinker Line Descaling & Citric Flush</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Responsible: Musa Ibrahim • Evidence: Water Record</p>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/tasks.html", "w") as f:
    f.write(wrap_donezo_page("Tasks & SOPs", "tasks", tasks_content))

# 13. biosecurity.html
biosecurity_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Gate 1 Wheel Spray Dip & Visitor Log</h1>
      <p>Enforced 24/7 by Sgt. Joshua Garba & Sunday Alabi (2 Security Officers).</p>
    </div>
  </div>

  <div class="data-table-container">
    <div class="data-table-header">
      <h3 style="font-size:1rem; font-weight:700;">Security Gate Registry</h3>
      <span class="status-pill completed">Audit Grade A</span>
    </div>
    <table>
      <thead>
        <tr>
          <th>Date & Time</th>
          <th>Visitor Name & Org</th>
          <th>Purpose</th>
          <th>Checks Passed</th>
          <th>Security Officer</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2026-08-18 • 09:30 AM</td>
          <td><strong>Engr. Patrick Agbo (Delta Ministry of Ag)</strong></td>
          <td>Biosecurity Audit</td>
          <td><span class="status-pill completed">✓ Wheel Dip • 48h Clear</span></td>
          <td>Sgt. Joshua Garba</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

with open(f"{base_dir}/biosecurity.html", "w") as f:
    f.write(wrap_donezo_page("Gate Biosecurity", "biosecurity", biosecurity_content))

# 14. reports.html
reports_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Performance Reports & Analytics</h1>
      <p>Weekly Hen-Day laying curve, FCR per dozen, egg sales revenue, and mortality analysis.</p>
    </div>

    <button onclick="window.print()" class="btn-forest">Print Report</button>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">7-Day Harvest</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">36,204</div>
      <div class="m-footer-badge">1,206.8 Crates</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Avg Hen-Day</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">87.5%</div>
      <div class="m-footer-badge green-tag">Benchmark 88.5%</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">FCR / Dozen</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">1.59</div>
      <div class="m-footer-badge green-tag">kg feed/doz</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">7-Day Livability</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">99.7%</div>
      <div class="m-footer-badge green-tag">19 mortalities total</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/reports.html", "w") as f:
    f.write(wrap_donezo_page("Analytics & Reports", "reports", reports_content))

# 15. alerts.html
alerts_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Alert Engine & Incident Center</h1>
      <p>Automated rule engine monitoring mortality spikes, heat stress, and food safety holds.</p>
    </div>
  </div>

  <div class="donezo-card" style="border-left:4px solid var(--rose-dark);">
    <span class="status-pill pending">CRITICAL HEALTH ALERT</span>
    <h3 style="font-size:1.1rem; margin-top:8px;">Mortality Count: 3 Dead Birds in Main House 1</h3>
    <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Recorded mortality requires post-mortem examination. On-farm incineration executed per SOP-BIO-004.</p>
  </div>
</div>
"""

with open(f"{base_dir}/alerts.html", "w") as f:
    f.write(wrap_donezo_page("Alert Engine", "alerts", alerts_content))

# 16. settings.html
settings_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Farm Settings, SOP Thresholds & RBAC</h1>
      <p>Configurable limits, unit economics (₦), and staff role directories.</p>
    </div>

    <button onclick="farmStore.reset();" class="btn-outline-pill">Reset Demo Data</button>
  </div>

  <div class="donezo-card">
    <h3 style="font-size:1.05rem; margin-bottom:14px;">Configurable SOP Thresholds</h3>
    <div class="form-row-2">
      <div class="form-group"><label class="form-label">Max Daily Mortality / Pen</label><input type="number" value="6" readonly></div>
      <div class="form-group"><label class="form-label">Max House Temp (°C)</label><input type="number" value="32.5" readonly></div>
      <div class="form-group"><label class="form-label">Expected Daily Feed (g/bird)</label><input type="number" value="118" readonly></div>
      <div class="form-group"><label class="form-label">30-Egg Tray Price (₦)</label><input type="number" value="4300" readonly></div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/settings.html", "w") as f:
    f.write(wrap_donezo_page("Settings", "settings", settings_content))

# 17. pages.html
pages_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Single-Click Page Navigator Directory</h1>
      <p>Click any card below to navigate directly to that dedicated page.</p>
    </div>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:18px;">
    <a href="dashboard.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Master Control</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">1. Personalized Dashboard</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Donezo-styled master dashboard with laying analytics, capsule chart & time tracker.</p>
    </a>

    <a href="sales.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">B2B Revenue</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">2. Corporate B2B Sales</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Hotels and supermarkets bulk waybills, orders and receivables.</p>
    </a>

    <a href="operations.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill in-progress">3 Shifts</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">3. Daily Shift Checklists</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Morning, Afternoon and Evening shifts with supervisor approvals.</p>
    </a>

    <a href="eggs.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill in-progress">Twice-Daily</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">4. Egg Harvest & Crate Grading</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Morning & afternoon harvests, Grade A vs cracked sorting.</p>
    </a>

    <a href="flocks.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Traceability</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">5. Flock PFV-LAY-001</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">6,000 POL layer records, age 34 wks peak, Lohmann Brown.</p>
    </a>

    <a href="houses.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Climate</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">6. Main House 1 & Fans</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">3-tier cages, 8 exhaust fans, 2.2 Bar drinker pressure.</p>
    </a>

    <a href="financials.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Accounting</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">7. Operating Expenses & P&L</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">General ledger, feed costs, generator diesel, and margins.</p>
    </a>

    <a href="health.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill pending">Veterinary</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">8. Health, Mortality & Sick Bay</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Mortality logging, Sick Bay Pen S-1 isolation and Rx hold.</p>
    </a>

    <a href="feed.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Nutrition</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">9. Feed Intake & Water</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">118g benchmark and Days of Feed remaining forecast.</p>
    </a>

    <a href="inventory.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Warehouse</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">10. Warehouse Inventory</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Feed bags, cold room egg crates, and vaccine cold chain.</p>
    </a>

    <a href="tasks.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">5-Q Rule</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">11. Tasks & SOP Manual</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Standard operating procedures and recurring task schedule.</p>
    </a>

    <a href="biosecurity.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">24/7 Gate</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">12. Gate Biosecurity Registry</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Gate 1 truck wheel spray dip, 48h screening and logs.</p>
    </a>

    <a href="reports.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Analytics</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">13. Executive Reports</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Hen-Day curve, FCR per dozen, and Print/CSV export.</p>
    </a>

    <a href="alerts.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill pending">Incident</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">14. Alert Engine</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Mortality threshold and heat stress automated escalation.</p>
    </a>

    <a href="settings.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Config</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">15. Settings & RBAC</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Farm parameters, pricing (₦), and staff role directories.</p>
    </a>

    <a href="index.html" class="donezo-card" style="text-decoration:none;">
      <span class="status-pill completed">Brand</span>
      <h3 style="font-size:1.1rem; margin-top:8px;">16. Brand Showcase</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Commercial showcase and enterprise overview.</p>
    </a>
  </div>
</div>
"""

with open(f"{base_dir}/pages.html", "w") as f:
    f.write(wrap_donezo_page("All 16 Pages Directory", "pages", pages_content))

print("All Donezo-styled pages built successfully!")
