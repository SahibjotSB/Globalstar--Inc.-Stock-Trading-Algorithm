// Function to display RBC information in a neat popup
const showRBCInfo = () => {
    const rbcInfo = `
        <strong>Royal Bank of Canada (RBC)</strong><br><br>
        RBC is one of Canada's largest financial institutions, providing comprehensive services including:
        <ul>
            <li>Personal Banking</li>
            <li>Business Banking</li>
            <li>Wealth Management</li>
            <li>Insurance</li>
            <li>Investment Solutions</li>
        </ul>
        It operates in over 35 countries with more than 80,000 employees globally, and is known for its commitment to innovation, especially in digital banking.
    `;

    // Creating a clean and simple popup using window.alert()
    alert(rbcInfo);
};

// Automatically show RBC info when the script is loaded
showRBCInfo();
