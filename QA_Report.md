# 🧪 QA Report – Segwise.ai Dashboard

## 🔍 Functional Testing Summary

Performed exploratory testing on Segwise.ai's dashboard using the provided test credentials. This report includes identified bugs, usability issues, and enhancement suggestions based on manual testing.

---

## 🔐 Test Credentials

- **Email**: `qa@segwise.ai`
- **Password**: `segwise_test`
- **Login URL**: [[https://segwise.ai/login](https://auth.segwise.ai/en/login)]

---

## 🐞 Found Bugs / Issues

| ID     | Component        | Description                                                                 | Severity | Status  |
|--------|------------------|-----------------------------------------------------------------------------|----------|---------|
| BUG-001| Login Page       | No error message appears when login fails with invalid credentials          | Medium   | Open    |
| BUG-002| Filters & Boards | Filters are not cleared after switching between boards                      | High     | Open    |
| BUG-003| Custom Reports   | "Export CSV" shows no feedback/loading indicator while processing           | Low      | Open    |
| BUG-004| Dashboard        | Certain charts take over 10s to load without a loading spinner              | High     | Open    |
| BUG-005| UI Consistency   | Inconsistent font size between "Custom Reports" and "Filters" sections      | Low      | Open    |

---

## 🔄 Suggested Test Cases

### 📋 Login Tests
- ✅ Valid credentials login
- ❌ Invalid credentials error message
- ✅ Redirection to dashboard after login
- ❌ Session timeout / inactivity auto logout

### 🧩 Filters & Boards
- ✅ Apply filters and check data updates
- ❌ Reset filters and check default view restores
- ✅ Switch between boards and validate independent states

### 📊 Custom Reports
- ✅ Generate new report with default settings
- ✅ Modify filters and generate reports
- ❌ Observe UI behavior during long report generation
- ✅ Export report to CSV and validate file

---

## 📌 UX Suggestions

- Add loading spinner when generating or loading reports/charts
- Add tooltips for unclear icon buttons in the filter section
- Persist user’s last-used filters between sessions (optional enhancement)

---

## 🧾 Notes

- No backend errors were observed in DevTools.
- Testing was conducted in **Chrome Version 124+**, **macOS & Windows**.
- All findings were based on the test environment; results may vary in production.

---

📅 **Date of Testing**: July 9, 2025  
🧑‍💻 **Tester**: Sayan Basu  
