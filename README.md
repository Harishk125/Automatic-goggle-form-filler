#  Agentic AI Project: Google Form Auto-Filler (Manual Submit)

Welcome to my first **Agentic AI project**, where a team of simple agents works together to automate the process of filling out a Google Form. This tool was built using Python and Playwright and follows a clean multi-agent architecture that separates responsibilities for better readability and functionality.

---

## Agent Architecture

This project consists of **three autonomous agents**, each performing a dedicated task:

###  Agent 1 – Label Extractor
- Connects to the provided Google Form.
- Extracts all visible question labels (field headings).
- Displays them in the terminal for the user to review.

###  Agent 2 – Input Collector
- Prompts the user, one label at a time, to provide an answer.
- Collects inputs in a user-friendly and sequential manner.

###  Agent 3 – Form Filler
- Launches a browser window and navigates to the Google Form.
- Automatically fills in the answers provided by Agent 2.
- **Does not auto-submit** the form — giving users the opportunity to review or modify their responses before submission.

---

## 🚀 How It Works

1. **Run the script** from your terminal:
   python Google_form_filler.py

2. Paste the Google Form URL when prompted.

3. The agents activate in the following order:

    -  Agent 1 extracts and prints all the form labels (questions).

    -  Agent 2 collects your answers one-by-one through the terminal.

    -  Agent 3 opens the Google Form in a browser and auto-fills all fields.

4. The browser remains open for 1 minutes, allowing you to:

    - Verify that the correct responses have been entered.

    - Manually submit or modify the form.

##  Libraries Used
1. playwight - Automates browser actions like navigating pages, locating fields, and filling them.

2. time - Introduces a delay to keep the form open for review before closing the browser.

## Notes

- This tool works only with public Google Forms (i.e., those that don’t require login).

- Currently supports only short and long text fields (i.e., text inputs and paragraph answers).

- The script does not submit the form automatically — you get time to manually review and submit.

## Planned Enhancements

Support all form field types, including:

  - Multiple Choice (Radio Buttons)

  - Checkboxes (Multi-select)

  - Dropdown Menus (Select Fields)

  - File Uploads (where applicable)

