from playwright.sync_api import sync_playwright
import time

def extract_form_labels_from_google_form(url):
    """Agent 1: Extracts visible question labels from a Google Form."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("form")

        labels = page.locator("div[role='listitem'] div[role='heading']").all_inner_texts()
        browser.close()
        return labels

def gather_user_inputs(labels):
    """Agent 2: Prompts the user for input based on extracted field labels."""
    print("\n📝 Please enter the following details:\n")
    user_data = {}
    for label in labels:
        value = input(f"{label}: ")
        user_data[label] = value
    return user_data

def fill_google_form_without_submit(url, user_inputs):
    """Agent 3: Fills the form but does NOT submit. Lets the user review."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("form")

        field_blocks = page.locator("div[role='listitem']")

        for i in range(field_blocks.count()):
            label_element = field_blocks.nth(i).locator("div[role='heading']")
            input_element = field_blocks.nth(i).locator("input, textarea")

            try:
                label = label_element.inner_text().strip()
                if label in user_inputs:
                    input_element.fill(user_inputs[label])
                    print(f"✅ Filled: {label} -> {user_inputs[label]}")
                else:
                    print(f"⚠️ No input provided for: {label}")
            except:
                print(f"❌ Could not process question {i + 1}")

        print("\n🧐 Please review the form in the opened browser and click Submit manually when you're ready.")
        time.sleep(60)  # keep browser open for 2 minutes (or adjust as needed)
        browser.close()

# -----------------------
# 👇 MAIN SCRIPT
# -----------------------

if __name__ == "__main__":
    print("🤖 Autonomous Google Form Filler (Manual Submit Mode)\n")
    form_url = input("🔗 Enter your Google Form URL: ").strip()

    print("\n⏳ Extracting form labels...")
    labels = extract_form_labels_from_google_form(form_url)

    if not labels:
        print("⚠️ No labels found. Please check the form URL or its visibility settings.")
    else:
        print("\n✅ Found the following form fields:")
        for i, label in enumerate(labels, 1):
            print(f"{i}. {label}")

        user_inputs = gather_user_inputs(labels)

        print("\n🚀 Opening the form and inserting your inputs (no auto-submit)...")
        fill_google_form_without_submit(form_url, user_inputs)
