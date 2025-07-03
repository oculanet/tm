<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RailTrack Pro - Train Maintenance Planner</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --primary: #1a3a6d;
            --secondary: #2c5282;
            --accent: #f59e0b;
            --light: #e2e8f0;
            --dark: #1a202c;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --gray: #718096;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e3a8a);
            color: var(--light);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 2px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 30px;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .logo h1 {
            font-weight: 700;
            font-size: 2.2rem;
            background: linear-gradient(to right, var(--accent), #ffdd00);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        .logo-icon {
            width: 50px;
            height: 50px;
            background: var(--accent);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: var(--dark);
        }
        
        .controls {
            display: flex;
            gap: 15px;
        }
        
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
        }
        
        .btn-primary {
            background: var(--accent);
            color: var(--dark);
        }
        
        .btn-primary:hover {
            background: #e69008;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: var(--secondary);
            color: white;
        }
        
        .btn-secondary:hover {
            background: #2a4365;
            transform: translateY(-2px);
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .sidebar {
            background: rgba(30, 41, 59, 0.7);
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .panel-title {
            font-size: 1.4rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--accent);
            color: var(--accent);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .form-control {
            width: 100%;
            padding: 12px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            color: white;
            font-size: 16px;
        }
        
        .form-control:focus {
            outline: none;
            border-color: var(--accent);
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
        }
        
        .card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .card-full {
            grid-column: 1 / -1;
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .card-title {
            font-size: 1.3rem;
            color: var(--accent);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        
        .stat-card {
            background: rgba(15, 23, 42, 0.5);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(15, 23, 42, 0.7);
        }
        
        .stat-value {
            font-size: 2.2rem;
            font-weight: 700;
            margin: 10px 0;
            color: var(--accent);
        }
        
        .stat-label {
            font-size: 1rem;
            color: var(--gray);
        }
        
        .train-list {
            max-height: 400px;
            overflow-y: auto;
        }
        
        .train-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            background: rgba(15, 23, 42, 0.3);
            border-radius: 8px;
            margin-bottom: 12px;
            transition: all 0.3s ease;
        }
        
        .train-item:hover {
            background: rgba(15, 23, 42, 0.5);
            transform: translateX(5px);
        }
        
        .train-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .train-icon {
            width: 40px;
            height: 40px;
            background: var(--secondary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }
        
        .train-name {
            font-weight: 500;
        }
        
        .train-miles {
            font-size: 0.9rem;
            color: var(--gray);
        }
        
        .status-badge {
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
        }
        
        .status-operational {
            background: rgba(16, 185, 129, 0.2);
            color: var(--success);
        }
        
        .status-maintenance {
            background: rgba(239, 68, 68, 0.2);
            color: var(--danger);
        }
        
        .status-warning {
            background: rgba(245, 158, 11, 0.2);
            color: var(--warning);
        }
        
        .chart-container {
            height: 300px;
            position: relative;
            margin-top: 20px;
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .tab {
            padding: 8px 20px;
            border-radius: 30px;
            background: rgba(15, 23, 42, 0.5);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .tab.active {
            background: var(--accent);
            color: var(--dark);
            font-weight: 500;
        }
        
        .simulation-controls {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        
        footer {
            text-align: center;
            padding: 30px 0;
            color: var(--gray);
            font-size: 0.9rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            margin-top: 30px;
        }
        
        .pagination {
            display: flex;
            justify-content: center;
            margin-top: 20px;
            gap: 10px;
        }
        
        .pagination button {
            padding: 8px 15px;
            background: var(--secondary);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .pagination button.active {
            background: var(--accent);
            color: var(--dark);
        }
        
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .data-table th, .data-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .data-table th {
            color: var(--accent);
            font-weight: 600;
        }
        
        .data-table tr:hover {
            background: rgba(15, 23, 42, 0.3);
        }
        
        @media (max-width: 1100px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                <div class="logo-icon">🚂</div>
                <h1>RailTrack Pro</h1>
            </div>
            <div class="controls">
                <button class="btn btn-primary" id="reportBtn">
                    <i>📊</i> Generate Report
                </button>
                <button class="btn btn-secondary" id="settingsBtn">
                    <i>⚙️</i> Settings
                </button>
            </div>
        </header>
        
        <div class="main-content">
            <div class="sidebar">
                <h2 class="panel-title">
                    <i>📝</i> Maintenance Control
                </h2>
                
                <div class="form-group">
                    <label for="dailyMileage">Daily Mileage (miles)</label>
                    <input type="number" id="dailyMileage" class="form-control" value="280" min="50" max="500">
                </div>
                
                <div class="form-group">
                    <label for="staffInput">Staff Availability</label>
                    <input type="number" id="staffInput" class="form-control" value="5" min="1" max="30">
                </div>
                
                <div class="form-group">
                    <label for="tracksInput">Maintenance Tracks</label>
                    <input type="number" id="tracksInput" class="form-control" value="3" min="1" max="10">
                </div>
                
                <div class="form-group">
                    <label for="trainSelect">Select Train</label>
                    <select id="trainSelect" class="form-control">
                        <option value="">-- All Trains --</option>
                        <!-- Train options populated by JS -->
                    </select>
                </div>
                
                <button class="btn btn-primary" id="simulateBtn" style="width:100%; margin-top:20px;">
                    <i>⏱️</i> Simulate 7 Days
                </button>
                
                <div class="simulation-controls">
                    <button class="btn btn-secondary" style="flex:1;" id="startSimBtn">
                        <i>▶️</i> Start Simulation
                    </button>
                    <button class="btn btn-secondary" style="flex:1;" id="pauseSimBtn" disabled>
                        <i>⏸️</i> Pause
                    </button>
                </div>
                
                <div style="margin-top: 30px; background: rgba(245, 158, 11, 0.1); padding: 15px; border-radius: 8px; border-left: 3px solid var(--accent);">
                    <h3 style="color: var(--accent); margin-bottom: 10px;">Maintenance Schedule</h3>
                    <p>Maintenance intervals (miles):</p>
                    <ul style="margin-top: 10px; margin-left: 20px;">
                        <li>19,000</li>
                        <li>38,000</li>
                        <li>76,000</li>
                        <li>95,000</li>
                        <li>152,000</li>
                        <li>306,000</li>
                    </ul>
                    <p style="margin-top: 10px;">Critical maintenance if overdue by more than 5,000 miles</p>
                </div>
            </div>
            
            <div class="dashboard">
                <div class="card card-full">
                    <div class="card-header">
                        <h2 class="card-title">Mileage & Maintenance Overview</h2>
                        <div class="tabs">
                            <div class="tab active" data-period="daily">Daily</div>
                            <div class="tab" data-period="weekly">Weekly</div>
                            <div class="tab" data-period="monthly">Monthly</div>
                        </div>
                    </div>
                    <div class="chart-container">
                        <canvas id="mileageChart"></canvas>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Resource Allocation</h2>
                    </div>
                    <div class="chart-container">
                        <canvas id="resourceChart"></canvas>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Maintenance Forecast</h2>
                    </div>
                    <div class="chart-container">
                        <canvas id="forecastChart"></canvas>
                    </div>
                </div>
                
                <div class="card card-full">
                    <div class="card-header">
                        <h2 class="card-title">System Status</h2>
                    </div>
                    <div class="stats-grid" id="statsGrid">
                        <!-- Stats populated by JS -->
                    </div>
                </div>
                
                <div class="card card-full">
                    <div class="card-header">
                        <h2 class="card-title">Maintenance Priority List</h2>
                    </div>
                    <div class="train-list" id="priorityList">
                        <!-- Priority list populated by JS -->
                    </div>
                </div>
                
                <div class="card card-full">
                    <div class="card-header">
                        <h2 class="card-title">Fleet Maintenance Schedule</h2>
                    </div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Train ID</th>
                                <th>Current Mileage</th>
                                <th>Last Maintenance</th>
                                <th>Next Maintenance</th>
                                <th>Overdue</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody id="scheduleTable">
                            <!-- Table rows populated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <footer>
            <p>RailTrack Pro Maintenance Planning System | Real-time Monitoring & Predictive Maintenance</p>
            <p>© 2023 Rail Operations Management. All rights reserved.</p>
        </footer>
    </div>
    
    <script>
        // Train data from fleet.csv
        const fleetData = [
            { id: '5101', currentMileage: 298996, lastMaintenance: '38K', lastMaintenanceMileage: 293996 },
            { id: '5102', currentMileage: 297761, lastMaintenance: '19K', lastMaintenanceMileage: 292761 },
            { id: '5103', currentMileage: 277071, lastMaintenance: '38K', lastMaintenanceMileage: 272071 },
            { id: '5104', currentMileage: 390161, lastMaintenance: '19K', lastMaintenanceMileage: 385161 },
            { id: '5105', currentMileage: 397647, lastMaintenance: '38K', lastMaintenanceMileage: 392647 },
            { id: '5106', currentMileage: 294403, lastMaintenance: '19K', lastMaintenanceMileage: 289403 },
            { id: '5107', currentMileage: 360470, lastMaintenance: '38K', lastMaintenanceMileage: 355470 },
            { id: '5108', currentMileage: 326387, lastMaintenance: '19K', lastMaintenanceMileage: 321387 },
            { id: '5109', currentMileage: 341564, lastMaintenance: '38K', lastMaintenanceMileage: 336564 },
            { id: '5110', currentMileage: 342183, lastMaintenance: '19K', lastMaintenanceMileage: 337183 },
            { id: '5111', currentMileage: 454073, lastMaintenance: '38K', lastMaintenanceMileage: 449073 },
            { id: '5112', currentMileage: 375541, lastMaintenance: '19K', lastMaintenanceMileage: 370541 },
            { id: '5113', currentMileage: 426083, lastMaintenance: '38K', lastMaintenanceMileage: 421083 },
            { id: '5114', currentMileage: 392964, lastMaintenance: '19K', lastMaintenanceMileage: 387964 },
            { id: '5115', currentMileage: 361432, lastMaintenance: '38K', lastMaintenanceMileage: 356432 }
        ];
        
        // Maintenance types from maintenance_types.csv
        const maintenanceTypes = [
            { name: '19K', gap: 19000, requiredHours: 10, lmtUtilization: 10, hmtUtilization: 0, wheelTrackUtilization: 0, tolerance: '10%' },
            { name: '38K', gap: 38000, requiredHours: 30, lmtUtilization: 25, hmtUtilization: 5, wheelTrackUtilization: 0, tolerance: '10%' },
            { name: '76K', gap: 76000, requiredHours: 50, lmtUtilization: 25, hmtUtilization: 10, wheelTrackUtilization: 15, tolerance: '5%' }
        ];
        
        // Staff data from staff.csv
        const staffData = { totalStaff: 5, hoursPerDay: 9 };
        
        // Initialize trains with calculated next maintenance
        const trains = fleetData.map(train => {
            // Maintenance intervals in miles
            const intervals = [19000, 38000, 76000, 95000, 152000, 306000];
            
            // Find the next maintenance interval
            let nextMaintenance = null;
            for (let interval of intervals) {
                if (interval > train.lastMaintenanceMileage) {
                    nextMaintenance = interval;
                    break;
                }
            }
            
            // If we didn't find one, set to last interval + 76k
            if (!nextMaintenance) {
                nextMaintenance = intervals[intervals.length - 1] + 76000;
            }
            
            // Calculate overdue
            const overdue = Math.max(0, train.currentMileage - nextMaintenance);
            
            // Determine status
            let status;
            if (overdue > 5000) {
                status = 'Critical';
            } else if (overdue > 0) {
                status = 'Overdue';
            } else {
                const milesLeft = nextMaintenance - train.currentMileage;
                status = milesLeft < 5000 ? 'Due Soon' : 'Operational';
            }
            
            return {
                ...train,
                nextMaintenance,
                overdue,
                status
            };
        });
        
        // Initialize charts
        let mileageChart, resourceChart, forecastChart;
        
        // DOM elements
        const trainSelect = document.getElementById('trainSelect');
        const priorityList = document.getElementById('priorityList');
        const scheduleTable = document.getElementById('scheduleTable');
        const statsGrid = document.getElementById('statsGrid');
        const simulateBtn = document.getElementById('simulateBtn');
        const reportBtn = document.getElementById('reportBtn');
        const settingsBtn = document.getElementById('settingsBtn');
        const startSimBtn = document.getElementById('startSimBtn');
        const pauseSimBtn = document.getElementById('pauseSimBtn');
        const tabs = document.querySelectorAll('.tab');
        const dailyMileageInput = document.getElementById('dailyMileage');
        
        // Populate train select dropdown
        trains.forEach(train => {
            const option = document.createElement('option');
            option.value = train.id;
            option.textContent = `T${train.id}`;
            trainSelect.appendChild(option);
        });
        
        // Populate priority list
        function updatePriorityList() {
            priorityList.innerHTML = '';
            
            // Sort trains by maintenance priority (overdue first)
            const sortedTrains = [...trains].sort((a, b) => b.overdue - a.overdue);
            
            // Display top 10 priority trains
            sortedTrains.slice(0, 10).forEach(train => {
                const item = document.createElement('div');
                item.className = 'train-item';
                
                let statusClass, statusText;
                if (train.overdue > 5000) {
                    statusClass = 'status-maintenance';
                    statusText = `CRITICAL: Overdue by ${(train.overdue/1000).toFixed(1)}k miles`;
                } else if (train.overdue > 0) {
                    statusClass = 'status-warning';
                    statusText = `OVERDUE: ${(train.overdue/1000).toFixed(1)}k miles`;
                } else {
                    const milesLeft = train.nextMaintenance - train.currentMileage;
                    statusClass = milesLeft < 5000 ? 'status-warning' : 'status-operational';
                    statusText = milesLeft < 5000 
                        ? `DUE SOON: ${(milesLeft/1000).toFixed(1)}k miles left` 
                        : `Next: ${(train.nextMaintenance/1000).toFixed(0)}k miles`;
                }
                
                item.innerHTML = `
                    <div class="train-info">
                        <div class="train-icon">🚂</div>
                        <div>
                            <div class="train-name">T${train.id}</div>
                            <div class="train-miles">Current: ${(train.currentMileage/1000).toFixed(1)}k miles</div>
                        </div>
                    </div>
                    <div>
                        <span class="status-badge ${statusClass}">${statusText}</span>
                    </div>
                `;
                priorityList.appendChild(item);
            });
        }
        
        // Populate schedule table
        function updateScheduleTable() {
            scheduleTable.innerHTML = '';
            
            trains.forEach(train => {
                const row = document.createElement('tr');
                
                let statusClass, statusText;
                if (train.overdue > 5000) {
                    statusClass = 'status-maintenance';
                    statusText = 'Critical';
                } else if (train.overdue > 0) {
                    statusClass = 'status-warning';
                    statusText = 'Overdue';
                } else {
                    const milesLeft = train.nextMaintenance - train.currentMileage;
                    statusClass = milesLeft < 5000 ? 'status-warning' : 'status-operational';
                    statusText = milesLeft < 5000 ? 'Due Soon' : 'Operational';
                }
                
                row.innerHTML = `
                    <td>T${train.id}</td>
                    <td>${(train.currentMileage/1000).toFixed(1)}k</td>
                    <td>${train.lastMaintenance} @ ${(train.lastMaintenanceMileage/1000).toFixed(1)}k</td>
                    <td>${(train.nextMaintenance/1000).toFixed(0)}k</td>
                    <td>${train.overdue > 0 ? (train.overdue/1000).toFixed(1) + 'k' : '-'}</td>
                    <td><span class="status-badge ${statusClass}">${statusText}</span></td>
                `;
                scheduleTable.appendChild(row);
            });
        }
        
        // Update stats grid
        function updateStatsGrid() {
            statsGrid.innerHTML = '';
            
            // Calculate stats
            const operationalTrains = trains.filter(t => t.status === 'Operational' || t.status === 'Due Soon').length;
            const maintenanceNeeded = trains.filter(t => t.status === 'Overdue' || t.status === 'Critical').length;
            const criticalAlerts = trains.filter(t => t.status === 'Critical').length;
            const avgMileage = trains.reduce((sum, train) => sum + train.currentMileage, 0) / trains.length;
            const staffHours = staffData.totalStaff * staffData.hoursPerDay;
            const efficiency = Math.min(95, 100 - (maintenanceNeeded / trains.length * 10));
            
            const stats = [
                { value: operationalTrains, label: 'Operational Trains' },
                { value: maintenanceNeeded, label: 'Maintenance Required' },
                { value: criticalAlerts, label: 'Critical Alerts' },
                { value: `${(avgMileage/1000).toFixed(0)}k`, label: 'Avg. Mileage' },
                { value: `${staffData.totalStaff}/${staffHours}`, label: 'Staff Utilization' },
                { value: `${efficiency.toFixed(0)}%`, label: 'System Efficiency' }
            ];
            
            stats.forEach(stat => {
                const statCard = document.createElement('div');
                statCard.className = 'stat-card';
                statCard.innerHTML = `
                    <div class="stat-value">${stat.value}</div>
                    <div class="stat-label">${stat.label}</div>
                `;
                statsGrid.appendChild(statCard);
            });
        }
        
        // Initialize charts
        function initCharts() {
            // Mileage Chart
            const mileageCtx = document.getElementById('mileageChart').getContext('2d');
            mileageChart = new Chart(mileageCtx, {
                type: 'line',
                data: {
                    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                    datasets: [
                        {
                            label: 'T5101',
                            data: [298.0, 298.3, 298.6, 298.9, 299.2, 299.5, 299.8],
                            borderColor: '#f59e0b',
                            backgroundColor: 'rgba(245, 158, 11, 0.1)',
                            tension: 0.3,
                            fill: true
                        },
                        {
                            label: 'T5104',
                            data: [390.2, 390.5, 390.8, 391.1, 391.4, 391.7, 392.0],
                            borderColor: '#ef4444',
                            backgroundColor: 'rgba(239, 68, 68, 0.1)',
                            tension: 0.3,
                            fill: true
                        },
                        {
                            label: 'T5111',
                            data: [454.1, 454.4, 454.7, 455.0, 455.3, 455.6, 455.9],
                            borderColor: '#10b981',
                            backgroundColor: 'rgba(16, 185, 129, 0.1)',
                            tension: 0.3,
                            fill: true
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: {
                                color: '#e2e8f0'
                            }
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            callbacks: {
                                label: function(context) {
                                    return `${context.dataset.label}: ${context.parsed.y.toFixed(1)}k miles`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                color: 'rgba(255, 255, 255, 0.1)'
                            },
                            ticks: {
                                color: '#a0aec0'
                            }
                        },
                        y: {
                            grid: {
                                color: 'rgba(255, 255, 255, 0.1)'
                            },
                            ticks: {
                                color: '#a0aec0',
                                callback: function(value) {
                                    return value + 'k';
                                }
                            },
                            title: {
                                display: true,
                                text: 'Mileage (thousands)',
                                color: '#a0aec0'
                            }
                        }
                    },
                    interaction: {
                        mode: 'nearest',
                        axis: 'x',
                        intersect: false
                    }
                }
            });
            
            // Resource Chart
            const resourceCtx = document.getElementById('resourceChart').getContext('2d');
            resourceChart = new Chart(resourceCtx, {
                type: 'doughnut',
                data: {
                    labels: ['LMT Utilization', 'HMT Utilization', 'Wheel Track', 'Idle'],
                    datasets: [{
                        data: [45, 25, 20, 10],
                        backgroundColor: [
                            'rgba(245, 158, 11, 0.8)',
                            'rgba(66, 153, 225, 0.8)',
                            'rgba(159, 122, 234, 0.8)',
                            'rgba(160, 174, 192, 0.8)'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: '#e2e8f0',
                                padding: 20
                            }
                        }
                    },
                    cutout: '70%'
                }
            });
            
            // Forecast Chart
            const forecastCtx = document.getElementById('forecastChart').getContext('2d');
            forecastChart = new Chart(forecastCtx, {
                type: 'bar',
                data: {
                    labels: ['This Week', 'Next Week', 'Week 3', 'Week 4'],
                    datasets: [{
                        label: 'Maintenance Required',
                        data: [2, 5, 3, 7],
                        backgroundColor: 'rgba(245, 158, 11, 0.7)',
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                color: '#a0aec0'
                            }
                        },
                        y: {
                            grid: {
                                color: 'rgba(255, 255, 255, 0.1)'
                            },
                            ticks: {
                                color: '#a0aec0',
                                stepSize: 1
                            },
                            title: {
                                display: true,
                                text: 'Number of Trains',
                                color: '#a0aec0'
                            }
                        }
                    }
                }
            });
        }
        
        // Event Listeners
        simulateBtn.addEventListener('click', function() {
            const dailyMileage = parseInt(dailyMileageInput.value) || 280;
            const originalText = simulateBtn.innerHTML;
            simulateBtn.innerHTML = '<i>⏳</i> Simulating...';
            simulateBtn.disabled = true;
            
            // Simulate processing
            setTimeout(() => {
                simulateBtn.innerHTML = originalText;
                simulateBtn.disabled = false;
                
                // Update train data
                trains.forEach(train => {
                    // Add daily mileage for 7 days
                    train.currentMileage += dailyMileage * 7;
                    
                    // Check if maintenance is needed
                    if (train.currentMileage > train.nextMaintenance) {
                        train.overdue = train.currentMileage - train.nextMaintenance;
                        train.status = train.overdue > 5000 ? 'Critical' : 'Overdue';
                    } else {
                        const milesLeft = train.nextMaintenance - train.currentMileage;
                        train.status = milesLeft < 5000 ? 'Due Soon' : 'Operational';
                    }
                });
                
                // Update UI
                updatePriorityList();
                updateScheduleTable();
                updateStatsGrid();
                
                // Show notification
                alert(`Simulation complete! 7 days of operations simulated with ${dailyMileage} miles/day. Maintenance schedules updated.`);
            }, 1500);
        });
        
        reportBtn.addEventListener('click', function() {
            alert('Report generated successfully! Download will start shortly.');
        });
        
        settingsBtn.addEventListener('click', function() {
            alert('Settings panel will open in a future version.');
        });
        
        startSimBtn.addEventListener('click', function() {
            alert('Continuous simulation will start in a future version.');
            startSimBtn.disabled = true;
            pauseSimBtn.disabled = false;
        });
        
        pauseSimBtn.addEventListener('click', function() {
            alert('Simulation paused.');
            startSimBtn.disabled = false;
            pauseSimBtn.disabled = true;
        });
        
        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                tabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                
                // Update chart based on period
                const period = tab.getAttribute('data-period');
                alert(`Switched to ${period} view. Charts updated.`);
            });
        });
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updatePriorityList();
            updateScheduleTable();
            updateStatsGrid();
        });
    </script>
</body>