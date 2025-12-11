document.addEventListener('DOMContentLoaded', function() {
    // Data and state
    let lastPurchasedItems = ['Almond Milk', 'Snacks', 'Birthday Cake'];
    let shoppingCart = [];
    let monthlyBudget = 200; // default budget
    let currentSpend = 0;

    const userProfile = {
        name: 'Alex',
        preferences: ['organic', 'vegan'],
        specialDates: ['05-10'], // MM-DD format for simplicity
        purchaseHistory: [...lastPurchasedItems]
    };

    // Utility functions
    function updateList(containerId, items) {
        const container = document.getElementById(containerId);
        if (!container) return;
        if (items.length === 0) {
            container.innerHTML = '<p>No items to display.</p>';
            return;
        }
        container.innerHTML = '<ul>' + items.map(item => `<li>${item}</li>`).join('') + '</ul>';
    }

    function showMessage(containerId, message, timeout = 3000) {
        const container = document.getElementById(containerId);
        if (!container) return;
        container.textContent = message;
        if (timeout > 0) {
            setTimeout(() => {
                container.textContent = '';
            }, timeout);
        }
    }

    // Personalized AI Shopping Assistant
    function displayLastPurchasedItems() {
        updateList('last-purchased-list', lastPurchasedItems);
    }

    function reorderLastPurchasedItems() {
        if (lastPurchasedItems.length === 0) {
            showMessage('reorder-message', 'No previous orders found.');
            return;
        }
        // Add last purchased items to cart
        shoppingCart.push(...lastPurchasedItems);
        showMessage('reorder-message', 'Reordered: ' + lastPurchasedItems.join(', '));
        updateCartDisplay();
    }

    document.getElementById('reorder-button').addEventListener('click', reorderLastPurchasedItems);

    // Voice-Activated Shopping (simulated)
    function processVoiceCommand() {
        const command = prompt('Please speak your order:');
        if (command && command.trim() !== '') {
            shoppingCart.push(command.trim());
            showMessage('voice-command-feedback', `Added "${command.trim()}" to your cart.`);
            updateCartDisplay();
        } else {
            showMessage('voice-command-feedback', 'No command received.');
        }
    }

    document.getElementById('voice-command-button').addEventListener('click', processVoiceCommand);

    // VR/AR Shopping placeholders
    document.getElementById('vr-tour-button').addEventListener('click', function() {
        alert('Launching Virtual Store Tour... (VR experience placeholder)');
    });
    document.getElementById('ar-preview-button').addEventListener('click', function() {
        alert('Launching AR Product Preview... (AR experience placeholder)');
    });

    // Smart Cart & Automated Checkout
    function updateCartDisplay() {
        updateList('cart-items-list', shoppingCart);
    }

    function scanItem() {
        const item = prompt('Scan item: Enter product name');
        if (item && item.trim() !== '') {
            shoppingCart.push(item.trim());
            showMessage('checkout-message', `"${item.trim()}" added to cart.`);
            updateCartDisplay();
        } else {
            showMessage('checkout-message', 'No item scanned.');
        }
    }

    function automaticCheckout() {
        if (shoppingCart.length === 0) {
            showMessage('checkout-message', 'Your cart is empty.');
            return;
        }
        // Calculate total cost simulation (assume $10 per item)
        const totalCost = shoppingCart.length * 10;
        currentSpend += totalCost;
        shoppingCart = [];
        updateCartDisplay();
        showMessage('checkout-message', `Checkout complete! Total: $${totalCost}.`);
        updateBudgetInfo();
    }

    document.getElementById('scan-item-button').addEventListener('click', scanItem);
    document.getElementById('checkout-button').addEventListener('click', automaticCheckout);

    // Planning & Budgeting Tools
    let mealPlan = [];

    function planMeal() {
        const meal = prompt('Enter meal name to plan:');
        if (meal && meal.trim() !== '') {
            mealPlan.push(meal.trim());
            updateList('meal-plan', mealPlan);
            showMessage('budget-info', `Meal "${meal.trim()}" added to plan.`);
        } else {
            showMessage('budget-info', 'No meal entered.');
        }
    }

    function setMonthlyBudget() {
        const newBudget = prompt('Enter your monthly budget:', monthlyBudget);
        if (newBudget && !isNaN(newBudget)) {
            monthlyBudget = Number(newBudget);
            showMessage('budget-info', `Budget set to $${monthlyBudget}.`);
            updateBudgetInfo();
        } else {
            showMessage('budget-info', 'Invalid budget entered.');
        }
    }

    function updateBudgetInfo() {
        const budgetInfo = document.getElementById('budget-info');
        if (!budgetInfo) return;
        budgetInfo.textContent = `Budget: $${monthlyBudget} | Spent: $${currentSpend} | Remaining: $${(monthlyBudget - currentSpend).toFixed(2)}`;
    }

    document.getElementById('plan-meal-button').addEventListener('click', planMeal);
    document.getElementById('set-budget-button').addEventListener('click', setMonthlyBudget);

    // Sustainability & Local Sourcing
    const products = [
        { name: 'Organic Apples', ecoFriendly: true, local: true },
        { name: 'Plastic Water Bottle', ecoFriendly: false, local: false },
        { name: 'Vegan Snacks', ecoFriendly: true, local: false },
        { name: 'Local Honey', ecoFriendly: true, local: true },
        { name: 'Imported Cheese', ecoFriendly: false, local: false }
    ];

    function filterProducts(filterKey) {
        return products.filter(p => p[filterKey]);
    }

    function showEcoFriendlyProducts() {
        const ecoProducts = filterProducts('ecoFriendly').map(p => p.name);
        updateList('eco-products-list', ecoProducts);
    }

    function showLocalProducts() {
        const localProducts = filterProducts('local').map(p => p.name);
        updateList('local-products-list', localProducts);
    }

    document.getElementById('eco-products-button').addEventListener('click', showEcoFriendlyProducts);
    document.getElementById('local-products-button').addEventListener('click', showLocalProducts);

    // Personalized suggestions for special dates
    function suggestForSpecialDates() {
        const today = new Date();
        const todayStr = ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
        if (userProfile.specialDates.includes(todayStr)) {
            alert('Reminder: Special occasion today! Consider buying a gift or cake.');
        }
    }

    // Initial UI setup
    displayLastPurchasedItems();
    updateCartDisplay();
    updateBudgetInfo();
    suggestForSpecialDates();
});
