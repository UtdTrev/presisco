import os
from generate_pages import wrap_donezo_page

base_dir = "/home/user/precisco-portal"

# 1. dashboard.html
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
        <span>+ Log Harvest (Size Derivatives)</span>
      </button>
      <button onclick="openModal('modalSalesOrder')" class="btn-outline-pill">
        <span>+ B2B Order</span>
      </button>
      <button onclick="window.print()" class="btn-outline-pill">
        <span>Export Data</span>
      </button>
    </div>
  </div>

  <!-- 4 Metric Cards -->
  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Total POL Birds</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">5,892</div>
      <div class="m-footer-badge">↑ 98.2% Livability from arrival</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Harvest Today</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">5,172</div>
      <div class="m-footer-badge green-tag">↑ 172.4 Crates (101 Large, 61 Med)</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Hen-Day Laying</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">87.8%</div>
      <div class="m-footer-badge green-tag">↑ Peak Target 88.5%</div>
    </div>

    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Days of Feed (80-100g)</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">7.0 Days</div>
      <div class="m-footer-badge green-tag" style="background:#f1f5f9; color:#64748b;">157 Bags Warehouse Buffer</div>
    </div>
  </div>

  <!-- 80-100g Feed Deduction Engine Card -->
  <div class="donezo-card">
    <div class="card-header-donezo">
      <h3>Feed Deduction Engine (80g - 100g Daily Requirement per Bird)</h3>
      <span class="status-pill completed">Live Flock: 5,892 Birds</span>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:14px; margin-top:8px;">
      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.75rem; color:#64748b; display:block;">Daily Consumption (95g)</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">559.7 kg</strong>
        <span style="font-size:0.7rem; color:#64748b;">22.4 Bags of 25kg</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.75rem; color:#64748b; display:block;">Weekly Requirement</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">3,918 kg</strong>
        <span style="font-size:0.7rem; color:#64748b;">156.7 Bags (₦2.90M)</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; border-radius:12px;">
        <span style="font-size:0.75rem; color:#64748b; display:block;">Monthly Requirement</span>
        <strong style="font-size:1.3rem; color:#124e3f; display:block;">16,792 kg</strong>
        <span style="font-size:0.7rem; color:#64748b;">671.7 Bags (₦12.42M)</span>
      </div>

      <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; border-radius:12px;">
        <span style="font-size:0.75rem; color:#166534; display:block;">Re-Order Level (ROL)</span>
        <strong style="font-size:1.3rem; color:#15803d; display:block;">55 Bags</strong>
        <span style="font-size:0.7rem; color:#166534;">MOQ: <strong>200 Bags</strong> • EOQ: <strong>553 Bags</strong></span>
      </div>
    </div>
  </div>

  <!-- Middle 3-Column Grid -->
  <div class="dashboard-middle-grid">
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Laying Analytics</h3>
      </div>

      <div class="pill-chart-container">
        <div class="pill-bar-col"><div class="pill-bar hatched" style="height: 65px;"></div><span class="pill-bar-day">S</span></div>
        <div class="pill-bar-col"><div class="pill-bar solid-green" style="height: 95px;"></div><span class="pill-bar-day">M</span></div>
        <div class="pill-bar-col"><div class="pill-bar mint-green" style="height: 75px;"><div class="pill-bar-tooltip">87.8%</div></div><span class="pill-bar-day">T</span></div>
        <div class="pill-bar-col"><div class="pill-bar solid-green" style="height: 105px;"></div><span class="pill-bar-day">W</span></div>
        <div class="pill-bar-col"><div class="pill-bar hatched" style="height: 60px;"></div><span class="pill-bar-day">T</span></div>
        <div class="pill-bar-col"><div class="pill-bar hatched" style="height: 70px;"></div><span class="pill-bar-day">F</span></div>
        <div class="pill-bar-col"><div class="pill-bar hatched" style="height: 80px;"></div><span class="pill-bar-day">S</span></div>
      </div>
    </div>

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
              <span style="font-size:0.72rem; color:var(--text-muted);">80 Large + 40 Medium Crates</span>
            </div>
          </div>
          <span class="status-pill pending" style="font-size:0.65rem;">14d Term</span>
        </div>

        <div class="project-item-row">
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="project-icon-box" style="background:#dcfce7; color:#16a34a;">🛒</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Grand Delta Supermarket (200 Crates)</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">100 Large + 100 Medium Crates</span>
            </div>
          </div>
          <span class="status-pill completed" style="font-size:0.65rem;">Paid</span>
        </div>

        <div class="project-item-row">
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="project-icon-box" style="background:#fef3c7; color:#d97706;">🍞</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Royal Crown Bakeries (150 Crates)</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">50 Large + 100 Medium Crates</span>
            </div>
          </div>
          <span class="status-pill completed" style="font-size:0.65rem;">Paid</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom 3-Column Grid -->
  <div class="dashboard-bottom-grid">
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Team Collaboration</h3>
        <button onclick="alert('Staff Duty Schedule active.');" class="btn-outline-pill" style="padding:4px 12px; font-size:0.75rem;">+ Schedule</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:4px;">
        <div class="team-member-row">
          <div class="team-user-flex">
            <div class="team-user-avatar" style="background:#fee2e2; color:#b91c1c;">CO</div>
            <div>
              <strong style="font-size:0.82rem; color:var(--text-main); display:block;">Chinedu Obi</strong>
              <span style="font-size:0.72rem; color:var(--text-muted);">Shift 1: Morning Harvest (3,164 Eggs)</span>
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
              <span style="font-size:0.72rem; color:var(--text-muted);">Shift 3: Manure Scraper & Evening Lock</span>
            </div>
          </div>
          <span class="status-pill pending">Pending</span>
        </div>
      </div>
    </div>

    <!-- Semi Circular Arc Progress Meter -->
    <div class="donezo-card">
      <div class="card-header-donezo">
        <h3>Production Target</h3>
      </div>

      <div class="semi-circle-chart-box">
        <svg width="220" height="120" viewBox="0 0 220 120">
          <path d="M 20 110 A 90 90 0 0 1 200 110" fill="none" stroke="#e2e8f0" stroke-width="24" stroke-linecap="round" />
          <path d="M 20 110 A 90 90 0 0 1 180 60" fill="none" stroke="#34d399" stroke-width="24" stroke-linecap="round" stroke-dasharray="280" stroke-dashoffset="60" />
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

    <!-- Time Tracker Widget -->
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

