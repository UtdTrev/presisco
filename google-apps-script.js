/**
 * ==============================================================================
 * PRECISCO FARM VENTURES LTD. — GOOGLE APPS SCRIPT DATABASE CONNECTOR
 * ==============================================================================
 * 
 * INSTRUCTIONS:
 * 1. Open Google Sheets (https://sheets.google.com) and create a new Spreadsheet.
 * 2. Name the sheet: "Precisco Farm Ventures - Master Operations Database".
 * 3. Go to: Extensions > Apps Script.
 * 4. Replace everything in the script editor with this code.
 * 5. Click "Deploy" > "New deployment" > Select type: "Web app".
 * 6. Set "Execute as": "Me" and "Who has access": "Anyone".
 * 7. Copy the generated Web App URL (e.g. https://script.google.com/macros/s/.../exec).
 * 8. Paste this URL into the "Settings" page of your Precisco Farm Portal!
 */

function doGet(e) {
  return handleRequest(e);
}

function doPost(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var payload = {};

    if (e.postData && e.postData.contents) {
      payload = JSON.parse(e.postData.contents);
    } else if (e.parameter) {
      payload = e.parameter;
    }

    var action = payload.action || "append_row";
    var sheetName = payload.sheetName || "Egg_Harvest_Log";
    var rowData = payload.data || {};

    // Get or Create the sheet tab
    var sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
      initializeSheetHeaders(sheet, sheetName);
    }

    if (action === "append_row") {
      var rowArray = formatDataForSheet(sheetName, rowData);
      sheet.appendRow(rowArray);
      
      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        message: "Row appended successfully to " + sheetName,
        timestamp: new Date().toISOString()
      })).setMimeType(ContentService.MimeType.JSON);
    } 
    else if (action === "fetch_all") {
      var data = sheet.getDataRange().getValues();
      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        data: data
      })).setMimeType(ContentService.MimeType.JSON);
    }

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// Automatically create professional formatted header rows
function initializeSheetHeaders(sheet, sheetName) {
  var headers = [];

  if (sheetName === "Egg_Harvest_Log") {
    headers = ["Log ID", "Date", "Time", "Harvest Round", "Grade A Good", "Cracked", "Broken", "Rejects", "Total Eggs", "Trays (30-Egg)", "Hen-Day %", "Collector Staff", "Recorded At"];
  } else if (sheetName === "Mortality_Records") {
    headers = ["Mortality ID", "Date", "Time", "Dead Birds Count", "Suspected Cause", "Biosecurity Disposal Action", "Reported By", "Review Status", "Recorded At"];
  } else if (sheetName === "Feed_Records") {
    headers = ["Feed ID", "Date", "Feed Formulation", "Issued (kg)", "Remaining (kg)", "Consumed (kg)", "Live Birds", "g / Bird / Day", "Intake Status", "Storekeeper Staff"];
  } else if (sheetName === "Corporate_Sales_Orders") {
    headers = ["Order ID", "Waybill #", "Date", "Corporate Client", "Crates (30-Egg)", "Unit Price (NGN)", "Total Invoiced (NGN)", "Paid (NGN)", "Balance Due (NGN)", "Payment Status", "Delivery Vehicle"];
  } else if (sheetName === "Farm_Expenses_PL") {
    headers = ["Voucher ID", "Date", "Category", "Description", "Amount (NGN)", "Payee / Vendor", "Authorized By"];
  } else if (sheetName === "Sick_Bay_Isolation") {
    headers = ["Case ID", "Date", "Cage Location", "Observed Symptoms", "Diagnosis", "Isolation Bay", "Prescribed Therapy", "Attendant", "Status"];
  } else if (sheetName === "Gate_Biosecurity_Visitors") {
    headers = ["Visitor ID", "Date", "Time In", "Visitor Name & Organization", "Purpose of Visit", "Biosecurity Checks Passed", "Security Officer On Duty"];
  } else {
    headers = ["Timestamp", "Record JSON Payload"];
  }

  sheet.appendRow(headers);
  var headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange.setBackground("#15803d");
  headerRange.setFontColor("#ffffff");
  headerRange.setFontWeight("bold");
  sheet.setFrozenRows(1);
}

function formatDataForSheet(sheetName, data) {
  var now = new Date().toLocaleString();

  if (sheetName === "Egg_Harvest_Log") {
    return [data.id || ("EGG-" + Date.now()), data.date, data.time, data.round, data.good, data.cracked, data.broken, data.reject, data.total, data.trays, data.henDay + "%", data.staff, now];
  } else if (sheetName === "Mortality_Records") {
    return [data.id || ("MORT-" + Date.now()), data.date, data.time, data.count, data.reason, data.action, data.staff, data.status, now];
  } else if (sheetName === "Feed_Records") {
    return [data.id || ("FEED-" + Date.now()), data.date, data.type, data.issuedKg, data.remainingKg, data.consumedKg, data.live, data.gramsPerBird + "g", data.status, data.staff];
  } else if (sheetName === "Corporate_Sales_Orders") {
    return [data.id || ("ORD-" + Date.now()), data.waybill, data.date, data.customer, data.crates, data.unitPrice, data.total, data.paid, data.balance, data.status, data.vehicle];
  } else if (sheetName === "Farm_Expenses_PL") {
    return [data.id || ("EXP-" + Date.now()), data.date, data.category, data.desc, data.amount, data.payee, data.authorizedBy || "Management"];
  } else if (sheetName === "Sick_Bay_Isolation") {
    return [data.id || ("SCK-" + Date.now()), data.date, data.tag, data.symptoms, data.diagnosis, data.isolation, data.treatment, data.staff, data.status];
  } else if (sheetName === "Gate_Biosecurity_Visitors") {
    return [data.id || ("VIS-" + Date.now()), data.date, data.time, data.name + " (" + (data.org || "Independent") + ")", data.purpose, data.result, data.guard];
  }
  return [now, JSON.stringify(data)];
}