# 2. feed.html
feed_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Feed Intake & Inventory Optimization (EOQ/ROL)</h1>
      <p>Deduction engine based on 80g - 100g intake per bird for 5,892 mature layers.</p>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Daily Consumption</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">559.7 kg</div>
      <div class="m-footer-badge">22.4 Bags/day @ 95g/bird</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Weekly Requirement</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#124e3f;">3,918 kg</div>
      <div class="m-footer-badge green-tag">156.7 Bags (₦2.90M)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Monthly Total</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#124e3f;">16,792 kg</div>
      <div class="m-footer-badge green-tag">671.7 Bags (₦12.42M)</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Economic Order (EOQ)</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">553 Bags</div>
      <div class="m-footer-badge green-tag">ROL: 55 Bags • MOQ: 200 Bags</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/feed.html", "w") as f:
    f.write(wrap_donezo_page("Feed & Water", "feed", feed_content))

# 3. eggs.html
eggs_content = """
<div style="display:flex; flex-direction:column; gap:24px;">
  <div class="dashboard-header-row">
    <div class="dashboard-header-title">
      <h1>Twice-Daily Harvest & Egg Size Grading</h1>
      <p>Grade A Large (53-63g+), Medium (45-52g), Small Pullet (&lt;45g), and Hairline Cracked segregation.</p>
    </div>

    <div class="dashboard-action-buttons">
      <button onclick="openModal('modalEggHarvest')" class="btn-forest">+ Log Graded Harvest</button>
      <button onclick="exportTableToCSV('Graded_Egg_Harvest.csv', [['Date','Round','Large','Medium','Small','Cracked','Total'],['2026-08-19','Round 1',1850,1120,150,22,3164]])" class="btn-outline-pill">Export CSV</button>
    </div>
  </div>

  <div class="metrics-row-4">
    <div class="metric-box-donezo highlight-forest">
      <div class="m-header-flex"><span class="m-title">Large Crates (53-63g+)</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number">101.0 Cr</div>
      <div class="m-footer-badge">Premium Hotel Rate ₦4,500/cr</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Medium Crates (45-52g)</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#15803d;">61.0 Cr</div>
      <div class="m-footer-badge green-tag">Supermarket Rate ₦4,300/cr</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Small Pullet Crates</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#d97706;">8.0 Cr</div>
      <div class="m-footer-badge" style="background:#fef3c7; color:#b45309;">Bakery Rate ₦3,800/cr</div>
    </div>
    <div class="metric-box-donezo white-card">
      <div class="m-header-flex"><span class="m-title">Cracked / Rejects</span><div class="m-arrow-btn">↗</div></div>
      <div class="m-number" style="color:#b91c1c;">2.4 Cr</div>
      <div class="m-footer-badge" style="background:#fee2e2; color:#b91c1c;">Cracked: 37 • Broken: 12</div>
    </div>
  </div>
</div>
"""

with open(f"{base_dir}/eggs.html", "w") as f:
    f.write(wrap_donezo_page("Twice-Daily Harvest", "eggs", eggs_content))

print("All Donezo pages updated with feed calculations and egg derivatives!")
